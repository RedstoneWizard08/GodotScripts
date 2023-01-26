import os
import argparse
import subprocess

from targets import CompileTarget
from arches import TargetArch
from compile_types import CompileType

from compiler import get_compilers, print_compilers
from info import print_info

parser = argparse.ArgumentParser(
    prog = "Cross Godot Compiler",
    description = "A quick wrapper around the scons command line to make it \
        easier to compile Godot for other platforms.",
    epilog = "Created by RedstoneWizard08.",
)

parser.add_argument(
    "-t",
    "--target",
    choices = CompileTarget.keys(),
    default = "current",
    help = "The target operating system or platform to compile to.",
    nargs = 1,
    required = False,
    type = CompileTarget.from_option,
)

parser.add_argument(
    "-m",
    "--module",
    choices = CompileType.keys(),
    default = "default",
    help = "The module to build, like the editor or export templates.",
    nargs = 1,
    required = False,
    type = CompileType.from_option,
)

parser.add_argument(
    "-a",
    "--arch",
    "--architecture",
    choices = TargetArch.keys(),
    default = "current",
    help = "The target architecture to compile to.",
    nargs = 1,
    required = False,
    type = TargetArch.from_option,
)

parser.add_argument(
    "-l",
    "--llvm",
    type = bool,
    help = "Whether or not to use LLVM.",
    nargs = 1,
    default = False,
    required = False,
)

parser.add_argument(
    "-ld",
    "--lld",
    type = bool,
    help = "Whether or not to use LLD.",
    nargs = 1,
    default = False,
    required = False,
)

args = parser.parse_args()

lld = bool(args.lld if (type(args.lld) == str or type(args.lld) == bool) else args.lld[0])
llvm = bool(args.llvm if (type(args.llvm) == str or type(args.llvm) == bool) else args.llvm[0])

target = CompileTarget.get(args.target if type(args.target) == str else args.target[0])
module = CompileType.get(args.module if type(args.module) == str else args.module[0])
arch = TargetArch.get(args.arch if type(args.arch) == str else args.arch[0])

compilers = get_compilers(arch, llvm = llvm, lld = lld)
print_compilers(compilers)

target_name = str(target).replace("CompileTarget.", "")
module_name = str(module).replace("CompileType.", "")
arch_name = str(arch).replace("TargetArch.", "")

print_info(target_name, module_name, arch_name)

subprocess.run(
    [
        "scons",
        "platform=" + target_name,
        "target=" + module_name,
        "arch=" + arch_name,
    ],
    
    shell = True,
    cwd = os.curdir + "/godot"
)
