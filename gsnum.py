

import random

num_1 = input('输入最小值:')
num_2 = input('输入最大值:')

num_1= int(num_1)
num_2= int(num_2)

count = 1

r = random.randint(num_1,num_2)

while True:

	num = input('猜数字:')
	num = int(num)
	if num == r:
		print('你猜对了!')
		break

	elif num > r:
		print('比答案大')
		

	elif num < r:
		print('比答案小')

	print('这是你猜的第',count,'次')

	count = count +1

