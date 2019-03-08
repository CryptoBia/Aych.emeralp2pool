from distutils.core import setup, Extension

emd_scrypt_module = Extension('emd_scrypt',
                               sources = ['scryptmodule.c',
                                          'scrypt.c'],
                               include_dirs=['.'])

setup (name = 'emd_scrypt',
       version = '1.0',
       description = 'Bindings for scrypt proof of work used by Emerald',
       ext_modules = [emd_scrypt_module])
