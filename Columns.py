from Background import *
from random import randint


class Columns:
    def __init__(self):
        self.x_coord = 700
        self.y_coord = randint(130, 320)

        self.width = 50
        self.height = 130
        self.x_coord_new_column = 700 + 700 // 2 + self.width // 2
        self.y_coord_new_column = randint(130, 320)
        self.space = 100
        self.obstacle_speed = 3
        self.add_height = 200  # protect from user's cheating if he decide to fly over the screen
        self.obstacle_down = pygame.transform.scale(OBSTACLE_DOWN,
                                                    (self.width, self.height + self.add_height))
        self.obstacle_up = pygame.transform.scale(OBSTACLE_UP,
                                                  (self.width, self.height + self.add_height))

    def draw_column(self):
        """
        draw up and down columns
        """
        win.blit(self.obstacle_up, (self.x_coord, -self.y_coord))
        win.blit(self.obstacle_down, (self.x_coord, (self.height + self.add_height) + self.space - self.y_coord))
        win.blit(self.obstacle_up, (self.x_coord_new_column, - self.y_coord_new_column))
        win.blit(self.obstacle_down, (self.x_coord_new_column,
                                      (self.height + self.add_height) + self.space - self.y_coord_new_column))

    def moving(self):
        """
        manage obstacle's coordinate of x direction

        :return: updated obstacle coordinate(int)
        """
        self.x_coord -= self.obstacle_speed
        self.x_coord_new_column -= self.obstacle_speed

    def update(self):
        """
        create new obstacle when previous
        go out of screen

        :return: new coordinate of x direction(int)
        """
        if self.x_coord < -self.width:
            self.x_coord = 700
            self.y_coord = randint(130, 320)

        if self.x_coord_new_column < -self.width:
            self.x_coord_new_column = 700
            self.y_coord_new_column = randint(130, 320)
