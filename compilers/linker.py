import shutil

from .util import get_cross_compiler_prefix
from arches import TargetArch

def get_ld():
    ld = shutil.which("ld")
    
    if ld == None:
        print(f"Could not find LD! Please install GNU LD!")
        exit(1)
    else:
        return ld

def get_lld():
    lld = shutil.which("lld")

    if lld == None:
        print(f"Could not find LLD! Using GNU LD...");
        return get_ld()
    else:
        return lld

def get_cross_linker(arch: TargetArch):
    prefix = get_cross_compiler_prefix(arch)
    compiler_name = prefix[0] + "ld"

    ld = shutil.which(compiler_name)
    
    if ld == None:
        print(f"Could not find a linker! Please install {compiler_name}!")
        print(f"=> Tip: This one should be binutils{prefix[1]} on Ubuntu!")
        exit(1)
    else:
        return ld
