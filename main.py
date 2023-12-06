import sys
import pygame
pygame.init()
screen = pygame.display.set_mode((900, 900))
screen.fill((255, 255, 255))
# draw the lines for the 4 by 4 karnaugh map grid
pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(100, 100, 150, 150))
pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(250, 100, 150, 150))
pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(400, 100, 150, 150))
pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(100, 250, 150, 150))
pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(250, 250, 150, 150))
pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(400, 250, 150, 150))
pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(100, 400, 150, 150))
pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(250, 400, 150, 150))
pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(400, 400, 150, 150))
pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(550, 100, 150, 150))
pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(550, 250, 150, 150))
pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(550, 400, 150, 150))
pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(100, 250, 150, 150))
pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(100, 550, 150, 150))
pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(250, 550, 150, 150))
pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(400, 550, 150, 150))
pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(550, 550, 150, 150))
pygame.draw.line(screen, (0, 0, 0), (250, 100), (250, 700), 1)
pygame.draw.line(screen, (0, 0, 0), (400, 100), (400, 700), 1)
pygame.draw.line(screen, (0, 0, 0), (550, 100), (550, 700), 1)
pygame.draw.line(screen, (0, 0, 0), (100, 400), (700, 400), 1)
pygame.draw.line(screen, (0, 0, 0), (100, 250), (700, 250), 1)
pygame.draw.line(screen, (0, 0, 0), (100, 550), (700, 550), 1)
pygame.display.update()
# while True:
#     for event in pygame.event.get():
#         print(pygame.mouse.get_pos())
#         x, y = pygame.mouse.get_pos()
#         if event.type == pygame.MOUSEBUTTONDOWN:
#             pygame.draw.rect(screen, (255, 0, 0), pygame.Rect((((x%150)*150)+100), ((y%150)*150), 150, 150))
#             pygame.display.update()
#         # if (x -100) % 150 == 0:
#         #     pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(x, y, 150, 150))
#         #     pygame.display.update()
#         if event.type == pygame.QUIT:
#             sys.exit()
#         if event.type == pygame.MOUSEBUTTONDOWN:
#             print(pygame.mouse.get_pos())
#             x, y = pygame.mouse.get_pos()
#             pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(100, 100, 150, 150))
#             pygame.display.update()
offset_x = 100  # replace with the actual x offset
offset_y = 100  # replace with the actual y offset
rect_states = [[False]*4 for _ in range(4)]  # initialize rectangle states

while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            index_x = (x - offset_x) // 150
            index_y = (y - offset_y) // 150
            if 0 <= index_x < 4 and 0 <= index_y < 4:  # check if within the 16 squares
                rect_states[index_x][index_y] = not rect_states[index_x][index_y]  # toggle state
                color = (255, 0, 0) if rect_states[index_x][index_y] else (0, 255, 0)  # choose color
                rect_x = index_x * 150 + offset_x
                rect_y = index_y * 150 + offset_y
                pygame.draw.rect(screen, color, pygame.Rect(rect_x, rect_y, 150, 150))
                pygame.draw.line(screen, (0, 0, 0), (250, 100), (250, 700), 1)
                pygame.draw.line(screen, (0, 0, 0), (400, 100), (400, 700), 1)
                pygame.draw.line(screen, (0, 0, 0), (550, 100), (550, 700), 1)
                pygame.draw.line(screen, (0, 0, 0), (100, 400), (700, 400), 1)
                pygame.draw.line(screen, (0, 0, 0), (100, 250), (700, 250), 1)
                pygame.draw.line(screen, (0, 0, 0), (100, 550), (700, 550), 1)
                pygame.display.update()
        if event.type == pygame.QUIT:
            sys.exit()
