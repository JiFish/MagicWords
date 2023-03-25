# MagicWords

A tiny script for generating SRD-related words. This isn't intended to be a generic utility, it's mostly just to show my working for my [100 magic items challenge](https://cme.jifish.co.uk/?100-magic-items-challenge).

## rollwords.py

Rolls two random words. One from `srd_dict.json` and one from `oxford.txt`.

## build_srd_dict.py

Builds `srd_dict.json` from `srd.txt` and `top_100_words.txt`.

`srd_dict.json` will contain a list of words from `srd.txt` weighted by frequency. Words in `top_100_words.txt` are excluded from the list.

## oxford.txt

Contains [The Oxford 3000 and the Oxford 5000](https://www.oxfordlearnersdictionaries.com/about/wordlists/oxford3000-5000) list of English words.

## srd.txt

Contains the [5e System Reference Document](https://dnd.wizards.com/resources/systems-reference-document).

## srd_dict.json

Output from `build_srd_dict.py`.

## top_100_words.txt

Contains a [list of the top 100 English words](https://en.wikipedia.org/wiki/Most_common_words_in_English).
