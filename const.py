WIDTH, HEIGHT = 1280, 720

BG_COLOR = (20, 20, 20)

FPS = 30

FACELET_DISPLAY_COLORS = [
    (0, 0, 255) for i in range(9) 
] + [
    (255, 0, 0) for i in range(9)
] + [
    (255, 255, 255) for i in range(9)
] + [
    (255, 140, 0) for i in range(9)
] + [
    (0, 255, 0) for i in range(9)
] + [
    (255, 255, 0) for i in range(9)
]

SIDES_DISPLAY_COLORS = [
    (0, 0, 255), 
    (255, 0, 0), 
    (255, 255, 255), 
    (255, 140, 0), 
    (0, 255, 0), 
    (255, 255, 0)
]

FACELET_DISPLAY_SIZE = 50

SIDES_DISPLAY_OFFSETS = [
    (0, FACELET_DISPLAY_SIZE * 3), 
    (FACELET_DISPLAY_SIZE * 3, 0), 
    (FACELET_DISPLAY_SIZE * 3, FACELET_DISPLAY_SIZE * 3), 
    (FACELET_DISPLAY_SIZE * 3, FACELET_DISPLAY_SIZE * 6), 
    (FACELET_DISPLAY_SIZE * 6, FACELET_DISPLAY_SIZE * 3), 
    (FACELET_DISPLAY_SIZE * 9, FACELET_DISPLAY_SIZE * 3)
]