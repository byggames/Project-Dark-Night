# Para realizar el .exe (instalar Py2Exe)

from distutils.core import setup
import py2exe

setup(name="Prueba",
 version="1.0",
 description="Breve descripcion",
 author="By",
 author_email="email del autor",
 url="url del proyecto",
 license="tipo de licencia",
 scripts=["menu.py","index.py"],
 console=["menu.py","index.py"],
 options={"py2exe": {"bundle_files": 1}},
 zipfile=None,
)
