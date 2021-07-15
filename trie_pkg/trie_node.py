class Trie_node:
    """A node in the trie structure"""
    def __init__(self, char):
        # the character stored in this node
        self.char = char

        # whether this can be the end of a word
        self.is_end = False

        # a dictionary of word information (whether this is the end)
        self.line = {}

        # a dictionary of child nodes
        # keys are characters, values are nodes
        self.children = {}

        self.counter = 0


