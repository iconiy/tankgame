import random
import tank as tank
# import infantry


def main():
    intro()
    rules()
    game()
    quit()

def intro():
    print('~~~~~~~~~~~~~~~~~~~~~~~')
    print('~~~~~ Tank Time! ~~~~~~')
    print('~~~~~~~~~~~~~~~~~~~~~~~')

def rules():
    def text_rules():
        print('Rules:')
    text_rules()
    again = input('Press t to read the rules again! ')
    if again == 't':
        text_rules()
    else:
        input('Press Enter to continue...')

def game():
    t = tank.Tank(100, 25, 10, 15, 2) # sets starting stats for tank
    t.siege()
    t.siege()

if __name__ == '__main__':
    main()