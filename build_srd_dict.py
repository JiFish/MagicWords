# Reads srd.txt (expected to contain the text format srd)
# and outputs srd_dict.json, a json dictionary containing words and weights.
# top_100_words.txt (expected to contain the top 100 english words) is read and these words are removed from the output.

import re
import json
import math

legaliseLines = 14
currentLine = 0

# Open the text file for reading
with open('srd.txt', 'r', encoding='utf8') as file:
    # Initialize an empty dictionary to store the word counts
    word_counts = {}

    # Iterate over each line in the file
    for line in file:
        # Skipping leagalease
        currentLine += 1
        if currentLine <= legaliseLines:
            continue
        # Convert the line to lowercase to make word counting case-insensitive
        line = line.lower()
        # strip non alpha characters
        line = re.sub(r'[^a-z]', ' ', line)
        # Split the line into a list of words using whitespace as the delimiter
        words = line.split()

        # Iterate over each word in the list of words
        for word in words:
            # Strip out anything that isn't an alpha character
            word = re.sub(r'[^a-z]', '', word)
            # Exclude words of length 3 or less
            if len(word) < 4:
                continue
            # If the word is already in the dictionary, increment its count
            if word in word_counts:
                word_counts[word] += 1
            # Otherwise, add the word to the dictionary with a count of 1
            else:
                word_counts[word] = 1

# Read in top 100 words
with open("top_100_words.txt") as file:
    top_words = {line.strip() for line in file}

# Remove top 100 words from word_counts
word_counts = [(word, count) for (word, count) in word_counts.items() if word not in top_words]

# Flatten the weight curve
word_dict = {word: math.log10(count + 1) for word, count in dict(word_counts).items()}

# Sort by weight
word_dict = {k: v for k, v in sorted(word_dict.items(), key=lambda item: item[1], reverse=True)}

# write dictionary
with open('srd_dict.json', 'w') as file:
    json.dump(word_dict, file)

