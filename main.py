from apriori import Apriori
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Apriori algorithm for groceries dataset.")
    parser.add_argument('-s', '--support', default=0.02, type=float)
    parser.add_argument('-c', '--confidence', default=0.3, type=float)
    parser.add_argument('-f', '--file', default="groceries.csv")
    args = parser.parse_args()

    apriori = Apriori(args.file, _support=args.support, _confidence=args.confidence)
    apriori.expand()
    apriori.make_res()
    apriori.print_res()
