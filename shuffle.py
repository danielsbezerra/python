#!/usr/bin/env python3

import random

def shuffle_text(text):
    shuffled_text = text.lower().replace(' ','')
    l = list(shuffled_text)
    random.shuffle(l)
    return ''.join(l)

def main():
    #obter nome do banco
    db_text = 'Daniel Souza Bezerra'
    shuffled_text = shuffle_text(db_text)
    print(shuffled_text)

if __name__ == '__main__': main()