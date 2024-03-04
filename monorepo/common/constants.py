import os

env_var = os.environ
if 'BASE_PATH' not in env_var:
    CURRENT_PATH = os.path.abspath(__file__)
    COMMON_PATH = os.path.dirname(CURRENT_PATH)
    BASE_PATH = os.path.dirname(COMMON_PATH)
    REPO_PATH = os.path.dirname(BASE_PATH)
LIST_TEMP_PATHS = []
LOCAL_DATA_PATH = os.path.join(REPO_PATH, 'LOCAL_DATA')
LIST_TEMP_PATHS.append(LOCAL_DATA_PATH)
CONFIG_PATH = os.path.join(LOCAL_DATA_PATH, 'LOCAL_CONFIGS')
CONFIG_FILE_PATH = os.path.join(CONFIG_PATH, "config.yml")
LIST_TEMP_PATHS.append(CONFIG_PATH)
DATA_PATH = os.path.join(LOCAL_DATA_PATH, 'DATA')
LIST_TEMP_PATHS.append(DATA_PATH)
LOCAL_DB_PATH = os.path.join(DATA_PATH, 'DB')
LIST_TEMP_PATHS.append(LOCAL_DB_PATH)
LOGS_PATH = os.path.join(LOCAL_DATA_PATH, 'LOGS')
LIST_TEMP_PATHS.append(LOGS_PATH)


PORT_KAFKA_NODE_01 = 87192

def create_temp_folders():
    for path in LIST_TEMP_PATHS:
        if not os.path.isdir(path):
            print("Creating path: \"{0}\"".format(path))
            os.mkdir(path)
        

create_temp_folders()

if __name__ == '__main__':
    pass