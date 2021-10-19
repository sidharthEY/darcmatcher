from re import match
from nltk.tokenize import word_tokenize
from nltk.util import ngrams

def get_ngrams(text_tokens, n):
    """
    splits the given text into phrases containing n consecutive words
    Args:
        text_tokens(list): The ordered list of tokenized text to form ngrams
        n(int): size of split
    Returns:
        (list): list of phrases with word-length = n
    """
    ngram_generator = ngrams(text_tokens, n)
    return [' '.join(grams) for grams in ngram_generator]

def find_ngram_match(phrase, headings):
    """
    Splits the longer sentence into ngrams and checks the list for matches
    Args:
        phrase(str): string to be matched
        keys(str): list of keys to which the phrase must be matched
    """
    match_found = False     #initializing variable
    phrase_tokens = word_tokenize(phrase)
    for heading in headings:
        ngram_combo_list = []
        heading_tokens = word_tokenize(heading)
        heading_tokens_len = len(heading_tokens)
        phrase_tokens_len = len(phrase_tokens)
        if heading_tokens_len >= phrase_tokens_len:
            ngram_combo_list = get_ngrams(heading_tokens, phrase_tokens_len)
            match_found = phrase in ngram_combo_list
        else:
            ngram_combo_list = get_ngrams(phrase_tokens, heading_tokens_len)
            match_found = heading in ngram_combo_list
        if match_found:
            # if match is found, return the heading ending the for loop
            return heading
    #TODO: Check if this is the standard approach
    return ""       # return empty string to denote no match is found
    
