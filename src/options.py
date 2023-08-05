#!/usr/bin/env python3
from dataclasses import dataclass

@dataclass
class ChooseOptions:
	"""Prefix to show on item that corresponds to the cursor position [default: >]"""
	cursor: str

@dataclass
class ConfirmOptions:
    """The title of the affirmative action [default: Yes]"""
    affirmative: str = None
    """The title of the negative action [default: No]"""
    negative: str = None
    """Default confirmation action [default: affirmative]"""
    default: str = None
    """Timeout for confirmation [default: 0]"""
    timeout: int = None

@dataclass
class FileOptions:
    """The path to the folder to begin traversing"""
    path: str = None
    """The cursor character [default: >]"""
    cursor: str = None
    """Show hidden and 'dot' files [default: false]"""
    all: bool = None
    """Allow files selection [default: true]"""
    file: bool = None
    """Allow directories selection [default: false]"""
    directory: bool = None

@dataclass
class InputOptions:
    """Placeholder value [default: Type something...]"""
    placeholder: str = None
    """Prompt to display [default: >]"""
    prompt: str = None
    """Cursor mode [default:blink]"""
    cursor_mode: str = None
    """Initial value (can also be passed via stdin) [default: ""]"""
    value: str = None
    """Maximum value length (0 for no limit [default: 400]"""
    char_limit: int = None
    """ Input width (0 for terminal width) [default: "40"]"""
    width: int = None
    """Mask input characters [default: false]"""
    password: bool = None
    """Header value [default: ""]"""
    header: str = None
    """Timeout until input aborts [default: 0]"""
    timeout: int = None

if __name__ == "__main__":
    print('This is not a script.')