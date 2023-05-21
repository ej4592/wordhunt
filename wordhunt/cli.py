import argparse

from wordhunt.game import WordHunt


def top_20_words():
    parser = argparse.ArgumentParser("CLI script that finds top wordhunt words")
    WordHunt.add_to_parser(parser)

    args = parser.parse_args()
    wordhunt = WordHunt.create_from_args(args)
    grid = wordhunt.solve()
    print(grid)
