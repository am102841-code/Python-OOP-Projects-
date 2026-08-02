import pygame, sys, random, math
from pygame.locals import *

pygame.init()

# Colours
BACKGROUND = (255, 255, 255)

# Game Setup
FPS = 60
fpsClock = pygame.time.Clock()
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 300

WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Physics Simulator')

class Ball():
    def __init__(self, x, y, x_vel, y_vel, radius, color):
        self.x = x
        self.y = y
        self.x_vel = x_vel
        self.y_vel = y_vel
        self.radius = radius
        self.color = color

    def move(self):
        self.x += self.x_vel
        self.y += self.y_vel

    def check_walls(self):
        if self.x - self.radius <= 0 or self.x + self.radius >= WINDOW_WIDTH:
            self.x_vel *= -1
        if self.y - self.radius <= 0 or self.y + self.radius >= WINDOW_HEIGHT:
            self.y_vel *= -1

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius)

    def collide(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        distance = math.sqrt(dx ** 2 + dy ** 2)

        if distance <= self.radius + other.radius:
            # swap velocities
            self.x_vel, other.x_vel = other.x_vel, self.x_vel
            self.y_vel, other.y_vel = other.y_vel, self.y_vel

# The main function that controls the game
def main():
    looping = True

    ball = Ball(50, 50, 2, 2, 12.5, (0, 0, 190))
    ball2 = Ball(75, 75, 1.5, 1.5, 10,(60, 70, 40))
    ball3 = Ball(20, 75, 1,1, 7.5, (255, 200, 90))

    ball_list = [ball, ball2, ball3]

    # The main game loop
    while looping:
        # Get inputs
        for event in pygame.event.get():

            #keys = pygame.
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        # movement and collision for the physics ball
        for x in ball_list:
            x.move()
            x.check_walls()
            for i in range(len(ball_list)):
                for j in range(i + 1, len(ball_list)):
                    ball_list[i].collide(ball_list[j])

        # Processing
        # This section will be built out later

        # Render elements of the game
        WINDOW.fill(BACKGROUND) # draw background
        for y in ball_list:
            y.draw(WINDOW) # draw each different physics ball
        pygame.display.update()
        fpsClock.tick(FPS)


main()
