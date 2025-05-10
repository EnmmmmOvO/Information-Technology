# Poetry Generation Assignment Boilerplate
# =========================================
# In this assignment, you will build a probabilistic language model to generate poetry.
# Your tasks include:
#   - Reading and tokenizing a poetry dataset.
#   - Building a bigram language model with smoothing.
#   - Converting counts into probabilities.
#   - Generating poetry that adheres to a given rhyme scheme.
#
# Complete the functions marked with TODO.
import re
from collections import defaultdict
import random
import argparse

import pronouncing
import pandas as pd
from nltk import bigrams  # Using bigrams

import itertools


def tokenize(text):
    # Remove all digits from the input text
    text = re.sub(r'\d+', '', text)

    # Define a pattern to match words, accounting for possible apostrophes in contractions
    word_pattern = r"[’']?[A-Za-z]+(?:[’'][A-Za-z]+)*[’']?"
    # Define a token pattern that matches either the word pattern or any non-whitespace character
    token_pattern = f"{word_pattern}|[^\\sa-zA-Z]"

    # Return all matches of the token pattern in the text
    return re.findall(token_pattern, text)

def get_next_word(probs, words):
    # Uses probabilities (weights) to randomly select the next word.
    return random.choices(words, weights=probs, k=1)[0]


def get_rhyming_words(probs, words, vocab):
    # Convert the vocabulary to lowercase for case-insensitive matching.
    vocab_lower = {w.lower() for w in vocab}

    # Pair each word with its probability and filter for words that exist in the lowercase vocabulary.
    rhyming_candidates = [(w, p) for w, p in zip(words, probs) if w.lower() in vocab_lower]

    if not rhyming_candidates:
        return None

    # Unzip the list of tuples into separate lists of words and their probabilities.
    candidate_words, candidate_probs = zip(*rhyming_candidates)

    # Randomly choose one word from the candidates using the provided probabilities as weights.
    return random.choices(candidate_words, weights=candidate_probs, k=1)[0]


class ProbLangModel:
    def __init__(self):
        """
        Tasks for __init__:
         - Read a poetry dataset (e.g., 'poetry_dataset.tsv').
         - Tokenize the text to build a vocabulary.
         - Build a bigram model with smoothing (initialize counts).
         - Convert counts to probabilities.
        """
        self.model = defaultdict(lambda: defaultdict(lambda: 0))

        # Read the poetry dataset
        df = pd.read_csv("poetry_dataset.tsv", sep="\t", header=None)
        df.columns = ["index", "text", "sentiment"]
        df["tokenized"] = df["text"].apply(tokenize)

        # Build the vocabulary Set
        self.vocab = set(list(itertools.chain.from_iterable(df["tokenized"])))

        # Initialize counts with Laplace smoothing
        sorted_vocab = sorted(self.vocab)
        for w1 in sorted_vocab:
            for w2 in sorted_vocab:
                self.model[w1][w2] = 1

        # Calculate probs
        for sentence in df["tokenized"]:
            for w1, w2 in bigrams(sentence, pad_right=True, pad_left=True):
                if w1 is None or w2 is None:
                    continue
                self.model[w1][w2] += 1

        # OPTIONAL: calculate probabilities
        for w1 in self.model.keys():
            total = sum(self.model[w1].values())
            for w2 in self.model[w1]:
                self.model[w1][w2] /= total

    def calculate_next_word(self, context) -> str:
        # Given a context, calculate the next word using the probabilities in the model.
        context_probs = self.model[context]
        words = list(context_probs.keys())
        probs = list(context_probs.values())

        next_word = get_next_word(probs, words)

        # If the next word is None, raise an exception.
        if next_word is None:
            raise Exception("Next word is none")

        return next_word

    def generate_poetry(self, sentence, num_words_per_line=10, rhyme="ABAB"):
        """
        Tasks for generate_poetry:
         - Starting with the given sentence, generate text until num_words_per_line*4 words are produced.
         - Enforce a rhyme scheme (e.g., ABAB or AABB) by selecting words that rhyme at the end of lines.
         - Format and print the generated poetry.
        """
        # Tokenize the input sentence
        tmp = sentence.split(" ")[:4 * num_words_per_line]
        # Split the sentence into lines of num_words_per_line words
        text = [tmp[i:i + num_words_per_line] for i in range(0, len(tmp), num_words_per_line)]

        # Pad the text with empty lists to ensure that there are 4 lines
        while len(text) < 4:
            text.append([])

        for i in range(4):
            # Generate the next word for each line without the last word of each line
            while len(text[i]) < num_words_per_line - 1:
                # Use the last word as the context.
                context = text[i][-1] if len(text[i]) > 0 else text[i - 1][-1] if i > 0 else None
                if context not in self.model:
                    raise Exception(f"{context} is not in the vocabulary")

                # Retrieve the dictionary mapping next words to probs.
                text[i].append(self.calculate_next_word(context))

            rhyme_word = None


            if rhyme == "ABAB" and i >= 2:
                # If the rhyme scheme is ABAB and the current line is the third or fourth line
                rhyme_word = text[i - 2][-1]
            elif rhyme == "AABB" and i % 2 == 1:
                # If the rhyme scheme is AABB and the current line is the second or fourth line
                rhyme_word = text[i - 1][-1]

            if rhyme_word:
                # Get a list of words that rhyme with the rhyme_word
                vocab = pronouncing.rhymes(rhyme_word)

                context_probs = self.model[rhyme_word]
                words = list(context_probs.keys())
                probs = list(context_probs.values())

                # Get the next word that rhymes with the rhyme_word
                next_word = get_rhyming_words(probs, words, vocab)

                # If the next word is None, calculate the next word using the rhyme_word
                if next_word is None:
                    next_word = self.calculate_next_word(rhyme_word)

                text[i].append(next_word)
            else:
                # When a rhyming word appears for the first time, generate it normally.
                context = text[i][-1] if len(text[i]) > 0 else text[i - 1][-1] if i > 0 else None
                if context not in self.model:
                    raise Exception(f"{context} is not in the vocabulary")

                text[i].append(self.calculate_next_word(context))

        # Print the formatted text
        print("\n".join([" ".join(t) for t in text]))


# DO NOT MODIFY THE CODE BELOW
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Poetry generator")
    parser.add_argument("-s", "--seed", help="Seed", required=True, default=5, type=int)
    parser.add_argument(
        "-w",
        "--words_start",
        help="Starting words",
        required=True,
        default="and when they",
        type=str,
    )
    parser.add_argument(
        "-n",
        "--num_words_per_line",
        help="Number of words per line",
        required=True,
        default=10,
        type=int,
    )
    parser.add_argument(
        "-r",
        "--rhyme",
        help="Rhyme pattern",
        choices=["ABAB", "AABB"],
        required=True,
        default="ABAB",
        type=str,
    )

    args = parser.parse_args()

    # Set seed
    random.seed(args.seed)

    plm = ProbLangModel()
    print("step 1")
    plm.generate_poetry(
        args.words_start,
        num_words_per_line=args.num_words_per_line,
        rhyme=args.rhyme,
    )
