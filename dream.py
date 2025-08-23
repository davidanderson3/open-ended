"""Dream a little dream of ASCII stars.

This script prints a randomly generated field of stars to the terminal.
"""

import random


def generate_star_field(width: int = 40, height: int = 10, density: float = 0.15) -> str:
    """Return a string representing a field of stars.

    Args:
        width: The number of characters in each line.
        height: The number of lines to generate.
        density: The probability that any given character will be a star.
    """
    rows = []
    for _ in range(height):
        row = ''.join('*' if random.random() < density else ' ' for _ in range(width))
        rows.append(row)
    return "\n".join(rows)


if __name__ == "__main__":
    print("I drift into a cosmic dream...\n")
    print(generate_star_field())
