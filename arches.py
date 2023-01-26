import platform

from enum import Enum

class TargetArch(Enum):
    x86_64 = 0,
    x86_32 = 1,
    arm64 = 2,
    arm32 = 3,
    rv64 = 4,
    ppc32 = 5,
    ppc64 = 6,
    wasm32 = 7,
    current = 8,
    
    @staticmethod
    def aliases():
        aliases = [
            "x64",
            "amd64",
            "x86",
            "i386",
            "i686",
            "armv8",
            "arm64v8",
            "aarch64",
            "armv7",
            "armhf",
            "rv",
            "riscv",
            "riscv64",
            "ppcle",
            "ppc",
            "ppc64",
            "ppc64le",
            "wasm",
            "browser",
            "web",
        ]
        
        return aliases

    @staticmethod
    def from_alias(alias: str):
        if (
            alias == "x64" or
            alias == "amd64"
        ):
            return TargetArch.x86_64

        if (
            alias == "x86" or
            alias == "i386" or
            alias == "i686"
        ):
            return TargetArch.x86_32

        if (
            alias == "armv8" or
            alias == "arm64v8" or
            alias == "aarch64"
        ):
            return TargetArch.arm64

        if (
            alias == "armv7" or
            alias == "armhf"
        ):
            return TargetArch.arm32

        if (
            alias == "rv" or
            alias == "riscv" or
            alias == "riscv64"
        ):
            return TargetArch.rv64

        if (
            alias == "ppcle" or
            alias == "ppc"
        ):
            return TargetArch.ppc32

        if (
            alias == "ppc64" or
            alias == "ppc64le"
        ):
            return TargetArch.ppc64

        if (
            alias == "wasm" or
            alias == "browser" or
            alias == "web"
        ):
            return TargetArch.wasm32

        if hasattr(TargetArch, alias):
            return TargetArch[alias]
        else:
            print("Unknown architecture: " + alias)
            exit(1)

    @staticmethod
    def keys():
        keys = TargetArch.__dict__.keys()
        actual = []

        for key in keys:
            if (
                not key.startswith("_") and
                key != "from_alias" and
                key != "aliases" and
                key != "keys" and
                key != "current_arch" and
                key != "options" and
                key != "from_option" and
                key != "get"
            ):
                actual.append(key)

        return actual
    
    @staticmethod
    def current_arch():
        machine = platform.machine()
        
        if (
            machine == "ia64" or
            machine == "x64" or
            machine == "x86_64"
        ):
            return TargetArch.x86_64
        
        if (
            machine == "ia32" or
            machine == "x86" or
            machine == "i386" or
            machine == "i686"
        ):
            return TargetArch.x86_32
        
        if (
            machine == "arm" or
            machine == "armv7l" or
            machine == "armhf"
        ):
            return TargetArch.arm32
        
        if (
            machine == "aarch64_be" or
            machine == "aarch64" or
            machine == "armv8b" or
            machine == "armv8l" or
            machine == "arm64"
        ):
            return TargetArch.arm64
        
        if (
            machine == "ppc" or
            machine == "ppcle"
        ):
            return TargetArch.ppc32
        
        if (
            machine == "ppc64" or
            machine == "ppc64le"
        ):
            return TargetArch.ppc64

        if hasattr(TargetArch, machine):
            return TargetArch[machine]
        else:
            return False
    
    @staticmethod
    def options():
        return TargetArch.keys() + TargetArch.aliases()
    
    @staticmethod
    def from_option(opt: str):
        if TargetArch.from_alias(opt) != False:
            return str(TargetArch.from_alias(opt)).replace("TargetArch.", "")
        else:
            print("Unknown architecture: " + opt)
            exit(1)
            
    @staticmethod
    def get(opt: str):
        if hasattr(TargetArch, opt):
            if opt == "current":
                return TargetArch.current_arch()
            else:
                return TargetArch[opt]
        else:
            print("Unknown architecture: " + opt)
            exit(1)
