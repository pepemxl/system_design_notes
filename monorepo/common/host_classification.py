from functools import lru_cache
import os
import platform
import socket


@lru_cache
def get_hostname() -> str:
    return socket.getfqdn()


@lru_cache
def is_mac_host() -> bool:
    return os.uname().sysname == 'Darwin'


@lru_cache
def get_operating_system():
    system = platform.system()
    if system == 'Linux':
        return 'Linux'
    elif system == 'Windows':
        return 'Windows'
    else:
        return 'Unknown'



if __name__ == '__main__':
    print(get_operating_system())
