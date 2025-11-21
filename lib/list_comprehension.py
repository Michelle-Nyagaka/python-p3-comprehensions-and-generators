#!/usr/bin/env python3

def return_evens(num_list):
    #returns a list of all even elements in the given sequence of integers
    return [e for e in num_list if e % 2 == 0]

def make_exclamation(sentence_list):
    #returns a list of sentences with exclamation marks at the end
    return [sentence + "!" for sentence in sentence_list]