import numpy as np
import pygame
import sns as sns

f = open('ArvEstrada.txt', 'r')

start = f.readlines()[0]

print(start)

f.close()

f = open('ArvEstrada.txt', 'r')

goal = f.readlines()[1]

print(goal)

f.close()


a_file = open("ArvEstrada.txt", "r")

lines = a_file.readlines()
a_file.close()

del lines[1]

new_file = open("field.txt", "w+")

for line in lines:
    new_file.write(line)

new_file.close()

a_file = open("field.txt", "r")

lines = a_file.readlines()
a_file.close()

del lines[0]

new_file = open("field.txt", "w+")

for line in lines:
    new_file.write(line)

new_file.close()

f = open("field.txt", "r")

f = open('field.txt', 'r')
a = []
for line in f.readlines():
    a.append([int(x) for x in line.split(',')])

print(a)



# start = list(map.py(int, f.))
# entries = list(map.py(int, int.split(,)))

#f = open('ArvEstrada.txt', 'r+')

#d = f.readlines()

#for i in d:
#    if i != 0 or i != 1:
#        f.write(i)
#f.truncate()
#f.close()