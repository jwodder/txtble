from   os.path    import dirname, join
import re
from   setuptools import setup

with open(join(dirname(__file__), 'txtble', '__init__.py')) as fp:
    for line in fp:
        m = re.search(r'^\s*__version__\s*=\s*([\'"])([^\'"]+)\1\s*$', line)
        if m:
            version = m.group(2)
            break
    else:
        raise RuntimeError('Unable to find own __version__ string')

setup(version=version)
