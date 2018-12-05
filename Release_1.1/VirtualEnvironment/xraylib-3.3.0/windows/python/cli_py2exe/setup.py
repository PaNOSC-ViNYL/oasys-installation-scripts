from distutils.core import setup
import py2exe

setup(
	name="xraylib",
	version='3.3.0',
	author="Tom Schoonjans",
	console=['..\\..\\..\\..\\windows\\python\\cli_py2exe\\xraylib-cli.py'],
	data_files=[('Doc',['..\\..\\..\\..\\doc\\xraybanner.txt']),('Doc',['..\\..\\..\\..\\doc\\xraydoc.txt']),('Doc',['..\\..\\..\\..\\doc\\xrayfunc.txt']),('Doc',['..\\..\\..\\..\\doc\\xrayhelp.txt'])],
	options={
		"py2exe":{
			"unbuffered": True,
			"optimize": 2,
			"bundle_files": 1,
			"includes":["_xraylib", "xraylib", "xraymessages","xrayhelp"],
			"dll_excludes":['w9xpopen.exe']
	        }
        },
	zipfile=None
)
