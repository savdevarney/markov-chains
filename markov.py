"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    read_file = open(file_path)
    massive_string = read_file.read()

    return massive_string


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """
    # dictionary
    chains = {}

    #list of strings of all words in text
    words = text_string.split()

    #list of tuples to represent keys in dictionary
    # key_list = []
    # for i in range(len(words)):
    #     if i == (len(words) - 1):
    #         key = (words[i], words[0])
    #         key_list.append(key)
    #     else:
    #         key = (words[i], words[i + 1])
    #         key_list.append(key)

    # for key in key_list:
    #     chains[key] = []

    # for i in range(len(words)):
    #     index_key = (words[i - 2], words[i - 1])
    #     chains[index_key].append(words[i])

    for i in range(len(words)):
        word = words[i]
        if i == (len(words) - 1):
            key = (words[i], words[0])
            chains[key] = []
            chains[key].append(words[1])
        elif i == (len(words) - 2):
            key = (words[i], words[-1])
            chains[key] = []
            chains[key].append(words[-1])
        else:
            key = (words[i], words[i+1])
            chains[key] = []
            chains[key].append(words[i+3])

    return chains


def make_text(chains):
    """Return text from chains."""

    words = []

    starting_point = choice(chains.keys())
    words.extend([starting_point[0], starting_point[1]])

    while True:
        next_word = choice(chains[starting_point])
        words.append(next_word)
        starting_point = (starting_point[1], next_word)
        stopping_point = starting_point[1][-1]
        if len(words) > 50 and stopping_point == "?":
            break

    print words
    return " ".join(words)


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)


# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print random_text

open_and_read_file("green-eggs.txt")
