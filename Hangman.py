import random
from turtle import color
import pyfiglet
from colorama import Fore,Back,Style
text = pyfiglet.figlet_format(text = 'Welcome to the game', font = 'digital')
print(Fore.LIGHTYELLOW_EX+Back.LIGHTBLUE_EX+text+Style.RESET_ALL)


list_letter = ['A','a','B','b', 'C','c', 'D','d', 'E','e', 'F','f', 'G','g', 'H','h', 'I','i',
                'J','j', 'K','k', 'L','l','M','m', 'N','n', 'O','o', 'P','p', 'Q','q', 'R','r',
                'S','s', 'T','t','U','u', 'V','v', 'W','w', 'X','x', 'Y','y','Z','z']

show_list=()
final_answer=()

def categury(categur):
    name = ['nazi','masome','amin','faride','mahya','maral','mozhde','zhale','shadi']
    
    color =['green','blue','magenta','yellow','white','black','brown','gold','silver']

    body = ['head','shouldesr','eyes','ears','nose','lips','eyebrows','heart','brain']

    food = ['pasta','sandwich','pizza','hotdog','kebab','sushi','lobster','salad','hamburger']

    countrie = ['itly','china','japan','iran','switzerland','canada','france','germany']

    animal = ['cheeta','bird','panda','lama','horse','rabbit','lion','snake','kangaroo']

    computer = ['keyboard','mouse','fan','ports','hard','motherboard','speaker','usd port','webcam']

    sport = ['volleyball','squash','kickboxing','taekwondo','gymnastics','swimming','wrestling']

    fruit = ['watermelon','kiwi','strawberry','banana','peach',' pine apple','mango',]

while True:
    type = int(input('Choose: 1.Hard 2.Easy\n'))
    if type == 1:
        while True:
            selection = int(input('Choose your item\n1.name\n2.color\n3.body\n4.food\n5.countrie\n6.animal\n7.computer\n8.sport\n9.fruit\n'))
            if selection == 1:
                final_answer = random.choice(name)
                break
            elif selection == 2:
                final_answer = random.choice(color)
                break
            elif selection == 3:
                final_answer = random.choice(body)
                break
            elif selection == 4:
                final_answer = random.choice(food)
                break
            elif selection == 5:
                final_answer = random.choice(countrie)
                break
            elif selection == 6:
                final_answer = random.choice(animal)
                break
            elif selection == 7:
                final_answer = random.choice(computer)
                break
            elif selection == 8:
                final_answer = random.choice(sport)
                break
            elif selection == 9:
                final_answer = random.choice(fruit)
                break
            else:
                print('enter one number between 1 to 9 !!\n')
                continue
        show_list , wrong_list = [] , []
        for i in range (len(final_answer)):
            show_list.append('_')
        print(' '.join(show_list))
        while True:
            while True:
                print(list_letter)
                letter_user = input('Enter one letter: ')
                if ('a' <= letter_user <= 'z') or ('A' <= letter_user <= 'Z'):
                    break
                else:
                    print('enter  only one letter!')
                    continue
            letter_user = letter_user.lower()
            if letter_user == final_answer:
                print('Hoora, you won :)')
                break
            if len(letter_user) >= 2:
                letter_user = letter_user[0]
            if letter_user in wrong_list or letter_user in show_list:
                print('This is a duplicate letter, please try again.')
                continue
            if letter_user in list_letter:
                list_letter.remove(letter_user)
            count = len(final_answer)
            if final_answer.find(letter_user) == -1:
                wrong_list.append(letter_user)
            else:
                for i in range (len(final_answer)):
                    if final_answer[i] == letter_user:
                        show_list[i] = letter_user
                    else:
                        continue
            print('wrong =',wrong_list)
            print(' '.join(show_list))
            if len(wrong_list) == len(final_answer) + 1:
                print('Game over :(')
                break
            for i in show_list:
                if i != '_':
                    count -= 1
            if count == 0:
                print('Hoora, you won :)')
                break
            print('\n')
        break
    elif type == 2:
        while True:
            selection = int(input('Choose your item\n1.names\n2.animals\n3.colors\n4.fruits\n5.foods\n6.countries\n7.things\n'))
            if selection == 1:
                print(name)
                final_answer = random.choice(name)
                break
            elif selection == 2:
                print(color)
                final_answer = random.choice(color)
                break
            elif selection == 3:
                print(body)
                final_answer = random.choice(body)
                break
            elif selection == 4:
                print(food)
                final_answer = random.choice(food)
                break
            elif selection == 5:
                print(countrie)
                final_answer = random.choice(countrie)
                break
            elif selection == 6:
                print(animal)
                final_answer = random.choice(animal)
                break
            elif selection == 7:
                print(computer)
                final_answer = random.choice(computer)
                break
            elif selection == 8:
                print(sport)
                final_answer = random.choice(sport)
                break
            elif selection == 9:
                print(fruit)
                final_answer = random.choice(fruit)
                break
            else:
                print('enter one number between 1 to 9 !!\n')
                continue
        show_list , wrong_list = [] , []
        for i in range (len(final_answer)):
            show_list.append('_')
        print(' '.join(show_list))
        while True:
            while True:
                print(list_letter)
                letter_user = input('Enter one letter: ')
                if ('a' <= letter_user <= 'z') or ('A' <= letter_user <= 'Z'):
                    break
                else:
                    print('just enter only one letter!')
                    continue
            letter_user = letter_user.lower()
            if letter_user == final_answer:
                print('yeah, you won :)')
                break
            if len(letter_user) >= 2:
                letter_user = letter_user[0]
            if letter_user in wrong_list or letter_user in show_list:
                print('This is a duplicate letter, please try again.')
                continue
            if letter_user in list_letter:
                list_letter.remove(letter_user)
            count = len(final_answer)
            if final_answer.find(letter_user) == -1:
                wrong_list.append(letter_user)
            else:
                for i in range (len(final_answer)):
                    if final_answer[i] == letter_user:
                        show_list[i] = letter_user
                    else:
                        continue
            print('wrong =',wrong_list)
            print(' '.join(show_list))
            if len(wrong_list) == len(final_answer) + 1:
                print('Game over :(')
                break
            for i in show_list:
                if i != '_':
                    count -= 1
            if count == 0:
                print('yeah, you won :)')
                break
            print('\n')
        break
    else:
        print('Choose 1 or 2 !!')
        continue
