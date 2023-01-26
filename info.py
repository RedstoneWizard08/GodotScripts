def pad(text: str, length: int):
    end = length - len(text)

    return text + (" " * end)

def print_info(target: str, module: str, arch: str):
    width = max(
        26,
        max(
            len(target),
            len(module),
            len(arch),
        ),
    )

    padding = width - 14

    print("-" * width)
    print("| " + pad("Compilation settings:", width - 4) + " |")
    print("-" * width)
    print("|  Target | " + pad(target, padding) + " |")
    print("|  Module | " + pad(module, padding) + " |")
    print("|    Arch | " + pad(arch, padding) + " |")
    print("-" * width)
