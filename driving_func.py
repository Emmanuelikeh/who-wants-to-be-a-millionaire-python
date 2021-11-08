import random


def Asktheaudience():
    e = 100
    new_list = []
    for x in range(1, 5):
        n = random.uniform(1, e)
        e -= n
        new_list.append(round(n, 2))
    print(str(new_list[0]) + ' percent of the audience think the answer is A ')
    print(str(new_list[1]) + ' percent of the audience think the answer is B ')
    print(str(new_list[2]) + ' percent of the audience think the answer is C ')
    print(str(new_list[3]) + ' percent of the audience think the answer is D ')


def phoneafriend(name):
    friend = random.choice(['jessica', 'dave'])
    options = random.choice(['A', 'B', 'C', 'D', 'E'])

    if friend == 'jessica':
        print('Jessica is on the line')
        print('Hi ' + name , ' how are you doing')
        print(
            ' i have been made aware that your are contesting in who wants to be a millionaire'
        )
        if options in 'ABCD':
            print('I think the answer is ' + options)
        else:
            print(' I am sorry bro i have no idea')
    if friend == 'dave':
        print('Dave is on the line')
        print('Hi ' + name, ' how are you doing')
        print(
            'i have been made aware that your are contesting in who wants to be a millionaire'
        )
        if options in 'ABCD':
            print('I think the answer is ' + options)
        else:
            print(' I am sorry bro i have no idea')


# def optioncount():
#   if 'A' > 1:


def usecount(y,name):
    while True:
        print('you have on attempts per each life line')
        print(
            "Type 'A' if you would like to ask the audience or 'P' if you would like to phone a friend"
        )
        userinput = input().upper()
        if y[userinput] > 0:
            print('you have already used this lifeline, pick another one')
        else:
            y[userinput] += 1
            if userinput == 'A':
                Asktheaudience()
            elif userinput == 'P':
                phoneafriend(name)
            break





def amount(x):
    if x == 1:
        money = 500
    if x == 2:
        money = 1000
    if x == 3:
        money = 2000
    if x == 4:
        money = 3000
    if x == 5:
        money = 5000
    if x == 6:
        money = 7000
    if x == 7:
        money = 10000
    if x == 8:
        money = 15000
    if x == 9:
        money = 20000
    if x == 10:
        money = 30000
    if x == 11:
        money = 50000
    if x == 12:
        money = 100000
    if x == 13:
        money = 250000
    if x == 14:
        money = 500000
    if x == 15:
        money = 1000000
    return money


def checkpoint(x):
    if x <= 5:
        checkpointmoney = 0
    if x > 5 and x <= 11:
        checkpointmoney = 5000
    if x > 11 and x < 15:
        checkpointmoney = 50000
    return checkpointmoney

def finaldecision(resp, numbers):
    print('\n')
    if resp == 'wrong':
        print('i am sorry, this is were the game ends unfortunately')
        number = str(checkpoint(numbers))
        print('you still work away with ' + number + ' dollars')
    else:
        print('congratulations on winning the game you amongst the lucky few to join the millionaire club')
    