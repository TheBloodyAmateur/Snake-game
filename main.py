import pygame
import random


class Snake:
    def __init__(self):
        self.snakeList = []
        self.snakeLength = 0
        self.clock = pygame.time.Clock()
        self.colour_point = (187, 75, 129)
        self.colour_player = (80, 128, 167)
        self.update_background()
        self.player_pos_x = 0
        self.player_pos_y = 0
        self.char_init()
        self.point_init()
        self.maingame()

    def maingame(self):
        pos_x_change = 0
        pos_y_change = 0
        speed = 10
        # Maingame loop
        while True:
            pygame.display.update()
            # Program waits for userinput
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        pos_y_change = speed
                        pos_x_change = 0
                    elif event.key == pygame.K_UP:
                        pos_y_change = -speed
                        pos_x_change = 0
                    elif event.key == pygame.K_RIGHT:
                        pos_x_change = speed
                        pos_y_change = 0
                    elif event.key == pygame.K_LEFT:
                        pos_x_change = -speed
                        pos_y_change = 0

            self.clock.tick(30)
            # Changing the position of the snake
            self.player_pos_y += pos_y_change
            self.player_pos_x += pos_x_change

            # If the snake hits any of the borders the game is over
            if self.player_pos_x > size - heigth_fence - player_size or self.player_pos_x < heigth_fence:
                self.end_text()
            elif self.player_pos_y > size - heigth_fence - player_size or self.player_pos_y < heigth_fence:
                self.end_text()

            # If the player collides with the point the snake is
            if self.player.colliderect(self.point):
                self.point_init()
                self.snakeLength += 10
            snake_head = [self.player_pos_x, self.player_pos_y]
            self.snakeList.append(snake_head)

            self.update_background()
            self.update_snake()

            if len(self.snakeList) > self.snakeLength:
                del self.snakeList[0]

            for snakeElement in self.snakeList[:-1]:
                if snakeElement == snake_head:
                    self.end_text()

            self.update()

    # Updating the background and the snake, due to the movement
    def update_background(self):
        screen.fill(colour_back)
        pygame.draw.rect(screen, colour_rec, pygame.Rect(0, 0, size, heigth_fence))
        pygame.draw.rect(screen, colour_rec, pygame.Rect(0, size - heigth_fence, size, heigth_fence))

        pygame.draw.rect(screen, colour_rec, pygame.Rect(0, heigth_fence, heigth_fence, size))
        pygame.draw.rect(screen, colour_rec, pygame.Rect(size - heigth_fence, 0, heigth_fence, size))

        image_grass = pygame.image.load("pictures/grass.png")
        image_grass = pygame.transform.scale(image_grass, (100, 100))
        image_rock = pygame.image.load("pictures/rock.png")
        image_rock = pygame.transform.scale(image_rock, (100, 100))
        screen.blit(image_rock, (200, 200))
        screen.blit(image_grass, (400, 500))

        font = pygame.font.SysFont("comicsans", 20)
        text = font.render(("Points: " + str(self.snakeLength)), True, (255, 255, 255))
        screen.blit(text, (10, 10))

    def end_text(self):
        font = pygame.font.SysFont("comicsans", 50)
        text = font.render("You failed!", True, (255, 0, 0))
        screen.blit(text, (100, 100))
        text = font.render(("Points: " + str(self.snakeLength)), True, (255, 0, 0))
        screen.blit(text, (100, 140))
        pygame.display.update()
        pygame.time.wait(5000)
        quit()

    # Initialise the snake
    def char_init(self):
        self.player_pos_x = random.randint(area_x, area_y)
        self.player_pos_y = random.randint(area_x, area_y)
        self.player = pygame.draw.rect(screen, self.colour_player,
                                       [self.player_pos_x, self.player_pos_y, player_size, player_size])

    # Initialise the point
    def point_init(self):
        self.point_pos_x = random.randint(area_x, area_y)
        self.point_pos_y = random.randint(area_x, area_y)
        self.point = pygame.draw.rect(screen, self.colour_point,
                                      [self.point_pos_x, self.point_pos_y, point_size, point_size])

    # Updating the snake on the new background
    def update(self):
        self.point = pygame.draw.rect(screen, self.colour_point,
                                      [self.point_pos_x, self.point_pos_y, point_size, point_size])
        self.player = pygame.draw.rect(screen, self.colour_player,
                                       [self.player_pos_x, self.player_pos_y, player_size, player_size])

    # Every snake rectangle changes it's position
    def update_snake(self):
        for XnY in self.snakeList:
            self.player = pygame.draw.rect(screen, self.colour_player, [XnY[0], XnY[1], player_size, player_size])


pygame.init()
# Size of the Window (Height & Width)
size = 800
heigth_fence = 40
point_size = 60
player_size = 30

colour_rec = (96, 0, 0)
colour_back = (0, 144, 0)

area_x = heigth_fence + point_size
area_y = size - heigth_fence - point_size

screen = pygame.display.set_mode((size, size))
pygame.display.set_caption("Snake")
Snake()
