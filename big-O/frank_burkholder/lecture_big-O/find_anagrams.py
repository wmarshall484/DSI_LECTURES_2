import numpy as np
import time
from collections import defaultdict
import matplotlib.pyplot as plt
import argparse
plt.rcParams.update({'font.size': 14})


def find_anagrams_m1(lst):
    time_start = time.time()
    result = []
    for word1 in lst:
        for word2 in lst:
            if word1 != word2 and sorted(word1) == sorted(word2):
                if word1 not in result:
                    result.append(word1)
                if word2 not in result:
                    result.append(word2)
    time_end = time.time()
    time_elapsed = time_end - time_start
    return (time_elapsed, result)


def find_anagrams_m2(lst):
    time_start = time.time()
    result = []
    d = defaultdict(list)
    for word in lst:
        d[str(sorted(word))].append(word)
    for key, value in d.items():
        if len(value) > 1:
            result.extend(value)
    time_end = time.time()
    time_elapsed = time_end - time_start
    return (time_elapsed, result)


def make_anagram_lst(all_anagrams, n_lst):
    return [list(np.random.choice(all_anagrams, size=n, replace=False)) for n
            in n_lst]


def plot_computation_time(n_lst, times_lst, title, label, color, fname,
                          keepopen=False):
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(1, 1, 1)
    ax.plot(n_lst, times_lst, 'o', color=color, label=label)
    ax.set_xlabel('n, number of words in input')
    ax.set_ylabel('computation time (s)')
    ax.set_xlim((0, max(n_lst)*1.1))
    ax.set_title(title)
    if keepopen == 'True':
        return ax
    else:
        ax.legend(loc='upper left', frameon=False)
        plt.tight_layout()
        plt.savefig(fname,  dpi=100)
        plt.close()
        return None


def plot_fit(x, y, p, fname, ax):
    if len(p) == 2:
        label = f'fit: {p[0]:0.1e}n + {p[1]:0.1e}'
    else:
        label = f'fit: {p[0]:0.1e}n^2 + {p[1]:0.1e}n + {p[2]:0.1e}'
    ax.plot(x, y, 'k:', label=label)
    ax.legend(loc='upper left', frameon=False)
    plt.tight_layout()
    plt.savefig(fname,  dpi=100)
    plt.close()


def get_averaged_computation_times(all_anagrams, n_lst, num_times):
    result_shape = (num_times, len(n_lst))
    computation_times_m1 = np.zeros(result_shape)
    computation_times_m2 = np.zeros(result_shape)
    for i in range(num_times):
        print(f"\nWord list {i+1}")
        anagrams_lst = make_anagram_lst(all_anagrams, n_lst)
        print("Method 1 - double for")
        anagram_results_m1 = [find_anagrams_m1(anagrams) for anagrams in anagrams_lst]
        print("Method 2 - use dictionary")
        anagram_results_m2 = [find_anagrams_m2(anagrams) for anagrams in anagrams_lst]
        computation_times_m1[i] = np.array([results[0] for results in anagram_results_m1])
        computation_times_m2[i] = np.array([results[0] for results in anagram_results_m2])
    comp_time_m1_avg = computation_times_m1.mean(axis=0)
    comp_time_m2_avg = computation_times_m2.mean(axis=0)
    return (comp_time_m1_avg, comp_time_m2_avg)


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument("-f", "--file", required=True, help="text file containing words")
    ap.add_argument("-m", "--mode", required=True, help="""mode determining
                    output. single: computation times based on one random
                    selection from word list, average: computation times based
                    on average of 10 random selections from word list""")
    ap.add_argument("-t", "--fit", required=True, help="""True or False: plot
                    polynomial fit on plots""")
    args = vars(ap.parse_args())

    all_anagrams = np.loadtxt(args['file'], dtype=str)
    max_n = all_anagrams.shape[0]
    n_step = max_n // 10
    n_lst = list(range(n_step, max_n, n_step))

    if args['mode'] == 'single':
        print("\nFinding computation times based on one selection from word list.")
        anagrams_lst = make_anagram_lst(all_anagrams, n_lst)
        print("Method 1 - double for")
        anagram_results_m1 = [find_anagrams_m1(anagrams) for anagrams in anagrams_lst]
        print("Method 2 - use dictionary")
        anagram_results_m2 = [find_anagrams_m2(anagrams) for anagrams in anagrams_lst]
        comp_times_m1 = [results[0] for results in anagram_results_m1]
        comp_times_m2 = [results[0] for results in anagram_results_m2]
    else:
        print("\nFinding computation times based on ten selections from word list.")
        comp_times_m1, comp_times_m2 = get_averaged_computation_times(all_anagrams, 
                                                               n_lst, num_times=10)

    if args['fit'] == 'True':
        p_m1 = np.polyfit(n_lst, comp_times_m1, deg=2)
        p_m2 = np.polyfit(n_lst, comp_times_m2, deg=1)
        x = np.linspace(0, max(n_lst)*1.1)
        y_m1 = np.polyval(p_m1, x)
        y_m2 = np.polyval(p_m2, x)

    print("\nPlotting")
    fname = 'm1_plot.png'
    ax = plot_computation_time(n_lst, comp_times_m1, title='method 1, double for',
                               label='m1: double for', color='blue', fname=fname,
                               keepopen=args['fit'])
    if args['fit'] == 'True':
        plot_fit(x, y_m1, p_m1, fname, ax)

    fname = 'm2_plot.png'
    ax = plot_computation_time(n_lst, comp_times_m2, title='method 2, use dictionary',
                               label='m2: use dict', color='green', fname=fname,
                               keepopen=args['fit'])
    if args['fit'] == 'True':
        plot_fit(x, y_m2, p_m2, fname, ax)

    print('\nComplete')

