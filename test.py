import time
import threading

run = True


def function(num):
    global run
    name = 'log/data{}.txt'.format(num)
    try:
        open(name, 'x')
    except FileExistsError:
        pass
    file = open(name, 'w')
    count = 0
    start = time.time()
    while run:
        count += 1
        file.write('{}: {}\n'.format(time.time(), count))
    file.close()
    print('thread', str(num) + ':', count / (time.time() - start))


threads = [threading.Thread(target=function, args=[n]) for n in range(10)]
for thread in threads:
    thread.start()

i = input()
run = False

# import time
# import random
# import threading
# import numpy
# import pygame
# from pygame.locals import *
# from PIL import Image
#
# screen = pygame.display.set_mode((700, 700))
# screen.fill((0, 0, 0))
# run = True
#
#
# def draw_circle(x, y):
#     while run:
#         pygame.draw.circle(screen, (255, 255, 255), (x, y), 25)
#
#
# thread = threading.Thread(target=draw_circle, args=(random.randint(0, 700), random.randint(0, 700)))
# thread2 = threading.Thread(target=draw_circle, args=(random.randint(0, 700), random.randint(0, 700)))
# thread3 = threading.Thread(target=draw_circle, args=(random.randint(0, 700), random.randint(0, 700)))
# thread4 = threading.Thread(target=draw_circle, args=(random.randint(0, 700), random.randint(0, 700)))
# thread5 = threading.Thread(target=draw_circle, args=(random.randint(0, 700), random.randint(0, 700)))
# thread6 = threading.Thread(target=draw_circle, args=(random.randint(0, 700), random.randint(0, 700)))
# thread7 = threading.Thread(target=draw_circle, args=(random.randint(0, 700), random.randint(0, 700)))
# thread8 = threading.Thread(target=draw_circle, args=(random.randint(0, 700), random.randint(0, 700)))
# thread9 = threading.Thread(target=draw_circle, args=(random.randint(0, 700), random.randint(0, 700)))
# thread10 = threading.Thread(target=draw_circle, args=(random.randint(0, 700), random.randint(0, 700)))
# thread.start()
# thread2.start()
# thread3.start()
# thread4.start()
# thread5.start()
# thread6.start()
# thread7.start()
# thread8.start()
# thread9.start()
# thread10.start()
#
# while run:
#     for event in pygame.event.get():
#         if event.type == QUIT:
#             run = False
#     pygame.display.update()
#     array = pygame.surfarray.pixels3d(pygame.transform.rotate(screen, 90))
#     img = Image.fromarray(array)
#     img.save('data/img{}.png'.format(time.time()))
#
# pygame.quit()
# exit()
