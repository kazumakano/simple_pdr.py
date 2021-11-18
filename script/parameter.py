import os.path as path
from typing import Union
import numpy as np
import yaml


def _set_log_params(conf: dict) -> None:
    global WIN_SIZE

    WIN_SIZE = int(conf["win_size"])                             # size of sliding window [second]

def _set_dist_params(conf: dict) -> None:
    global STEP_LEN_COEF, STATURE, DEFAULT_SPEED, BEGIN_THRESH, POS_PEAK_THRESH, NEG_PEAK_THRESH, END_THRESH, MIN_STEP_INTERVAL, MAX_STATE_INTERVAL

    STEP_LEN_COEF = np.float16(conf["step_len_coef"])            # ratio of step length to stature
    STATURE = np.float16(conf["stature"])                        # subject's stature [meter]
    DEFAULT_SPEED = np.float16(conf["default_speed"])            # default subject's speed [meter/second]

    BEGIN_THRESH = np.float16(conf["step_begin_acc_thresh"])     # threshold values of acceleration [G]
    POS_PEAK_THRESH = np.float16(conf["pos_peak_acc_thresh"])
    NEG_PEAK_THRESH = np.float16(conf["neg_peak_acc_thresh"])
    END_THRESH = np.float16(conf["step_end_acc_thresh"])
    MIN_STEP_INTERVAL = float(conf["min_step_interval"])         # minimum interval from last step to detect new step [second]
    MAX_STATE_INTERVAL = float(conf["max_state_interval"])       # maximum interval from last state transition to recognize as moving [second]

def _set_direct_params(conf: dict) -> None:
    global DRIFT

    DRIFT = np.float16(conf["gyro_drift"])                       # drift value of gyroscope [degree/second]

def set_params(conf_file: Union[str, None] = None) -> dict:
    global ROOT_DIR, IS_LOST

    ROOT_DIR = path.dirname(__file__) + "/../"                   # project root directory
    IS_LOST = False                                              # subject is lost or not

    if conf_file is None:
        conf_file = ROOT_DIR + "config/default.yaml"    # load default config file if not specified
    else:
        conf_file = conf_file

    with open(conf_file) as f:
        conf: dict = yaml.safe_load(f)
    print(f"parameter.py: {path.basename(conf_file)} has been loaded")

    _set_log_params(conf)
    _set_dist_params(conf)
    _set_direct_params(conf)

    return conf