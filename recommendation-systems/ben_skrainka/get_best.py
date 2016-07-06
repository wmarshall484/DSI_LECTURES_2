# get_best.py - copy Slack rec_runner results into a text file list top scores

import sys
import re
import operator

def get_data(in_file):
    with open(in_file, "r") as f:
        lines = f.readlines()
    return lines


def get_scores(lines):
    scores = []
    b_got_user = False
    user = None
    for line in lines:
        if b_got_user:
            score = float(line.split()[-1])
            scores.append((user, score,))
            b_got_user = False
            user = None
        else:
            tokens = line.split()
            if len(tokens) >= 3:
                if tokens[1] == 'BOT':
                    b_got_user = True
                    user = tokens[0]
                else:
                    b_got_user = False

    return scores


def main():
    if len(sys.argv) != 2:
        print "Usage: python get_best.py <score_file>"
        sys.exit(-1)

    # load data
    in_file = sys.argv[1]
    lines = get_data(in_file)

    scores = get_scores(lines)
    scores = sorted(scores, key=operator.itemgetter(1), reverse=True)
    return scores

if __name__ == '__main__':
    scores = main()
    for ix, val in enumerate(scores[:20]):
        print ix, val
