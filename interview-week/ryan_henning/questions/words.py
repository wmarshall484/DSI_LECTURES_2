import requests
import matplotlib.pyplot as plt
import os


def download_vocab(vocab_file_url, vocab_file_path):
    r = requests.get(vocab_file_url)
    with open(vocab_file_path, 'w') as f:
        f.write(r.text)


def load_vocab(vocab_file_path):
    with open(vocab_file_path) as f:
        vocab = {word.strip() for word in f}
    return vocab


def insert_spaces(string, vocab):
    if not string:    # len(string) == 0
        return ['']
    solns = []
    for i in xrange(1, len(string)+1):
        w = string[:i]
        if w in vocab:
            next_solns = insert_spaces(string[i:], vocab)
            for next_soln in next_solns:
                solns.append((w + ' ' + next_soln).strip())
    return solns


def show_exponential_growth():
    x = []
    y = []

    for i in range(1, 15):
        num_solns = len(insert_spaces('atop' * i, vocab))
        print i, num_solns
        x.append(i)
        y.append(num_solns)

    plt.plot(x, y)
    plt.show()


def print_example(string):
    print string
    solns = insert_spaces(string, vocab)
    for soln in solns:
        print '  ', soln
    print 'len(solns) =', len(solns)
    print


if __name__ == '__main__':

    vocab_file_path = 'vocab.txt'
    vocab_file_url = 'http://goo.gl/NEdffT'

    if not os.path.isfile(vocab_file_path):
        download_vocab(vocab_file_url, vocab_file_path)

    vocab = load_vocab(vocab_file_path)

    print_example('applepie')
    print_example('appleseed')
    print_example('acornbread')
    print_example('aortacoat')
    print_example('aortacorn')
    print_example('atopicend')
    print_example('lambsforlife')
    print_example('lambsalt')
    print_example('themonkeyisinthetree')
    print_example('atop' * 3)

    #show_exponential_growth()

