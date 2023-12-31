import pygame
import random
import os

pygame.init()

white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)

dis_width = 1920
dis_height = 1080
congratulation_image = pygame.image.load('highscoreimg.png')
    # Scale the image to fit the screen
congratulation_image = pygame.transform.scale(congratulation_image, (dis_width, dis_height))
loss_image = pygame.image.load('deadsnake.jpg')
    # Scale the image to fit the screen
loss_image = pygame.transform.scale(loss_image, (dis_width, dis_height))

dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game')

clock = pygame.time.Clock()
snake_block = 10
snake_speed = 30

font_style = pygame.font.SysFont(None, 50)
score_font = pygame.font.SysFont(None, 35)

def our_snake(snake_block, snake_List):
    for x in snake_List:
        pygame.draw.rect(dis, white, [x[0], x[1], snake_block, snake_block])

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    text_rect = mesg.get_rect(center=(dis_width / 2, dis_height / 2))  # Get the rectangle and center it
    dis.blit(mesg, text_rect) 

def gameLoop():
    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    if not os.path.exists('high_score.txt'):
        with open('high_score.txt', 'w') as f:
            f.write("0")

    with open('high_score.txt', 'r') as f:
        high_score = int(f.read())

    new_high_score = False

    while not game_over:

        while game_close == True:

            dis.fill(black)
            if new_high_score:
                dis.blit(congratulation_image, (0, 0))  # Display the image as background
                message("Congratulations! New High Score! Press C-Play Again or Q-Quits", red)
            else:
                dis.blit(loss_image, (0, 0))  # Display the image as background
                message("You Lost! Press C-Play Again or Q-Quit", red)
            score = score_font.render("High Score: " + str(high_score), True, white)
            dis.blit(score, [0, 0])
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
                game_close = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
                elif event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(black)
        pygame.draw.rect(dis, red, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)

        score = score_font.render("Score: " + str(Length_of_snake - 1), True, white)
        dis.blit(score, [0, 0])
        hscore = score_font.render("High Score: " + str(high_score), True, white)
        dis.blit(hscore, [1750, 0])
        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1

        if Length_of_snake - 1 > high_score:
            high_score = Length_of_snake - 1
            new_high_score = True
            with open('high_score.txt', 'w') as f:
                f.write(str(high_score))

        clock.tick(snake_speed)

    pygame.quit()
    quit()

gameLoop()
