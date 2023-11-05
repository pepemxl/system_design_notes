import os
if __name__ == '__main__':
    import sys
    temp_path = os.path.join(os.path.dirname(__file__), '.')
    print("Adding \"{0}\" to path  for testing".format(temp_path))
    sys.path.append(temp_path)
from .common.constants import CONFIG_PATH


config_filename = "config.yml"
config_full_filename = os.path.join(CONFIG_PATH, config_filename)
if os.path.isfile(config_full_filename):
    import yaml
    with open(config_full_filename, 'r') as ptr_file:
        yaml_data = yaml.safe_load(ptr_file)
        config = yaml_data['data']
        os.environ.update(config)
        mi_dummy_variable = os.getenv("mi_dummy_variable")


if __name__ == '__main__':
    print(mi_dummy_variable)