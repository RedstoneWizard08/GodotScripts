from enum import Enum

class CompileType(Enum):
    editor = 0,
    templates = 1,
    template_debug = 2,
    template_release = 3,
    default = 4,

    @staticmethod
    def keys():
        keys = CompileType.__dict__.keys()
        actual = []

        for key in keys:
            if (
                not key.startswith("_") and
                key != "keys" and
                key != "from_option" and
                key != "get"
            ):
                actual.append(key)

        return actual
    
    @staticmethod
    def from_option(opt: str):
        if hasattr(CompileType, opt):
            return opt
        else:
            print("Unknown type: " + opt)
            exit(1)
            
    @staticmethod
    def get(opt: str):
        if hasattr(CompileType, opt):
            return CompileType[opt]
        else:
            print("Unknown type: " + opt)
            exit(1)
