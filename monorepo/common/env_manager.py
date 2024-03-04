import os
import sys
from typing import Optional
import yaml
from monorepo.common.constants import CONFIG_FILE_PATH
from monorepo.common.logger import get_logger


log = get_logger(__file__, "WARNING")
ENV_VARS_LOADED = False


def load_config_environment_variables():
    log.info("Loading environment variables")
    global ENV_VARS_LOADED
    if os.path.isfile(CONFIG_FILE_PATH):
        with open(CONFIG_FILE_PATH, "r") as ptr_file:
            yml_data = yaml.safe_load(ptr_file)
            local_env_variables = yml_data['data']
            os.environ.update(local_env_variables)
            ENV_VARS_LOADED = True
    else:
        log.error("Config file not found {0}".format(CONFIG_FILE_PATH))
        sys.exit(1)


def get_env_variable(env_variable_key: str) -> Optional[str]:
    if not ENV_VARS_LOADED:
        load_config_environment_variables()
    try:
        value = os.getenv(env_variable_key)
    except Exception as e:
        log.exception("Error: {0}".format(str(e)))
    if value is None:
        log.error("Environment variable {0} not found".format(env_variable_key))
    return value
    