"""
Citations:
    1. Python: https://www.python.org/
    2. random module: https://docs.python.org/3/library/random.html
    3. pygame module: pygame.org
    4. star.png file source: data:image/jpeg;base64,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
    5. IDE: https://www.jetbrains.com/pycharm/

System Requirements:
    1. Python (version 3.7.7)
    2. pygame (version 2.0.0)
"""

#   IMPORTING DEPENDENCIES

# the random module allows provides access to a multitude of mathematical operations to generate pseudorandom numbers
# used for random variability to make the game unpredictable
import random
# the pygame module is a 2D game engine in python
# used for graphics
import pygame
# the pygame.locals sub-module provides access to system event detections like key presses or mouse inputs
# used fpr event handling
from pygame.locals import *


#   ABSTRACTION USING OBJECT ORIENTATION AND FUNCTION DEFINITIONS


# renders text on the screen
def show_text(text, x, y, color=(255, 255, 255), size=30):
    font = pygame.font.SysFont('times', size)
    screen.blit(font.render(text, False, color), (x, y))


# the Brick class defines a generic rectangular object used in the game
class Brick:

    # constructor
    def __init__(self, x, y, color):
        self.position = [x, y]
        self.dimensions = [75, 50]
        self.color = color

    # draw function for graphic display
    def draw(self, window):
        pygame.draw.rect(window, self.color, self.position + self.dimensions)


# the Button class (subclass of Brick) is used to create rectangular buttons on the screen
class Button(Brick):

    # constructor
    def __init__(self, x, y, color, text):
        super().__init__(x, y, color)
        self.text = text
        self.dimensions = [len(text) * 35, 50]
        self.active = False

    # draw function for graphic display
    def draw(self, window):
        super().draw(window)
        show_text(self.text, self.position[0] + 20, self.position[1] + 10)

    # click detector
    # params (list): click_coordinates contains x and y points of a mouse click
    # return (boolean): returns True if the button is clicked
    def detect_click(self, click_coordinates):
        return (self.position[0] <= click_coordinates[0] <= self.position[0] + self.dimensions[0]) and (
                self.position[1] <= click_coordinates[1] <= self.position[1] + self.dimensions[1])


class Paddle(Brick):

    # constructor
    def __init__(self, size):
        super().__init__(int(size // 2) - 20, size - 40, (255, 255, 255))
        self.dimensions = [40, 20]
        self.velocity = 0
        self.window_size = size

    # move function to control the paddle's motion
    def move(self):
        if (self.position[0] < 0 and self.velocity < 0) or (
                self.position[0] + self.dimensions[0] > self.window_size and self.velocity > 0):
            pass
        else:
            self.position[0] += self.velocity * 1.5


class Ball:

    # constructor
    def __init__(self, size):
        self.radius = 10
        self.position = [int(size // 2), 5 * self.radius]
        self.velocity = [0, 0]
        self.maximum_velocity = 0
        self.gravity = 0.018
        self.screen_size = size
        self.score = False

    # move function to control the ball's motion
    def move(self):
        self.position[0] += self.velocity[0]
        self.position[1] += self.velocity[1]
        self.velocity[1] += self.gravity

        if self.position[0] - self.radius < 0:
            self.velocity[0] = abs(self.velocity[0])
        elif self.position[0] + self.radius > self.screen_size:
            self.velocity[0] = -abs(self.velocity[0])

    # draw function to render graphic display
    def draw(self, window):
        pygame.draw.circle(window, (255, 255, 255), self.position, self.radius)

    # drift function to randomly manipulate the ball's x-velocity component
    def drift(self):
        self.velocity[0] = random.randint(-10, 10) / 6

    # detect_collision function
    # params (Brick): the surface parameter holds a Brick (or sub-Brick) object
    # return (boolean): returns true if the ball has collided with the surface
    def detect_collision(self, surface):
        return (self.position[0] + self.radius >= surface.position[0] and self.position[0] - self.radius <=
                surface.position[0] + surface.dimensions[0]) and (
                       self.position[1] - self.radius <= surface.position[1] + surface.dimensions[1] and
                       self.position[1] + self.radius >= surface.position[1])


def display_metrics():
    pygame.draw.line(screen, (255, 255, 255), (WINDOW_SIZE, 0), (WINDOW_SIZE, 900), 1)
    show_text('metrics', WINDOW_SIZE + 50, 50)
    show_text('score: ' + str(score), WINDOW_SIZE + 50, 100)
    show_text('level: ' + str(level), WINDOW_SIZE + 50, 150)
    if pad.velocity < 0:
        show_text('key: left', WINDOW_SIZE + 50, 200)
    elif pad.velocity > 0:
        show_text('key: right', WINDOW_SIZE + 50, 200)
    else:
        show_text('key: none', WINDOW_SIZE + 50, 200)


def game_over_screen(win):
    global screen, home_button

    if win:
        show_text('CONGRATULATIONS! You won!', 250, 200)
        screen.blit(star, [WINDOW_SIZE // 2 - 50, 300])
    else:
        show_text('GAME OVER!', WINDOW_SIZE // 2, 200)
        show_text('Your final level was {}'.format(level), WINDOW_SIZE // 2, 250)
        show_text('Your final score was {}'.format(score), WINDOW_SIZE // 2, 300)

    home_button.draw(screen)
    home_button.active = True


def home_screen():
    global screen, play_button, quit_button
    show_text('BREAKOUT', 400, 100)
    play_button.draw(screen)
    quit_button.draw(screen)


#   GRAPHICS SETUP

WINDOW_SIZE = 720  # size of the playing window
pygame.init()  # graphics initialization
screen = pygame.display.set_mode((WINDOW_SIZE + 250, WINDOW_SIZE))  # screen object to hold the window
pygame.display.set_caption('breakout')  # title of the window
clock = pygame.time.Clock()  # clock object to control the graphics frame-rate

# VARIABLE DEFINITIONS

play_button = Button(WINDOW_SIZE // 2, WINDOW_SIZE // 3, (0, 0, 255), 'PLAY')  # button to start playing
quit_button = Button(WINDOW_SIZE // 2, 2 * WINDOW_SIZE // 3, (255, 0, 0), 'QUIT')  # button to quit
home_button = Button(WINDOW_SIZE // 2, 600, (255, 0, 255), 'HOME')  # button to return home
play = False  # holds if the game has started
star = pygame.image.load('star.png')  # star image

ball = None  # ball object (instantiated after play_button is clicked)
pad = None  # pad object (instantiated after play button is clicked)
bricks = []  # stored brick objects (instantiated after play button is clicked)
level = 1  # level (1 to 5 inclusive)
score = 0  # score: counts the total number of bricks destroyed
colors = [(255, 0, 0), (255, 255, 0), (0, 255, 0), (0, 255, 255),
          (0, 0, 255)]  # holds RGB color tuples for new bricks each level

while True:

    screen.fill((0, 0, 0))  # blanks screen out

    # if the user wins (results screen)
    if play and (ball.position[1] - ball.radius > WINDOW_SIZE or score == 120):
        game_over_screen(score == 120)
    # if the user is playing (game screen)
    elif play:

        display_metrics()
        ball.move()
        pad.move()
        ball.draw(screen)
        pad.draw(screen)

        for brick in bricks:
            brick.draw(screen)
            if ball.detect_collision(brick) and ball.score:
                score += 1
                bricks.remove(brick)
                ball.velocity[1] = abs(ball.velocity[1])

        if len(bricks) == 0:
            if level < len(colors):
                # pad.dimensions[0] += 10
                level += 1
                bricks = [Brick(x % 8 * 90, x // 8 * 55 + 20, colors[x // 8]) for x in range(8 * level)]

        if ball.detect_collision(pad):
            ball.position[1] = pad.position[1] - ball.radius
            ball.drift()
            if not ball.score:
                ball.maximum_velocity = ball.velocity[1]
                ball.score = True
            else:
                ball.velocity[1] = -ball.maximum_velocity
    # if the user is not playing (home screen)
    else:
        home_screen()

    # event handlers
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        elif event.type == KEYDOWN and play:
            if event.key == K_RIGHT:
                pad.velocity = 1
            elif event.key == K_LEFT:
                pad.velocity = -1
        elif event.type == KEYUP and play:
            if event.key == K_LEFT or event.key == K_RIGHT:
                pad.velocity = 0
        elif event.type == MOUSEBUTTONDOWN and event.button == 1:
            if play_button.detect_click(event.pos) and not play:
                play = True
                ball = Ball(WINDOW_SIZE)
                pad = Paddle(WINDOW_SIZE)
                level = 1
                score = 0
                bricks = [Brick(10 + x * 90, 20, colors[0]) for x in range(8)]
            elif quit_button.detect_click(event.pos) and not play:
                pygame.quit()
                exit()
            elif home_button.detect_click(event.pos) and home_button.active:
                home_button.active = False
                play = False

    clock.tick(160)  # frame-rate set to 40 fps
    pygame.display.update()  # graphics update
