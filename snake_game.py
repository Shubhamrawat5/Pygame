import pygame
import random
pygame.init()

# colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)

width = 500
height = 300
# Creating window
pygame.display.set_caption("Snake Game")
# pygame.display.update()
gameWindow = pygame.display.set_mode((width, height))

#game variable
exit_game = False
gmae_game = False
snake_x = 10
snake_y = 10
snake_size = 10
fps = 20
velocity_x = 0
velocity_y = 0

snake_list = []
snake_length = 0

food_x = random.randint(10, width-10)
food_x = food_x - (food_x % 10)
food_y = random.randint(10, height-10)
food_y = food_y - (food_y % 10)
clock = pygame.time.Clock()

# print(food_x, food_y)
score = 0
highScore = 0
font = pygame.font.SysFont(None, 55)

def resetGame(x, y):
    global snake_list, score
    score = 0
    snake_list = [[x,y]]
    global food_x
    food_x = random.randint(10, width - 10)
    food_x = food_x - (food_x % 10)
    global food_y
    food_y = random.randint(10, height - 10)
    food_y = food_y - (food_y % 10)


def scoreOnScreen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, (x,y))


def makeSnakeGrow(snake_list, snake_x, snake_y, snake_size):
    for i,j in snake_list:
        pygame.draw.rect(gameWindow, black, (i, j, snake_size, snake_size))

    if snake_list[len(snake_list)-1] in snake_list[0:len(snake_list)-2]:
        print("COLLAPSE !!!!!")
        resetGame(snake_x, snake_y)



while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                velocity_y = 0
                velocity_x = 10
            elif event.key == pygame.K_LEFT:
                velocity_y = 0
                velocity_x = - 10
            elif event.key == pygame.K_UP:
                velocity_x = 0
                velocity_y = - 10
            elif event.key == pygame.K_DOWN:
                velocity_x = 0
                velocity_y = 10

    if snake_x >= width:
        snake_x = 0
    elif snake_y >= height:
        snake_y = 0
    elif snake_x < 0:
        snake_x = width
    elif snake_y < 0:
        snake_y = height
    snake_x = snake_x + velocity_x
    snake_y = snake_y + velocity_y
    # print(snake_x, snake_y)
    if snake_x == food_x and snake_y == food_y:
        score += 1
        if highScore < score:
            highScore = score
        snake_length += 1
        print(score)
        food_x = random.randint(10, width - 10)
        food_x = food_x - (food_x % 10)
        food_y = random.randint(10, height - 10)
        food_y = food_y - (food_y % 10)
        # makeSnakeGrow(snake_list, snake_x, snake_y, snake_size)
        t = [snake_x, snake_y]
        snake_list.append(t)
        # print(food_x, food_y)

    t = [snake_x, snake_y]
    snake_list.append(t)
    # print(snake_list)
    gameWindow.fill(white)
    # scoreOnScreen("Score : " + str(score), red, 5, 5)
    pygame.display.set_caption("Snake Game   |   Score : "+str(score)+"   |   High Score : "+str(highScore))
    makeSnakeGrow(snake_list, snake_x, snake_y, snake_size)
    del snake_list[0]
    print(snake_list)

    pygame.draw.rect(gameWindow, red, (food_x, food_y, snake_size, snake_size))
    # pygame.draw.rect(gameWindow, black, (snake_x, snake_y, snake_size, snake_size))
    pygame.display.update()
    clock.tick(fps)