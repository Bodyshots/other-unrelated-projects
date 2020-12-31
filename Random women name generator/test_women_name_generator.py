""" Random women name generator for the bootleg seducer game """

from random import choice
from sys import exit

def main():
    with open('women_first_names.txt') as f:
        first_names = f.read().split('\n')
    with open('last_names.txt') as f:
        last_names = f.read().split('\n')

    while True:
        prompt, name = '', ''
        prompt = input('Type in "s" to generate a new random name'\
                       ' or "q" to quit.\n')
        if prompt.lower() == 'q':
            exit()
        elif prompt.lower() == 's':
            name += choice(first_names) + ' ' + choice(last_names)
            print(name)

main()
