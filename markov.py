"""Generate Markov text from text files."""

from random import choice
import sys


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    read_file = open(file_path)
    massive_string = read_file.read()

    print massive_string

    return massive_string


def make_chains(text_string, n_length):
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

    #ORIGINAL WORKING VERSION OF MAKE_CHAINS

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

    #ALTERNATIVE OF MAKE_CHAINS

    # decided wasn't best to wrap back around ...
    # bigram
    #for i in range(len(words)-2):

        #if i == (len(words) - 1):
            #key = (words[i], words[i+1])
            #chains[key] = []
        #elif i == (len(words)):
            #pass
        #else:
        #key = (words[i], words[i+1])
        #if key in chains:
            #chains[key].append(words[i+2])
        #else:
            #chains[key] = []
            #chains[key].append(words[i+2])

    for i in range(len(words) - n_length):
        print i
        key = []
        for word in words[i:(i + n_length)]:
            key.append(word)

        print key

        key = tuple(key)

        if key in chains:
            chains[key].append(words[i + n_length])
        else:
            chains[key] = []
            chains[key].append(words[i + n_length])

    return chains


def make_text(chains):
    """Return text from chains."""

    words = []

    starting_point = choice(chains.keys())
    starting_words = [word for word in starting_point]
    words.extend(starting_words)

    while starting_point in chains:

        next_word = choice(chains[starting_point])
        words.append(next_word)
        starting_point = [word for word in starting_point[1:]] + [next_word]
        starting_point = tuple(starting_point)
        #stopping_point = starting_point[1][-1]
        #if len(words) > 50 and stopping_point == "?":
        #    break

    return " ".join(words)


input_path = sys.argv[1]

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain (makes 'chains dictionary')
chains = make_chains(input_text, 2)
print chains

# Produce random text
random_text = make_text(chains)

print random_text



