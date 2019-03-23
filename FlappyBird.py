import pygame
from random import randint

pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.mixer.init()
pygame.init()

win = pygame.display.set_mode((700, 500))

pygame.display.set_caption("Flappy Bird")


class FlappyBird:
    def __init__(self):
        self.x_size = 25
        self.y_size = 25
        self.flap = pygame.transform.scale(pygame.image.load('Bird.png'), (self.x_size, self.y_size))
        self.x = 250
        self.y = 150
        self.y_speed = 0

    def show(self):
        win.blit(self.flap, (self.x, self.y))

    def moving(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    SOUND['wing'].play()
                    self.y_speed = -11
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    self.y_speed = 2
        if self.y_speed != 0:
            self.y_speed += 0.3
        self.y += self.y_speed


class Columns:
    def __init__(self):
        self.x = 700
        self.y = 0

        self.width = 50
        self.height = 130
        self.x_new_column = 700 + 700 // 2 + self.width // 2
        self.space = 100
        self.obstacle_speed = 6
        self.rand = 100
        self.rand_new_column = 100
        self.obstacle_down = pygame.transform.scale(pygame.image.load('Column.png').convert_alpha(),
                                                    (self.width, self.height + 200))
        self.obstacle_up = pygame.transform.scale(pygame.transform.flip(pygame.image.load('Column.png'), False, True),
                                                  (self.width, self.height + 200))

    def draw_column(self):
        win.blit(self.obstacle_up, (self.x, - self.rand))
        win.blit(self.obstacle_down, (self.x, (self.height + 200) + self.space - self.rand))
        win.blit(self.obstacle_up, (self.x_new_column, - self.rand_new_column))
        win.blit(self.obstacle_down, (self.x_new_column, (self.height + 200) + self.space - self.rand_new_column))

    def moving(self):
        self.x -= self.obstacle_speed
        self.x_new_column -= self.obstacle_speed

    def update(self):
        if self.x < -self.width:
            self.x = 700
            self.rand = randint(130, 320)
        if self.x_new_column < -self.width:
            self.x_new_column = 700
            self.rand_new_column = randint(130, 320)


def draw_sky():
    width = 700
    height = 500
    sky = pygame.transform.scale(pygame.image.load('Sky.png').convert_alpha(), (width, height))
    win.blit(sky, (0, 0))


def draw_ground():
    width = 700
    height = 100
    ground = pygame.transform.scale(pygame.image.load('Ground.png').convert_alpha(), (width, height))
    win.blit(ground, (0, 400))


def scorer(current_score):
    field = pygame.font.SysFont(None, 40)
    text = field.render("Score: " + str(current_score), True, (0, 0, 0))
    win.blit(text, (0, 0))


def game_over():
    image = pygame.transform.scale(pygame.image.load('GameOver.png').convert_alpha(), (200, 120))
    win.blit(image, (250, 170))


def is_touch_ground():
    if bird.y + bird.y_size > 400:
        return True
    return False


def is_touch_up_obstacle():
    if bird.x + bird.x_size > obstacle.x and bird.y < obstacle.height + 200 - obstacle.rand \
            and bird.x < obstacle.x + obstacle.width:
        return True

    if bird.x + bird.x_size > obstacle.x_new_column and bird.y < obstacle.height + 200 - obstacle.rand_new_column \
            and bird.x < obstacle.x_new_column + obstacle.width:
        return True

    return False


def is_touching_down_obstacle():
    if bird.x + bird.x_size > obstacle.x and \
            bird.y + bird.y_size > obstacle.height + 200 - obstacle.rand + obstacle.space and \
            bird.x < obstacle.x + obstacle.width:
        return True

    if bird.x + bird.x_size > obstacle.x_new_column and \
            bird.y + bird.y_size > obstacle.height + 200 - obstacle.rand_new_column + obstacle.space \
            and bird.x < obstacle.x_new_column + obstacle.width:
        return True

    return False


def restart_or_quit():
    global bird, obstacle, score, is_game_over
    font = pygame.font.SysFont(None, 45)
    info = font.render("Press ENTER to Restart or ESC to Quit", True, (255, 0, 0))
    win.blit(info, (65, 450))
    key = pygame.key.get_pressed()
    if key[pygame.K_RETURN]:
        bird = FlappyBird()
        obstacle = Columns()
        is_game_over = False
        score = 0
    if key[pygame.K_ESCAPE]:
        quit()


def process_game():
    draw_sky()
    obstacle.update()
    obstacle.draw_column()
    draw_ground()

    bird.show()
    bird.moving()
    obstacle.moving()


def high_scorer(current_score):
    global high_score
    if high_score < current_score:
        high_score = current_score
    font = pygame.font.SysFont(None, 35)
    info = font.render("HighScore: " + str(high_score), True, (0, 0, 0))
    win.blit(info, (0, 35))


SOUND = {
    'wing': pygame.mixer.Sound('wing.ogg'),
    'point': pygame.mixer.Sound('point.ogg'),
    'hit': pygame.mixer.Sound('hit.ogg')
}


score = 0
high_score = 0

run = True
is_game_over = False

bird = FlappyBird()
obstacle = Columns()

while run:
    pygame.time.delay(10)

    process_game()

    scorer(score)
    high_scorer(score)

    if is_touch_up_obstacle() or is_touching_down_obstacle() or is_touch_ground():
        game_over()
        if not is_game_over:
            SOUND['hit'].play()
        is_game_over = True
        bird.y_speed = 0
        obstacle.obstacle_speed = 0

    if is_game_over:
        restart_or_quit()

    if obstacle.x + obstacle.width < bird.x < obstacle.x + obstacle.width + 5:
        score += 1
        SOUND['point'].play()
    if obstacle.x_new_column + obstacle.width < bird.x < obstacle.x_new_column + obstacle.width + 5:
        SOUND['point'].play()
        score += 1

    pygame.display.update()

pygame.quit()
