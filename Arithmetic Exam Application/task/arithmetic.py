from random import randint, choice
from textwrap import dedent


def do_op(a, op, b) -> int:
    match op:
        case '+':
            return a+b
        case '-':
            return a-b
        case '*':
            return a*b


def get_input() -> int:
    while True:
        try:
            return int(input())
        except ValueError:
            print('Incorrect format.')


description = {
    1: 'simple operations with numbers 2-9',
    2: 'integral squares of 11-29'
}

print(dedent(f'''\
    Which level do you want? Enter a number:
    1 - {description[1]}
    2 - {description[2]}\
    '''))

level = get_input()
mark = 0
match level:
    case 1:
        for _ in range(5):
            a1, b1 = randint(2, 9), randint(2, 9)
            op = choice(['+', '-', '*'])
            print(a1, op, b1)

            line = get_input()

            if do_op(a1, op, b1) == line:
                print('Right!')
                mark += 1
            else:
                print('Wrong!')
    case 2:
        for _ in range(5):
            a = randint(11, 29)
            print(a)

            line = get_input()

            if a*a == line:
                print('Right!')
                mark += 1
            else:
                print('Wrong!')

print(f'Your mark is {mark}/5.')
print('Would you like to save your result to the file? Enter yes or no.')

line = input()
match line:
    case 'yes' | 'YES' | 'y' | 'Yes':
        print('What is your name?')
        name = input()
        with open('results.txt', 'a') as f:
            f.write(f'{name}: {mark}/5 in level {level} ({description[level]})')
        print('The results are saved in "results.txt".')
    case _:
        pass
