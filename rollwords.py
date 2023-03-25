# Picks one random word from srd_dict.yaml weighted. (See build_srd_dict.py for creation method)
# Picks one random word from oxford.txt

import random
import json

def get_random_word(word_dict):
    # Initialize variables
    N = sum(count for _, count in word_dict.items())
    random_word = None
    weight_sum = 0

    target = random.random()
    for word, count in word_dict.items():
        weight = count / N
        weight_sum += weight
        if target < weight_sum:
            random_word = word
            break

    return random_word

# Open the YAML file for reading
with open('srd_dict.json', 'r') as file:
    # Load the contents of the file into a dictionary
    word_dict = json.load(file)
with open('oxford.txt') as f:
    full_dict = f.read().splitlines()
pick1 = get_random_word(word_dict)
pick2 = "";
# Pick 2 must be over 2 characters, and not pick1
while (len(pick2) <= 2 or pick1 == pick2):
    pick2 = random.choice(full_dict)

print("{} {}".format(pick1, pick2))
