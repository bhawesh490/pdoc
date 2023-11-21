"""
A small `pdoc` example.
"""

class Dog:
    """🐕"""
    name: str
    """The name of our dog."""
    friends: list["Dog"]
    """The friends of our dog."""

    def __init__(self, name: str):
        """Make a Dog without any friends (yet)."""
        # this is for testing
        self.name = name
        self.friends = []

    def bark(self, loud: bool = True):
        """*woof* and *bark*"""