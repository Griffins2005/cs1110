"""
Analyzing word usage in persuasive vs unpersuasive arguments
in the Change My View subreddit

Author: STUDENTS: Griffins Lelgut(gkl39)
    Stubs: Lillian Lee (LJL2)
Version: STUDENTS: 5th May, 2025
    Stubs: Apr 26, 2025
"""

from extract_counts import compare_usage
from collections import Counter
import json
import os
# STUDENTS: add any needed imports here
from extract_counts import per_and_unper_counts


def report_usage(samples_file_list, target_words_lists):
    """
    Reports usage rates, for the words in each word list in target_words_lists,
    among persuasive vs nonpersuasive comments from the data in samples_file_list.

    Returns a string (rather than direct printing) for autograding purposes.

    Precondition:
    * samples_file_list is a list of the names of CMV json files in local
    directory named `samples`.
    * target_words_lists is a non-empty list of non-empty lists of non-empty
    lowercased strings.  For example, [['US', 'USA'], ['Canada', 'Mexico']]
    """
    # STUDENTS: only modify where indicated; leave the rest of
    # the code alone

    report_string = f"Files requested: {samples_file_list}\n"

    per_counts = Counter()
    nonper_counts = Counter()
    used_files = []

    for jfile_name in samples_file_list:
        jfile_path = os.path.join('samples', jfile_name)
        try:
            with open(jfile_path, 'r') as f:
                data = json.load(f)
        except FileNotFoundError:
            report_string += f"{jfile_name} is missing; skipping it.\n"
        else:

            used_files.append(jfile_name)
            results = per_and_unper_counts(data)
            pers    = results["per_counts"]
            nonpers = results["nonper_counts"]
            per_counts.update(pers)
            nonper_counts.update(nonpers)



             # STUDENTS: Implement this loop body so that:
             #  1. The Counters are appropriately updated with the results of
             #     running the appropriate function from file extract_counts
             #     on the contents of the files given by samples_file_list.
             #  2. If a file in samples_file_list is not found, the appropriate
             #     error message is added to report_string, rather than the
             #     program crashing.
             #  3. used_files becomes the list of names (jfile_name) for the
             #     files that were found
             # You can use the code we wrote in A4 for inspiration.

    #   STUDENTS: your additions should be *above* this line.
    report_string += ('Files used: '+ ', '.join(used_files) + '\n')

    try:
        for target_words in target_words_lists:
            usage_rates = compare_usage(target_words, per_counts, nonper_counts)

            report_string += f'Usage rates for {target_words}:\n'
            report_string += f'\t{usage_rates["persuasive rate"]*100:.3f}% '
            report_string += 'for persuasive texts\n'
            report_string += f'\t{usage_rates["nonpersuasive rate"]*100:.3f}% '
            report_string += 'for nonpersuasive texts\n'
    except ZeroDivisionError:
        report_string += '*** No data acquired ***\n'

    return report_string


def report_experiments():
    """
    Analyze word usage in the example files and the real CMV files.

    Returns a string with the report of the experiments
    """
    # define interesting lists of words to look at
    target_words_lists = [
        ['i'],
        ['i', 'me', 'my', 'mine'],
        ['you'],
        ['you', 'your', 'yours'],
        ['we', 'us', 'our', 'ours'],
        ['we'],
        ['delta']  # This should definitely lean towards persuasive
    ]

    # One fake file to test exception handling
    example_files = ['example_left.json',
                     'example_middle.json',
                     'example_right.json',
                     'fake_file.json']
    full_report =report_usage(example_files, target_words_lists)
    full_report += "\n\n"
    full_report += report_usage(["1k2kc3t_grocery_music.json",
                                    "2rpvc7_bench_clearing.json",
                                    "3mzc6u_tontine.json",
                                    "7xirrw_fisking.json",
                                    "bd2zne_contribute.json",
                                    "et9kvt_amazon.json",
                                    "5y58tv_grass.json"], target_words_lists)
    return full_report


if __name__ == '__main__':
    print(report_experiments())
