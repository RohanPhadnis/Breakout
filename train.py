import threading
from abstractions import *


pygame.init()
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption('training')

run = True


class Environment:

    def __init__(self, model, num):
        self.model = model
        self.size = 800
        self.surf = pygame.Surface((self.size, self.size))
        self.display = pygame.Surface((self.size, self.size))
        self.ball = Ball(self.size)
        self.paddle = Paddle(self.size)
        self.bricks = [Brick(10 + x * 100, 20, (255, 0, 0)) for x in range(8)]
        self.thread = threading.Thread(target=self.compute)
        self.num = num

    def compute(self):
        counts = 0
        start = time.time()
        while run and len(self.bricks) > 0 and self.ball.position[1] - self.ball.radius <= self.paddle.position[1] + self.paddle.dimensions[1]:
            counts += 1

            self.surf.fill((0, 0, 0))
            self.ball.move()
            self.paddle.move()
            self.ball.draw(self.surf)
            self.paddle.draw(self.surf)

            if self.ball.detect_collision(self.paddle):
                self.model.score += 0.25 - abs(self.ball.position[0] - (self.paddle.position[0] + self.paddle.dimensions[0] / 2)) / self.size
                self.ball.velocity[1] = -abs(self.ball.velocity[1])
                self.ball.drift()
                if not self.ball.score:
                    self.ball.score = True

            for brick in self.bricks:
                brick.draw(self.surf)
                if self.ball.detect_collision(brick) and self.ball.score:
                    self.model.score += 1
                    self.ball.velocity[1] = abs(self.ball.velocity[1])
                    self.bricks.remove(brick)

            self.display.unlock()
            self.display.blit(self.surf, (0, 0))
            data = numpy.array(
                flatten(
                    flatten(
                        pygame.surfarray.pixels3d(
                            pygame.transform.scale(
                                pygame.transform.rotate(self.surf, 90), (80, 80))).tolist()
                    )
                )
            ) / 255.
            output = [abs(n) for n in self.model.calculate(data)]
            self.paddle.velocity = output.index(max(output)) - 1
        self.model.score -= abs(self.ball.position[0] - (self.paddle.position[0] + self.paddle.dimensions[0] / 2)) / self.size
        print('thread {}:'.format(self.num), counts / (time.time() - start))

    def start(self):
        self.thread.start()


envs = [Environment(Model([16, 32, 64, 3], 80*80*3), n) for n in range(16)]
for env in envs:
    env.start()

main_counts = 0
start_time = time.time()
while run:
    main_counts += 1
    for index, env in enumerate(envs):
        try:
            screen.blit(pygame.transform.scale(env.display, (200, 200)), ((index % 4) * 200, (index // 4) * 200))
        except pygame.error:
            pass
    for x in range(4):
        pygame.draw.line(screen, (255, 255, 255), (x*200, 0), (x*200, 800), 1)
    for y in range(4):
        pygame.draw.line(screen, (255, 255, 255), (0, y*200), (800, y*200), 1)
    for event in pygame.event.get():
        if event.type == QUIT:
            run = False
    pygame.display.update()

pygame.quit()
print('main:', main_counts / (time.time() - start_time))
exit()
