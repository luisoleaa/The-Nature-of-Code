# Uses a GA to at first randomly guess the target string, but eventually uses previous random guesses
# to reproduce the "fittest" guesses to eventually find the most "fit" guess -> the target string

import random
import string
import math
import pygame

target = "Luis Olea"
characters = string.ascii_letters + string.digits + " "

# the DNA the population will have and how they will mutate and change while trying to find the target
class DNA:
    def __init__(self, length):
        self.genes = [random.choice(characters) for _ in range(length)]
        self.fitness = 0

    def get_phrase(self):
        return "".join(self.genes)

    def calculate_fitness(self, target):
        score = 0
        for i in range(len(target)):
            if self.genes[i] == target[i]:
                score += 1
        self.fitness = score / len(target)
# reproduces children with genes from both parents
    def crossover(self, parent):
        child = DNA(len(self.genes))
        midpoint = random.randint(0, len(self.genes) - 1)
        for i in range(len(self.genes)):
            if i < midpoint:
                child.genes[i] = self.genes[i]
            else:
                child.genes[i] = parent.genes[i]
        return child
# uses a mutation rate to simulate the randomness of nature's mutations
    def mutate(self, mutation_rate):
        for i in range(len(self.genes)):
            if random.random() < mutation_rate:
                self.genes[i] = random_character()


def random_character():
    return random.choice(characters)


mutation_rate = 0.01
population_size = 150
population = []
generation = 0
best_phrase = ""
best_fitness = 0


def setup():
    global population
    population = [DNA(len(target)) for _ in range(population_size)]


def draw():
    global population, generation, best_phrase, best_fitness

    for phrase in population:
        phrase.calculate_fitness(target)

    best = max(population, key=lambda p: p.fitness)
    if best.fitness > best_fitness:
        best_fitness = best.fitness
        best_phrase = best.get_phrase()

    mating_pool = []
    for phrase in population:
        n = math.floor(phrase.fitness * 100)
        for _ in range(n):
            mating_pool.append(phrase)

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


def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 420))
    pygame.display.set_caption("Genetic Algorithm - Phrase Match")
    clock = pygame.time.Clock()
    font_large = pygame.font.SysFont("consolas", 26)
    font_small = pygame.font.SysFont("consolas", 18)

    setup()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        draw()

        screen.fill((20, 20, 30))

        screen.blit(font_small.render(f"Target: {target}", True, (200, 200, 200)), (20, 20))
        screen.blit(font_small.render(f"Generation: {generation}", True, (200, 200, 200)), (20, 50))
        screen.blit(font_small.render(f"Best fitness: {best_fitness:.2f}", True, (200, 200, 200)), (20, 80))
        screen.blit(font_large.render(best_phrase, True, (100, 220, 140)), (20, 120))

        y = 180
        for phrase in population[:12]:
            color = (80, 160, 220) if phrase.fitness > 0.5 else (120, 120, 120)
            screen.blit(font_small.render(phrase.get_phrase(), True, color), (20, y))
            y += 20

        pygame.display.flip()
        clock.tick(30)

        if best_phrase == target:
            pygame.display.set_caption("Genetic Algorithm - Phrase Match (solved!)")
            pygame.time.wait(2000)
            running = False

    pygame.quit()


if __name__ == "__main__":
    main()
