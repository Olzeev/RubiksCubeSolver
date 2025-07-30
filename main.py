from state import *
from const import *
from cursor import *
from moves import *
import pygame


pygame.init()


def print_text(text, pos, size, color, align='left'):
    font = pygame.font.Font(None, size)
    surf = font.render(text, True, color)
    
    if align == 'center':
        sc.blit(surf, (pos[0] - surf.get_width() / 2, pos[1]))
    elif align == 'right':
        sc.blit(surf, (pos[0] - surf.get_width(), pos[1]))
    else:
        sc.blit(surf, pos)


sc = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()


'''
cur_colors = [
    0, 0, 3, 3, 0, 5, 3, 2, 0, 
    2, 5, 3, 2, 1, 2, 0, 3, 5, 
    2, 0, 1, 4, 2, 2, 3, 4, 0, 
    5, 1, 1, 1, 3, 1, 4, 5, 4, 
    4, 3, 4, 4, 4, 5, 5, 0, 2, 
    2, 1, 1, 3, 5, 4, 1, 0, 5
]
'''

cur_colors = [i for i in range(6) for j in range(9)]

cur_facelets = get_facelets_by_colors(cur_colors)

cur_state = State(cur_facelets)

cur_phaseone_state = PhaseOneState(cur_facelets)

cursor = Cursor(1, 0)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    sc.fill(BG_COLOR)


    for i in range(6):
        for j in range(9):
            pygame.draw.rect(sc, 
                             FACELET_DISPLAY_COLORS[cur_state.facelets[i * 9 + j] - 1], 
                             (SIDES_DISPLAY_OFFSETS[i][0] + FACELET_DISPLAY_SIZE * (j % 3), SIDES_DISPLAY_OFFSETS[i][1] + FACELET_DISPLAY_SIZE * (j // 3),
                              FACELET_DISPLAY_SIZE, FACELET_DISPLAY_SIZE))
            pygame.draw.rect(sc, 
                             (0, 0, 0), 
                             (SIDES_DISPLAY_OFFSETS[i][0] + FACELET_DISPLAY_SIZE * (j % 3), SIDES_DISPLAY_OFFSETS[i][1] + FACELET_DISPLAY_SIZE * (j // 3),
                              FACELET_DISPLAY_SIZE, FACELET_DISPLAY_SIZE), 2)

            print_text(str(cur_facelets[i * 9 + j]), 
                       (SIDES_DISPLAY_OFFSETS[i][0] + FACELET_DISPLAY_SIZE * (j % 3), SIDES_DISPLAY_OFFSETS[i][1] + FACELET_DISPLAY_SIZE * (j // 3)), 
                       FACELET_DISPLAY_SIZE - 20, (0, 0, 0), 'left')
            
    pygame.draw.rect(sc, 
                             SIDES_DISPLAY_COLORS[cursor.color], 
                             (SIDES_DISPLAY_OFFSETS[(cursor.facelet - 1) // 9][0] + FACELET_DISPLAY_SIZE * (((cursor.facelet - 1) % 9) % 3), SIDES_DISPLAY_OFFSETS[(cursor.facelet - 1) // 9][1] + FACELET_DISPLAY_SIZE * (((cursor.facelet - 1) % 9) // 3),
                              FACELET_DISPLAY_SIZE, FACELET_DISPLAY_SIZE), 5)

    cursor.move()
    if key.is_pressed('space'):
        cur_colors[cursor.facelet - 1] = cursor.color
    if key.is_pressed('shift'):
        cur_facelets = get_facelets_by_colors(cur_colors)
        cur_state.update(cur_facelets)
        print('updated')
        print([(cur_state.cubies[0][i].c, cur_state.cubies[1][i].o) for i in range(8)])
        print([(cur_state.cubies[1][i].e, cur_state.cubies[1][i].o) for i in range(12)])
        print(cur_state.coordinates)
    if key.is_pressed('enter'):
        cur_state.implement_move(Rmove)

    pygame.display.flip()
    clock.tick(FPS)