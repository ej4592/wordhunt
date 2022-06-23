import argparse

from wordhunt.game import WordHunt


def top_20_words():
    parser = argparse.ArgumentParser("CLI script that finds top wordhunt words")
    WordHunt.add_to_parser(parser)

    args = parser.parse_args()
    print(args.letters)
    wordhunt = WordHunt.create_from_args(args)
    print(WordHunt.exists("boomiest"))
    # grid = wordhunt.solve()
    #print(grid.index("steam"))
    # print(grid)
