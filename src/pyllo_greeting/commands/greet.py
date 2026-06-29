from typing import Literal
import random

def greet(
    name: str = None,
    tone: Literal["quick", "normal", "fancy"] = "normal"
) -> int:
    if tone == "quick":
        if name: print(f"Hi, {name}.")
        else: print("Hi.")

    elif tone == "fancy":
        if name: print(f"Greetings. It is truly a pleasure to acknowledge your existence, {name}.")
        else: print("Greetings. It is truly a pleasure to acknowledge your existence.")

    else:
        if name: print(f"Hello there, {name}.")
        else: print("Hello there.")
        
    return 0

def random_greet(name: str = None) -> int:
    name_suffix = f", {name}" if name else ""
    
    phrases = [
        f"Hey there{name_suffix}.",
        f"Hi{name_suffix}.",
        f"Greetings. It is truly a pleasure to acknowledge your existence{name_suffix}.",
        f"Ahoy{name_suffix}!",
        f"It is an absolute honor to acknowledge your presence{name_suffix}.",
        f"Hey there{name_suffix}!",
        f"What's up{name_suffix}?",
        f"How's it going{name_suffix}?",
        f"Yo{name_suffix}!",
        f"Good to see you{name_suffix}.",
        f"Greetings{name_suffix}.",
        f"A very warm welcome to you{name_suffix}.",
        f"It is an absolute honor to acknowledge your presence{name_suffix}.",
        f"Good day{name_suffix}.",
        f"Salutations{name_suffix}.",
        f"Hello World! Special shoutout to you{name_suffix}.",
        f"Ahoy{name_suffix}!",
        f"Look who just spawned into the terminal{name_suffix}.",
        f"System check complete. Welcome{name_suffix}.",
    ]
    
    print(random.choice(phrases))
    return 0