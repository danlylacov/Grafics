import pygame

x11, y11, x12, y12, x21, y21, x22, y22 = float(input()), float(input()), float(input()), float(input()), float(input()), float(input()), float(input()), float(input())
print('Data get!')



def get_yravnenie(x1, y1, x2, y2): # -> k, b
    return [((y1 - y2) / (x1 - x2)), (y2 - ((y1 - y2) / (x1 - x2)) * x2)]


def find_point_x(x11, y11, x12, y12, x21, y21, x22, y22):
    if x11 - x12 == 0:
        return (max(y11, y12) - min(y11, y12))

    elif x21 - x22 == 0:
        return (max(y21, y12) - min(y21, y22))

    else:
        return ((get_yravnenie(x21, y21, x22, y22)[1] - get_yravnenie(x11, y11, x12, y12)[1]) / (
                    get_yravnenie(x11, y11, x12, y12)[0] - get_yravnenie(x21, y21, x22, y22)[0]))

def find_point_y(x,  x21, y21, x22, y22):
    return get_yravnenie(x21, y21, x22, y22)[0]*x+get_yravnenie(x21, y21, x22, y22)[1]

x = find_point_x(x11, y11, x12, y12, x21, y21, x22, y22)
y = find_point_y(x, x21, y21 ,x22, y22)
k1 , b1 = get_yravnenie(x11, y11, x12, y12)[0], get_yravnenie(x11, y11, x12, y12)[1]
k2, b2 =  get_yravnenie(x21, y21, x22, y22)[0], get_yravnenie(x21, y21, x22, y22)[1]




WIDTH = 900
HEIGHT = 900
FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Draw grafic")
clock = pygame.time.Clock()
screen.fill(WHITE)


pygame.draw.line(screen, BLACK, # Oy
                 [WIDTH/2, 0],
                 [WIDTH/2,HEIGHT], 5)
pygame.draw.line(screen, BLACK, # Oy
                 [0, HEIGHT/2],
                 [WIDTH,HEIGHT/2], 5)

for i in range(0, WIDTH, 30):
    pygame.draw.line(screen, BLACK,  # Oy
                         [0, HEIGHT - i],
                         [WIDTH, HEIGHT - i], 1)
    pygame.draw.line(screen, BLACK,  # Oy
                     [WIDTH - i, 0],
                     [WIDTH - i, HEIGHT], 1)

pygame.draw.line(screen, RED, [WIDTH/2 + (30*x11), HEIGHT/2 - (30*y11)], [WIDTH/2 + (30*x12), HEIGHT/2 - (30*y12)], 5)
pygame.draw.line(screen, RED, [WIDTH/2 + (30*x21), HEIGHT/2 - (30*y21)], [WIDTH/2 + (30*x22), HEIGHT/2 - (30*y22)], 5)
pygame.draw.circle(screen, RED, (WIDTH/2 + (30*x11), HEIGHT/2 - (30*y11)), 5)
pygame.draw.circle(screen, RED, (WIDTH/2 + (30*x12), HEIGHT/2 - (30*y12)), 5)
pygame.draw.circle(screen, RED, (WIDTH/2 + (30*x21), HEIGHT/2 - (30*y21)), 5)
pygame.draw.circle(screen, RED, (WIDTH/2 + (30*x22), HEIGHT/2 - (30*y22)), 5)


x = find_point_x(x11, y11, x12, y12, x21, y21, x22, y22)
y = find_point_y(x, x21, y21 ,x22, y22)
print(x, y)
text = 'Отрезок 1: y = {}x + {}'.format(k1, b1)
font = pygame.font.Font(None, 30)
text = font.render(
    text, True, (0, 100, 0))
screen.blit(text, (20, 800))

text = 'Отрезок 2: y = {}x + {}'.format(k2, b2)
font = pygame.font.Font(None, 30)
text = font.render(
    text, True, (0, 100, 0))

screen.blit(text, (20, 830))

text = 'Точка пересечения: ({}, {})'.format(x, y)
font = pygame.font.Font(None, 30)
text = font.render(
    text, True, (0, 100, 0))
screen.blit(text, (20, 860))

pygame.display.flip()
running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False






