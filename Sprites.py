import pygame

pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.mixer.init()
pygame.init()

SCREEN_WIDTH = 500
SCREEN_LENGTH = 700

SKY_WIDTH = 700
SKY_LENGTH = 500

GROUND_LENGTH = 700
GROUND_WIDTH = 100

win = pygame.display.set_mode((SCREEN_LENGTH, SCREEN_WIDTH))

pygame.display.set_caption("Flappy Bird")

BIRD = pygame.image.load('tools/Bird.png')

OBSTACLE_DOWN = pygame.image.load('tools/Column.png').convert_alpha()

OBSTACLE_UP = pygame.transform.flip(pygame.image.load('tools/Column.png'), False, True)

SKY = pygame.image.load('tools/Sky.png').convert_alpha()

GROUND = pygame.image.load('tools/Ground.png').convert_alpha()

GAME_OVER = pygame.image.load('tools/GameOver.png').convert_alpha()

SOUND = {
    'wing': pygame.mixer.Sound('tools/wing.ogg'),
    'point': pygame.mixer.Sound('tools/point.ogg'),
    'hit': pygame.mixer.Sound('tools/hit.ogg')
}

BLACK_COLOUR = (0, 0, 0)

RED_COLOUR = (255, 0, 0)

TIME_DELAY = 10
