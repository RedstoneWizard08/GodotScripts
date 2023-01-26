import shutil

from .util import get_cross_compiler_prefix
from arches import TargetArch

def get_ar():
    ar = shutil.which("ar")
    
    if ar == None:
        print(f"Could not find AR! Please install GNU AR!")
        exit(1)
    else:
        return ar

def get_cross_archiver(arch: TargetArch):
    prefix = get_cross_compiler_prefix(arch)
    compiler_name = "emar" if arch == TargetArch.wasm32 else prefix[0] + "ar"

    ar = shutil.which(compiler_name)
    
    if ar == None:
        print(f"Could not find an archiver! Please install {compiler_name}!")
        
        if arch != TargetArch.wasm32:
            print(f"=> Tip: This one should be binutils{prefix[1]} on Ubuntu!")
        
        exit(1)
    else:
        return ar
