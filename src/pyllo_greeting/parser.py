from argparse import ArgumentParser
from pyllo_greeting.commands import credits, version
from pyllo_greeting.commands import greet 

app_parser = ArgumentParser(
    prog="pyllo",
    description="A simple CLI tool to test Python distribution."
)

# Positional argument: name. Whatever the app will greet.
app_parser.add_argument("name", type=str, nargs="?", help="Name of the person to greet")

# Separate flags for tones
app_parser.add_argument("-q", "--quick", action="store_true", help="Greet with a quick tone")
app_parser.add_argument("-f", "--fancy", action="store_true", help="Greet with a fancy tone")

# Meta flags
app_parser.add_argument("-v", "--version", action="store_true", help="Show the app version")
app_parser.add_argument("-c", "--credits", action="store_true", help="Show project credits")

def run():
    """Command's execution based on user's inputs."""
    args = app_parser.parse_args()
    
    if args.version:
        return version()
    elif args.credits:
        return credits()
    
    tone = "normal"
    if args.quick:
        tone = "quick"
    elif args.fancy:
        tone = "fancy"
    
    return greet(name=args.name, tone=tone)