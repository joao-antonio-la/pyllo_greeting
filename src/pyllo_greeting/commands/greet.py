from typing import Literal

def greet(
    name: str = None,
    tone: Literal["quick", "normal", "fancy"] = "normal"
) -> int:
    if tone == "quick":
        if name: print(f"Hi, {name}")
        else: print("Hi")

    elif tone == "fancy":
        if name: print(f"Greetings. It is truly a pleasure to acknowledge your existence, {name}")
        else: print("Greetings. It is truly a pleasure to acknowledge your existence")

    else:
        if name: print(f"Hello there, {name}")
        else: print("Hello there")
        
    return 0