import shutil

from .util import get_cross_compiler_prefix, get_compiler_name
from arches import TargetArch

def get_gcc(cpp = False):
    cpp_msg = "C++" if cpp else "C"
    compiler_name = "g++" if cpp else "gcc"
    
    gcc = shutil.which(compiler_name)
    
    if gcc == None:
        print(f"Could not find a {cpp_msg} compiler! Please install {compiler_name}!")
        exit(1)
    else:
        return gcc

def get_clang(cpp = False):
    cpp_msg = "G++" if cpp else "GCC"
    compiler_name = "clang++" if cpp else "clang"
    
    clang = shutil.which(compiler_name)

    if clang == None:
        print(f"Could not find Clang! Using {cpp_msg}...");
        return get_gcc(cpp)
    else:
        return clang

def get_cross_compiler(arch: TargetArch, cpp = False):
    cpp_msg = "C++" if cpp else "C"
    prefix = get_cross_compiler_prefix(arch)
    compiler_name = prefix[0] + get_compiler_name(arch, cpp)
    
    cc = shutil.which(compiler_name)
    
    if cc == None:
        print(f"Could not find a {cpp_msg} compiler! Please install {compiler_name}!")
        print(f"=> Tip: This one should be {get_compiler_name(arch, cpp)}{prefix[1]} on Ubuntu!")
        exit(1)
    else:
        return cc
