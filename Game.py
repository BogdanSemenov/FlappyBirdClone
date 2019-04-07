from Columns import *
from FlappyBird import *
from Background import *


class Game:
    def __init__(self):
        self.score = 0
        self.high_score = 0

        self.is_game_over = False

        self.background = Background()
        self.bird = FlappyBird()
        self.obstacle = Columns()

    def is_touch_ground(self):
        """
        checking of touching ground by bird

        :return: bool
        """
        if self.bird.y_coord + self.bird.y_size > SCREEN_WIDTH - GROUND_WIDTH:
            return True
        return False

    def is_touch_up_obstacle(self):
        """
        checking of touching up column by bird

        :return: bool
        """
        if self.bird.x_coord + self.bird.x_size > self.obstacle.x_coord:
            if self.bird.y_coord < self.obstacle.height + self.obstacle.add_height - self.obstacle.y_coord:
                if self.bird.x_coord < self.obstacle.x_coord + self.obstacle.width:
                    return True

        if self.bird.x_coord + self.bird.x_size > self.obstacle.x_coord_new_column:
                if self.bird.y_coord < self.obstacle.height + \
                        self.obstacle.add_height - self.obstacle.y_coord_new_column:
                    if self.bird.x_coord < self.obstacle.x_coord_new_column + self.obstacle.width:
                        return True

        return False

    def is_touching_down_obstacle(self):
        """
        checking of touching down column by bird

        :return: bool
        """
        if self.bird.x_coord + self.bird.x_size > self.obstacle.x_coord:
            if self.bird.y_coord + self.bird.y_size > self.obstacle.height \
                 + self.obstacle.add_height - self.obstacle.y_coord + self.obstacle.space:
                if self.bird.x_coord < self.obstacle.x_coord + self.obstacle.width:
                    return True

        if self.bird.x_coord + self.bird.x_size > self.obstacle.x_coord_new_column:
            if self.bird.y_coord + self.bird.y_size > self.obstacle.height\
                 + self.obstacle.add_height - self.obstacle.y_coord_new_column + self.obstacle.space:
                if self.bird.x_coord < self.obstacle.x_coord_new_column + self.obstacle.width:
                    return True

        return False

    def process_game(self):
        """
        regulate the process of the game
        draw all subjects and objects and move them

        :return: updated landscape
        """
        self.background.draw_sky()
        self.obstacle.update()
        self.obstacle.draw_column()
        self.background.draw_ground()

        self.bird.show_bird()
        self.bird.moving()
        self.obstacle.moving()

    def restart_or_quit(self):
        """
        when user lose banner with
        suggestion of quit or restart is appearing

        :return: script
        """
        font = pygame.font.SysFont(None, 45)
        info = font.render("Press ENTER to Restart or ESC to Quit", True, RED_COLOUR)
        win.blit(info, (65, 450))
        key = pygame.key.get_pressed()
        if key[pygame.K_RETURN]:
            self.bird = FlappyBird()
            self.obstacle = Columns()
            self.is_game_over = False
            self.score = 0
        if key[pygame.K_ESCAPE]:
            quit()

    def high_scorer(self, current_score):
        """
        update user's record

        :param current_score: int
        :return: updated high_score: int
        """
        if self.high_score < current_score:
            self.high_score = current_score
        font = pygame.font.SysFont(None, 35)
        info = font.render("HighScore: " + str(self.high_score), True, BLACK_COLOUR)
        win.blit(info, (0, 35))

    def count_score(self):
        """
        update user's score

        :return: updated score: int
        """
        if self.obstacle.x_coord + self.obstacle.width < self.bird.x_coord < \
                self.obstacle.x_coord + self.obstacle.width + 5:
            self.score += 1
            SOUND['point'].play()

        if self.obstacle.x_coord_new_column + self.obstacle.width < self.bird.x_coord < \
                self.obstacle.x_coord_new_column + self.obstacle.width + 5:
            SOUND['point'].play()
            self.score += 1

    def run(self):
        """
        show process of user's current game

        :return: True(continue the game) or False(quit)
        """
        while True:
            pygame.time.delay(TIME_DELAY)

            self.process_game()

            self.background.scorer(self.score)
            self.high_scorer(self.score)

            if self.is_touch_up_obstacle() or self.is_touching_down_obstacle() or self.is_touch_ground():
                self.background.game_over()

                if not self.is_game_over:
                    SOUND['hit'].play()
                self.is_game_over = True
                self.bird.y_speed = 0
                self.obstacle.obstacle_speed = 0

            if self.is_game_over:
                self.restart_or_quit()

            self.count_score()

            pygame.display.update()
