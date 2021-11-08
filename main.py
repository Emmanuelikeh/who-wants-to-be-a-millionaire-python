from questions import QUESTION
from driving_func import usecount, checkpoint, amount, finaldecision
import random
import pygame
from pygame import mixer
applause = pygame.mixer.Sound("applause-crowd-cheering-sound-effect.mp3")


def main():
    mixer.init()
    print('------------------------------\n'
          'who wants to be a millionaire \n' +
          '------------------------------\n')
    print(
        'welcome to who wants to be a millionaire, a fun game show were our love for trivia is spread and we eargely crown our next Millionaire \n '
    )
    name = input('please introduce your self: ' +'\n')

    print('Glad you could be here ' + name + ' the questions would begin shortly \n')
    starterlife = 0
    life = {'A': 0, 'P': 0}
    for numbers in range(1, 16):
        lifelinescount = starterlife
        query = QUESTION.pop(random.randint(0, len(QUESTION) - 1))
        quiz = (query['question'])
        print(quiz)
        if lifelinescount < 2:
            use = input('Do your want to use your life lines, y or n?')
            if use == 'y':
                usecount(life, name)
                starterlife = starterlife + 1
            else:
                print('no problem')
        attempt = input('Type in your option letter' + '\n').upper()
        if attempt == (query['answer']):
            resp = 'That is right'
            change = str(amount(numbers))
            print(resp)
            print('You have currently made ' + change + ' dollars so far ')
            applause.play
            

            if numbers != 15:
                print('\n------ NEXT ROUND----- \n')
            if (numbers +1) in [5,11]:
                print('you have currently reached a check point round \n')

            continue
        else:
            resp = 'wrong'
            print(resp)
            break
    finaldecision(resp, numbers)
    print(
        'On behalf our producers and creators of this show i would like to say Thank you to all our viewers at home, and Happy Novemeber, see you next time'
    )


if __name__ == '__main__':
    main()
