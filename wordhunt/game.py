import argparse
import pickle
import string


class WordHunt:
    """assert letter list is 25 later"""

    def __init__(self, letterlist, size=4):
        self.board = WordHunt.setup_board(letterlist, size)
        self.size = size

    def add_to_parser(parser: argparse.ArgumentParser()):
        parser.add_argument(
            "--letters", nargs="+", help="letters read like a book",
        )

    @classmethod
    def create_from_args(cls, args: argparse.Namespace):
        return cls(args.letters)

    @staticmethod
    def setup_board(letterlist, size=4):
        board = []
        row = []
        counter = 0
        for i in letterlist:
            counter += 1
            row.append(i)
            if counter % size == 0:
                board.append(row)
                row = []
        return board

    def valid_surrounding_tiles(self, tile_position):
        x, y = tile_position
        surrounding = [
            (x + 1, y),
            (x + 1, y + 1),
            (x, y + 1),
            (x - 1, y + 1),
            (x - 1, y),
            (x - 1, y - 1),
            (x, y - 1),
            (x + 1, y - 1),
        ]
        valid = []
        for i in surrounding:
            x, y = i
            if x < self.size and x >= 0 and y < self.size and y >= 0:
                valid.append((x, y))

        return valid

    def solve(self):
        new_root = pickle.load(open("trie", "rb"))  # trie structure
        # next = new_root.get_child("b")
        # next = next.get_child("o")
        # next = next.get_child("o")
        # next = next.get_child("m")
        # next = next.get_child("i")
        # next = next.get_child("e")
        # next = next.get_child("s")
        # next = next.get_child("t")
        # print(next.valid

        final_valid_list = []

        def possible_valid_words(x, y):
            valid_words = []
            potential_wordlist = []
            curr_node = new_root.get_child(self.board[x][y])
            # print(counter)
            seen = []
            seen.append((x, y))
            potential_wordlist.append((curr_node, (x, y), seen))

            # print(valid_words)
            # DFS here
            while len(potential_wordlist) != 0:
                pot_word, (x, y), seen = potential_wordlist.pop(0)
                if pot_word.valid:
                    word = ""
                    word = pot_word.letter + word
                    curr_node = pot_word
                    # print(counter)
                    while curr_node.parent != None:
                        curr_node = curr_node.parent
                        word = curr_node.letter + word

                    # print(word)

                    if len(word) > 2:
                        # print(word)
                        valid_words.append(word)

                for i in self.valid_surrounding_tiles((x, y)):
                    x2, y2 = i
                    if seen.count((x2, y2)) == 0:
                        # print((x2,y2))
                        new_letter = self.board[x2][y2]
                        if pot_word.has_child(new_letter):
                            child_node = pot_word.get_child(new_letter)
                            seen2 = seen.copy()
                            seen2.append((x2, y2))
                            potential_wordlist.append((child_node, (x2, y2), seen2))

            valid_words = WordHunt.unique(valid_words)
            valid_words.sort(key=len)
            valid_words.reverse()
            return valid_words

        for x in range(self.size):
            for y in range(self.size):
                final_valid_list.extend(possible_valid_words(x, y))

        final_valid_list = WordHunt.unique(final_valid_list)
        final_valid_list.sort(key=len)
        final_valid_list.reverse()
        return final_valid_list

        # bfs

    @staticmethod
    def exists(word):
        curr = pickle.load(open("trie", "rb"))  # trie structure
        for i in word:
            if curr.has_child(i):
                curr = curr.get_child(i)
            else:
                return False
        return curr.valid

    @staticmethod
    def unique(list1):

        # initialize a null list
        unique_list = []

        # traverse for all elements
        for x in list1:
            # check if exists in unique_list or not
            if x not in unique_list:
                unique_list.append(x)
        return unique_list


def main():
    print("hello")
    # letterlist = [
    #     "e",
    #     "a",
    #     "t",
    #     "a",
    #     "t",
    #     "r",
    #     "r",
    #     "a",
    #     "c",
    #     "m",
    #     "e",
    #     "s",
    #     "e",
    #     "i",
    #     "i",
    #     "s",
    # ]
    # # print(len(letterlist))
    # wh = WordHunt(letterlist)
    # # print(wh.board)
    # grid = wh.solve()
    # print(grid[0:10])
