from Sprites import *


class Background:
    def __init__(self):
        self.sky = pygame.transform.scale(SKY, (SKY_WIDTH, SKY_LENGTH))
        self.ground = pygame.transform.scale(GROUND, (GROUND_LENGTH, GROUND_WIDTH))
        self.image_of_game_over = pygame.transform.scale(GAME_OVER, (200, 120))
        self.field = pygame.font.SysFont(None, 40)

    def draw_sky(self):
        """
        draw sky on screen
        """
        win.blit(self.sky, (0, 0))

    def draw_ground(self):
        """
        draw ground on screen
        """
        win.blit(self.ground, (0, 400))

    def scorer(self, current_score):
        """
        show user's current score

        :param current_score: int
        :return: script of user's score
        """
        text = self.field.render("Score: " + str(current_score // 2), True, BLACK_COLOUR)
        win.blit(text, (0, 0))

    def game_over(self):
        """
        inform about user's failed game
        """
        win.blit(self.image_of_game_over, (250, 170))
