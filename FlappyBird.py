from Background import *


class FlappyBird:
    def __init__(self):
        self.x_size = 25
        self.y_size = 25
        self.bird = pygame.transform.scale(BIRD, (self.x_size, self.y_size))
        self.x_coord = 250
        self.y_coord = 150
        self.y_speed = 0

    def show_bird(self):
        """
        draw bird on screen
        """
        win.blit(self.bird, (self.x_coord, self.y_coord))

    def moving(self):
        """
        manage bird's vertical speed
        manage user's pressing on buttons

        :return: quit the game or updated bird's speed(float)
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    SOUND['wing'].play()
                    self.y_speed = -6

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    self.y_speed = 1.25
        if self.y_speed != 0:
            self.y_speed += 0.15
        self.y_coord += self.y_speed
