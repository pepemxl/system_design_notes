import argparse
import logging
import os
import sys
from monorepo.common.constants import CONFIG_PATH
from monorepo.version import __version__ as VERSION


log = logging.getLogger(__name__)
current_level_logging = logging.INFO
log.setLevel(current_level_logging)

filename_config = 'config.yml'
full_filname_config = os.path.join(CONFIG_PATH, filename_config)
if os.path.isfile(full_filname_config):
    import yaml
    with open(full_filname_config, 'r') as ptr_file:
        yaml_data = yaml.safe_load(ptr_file)
        config = yaml_data['data']
        os.environ.update(config)


def main(sys_argv=None) -> None:
    log.info("Starting project SDI")
    parser = argparse.ArgumentParser(
        description="SDI Learning COURSE",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument(
        '--service',
        '-s',
        type=str,
        default='sdi',
        help='SDI course tool'
    )
    parser.add_argument(
        '--version',
        action='version',
        version=f"%(prog)s {VERSION}"
    )
    sys_argv = sys_argv or sys.argv[1:]
    args = parser.parse_args(sys_argv)
    level = current_level_logging
    log.info(sys_argv)


if __name__ == '__main__':
    main()