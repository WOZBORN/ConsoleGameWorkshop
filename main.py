# Игра "Виселица"
import random
from colorama import init, Fore

init(autoreset=True)

# Вводные параметры
word_list = ['питон', 'программа', 'разработчик', 'алгоритм', 'переменная']


def get_word() -> str:
    word = random.choice(word_list)
    return word.upper()


def display_hangman(tries: int) -> str:
    stages = [
        '''
            +-----+
            |     |
            |     O
            |    /|\\
            |    / \\
            |
          ========
        ''',
        '''
            +-----+
            |     |
            |     O
            |    /|\\
            |    / 
            |
          ========
        ''',
        '''
            +-----+
            |     |
            |     O
            |    /|\\
            |    
            |
          ========
        ''',
        '''
            +-----+
            |     |
            |     O
            |    /|
            |
            |
          ========
        ''',
        '''
            +-----+
            |     |
            |     O
            |     |
            |
            |
          ========
        ''',
        '''
            +-----+
            |     |
            |     O
            |    
            |
            |
          ========
        ''',
        '''
            +-----+
            |     |
            |     
            |    
            |    
            |
          ========
        ''',
    ]
    return stages[tries]


# Игровой цикл
def main():
    word = get_word()
    word_completed = '_' * len(word)
    guessed = False
    guessed_letters = []
    tries = 6

    print(Fore.CYAN +'Добро пожаловать в игру "Виселица"')
    print(Fore.MAGENTA + display_hangman(tries))
    print("Загаданное слово:", word_completed)
    print('\n')

    while not guessed and tries > 0:
        guess = input('Введи букву или слово целиком: ').upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print(Fore.YELLOW + 'Вы уже называли эту букву:', guess)
            elif guess not in word:
                print(Fore.RED + f'Буквы {guess} нет в слове...')
                tries -= 1
                guessed_letters.append(guess)
            else:
                print(Fore.GREEN + f'Буква {guess} есть в слове!')
                guessed_letters.append(guess)
                word_as_list = list(word_completed)
                for i in range(len(word)):
                    if word[i] == guess:
                        word_as_list[i] = guess
                word_completed = ''.join(word_as_list)
                if word_completed == word:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess == word:
                guessed = True
                word_completed = word
            else:
                print(Fore.RED + "Неверное слово...")
                tries -= 1
        else:
            print(Fore.RED + 'Нужно ввести букву или слово целиком!')

        print(Fore.MAGENTA + display_hangman(tries))
        print(Fore.MAGENTA + "Загаданное слово:", word_completed)
        print('\n')

    if guessed:
        print(Fore.GREEN + f"Ты угадал слово {word}!")
    else:
        print(Fore.RED + f"Ты проиграл! Слово было {word}...")

    if input('Хочешь повторить? (Да/Нет): ').upper() == 'ДА':
        main()
    else:
        print('Спасибо за игру!')

# Запуск программы
if __name__ == "__main__":
    main()