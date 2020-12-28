import pygame
import random


class Snake:
    def __init__(self):
        self.snakeList = []
        self.snakeLength = 1
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
        #Maingame loop
        while True:
            pygame.display.update()
            #Program waits for userinput
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
            #Changing the position of the snake
            self.player_pos_y += pos_y_change
            self.player_pos_x += pos_x_change

            #If the snake hits any of the borders the game is over
            if self.player_pos_x > width - heigth_fence - player_size or self.player_pos_x < 50:
                quit()
            elif self.player_pos_y > width - heigth_fence - player_size or self.player_pos_y < 50:
                quit()

            #If the player collides with the point the snake is
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
                    quit()

            self.update()

    def char_init(self):
        self.player_pos_x = random.randint(area_x, area_y)
        self.player_pos_y = random.randint(area_x, area_y)
        self.player = pygame.draw.rect(screen, self.colour_player,
                                       [self.player_pos_x, self.player_pos_y, player_size, player_size])

    def point_init(self):
        self.point_pos_x = random.randint(area_x, area_y)
        self.point_pos_y = random.randint(area_x, area_y)
        self.point = pygame.draw.rect(screen, self.colour_point,
                                      [self.point_pos_x, self.point_pos_y, point_size, point_size])

    def update(self):
        self.point = pygame.draw.rect(screen, self.colour_point,
                                      [self.point_pos_x, self.point_pos_y, point_size, point_size])
        self.player = pygame.draw.rect(screen, self.colour_player,
                                       [self.player_pos_x, self.player_pos_y, player_size, player_size])

    def update_snake(self):
        for XnY in self.snakeList:
            self.player = pygame.draw.rect(screen, self.colour_player, [XnY[0], XnY[1], player_size, player_size])

    def update_background(self):
        screen.fill(colour_back)
        pygame.draw.rect(screen, colour_rec, pygame.Rect(0, 0, width, heigth_fence))
        pygame.draw.rect(screen, colour_rec, pygame.Rect(0, height - heigth_fence, width, heigth_fence))

        pygame.draw.rect(screen, colour_rec, pygame.Rect(0, heigth_fence, heigth_fence, height))
        pygame.draw.rect(screen, colour_rec, pygame.Rect(height - heigth_fence, 0, heigth_fence, height))

        font = pygame.font.SysFont("comicsans", 20)
        text = font.render(("Points: " + str(self.snakeLength)), True, (255, 255, 255))
        screen.blit(text, (10, 10))


pygame.init()
height = 800
width = 800
heigth_fence = 40

colour_rec = (96, 0, 0)
colour_back = (0, 144, 0)

player_size = 30
point_size = 60
area_x = heigth_fence + player_size
area_y = height - heigth_fence - player_size

screen = pygame.display.set_mode((height, width))
pygame.display.set_caption("Snake")
Snake()