import pickle


class Trie:
    def __init__(self, letter):
        self.letter = letter
        self.children = []
        self.parent = None
        self.valid = False

    def add_child(self, node):
        self.children.append(node)
        node.parent = self

    def has_child(self, letter):
        for n in self.children:
            if n.letter == letter:
                return True
        return False

    def get_child(self, letter):
        for n in self.children:
            if n.letter == letter:
                return n
        return None


def init_dictionary():
    dictionary = open("words", "r")
    root = Trie("")
    counter = 0
    for word in dictionary:
        word = word.strip()
        counter += 1
        if word.islower():
            print(word)
            curr_node = root
            for letter in word:
                # print(letter)
                if curr_node.has_child(letter):
                    # print(curr_node.valid)
                    curr_node = curr_node.get_child(letter)
                else:
                    new_node = Trie(letter)
                    curr_node.add_child(new_node)
                    curr_node = new_node
            curr_node.valid = True
            # print(curr_node.letter)

            # print(curr_node.valid)

    return root


def main():
    full_dict = init_dictionary()
    # print(full_dict.children)
    # full_dict.valid = True
    # print(full_dict.valid)

    # print(full_dict.valid)
    trie = open("trie", "wb")
    pickled_dict = pickle.dump(full_dict, trie)
    new_root = pickle.load(open("trie", "rb"))
