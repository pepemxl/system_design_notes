import importlib.metadata

__version__ = importlib.metadata.version("sdi")

# MAJOR = '0'
# MINOR = '0'
# PATCH = '2'
# VERSION = f"{MAJOR}.{MINOR}.{PATCH}"
# __version__ = VERSION

if __name__ == '__main__':
    print(__version__)