import random
r = random.randint(1,100)
while True:
    num = input('enter your number: ')
    num = int(num)
    if num == r:
        print('you guess right!')
        break
    elif num < r:
        print('your number is smaller than the answer.')
    elif num > r:
        print('your number is larger than the answer.')
