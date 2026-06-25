from importlib import metadata

def version():
    """Prints out the project's current version."""
    print(metadata.version("pyllo"))
    
    return 0

def credits():
    """Print's out the credits of the ones involved in the project."""
    print("Project created by:")
    print("\tJoão Antônio")

    print("\nAuthor's GitHub:")
    print("\thttps://github.com/joao-antonio-la")

    print("\nProject's Repository:")
    print("\thttps://github.com/joao-antonio-la/pyllo")

    return 0