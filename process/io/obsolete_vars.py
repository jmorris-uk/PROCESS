"""Dict of obsolete vars and their new names for the input validator, and dict of help messages for certain obsolete vars.

This is used by the input_validator module to find any obsolete variables in the
input file (which have since been renamed in the current version of the source).
If the input validator finds an obsolete var, it can then suggest the new name
of that variable, based on this dictionary. This should make migration of old
input files easier, and variable renaming less painful.

Each key is an obsolete var, the value is either the new var name or None if the
var is deprecated.

Note: this is now relied upon by Blueprint, pending implementing a proper API.
"""

OBS_VARS = {
    "snull": "i_single_null",
    "tfno": "n_tf",
    "itfsup": "i_tf_sup",
    "r_tf_inleg_mid": "r_tf_inboard_mid",
    "rtot": "r_tf_outboard_mid",
    "a_tf_inboard": "tfareain",
    "r_tf_inleg_in": "r_tf_inleg_in",
    "r_tf_inleg_out": "r_tf_inleg_out",
    "a_tf_wp": "awpc",
    "sigttf": "sig_tf_t",
    "sigtcon": "sig_tf_t",
    "sigrtf": "sig_tf_r",
    "sigrcon": "sig_tf_r",
    "sigvert": "sig_tf_z",
    "sig_vmises_case": "sig_tf_vmises",
    "sig_vmises_cond": "sig_tf_vmises",
    "sig_tresca_case": "sig_tf_treca",
    "sig_tresca_cond": "sig_tf_treca",
    "sigver": None,
    "sigrad": None,
    "poisson": "poisson_steel",
    "eywp": "eyoung_winding",
    "eyins": "eyoung_ins",
    "eystl": "eyoung_steel",
    "isumattf": "i_tf_sc_mat",
    "turnstf": "n_tf_turn",
    "awptf": "a_tf_wp",
    "dr_tf_case_in": "thkcas",
    "f_tf_case_out": "casthi_fraction",
    "dr_tf_case_out": "casthi",
    "eyoung_reinforced_al": "eyoung_nibron",
    "thkwp": "dr_tf_wp",
    "leni": "t_cable",
    "leno": "t_turn",
    "conductor_width": "t_conductor",
    "deltf": "tftsgap",
    "ddwi": "d_vv_out",
    "pnuccp": "pnuc_cp",
    "nuc_pow_dep_tot": "pnuc_tot_blk_sector",
    "t_turn": "t_turn_tf",
    "ratecdol": "discount_rate",
    "strtf1": "sig_tf_case",
    "strtf2": "sig_tf_wp",
    "alstrtf": ["sig_tf_case_max", "sig_tf_wp_max"],
    "strtf0": "sig_tf_cs_bucked",
    "eyoung_winding": ["eyoung_cond_axial", "eyoung_cond_trans"],
    "i_tf_plane_stress": "i_tf_stress_model",
    "windstrain": "strncon_tf",
    "eyzwp": "eyoung_wp_z_eff",
    "strncon_cs": "str_cs_con_res",
    "strncon_pf": "str_pf_con_res",
    "strncon_tf": "str_tf_con_res",
    "i_strain_wp": "i_str_wp",
    "strain_wp_max": "str_wp_max",
    "strain_wp": "str_wp",
    "fstrain_wp": "fstr_wp",
    "rad_fraction": "rad_fraction_total",
    "pcoreradmw": "p_plasma_inner_rad_mw",
    "pedgeradmw": "p_plasma_outer_rad_mw",
    "rad_fraction_core": "rad_fraction_LCFS",
    "thshield": ["thshield_ib", "thshield_ob", "thshield_vb"],
    "igeom": None,
    "fgamp": None,
    "divleg_profile_inner": None,
    "divleg_profile_outer": None,
    "iprimnloss": None,
    "rho_ecrh": None,
    "ifispact": None,
    "fmsbc": None,
    "fmsbl": None,
    "fmsdwe": None,
    "fmsdwi": None,
    "fmsfw": None,
    "fmsoh": None,
    "fmssh": None,
    "fmstf": None,
    "quench_detection_ef": None,
    "farc4tf": None,
    "impvar": None,
    "fimpvar": None,
    "sigvvall": "max_vv_stress",
    "ftaucq": "fmaxvvstress",
    "fradmin": None,
    "ftr": "f_tritium",
    "iculdl": "idensl",
    "iiter": None,
    "ires": None,
    "fjtfc": None,
    "bcylth": None,
    "itfmod": None,
    "jcrit_model": None,
    "fcohbof": None,
    "fvolbi": "fhole",
    "fvolbo": "fhole",
    "fvolcry": None,
    "idhe3": "f_helium3",
    "blnktth": None,
    "theat": "t_fusion_ramp",
    "ieped": None,
    "eped_sf": None,
    "icurr": "i_plasma_current",
    "idia": "i_diamagnetic_current",
    "ibss": "i_bootstrap_current",
    "ips": "i_pfirsch_schluter_current",
    "bootipf": "bootstrap_current_fraction",
    "bscfmax": "bootstrap_current_fraction_max",
    "vgap2": "vgap_vv_thermalshield",
    "vgap": "vgap_xpoint_divertor",
    "ftritbm": "f_tritium_bream",
    "enbeam": "beam_energy",
    "fdeut": "f_deuterium",
    "ftrit": "f_tritium",
    "fhe3": "f_helium3",
    "falpha": "f_alpha_plasma",
    "idensl": "i_density_limit",
    "ftburn": "ft_burn",
    "ftohs": "ft_current_ramp_up",
    "tbrnmn": "t_burn_min",
    "tohs": "t_current_ramp_up",
    "tdwell": "t_between_pulse",
    "tramp": "t_precharge",
    "tqnch": "t_ramp_down",
    "tburn": "t_burn",
    "pdivmax/rmajor": "pdivmax_over_rmajor",
    "pdivtbt/qar": "pdivtbt_over_qar",
    "betpmx": "beta_poloidal_max",
    "fbetatry": "fbeta_max",
    "fbetap": "fbeta_poloidal",
    "iculbl": "i_beta_component",
    "epbetmax": "beta_poloidal_eps_max",
    "dnbeta": "beta_norm_max",
    "ifalphap": "i_beta_fast_alpha",
    "betalim": "beta_max",
    "betalim_lower": "beta_min",
    "fbeta": "fbeta_poloidal_eps",
    "fcwr": "fr_conducting_wall",
    "cvol": "f_vol_plasma",
    "cwrmax": "f_r_conducting_wall",
    "ishape": "i_plasma_geometry",
    "iscrp": "i_plasma_wall_gap",
    "peakfactrad": "f_fw_rad_max",
    "nimp": "n_impurities",
    "ssync": "f_sync_reflect",
    "rnbeam": "f_nd_beam_electron",
    "ralpne": "f_nd_alpha_electron",
    "protium": "f_nd_protium_electrons",
}

OBS_VARS_HELP = {
    "iculdl": "(use IDENSL=3 for equivalent model to ICULDL=0). ",
    "blnktth": "WARNING. BLNKTTH is now always calculated rather than input - please remove it from the input file. ",
}

kallenbach_list = [
    "target_spread",
    "lambda_q_omp",
    "lcon_factor",
    "netau_sol",
    "kallenbach_switch",
    "kallenbach_tests",
    "kallenbach_test_option",
    "kallenbach_scan_switch",
    "kallenbach_scan_var",
    "kallenbach_scan_start",
    "kallenbach_scan_end",
    "kallenbach_scan_num",
    "targetangle",
    "ttarget",
    "qtargettotal",
    "impurity_enrichment",
    "fractionwidesol",
    "abserr_sol",
    "relerr_sol",
    "mach0",
    "neratio",
]
kallenbach_message = "The Kallenbach model is currently not included in PROCESS. See issue #1886 for more information on the use of the Kallenbach model. "
OBS_VARS.update(dict.fromkeys(kallenbach_list, None))
OBS_VARS_HELP.update(dict.fromkeys(kallenbach_list, kallenbach_message))
