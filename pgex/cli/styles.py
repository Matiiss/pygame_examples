"""
This file is a part of the 'Pygame Examples (pgex)' source code.
The source code is distributed under the MIT license.

Defines a few styles used by the CLI
"""

import random
from enum import Enum

from colorama import Fore

del Fore.__dict__["BLACK"]


class OutputStyle(Enum):
    """
    Enum containing different output styles
    to output text to the console.
    """

    RAINBOW_BOX = (
        "[n]",
        (
            (
                Fore.LIGHTYELLOW_EX,
                Fore.YELLOW,
                Fore.LIGHTGREEN_EX,
                Fore.GREEN,
                Fore.LIGHTCYAN_EX,
                Fore.CYAN,
                Fore.LIGHTMAGENTA_EX,
                Fore.MAGENTA,
                Fore.RED,
            )
        ),
    )
    RANDOM_BOX = (
        "[n]",
        random.sample(list(Fore.__dict__.values()), len(Fore.__dict__)),
    )
    PLAIN_BOX = ("[n]", "")

    RAINBOW_PERIOD = ("n.", RAINBOW_BOX[1])
    RANDOM_PERIOD = (
        "n.",
        RANDOM_BOX[1],
    )
    PLAIN_PERIOD = ("n.", "")
