import pygame

pygame.init()
w = 10
generation = 0
cell_size = 50
clock = pygame.time.Clock()


def setup():
    global cells, screen

    # createCanvas(640, 240);
    pygame.init()
    screen = pygame.display.set_mode((640, 240))

    # background(255);
    screen.fill((255, 255, 255))

    # cells = new Array(floor(width / w));
    width = screen.get_width()
    cells = [0] * (width // w)

    # cells[floor(cells.length / 2)] = 1;
    cells[len(cells) // 2] = 1

def rules(a, b, c):
    ruleset = [0, 1, 0, 1, 1, 0, 1, 0]
    if(a == 1 and b == 1 and c == 1):
         return ruleset[0]
    elif (a == 1 and b == 1 and c == 0):
         return ruleset[1]
    elif (a == 1 and b == 0 and c == 1):
        return ruleset[2]
    elif (a == 1 and b == 0 and c == 0):
        return ruleset[3]
    elif (a == 0 and b == 1 and c == 1):
        return ruleset[4]
    elif (a == 0 and b == 1 and c == 0):
        return ruleset[5]
    elif (a == 0 and b == 0 and c == 1):
        return ruleset[6]
    elif (a == 0 and b == 0 and c == 0): 
        return ruleset[7]
setup()


running = True
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    y = generation * w

    if y < screen.get_height():
        
        for i,state in enumerate(cells):
            color_val = 255 - (state * 255)
            color = (color_val, color_val, color_val)

            # pygame.draw.rect(surface, color, (x, y, width, height))
            pygame.draw.rect(screen, color, (i * w, y, w, w))

        next_gen = cells.copy()
        for i in range(1, len(cells) -1):
            left = cells[i - 1]
            middle = cells[i]
            right = cells[i + 1]
            new_state = rules(left, middle, right)
            next_gen[i] = new_state
        cells = next_gen
        generation += 1
    pygame.display.flip()
    clock.tick(15)

pygame.quit()