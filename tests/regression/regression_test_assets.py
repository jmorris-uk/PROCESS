"""Provides the classes to find, download, and access tracked MFiles on
a remote data repository
"""

import dataclasses
import logging
import re
import subprocess
from pathlib import Path

import requests

logger = logging.getLogger(__name__)


@dataclasses.dataclass
class TrackedMFile:
    hash: str
    scenario_name: str
    download_link: str


class RegressionTestAssetCollector:
    remote_repository_owner = "timothy-nunn"
    remote_repository_repo = "process-tracking-data"

    def __init__(self) -> None:
        self._hashes = self._git_commit_hashes()
        self._tracked_mfiles = self._get_tracked_mfiles()

    def get_reference_mfile(
        self, scenario_name: str, directory: Path, target_hash: str | None = None
    ):
        """Finds the most recent reference MFile for `<scenario_name>.IN.DAT`
        and downloads it to the `directory` with the name `ref.<scenario_name>.MFILE.DAT`.

        Providing a `target_hash` will ONLY return a reference MFILE that exactly
        matches the requested commit hash.

        :param scenario_name: the reference MFile to be found was generated by running
        <scenario_name>.IN.DAT.
        :type scenario_name: str
        :param directory: the directory to download the reference MFile to
        :type directory: Path
        :param target_hash: if provided, only a reference MFile tracked for this commit
        will be downloaded, if available.
        :type target_hash:

        :returns: Path to the downloaded reference MFile, if no reference MFile can be found,
        `None` is returned.
        :rtype: Path
        """
        reference_mfile_location = directory / f"ref.{scenario_name}.MFILE.DAT"
        for mf in self._tracked_mfiles:
            if (mf.scenario_name == scenario_name and target_hash is None) or (
                mf.scenario_name == scenario_name and target_hash == mf.hash
            ):
                with open(reference_mfile_location, "w") as f:
                    f.write(requests.get(mf.download_link).content.decode())

                logger.info(f"Reference MFile found for commit {mf.hash}")
                return reference_mfile_location

        return None

    def _git_commit_hashes(self):
        """Returns the list of commit hashes.

        :returns: a list of commit hashes from 'git log'
        :rtype: list[str]
        """
        return (
            subprocess.run(
                'git log --format="%H"',
                shell=True,
                capture_output=True,
                check=True,
            )
            .stdout.decode()
            .split("\n")
        )

    def _get_tracked_mfiles(self):
        """Gets a list of tracked MFiles from the remote repository.

        :returns: a list of tracked MFiles sorted to match the order of
        hashes returned from `_git_commit_hashes`.
        :rtype: list[TrackedMFile]
        """
        repository_files = requests.get(
            f"https://api.github.com/repos/"
            f"{self.remote_repository_owner}/{self.remote_repository_repo}/git/trees/master"
        ).json()["tree"]

        # create a list of tracked MFiles from the list of all files
        # in the remote repository.
        # Only keep TrackedMFiles that are tracked for a commit on the
        # current branch. This stops issues arising from main being
        # ahead of the feature branch and having newer tracks.
        tracked_mfiles = [
            mfile
            for f in repository_files
            if (mfile := self._get_tracked_mfile(f)) is not None
            and mfile.hash in self._hashes
        ]

        # order tracked MFiles to match order of the git log
        return sorted(
            tracked_mfiles,
            key=lambda m: self._hashes.index(m.hash),
        )

    def _get_tracked_mfile(self, json_data):
        """Converts JSON data of a file tracked on GitHub into a
        `TrackedMFile`, if appropriate

        :param json_data: a dictionary representing a file in the remote repository.
        The dictionary must have fields: 'name' and 'download_url'.
        :type json_data: dict[str, Any]

        :returns: A representation of the tracked MFile, if the file is indeed a
        tracked mfile.
        :rtype: TrackedMFile | None
        """
        rematch = re.match(r"([a-zA-Z0-9_.]+)_MFILE_([a-z0-9]+).DAT", json_data["path"])

        if rematch is None:
            return None
        return TrackedMFile(
            hash=rematch.group(2),
            scenario_name=rematch.group(1),
            download_link=f"https://raw.githubusercontent.com/"
            f"{self.remote_repository_owner}/{self.remote_repository_repo}/master/{json_data['path']}",
        )
