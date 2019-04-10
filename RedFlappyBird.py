from FlappyBird import *


class RedFlappyBird(FlappyBird):
    def __init__(self):
        super().__init__()
        self.bird = pygame.transform.scale(RED_BIRD, (self.x_size, self.y_size))
        self.acceleration = 0.178
