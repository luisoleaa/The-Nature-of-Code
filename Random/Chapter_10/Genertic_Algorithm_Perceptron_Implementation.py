# Chapter 10 of "The Nature of Code" - Nueral Networks
# In this file I explore the use of the most basic neural network the "Perceptron"
# This is a program that trains itself over iterations of random x and y points to 
# Draw grey dots over a function f(x) and white dots under

# This specific file is a mix of chapter 9 and 10, combining the nueral network Perceptron with the genetic algorithm
# to create new guesses that get more "fit" (accurate) over generations


import random
import math
import pygame

class Perceptron:
    def __init__(self, n, ):
        self.weights = [random.uniform(-1, 1) for _ in range(n)]
        self.fitness = 0

    def get_fitness(self, training_points):
        score = 0
        for x, y, bias in training_points:
            desired = 1 if y > f(x) else -1
            if self.feedForward([x, y, bias]) == desired:
                score += 1
        self.fitness = score / len(training_points)
    

    def feedForward(self, inputs):
        sum = 0
        for i in range(len(self.weights)):
            sum = sum + inputs[i] * self.weights[i]
        return self.activate(sum)

    def crossover(self,parent):
        child = Perceptron(len(self.weights))
        midpoint = random.randint(0, len(self.weights) -1)
        for i in range(len(self.weights)):
            if i < midpoint:
                child.weights[i] = self.weights[i]
            else:
                child.weights[i] = parent.weights[i]
        return child

    def mutate(self,mutationRate):
        for i in range(len(self.weights)):
            if random.random() < mutationRate:
                self.weights[i] = random.uniform(1, -1)


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

mutation_rate = 0.01
population_size = 100
population = [Perceptron(3) for _ in range(population_size)]
generation = 0
best_fitness = 0

# build the training set once, up front: each point is [x, y, bias]
training = []
for i in range(200):
    x = random.uniform(-width / 2, width / 2)
    y = random.uniform(-height / 2, height / 2)
    training.append([x, y, 1])




# with this helper before it's drawn.
def to_screen(x, y):
    return (width / 2 + x, height / 2 - y)

pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Perceptron")
clock = pygame.time.Clock()
font = pygame.font.SysFont("consolas", 18)




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
    
    for phase in population:
        phase.get_fitness(training)
    best = max(population, key=lambda p: p.fitness)
    if best.fitness > best_fitness:
        best_fitness = best.fitness
    mating_pool = []
    for phase in population:
        n = math.floor(phase.fitness *100)
        for x in range(n):
            mating_pool.append(phase)
    if not mating_pool:
        mating_pool = population[:]
    new_population = []
    for _ in range(len(population)):
        parent_a = random.choice(mating_pool)
        parent_b = random.choice(mating_pool)
        child = parent_a.crossover(parent_b)
        child.mutate(mutation_rate)
        new_population.append(child)

    population = new_population
    generation += 1

    # draw all the points, colored by the best perceptron's current guess
    for dataPoint in training:
        guess = best.feedForward(dataPoint)
        if guess > 0:
            fillColor = (127, 127, 127)
        else:
            fillColor = (255, 255, 255)
        pygame.draw.circle(screen, fillColor, to_screen(dataPoint[0], dataPoint[1]), 4)
        pygame.draw.circle(screen, (0, 0, 0), to_screen(dataPoint[0], dataPoint[1]), 4, 1)

    screen.blit(font.render(f"Generation: {generation}", True, (0, 0, 0)), (10, 10))
    screen.blit(font.render(f"Best fitness: {best_fitness:.2f}", True, (0, 0, 0)), (10, 30))

    pygame.display.flip()
    clock.tick(60)
    pygame.time.wait(1000)

pygame.quit()

