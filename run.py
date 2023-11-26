import importlib
from autonomousAJ_squareAPI import config

base_path = config.BASE_PATH
app_run_input = config.APP_RUN_INPUT

if app_run_input == "all":
    for script_name in config.all_scripts:
    module = importlib.import_module('autonomousAJ_squareAPI.TBD')
else:
    module = importlib.import_module(f'autonomousAJ_squareAPI.TBD')
    