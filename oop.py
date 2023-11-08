#class emails():
#    def __init__(self, firstname, surname, startyr):
#        firstname = input('Enter your first name: ')
#        self.firstname = firstname
#        surname = input('Enter your surname: ')
#        self.surname = surname
#        startyr = input('Enter your starting year: ')
#        self.startyr = startyr
#        self.email = firstname[0]+ surname +startyr[2]+startyr[3]+ '@agsb.co.uk'
#person1 = emails(surname='Smith', firstname='John', startyr='2019')
#print(person1.email)
from random import randint
class safecracker():
    def __init__(self, tries,random ):
        tries = 10
        self.random = random
        for i in range(0, 6):
            random[i]

        self.tries = tries
        print('You have 20 tries to guess the number between 1 and 20')
        while tries > 0:
            
            guess = int(input('Enter your guess: '))
            if guess == random[i]:
                print('You guessed correctly!')
                break
            elif guess < random[i]:
                print('Your guess is too low')
            elif guess > random[i]:
                print('Your guess is too high')
            tries -= 1
            print('You have', tries, 'tries left')
        if tries == 0:
            print('You have run out of tries, the number was', random)
            print(random)
person1 = safecracker(tries=20, random=[randint(1,20), randint(1,20), randint(1,20), randint(1,20), randint(1,20), randint(1,20)])