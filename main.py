import random
# import tank
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
        main()

def game():
    pass

if __name__ == '__main__':
    main()

print('hello world')