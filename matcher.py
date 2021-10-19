import Levenshtein
from ngram_matcher import find_ngram_match

from constants import LOOKUP_DICT

INVERSE_LOOKUP_DICT = dict()
for key in LOOKUP_DICT:
    for item in LOOKUP_DICT[key]:
        INVERSE_LOOKUP_DICT[item] = key


def lookup(text):

    # either returns matching value or raises KeyError
    try:
        return INVERSE_LOOKUP_DICT[text]
    except KeyError as e:
        # print("lookup: Matching phrase not found, return empty string")
        # return empty string to denote 'No match found'
        return ""


def find_match(phrase):
    # try:
    #     match = lookup(phrase)
    # except KeyError:
    #     # print("find_match: lookup function raised KeyError. Next step for matching is levenshtein")
    #     score_dict = dict()
    #     # Find distance of phrase from all keys
    #     for key in LOOKUP_DICT:
    #         score_dict[key] = Levenshtein.distance(phrase, key)
    #     match = min(score_dict, key=score_dict.get)
    # return match
    try:
        match = lookup(phrase)
        if match == "":
            # Match not found in lookup, try ngram
            match = find_ngram_match(phrase, LOOKUP_DICT.keys())
        if match == "":
            # Match not found after ngram lookup, try levenshtein
            score_dict = dict()
            for key in LOOKUP_DICT:
                score_dict[key] = Levenshtein.distance(phrase, key)
            match = min(score_dict, key=score_dict.get)
        return match
    except Exception as e:
        print("Exceptions:", e)
        raise e