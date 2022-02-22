from tkinter import N


teams = {}

# opens the file and puts the teams in the dictionary as the key and then their w-l as a list
with open('teams.txt') as f:
    for i in f:
        i = i.strip()
        line = i.split(',')
        teams[line[0]] = [int(line[1]), int(line[2])]


def add_win():
    # adds one to the win sections of the team
    win = input('Who won a game?').lower()
    teams[win][0] += 1


def add_lost():
    # adds one to the lose sections of the team
    loss = input('Who won a game?').lower()
    teams[loss][1] += 1


def percent_to_decimal(percent):
    return 100/percent


def decimal_to_percent(decimal):
    return 100/decimal


def save_file():
    pass


def calc_odds(a, b):
    # calculate the decent odds based on how many wins they have
    w1 = teams[a][0]
    w2 = teams[b][0]
    total = w1 + w2
    percent1 = percent_to_decimal(w1 / total * 100)
    percent2 = percent_to_decimal(w2 / total * 100)
    print(
        f'For team {a} you should bet on them if the odds are above {percent1}')
    print(
        f'For team {b} you should bet on them if the odds are above {percent2}')


def display_standings():
    # prints out all of the time and their win lose stats
    print('These are the standings of the team currently')
    for i in teams:
        print(
            f'{i.upper()} :   Wins:  {teams[i][0]}   Loses:  {teams[i][1]}')


def program():
    print('Welcome to my simple betting guide based solely on math!!')
    print('I have many options that you can choose from')
    print('1 = adding a win to a team, 2 = adding a loss to a team, 3 = save results of what ever you are working on, 4 = calculate odds for a math, 5 = current standings')
    choice = input('Enter the number of which you would like to choose: ')
    valid = ['1', '2', '3', '4', '5']

    while choice in valid:
        if choice == '1':
            add_win()
        elif choice == '2':
            add_lost()
        elif choice == '3':
            save_file()
        elif choice == '4':
            bet = input(
                'Put in the teams that are playing separated by a comma: ')
            a, b = bet.split(',')
            calc_odds(a, b)
        elif choice == '5':
            display_standings()

        print('\n')
        choice = input('Enter the number of which you would like to choose: ')


program()
