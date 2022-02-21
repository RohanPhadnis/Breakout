import os
import time
import random
import pickle
import numpy
import pygame
from pygame.locals import *


def flatten(tensor):
    output = []
    for n in range(len(tensor)):
        output += list(tensor[n])
    return output


class Layer:

    def __init__(self, size, input_size):
        self.weights = numpy.array([[random.choice([-1, 1]) * random.random() for _ in range(input_size)] for _ in range(size)])
        self.biases = numpy.array([random.choice([-1, 1]) * random.random() for _ in range(size)])
        self.output = numpy.array([0 for _ in range(size)])
        self.size = size
        self.input_size = input_size

    def calculate(self, inputs):
        for n in range(self.size):
            self.output[n] = numpy.dot(self.weights[n], inputs) + self.biases[n]
        return self.output.copy()

    def mod_copy(self, mag=0):
        output = Layer(self.size, self.input_size)
        output.weights = self.weights.copy().tolist()
        output.biases = self.biases.copy().tolist()
        for x in range(self.size):
            for y in range(self.input_size):
                output.weights[x][y] += mag * random.choice([-1, 1]) * random.random()
            output.biases[x] += mag * random.choice([-1, 1]) * random.random()
        output.weights = numpy.array(output.weights)
        output.biases = numpy.array(output.biases)
        return output


class Model:

    def __init__(self, layer_config, input_size):
        self.size = len(layer_config)
        self.layer_config = layer_config
        self.input_size = input_size
        self.layers = []
        for n in range(self.size):
            if n == 0:
                self.layers.append(Layer(layer_config[0], input_size))
            else:
                self.layers.append(Layer(layer_config, self.layers[n-1].size))
        self.score = 0

    def calculate(self, inputs):
        for n in range(self.size):
            output = self.layers[n].calculate(inputs)
        return output.copy()

    def clone(self, mag=0, n=1):
        output = []
        for _ in range(n):
            l = []
            for layer in self.layers:
                l.append(layer.mod_copy(mag=mag))
            model = Model(layer_config=self.layer_config.copy(), input_size=self.input_size)
            model.layers = l.copy()
        return output

    def save(self):
        DIR = 'models/model{}'.format(time.time())
        os.mkdir(DIR)
        open('{}/model.pickle'.format(DIR), 'x')
        file = open('{}/model.pickle'.format(DIR), 'wb')
        pickle.dump(self, file)
        file.close()


# renders text on the screen
def show_text(window, text, x, y, color=(255, 255, 255), size=30):
    font = pygame.font.SysFont('times', size)
    window.blit(font.render(text, False, color), (x, y))


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


class Environment:

    def __init__(self, model):
        self.model = model
        self.size = 720
        self.surf = pygame.Surface((self.size, self.size))

    # def compute