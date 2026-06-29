import pytest
from pyllo_greeting.commands import greet, random_greet, version, credits

def test_version_output(capsys):
    """Ensure the version function prints the correct version string."""
    exit_code = version()
    captured = capsys.readouterr()
    
    assert exit_code == 0
    assert captured.out.strip() == "1.1.2"

def test_credits_output(capsys):
    """Ensure credits output contains key author details."""
    exit_code = credits()
    captured = capsys.readouterr()
    
    assert exit_code == 0
    assert "João Antônio" in captured.out
    assert "https://github.com/joao-antonio-la" in captured.out

@pytest.mark.parametrize("name, tone, expected", [
    (None, "normal", "Hello there.\n"),
    ("Alice", "normal", "Hello there, Alice.\n"),
    (None, "quick", "Hi.\n"),
    ("Bob", "quick", "Hi, Bob.\n"),
    (None, "fancy", "Greetings. It is truly a pleasure to acknowledge your existence.\n"),
    ("Charlie", "fancy", "Greetings. It is truly a pleasure to acknowledge your existence, Charlie.\n"),
])
def test_greet_tones(capsys, name, tone, expected):
    """Test all combinations of names and tones."""
    exit_code = greet(name=name, tone=tone)
    captured = capsys.readouterr()
    
    assert exit_code == 0
    assert captured.out == expected

def test_random_greet_with_name(capsys):
    """Ensure that when a name is provided, it always appears in the output."""
    name = "João"
    exit_code = random_greet(name=name)
    captured = capsys.readouterr()
    
    assert exit_code == 0
    assert name in captured.out

def test_random_greet_without_name(capsys):
    """Ensure that when no name is provided, the output doesn't contain a stray comma."""
    exit_code = random_greet(name=None)
    captured = capsys.readouterr()
    
    assert exit_code == 0
    assert ", " not in captured.out