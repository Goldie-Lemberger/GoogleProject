import re

from auto_complete_pkg.auto_complete_data import AutoCompleteData
from trie_pkg.trie_node import Trie_node


class Trie(object):
    """The suffix tri object"""
    def __init__(self):
        """
        The trie_dir has at least the root node.
        The root node does not store any character
        """
        self.root = Trie_node("")

    def handle_insert (self, text):
        text = re.sub(r'[^a-z+ ' ']', '', text.lower())
        text = " ".join(text.split())
        return text

    def insert(self, word,file,line):
        """Insert a word into the suffix tree"""
        lower_word = self.handle_insert(word)
        for i in range(len(word)):
            node = self.root
            # Loop through each character in the word
            # Check if there is no child containing the character, create a new child for the current node
            # Assume the longest search sentence is 20 in length
            for char in lower_word[i:i+20:]:
                if char in node.children:
                    node = node.children[char]
                else:
                    # If a character is not found,
                    # create a new node in the trie_dir
                    new_node = Trie_node(char)
                    node.children[char] = new_node
                    node = new_node
            # the leaf of the suffix contains the full sentence node
            new_node = Trie_node(word)
            node.children[i] = new_node
            node = new_node
            # Mark the end of a word
            node.is_end = True

            # Increment the counter to indicate that we see this word once more
            node.counter += 1

            node.line=({"file":file,"line":line,"offset":i})

    def dfs(self, node, sub_string,score):
        """Depth-first traversal of the trie_dir
        Args:
            - node: the node to start with
            - sub_string: the current prefix, for tracing a
                word while traversing the suffix tree
        """
        if node.is_end:
            new_node = AutoCompleteData(node.char, node.line["file"], node.line["line"],node.line["offset"],score)
            self.output.append(new_node.get_data())

        for child in node.children.values():
            self.dfs(child, sub_string + node.char,score)

    def query(self, x,score):
        """Given an input (sub string), retrieve all words stored in
        the trie with that sub string, sort the words by the number of
        times they have been inserted
        """

        # Use a variable within the class to keep all possible outputs
        # As there can be more than one word with such sub string
        self.output = []
        node = self.root

        # Check if the sub string is in the trie

        score = len(x)*2 - score

        for char in x:
            if char == '*':
                continue
            if char in node.children:
                node = node.children[char]

            else:
                # cannot found the prefix, return empty list
                return []

        # Traverse the trie_dir to get all candidates
        self.dfs(node, x[:-1],score)

        # Sort the results in reverse order and return
        return  self.output


