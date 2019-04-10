from Background import *


class NightBackground(Background):
    def __init__(self):
        super().__init__()
        self.sky = pygame.transform.scale(SKY_NIGHT, (SKY_WIDTH, SKY_LENGTH))
