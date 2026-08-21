import math
import random
import pygame

inputs = [12,4]
weights = [.5,-2]



sum = 0
for i in range(len(inputs)):
    sum = inputs[i] * weights[i]


def activate(number):
    if number >= 0:
        return 1
    else:
        return 0
output = activate(sum)
print(sum)
print(output)