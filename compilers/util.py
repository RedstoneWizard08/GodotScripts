from arches import TargetArch

def get_cross_compiler_prefix(arch: TargetArch):
    arch_str = str(arch).replace("TargetArch.", "")
    
    if arch == TargetArch.x86_64:
        return ("x86_64-linux-gnu-", "-x86-64-linux-gnu")
    elif arch == TargetArch.x86_32:
        return ("i686-linux-gnu-", "-i686-linux-gnu")
    elif arch == TargetArch.arm64:
        return ("aarch64-linux-gnu-", "-aarch64-linux-gnu")
    elif arch == TargetArch.arm32:
        return ("arm-linux-gnueabihf-", "-arm-linux-gnueabihf")
    elif arch == TargetArch.rv64:
        return ("riscv64-linux-gnu-", "-riscv64-linux-gnu")
    elif arch == TargetArch.ppc32 or arch == TargetArch.ppc64:
        return ("powerpc64le-linux-gnu-", "-powerpc64le-linux-gnu")
    elif arch == TargetArch.wasm32:
        return ("", "")
    else:
        print("Could not detect compiler! Unknown architecture: " + arch_str)
        exit(1)

def get_compiler_name(arch: TargetArch, cpp = False):
    if arch == TargetArch.wasm32:
        return "em++" if cpp else "emcc"
    else:
        return "g++" if cpp else "gcc"
