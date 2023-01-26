from arches import TargetArch

from compilers.gcc import get_clang, get_gcc, get_cross_compiler
from compilers.linker import get_ld, get_lld, get_cross_linker
from compilers.archiver import get_ar, get_cross_archiver
from compilers.strip import get_strip, get_cross_strip

class Compilers:
    def __init__(self, CC: str, CXX: str, LD: str, AR: str, STRIP: str):
        self.CC = CC
        self.CXX = CXX
        self.LD = LD
        self.AR = AR
        self.STRIP = STRIP

def get_compiler(arch: TargetArch, llvm = False, cpp = False):
    system_arch = TargetArch.current_arch()
    
    if arch == system_arch:
        if llvm:
            return get_clang(cpp)
        else:
            return get_gcc(cpp)
    else:
        return get_cross_compiler(arch, cpp)

def get_linker(arch: TargetArch, lld = False):
    system_arch = TargetArch.current_arch()
    
    if arch == system_arch:
        if lld:
            return get_lld()
        else:
            return get_ld()
    else:
        return get_cross_linker(arch)

def get_archiver(arch: TargetArch):
    system_arch = TargetArch.current_arch()
    
    if arch == system_arch:
        return get_ar()
    else:
        return get_cross_archiver(arch)

def get_strip_bin(arch: TargetArch):
    system_arch = TargetArch.current_arch()
    
    if arch == system_arch:
        return get_strip()
    else:
        return get_cross_strip(arch)

def get_compilers(arch: TargetArch, llvm = False, lld = False):
    return Compilers(
        CC = get_compiler(arch, llvm = llvm, cpp = False),
        CXX = get_compiler(arch, llvm = llvm, cpp = True),
        LD = get_linker(arch, lld = lld),
        AR = get_archiver(arch),
        STRIP = get_strip_bin(arch),
    )

def pad(text: str, length: int):
    end = length - len(text)

    return text + (" " * end)

def print_compilers(compilers: Compilers):
    length = max(
        34,
        max(
            len(compilers.CC),
            len(compilers.CXX),
            len(compilers.LD),
            len(compilers.AR),
            len(compilers.STRIP),
        ),
    )

    width = length + 21

    print("-" * width)
    print("| " + pad("Using the following utilities:", width - 4) + " |")
    print("-" * width)
    print("|     C Compiler | " + pad(compilers.CC, length) + " |")
    print("|   C++ Compiler | " + pad(compilers.CXX, length) + " |")
    print("|         Linker | " + pad(compilers.LD, length) + " |")
    print("|       Archiver | " + pad(compilers.AR, length) + " |")
    print("|          Strip | " + pad(compilers.STRIP, length) + " |")
    print("-" * width)
