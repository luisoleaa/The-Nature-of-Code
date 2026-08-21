# Chapter 10 of "The Nature of Code" - Nueral Networks
# In this file I explore the use of the most basic neural network the "Perceptron"
# This is a program that trains itself over iterations of random x and y points to 
# Draw grey dots over a function f(x) and white dots under


import random
import pygame

class Perceptron:
    def __init__(self, n, learningRate):
        self.weights = [random.uniform(-1, 1) for _ in range(n)]
        self.learningConstant = learningRate

    def feedForward(self, inputs):
        sum = 0
        for i in range(len(self.weights)):
            sum = sum + inputs[i] * self.weights[i]
        return self.activate(sum)

    def train(self, inputs, desired):
        guess = self.feedForward(inputs)
        error = desired - guess
        for i in range(len(self.weights)):
            self.weights[i] = self.weights[i] + error * inputs[i] * self.learningConstant

    def activate(self, sum):
        if sum >= 0:
            return 1
        else:
            return -1

# Function for line on screen
def f(x):
    return 0.5 * x + 1

width = 640
height = 240

# p5's translate(width/2, height/2) + scale(1, -1) moves the origin to the
# center of the canvas and flips the y-axis so it points up (Cartesian,
# like math coords) instead of pygame's default top-left/y-down. Pygame has
# no matrix stack, so every math-space point has to be converted by hand
# with this helper before it's drawn.
def to_screen(x, y):
    return (width / 2 + x, height / 2 - y)

pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Perceptron")
clock = pygame.time.Clock()

perceptron = Perceptron(3, 0.0001)

# build the 2000 training points once, up front
training = []
for i in range(2000):
    x = random.uniform(-width / 2, width / 2)
    y = random.uniform(-height / 2, height / 2)
    training.append([x, y, 1])
count = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # drawing the "background(255)""
    screen.fill((255, 255, 255))

    # draw the line
    pygame.draw.line(
        screen, (0, 0, 0),
        to_screen(-width / 2, f(-width / 2)),
        to_screen(width / 2, f(width / 2)),
        2,
    )
    

    # get the current training point and its desired output
    x = training[count][0]
    y = training[count][1]

    desired = -1
    if y > f(x):
        desired = 1

    # train the perceptron on it
    perceptron.train(training[count], desired)

    # train one point at a time, for animation
    count = (count + 1) % len(training)

    # draw all the points, colored by the perceptron's current guess
    for dataPoint in training:
        guess = perceptron.feedForward(dataPoint)
        if guess > 0:
            fillColor = (127, 127, 127)
        else:
            fillColor = (255, 255, 255)
        pygame.draw.circle(screen, fillColor, to_screen(dataPoint[0], dataPoint[1]), 4)
        pygame.draw.circle(screen, (0, 0, 0), to_screen(dataPoint[0], dataPoint[1]), 4, 1)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()

