import pygame

w = input()
n = input()
if w.isdigit() == False or n.isdigit() == False:
    print("Неправильный формат ввода")
x = int(w) * int(n) * 2
size = size_x, size_y = x, x
pygame.init()
scr = pygame.display.set_mode(size)
pygame.display.set_caption("круги")

scr.fill((0, 0, 0))

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
color = blue

count = 0
center = x // 2
radius = 0

for i in range(int(n)):
    count += 1
    if count > 3:
        count = 1
    if count == 1:
        color = red
    elif count == 2:
        color = green
    elif count == 3:
        color = blue
    radius += int(w)
    pygame.draw.circle(scr, color, (center, center), radius, int(w))

while pygame.event.wait().type != pygame.QUIT:
    pygame.display.update()
pygame.quit()