import random
from secrets import choice

chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
num1 = int(input('enter count:'))
len = 5
for n in range(num1):
    key = ''
    part1 = ''
    part2 = ''
    part3 = ''
    for i in range(len):
        part1 += random.choice(chars)
        part2 += random.choice(chars)
        part3 += random.choice(chars)
    finkey = part1 + '-' + part2 + '-' + part3
    with open ('results.txt', 'a') as file:
        print(*finkey, file=file)
