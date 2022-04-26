import random
r = random.randint(1, 100)
count = 0
while True:
	count = count + 1
	num = input('enter your number: ')
	num = int(num)
	if num == r:
		print('your guess is right!')
		print('this is your', count, 'time try.')
		break
	elif num < r:
		print('your number is smaller than the answer.')
	elif num > r:
		print('your number is larger than the answer.')
	print('this is your', count, 'time try.')
