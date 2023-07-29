import os
import sys
import importlib
from types import ModuleType
from typing import Any

current_dir=os.path.dirname(__file__)
python_path=sys.executable

site_package_dir=os.path.join(python_path,"../lib/site-packages")

def add_environment(lib_dir,lib_nm=None,lib_version="1.0.0"):
    """
    Args:
        lib_dir (_type_): _description_ 绝对路径
        lib_nm (_type_, optional): _description_. Defaults to None.
        lib_version (str, optional): _description_. Defaults to "1.0.0".
    """
    if lib_nm==None:
        lib_nm=os.path.split(lib_dir)
    
    context_=lib_dir+"\n"
    print(lib_dir,os.path.isdir(lib_dir))
    with open(os.path.join(site_package_dir,"{}.pth".format(lib_nm)),"w") as f:
        f.write(context_)
    
    egg_info=os.path.join(site_package_dir,"{}-{}.egg-info".format(lib_nm,lib_version))
    content_version="Version: {}\n".format(lib_version)
    name_="Name: {}\n".format(lib_nm)
    with open(egg_info,"w") as f:
        f.write(context_)
        f.write(content_version)
        f.write(name_)
# print(site_package_dir)
# print(os.path.isdir(site_package_dir))

def direct_transformers_import(path: str, file="__init__.py") -> ModuleType:
    """Imports transformers directly

    Args:
        path (`str`): The path to the source file
        file (`str`, optional): The file to join with the path. Defaults to "__init__.py".

    Returns:
        `ModuleType`: The resulting imported module
    """
    name = "transformers"
    location = os.path.join(path, file)
    spec = importlib.util.spec_from_file_location(name, location, submodule_search_locations=[path])
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    module = sys.modules[name]
    return module


if __name__== "__main__":
    from cores.transformers import __version__ as transformers_version
    path=os.path.join(current_dir,"cores/transformers")
    add_environment(path,"transformers",transformers_version)
    