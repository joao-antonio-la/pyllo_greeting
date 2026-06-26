import pytest
import sys
from pyllo_greeting.parser import run

def test_cli_version(monkeypatch, capsys):
    """Simulate running: pyllo -v"""
    monkeypatch.setattr(sys, "argv", ["pyllo", "-v"])
    
    run()
    captured = capsys.readouterr()
    assert "0.2.0" in captured.out


def test_cli_greeting_with_name_and_tone(monkeypatch, capsys):
    """Simulate running: pyllo Carlos --fancy"""
    monkeypatch.setattr(sys, "argv", ["pyllo", "Carlos", "--fancy"])
    
    run()
    captured = capsys.readouterr()
    assert "Greetings. It is truly a pleasure to acknowledge your existence, Carlos" in captured.out


def test_cli_invalid_tone(monkeypatch):
    """Simulate running an invalid choice: pyllo --brutal"""
    monkeypatch.setattr(sys, "argv", ["pyllo", "--brutal"])
    
    with pytest.raises(SystemExit):
        run()