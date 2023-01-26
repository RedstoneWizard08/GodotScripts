import shutil

from .util import get_cross_compiler_prefix
from arches import TargetArch

def get_strip():
    strip = shutil.which("strip")
    
    if strip == None:
        print(f"Could not find GNU strip! Please install GNU strip!")
        exit(1)
    else:
        return strip

def get_cross_strip(arch: TargetArch):
    prefix = get_cross_compiler_prefix(arch)
    compiler_name = "emstrip" if arch == TargetArch.wasm32 else prefix[0] + "strip"

    strip = shutil.which(compiler_name)
    
    if strip == None:
        print(f"Could not find a cross strip utility! Please install {compiler_name}!")
        
        if arch != TargetArch.wasm32:
            print(f"=> Tip: This one should be binutils{prefix[1]} on Ubuntu!")
        
        exit(1)
    else:
        return strip

