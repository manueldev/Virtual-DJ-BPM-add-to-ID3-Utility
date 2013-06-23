from distutils.core import setup
import py2exe


setup(
    options = {'py2exe': {'bundle_files': 2, 'dist_dir' : 'bin/','compressed': True, 'dll_excludes' : ['w9xpopen.exe']}},
    console = [{'script': "virtualdjbpmutility-console.py"}],
    windows = [{'script': "virtualdjbpmutility-gui.py"}],
    zipfile = None,
)