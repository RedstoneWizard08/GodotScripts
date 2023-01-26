import platform

from enum import Enum

class CompileTarget(Enum):
    linuxbsd = 0,
    windows = 1,
    macos = 2,
    android = 3,
    uwp = 4,
    web = 5,
    current = 6,
    
    @staticmethod
    def current_target():
        if platform.system() == "Linux":
            return CompileTarget.linuxbsd

        if platform.system() == "Windows":
            return CompileTarget.windows

        if platform.system() == "Darwin":
            return CompileTarget.macos
    
    @staticmethod
    def keys():
        keys = CompileTarget.__dict__.keys()
        actual = []

        for key in keys:
            if (
                not key.startswith("_") and
                key != "keys" and
                key != "current_target" and
                key != "from_option" and
                key != "get"
            ):
                actual.append(key)

        return actual

    @staticmethod
    def from_option(opt: str):
        if hasattr(CompileTarget, opt):
            return opt
        else:
            print("Unknown target: " + opt)
            exit(1)
            
    @staticmethod
    def get(opt: str):
        if hasattr(CompileTarget, opt):
            if opt == "current":
                return CompileTarget.current_target()
            else:
                return CompileTarget[opt]
        else:
            print("Unknown target: " + opt)
            exit(1)
