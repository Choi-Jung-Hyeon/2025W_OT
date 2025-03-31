
import pygame
import random
import time
import sys
import datetime

# Pygame 초기화
pygame.init()


# Frame 설정
fps = 20
frame = (720, 480)

background_img = pygame.image.load("background.png")
background_img = pygame.transform.scale(background_img, frame)  # 화면 크기에 맞도록 사진 조정


# 색깔 정의
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0) #정상적인 먹이의 색
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)  # 잘못된 먹이의 색

# FPS 조절을 위한 Clock
fps_controller = pygame.time.Clock()

# Pygame 창 설정
def Init(size):
    pygame.display.set_caption('Snake Game')
    return pygame.display.set_mode(size)

# 점수 및 시간 표시 함수
def show_score(window, size, choice, color, font, fontsize, score, start_time):
    score_font = pygame.font.SysFont(font, fontsize)
    elapsed_time = (pygame.time.get_ticks() - start_time) // 1000  
    score_surface = score_font.render(f"Score: {score}  Time: {elapsed_time}s", True, color)
    score_rect = score_surface.get_rect()

    if choice == 1:
        score_rect.midtop = (size[0] / 5, 15)
    else:
        score_rect.midtop = (size[0] / 2, size[1] / 1.25)

    window.blit(score_surface, score_rect)

# Scoreboard 저장 함수
def save_score(score, elapsed_time):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("scores.txt", "a") as file:
        file.write(f"{score},{elapsed_time},{timestamp}\n")

# Scoreboard 읽기 및 정렬
def get_scoreboard():
    try:
        with open("scores.txt", "r") as file:
            scores = [line.strip().split(",") for line in file.readlines()]
            scores = sorted(scores, key=lambda x: int(x[0]), reverse=True)  # 점수로 분류
        return scores[:5]  # 상위 5명의 결과를 보여줌
    except FileNotFoundError:
        return []

# 🎮 게임 종료 화면 및 Scoreboard 표시
def game_over(window, size, score, start_time):
    elapsed_time = (pygame.time.get_ticks() - start_time) // 1000
    save_score(score, elapsed_time)  # 파일에 점수를 저장

    window.fill(black)

    # Game Over 메시지
    my_font = pygame.font.SysFont('times new roman', 90)
    game_over_surface = my_font.render('Game Over', True, red)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (size[0] / 2, size[1] / 6)
    window.blit(game_over_surface, game_over_rect)

    # 점수 표시
    show_score(window, size, 0, green, 'times', 20, score, start_time)

    # Scoreboard 표시
    scoreboard = get_scoreboard()
    font = pygame.font.SysFont('times new roman', 25)
    y_pos = size[1] / 3

    for i, (score, time_taken, timestamp) in enumerate(scoreboard):    #enumerate 파이썬 내장함수:순서가 있는 자료형을 입력받았을 때 ,인덱스와 값을 포함하여 리턴
        text = f"#{i+1}: Score: {score}, Time: {time_taken}s, {timestamp}"
        score_surface = font.render(text, True, white)
        score_rect = score_surface.get_rect()
        score_rect.midtop = (size[0] / 2, y_pos)
        window.blit(score_surface, score_rect)
        y_pos += 30

    # Restart & Quit 메시지
    restart_font = pygame.font.SysFont('times new roman', 30)
    restart_surface = restart_font.render("Press R to Restart or Q to Quit", True, white)
    restart_rect = restart_surface.get_rect()
    restart_rect.midtop = (size[0] / 2, y_pos + 40)
    window.blit(restart_surface, restart_rect)

    pygame.display.flip()

    # Restart or Quit
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    gameLoop()
                elif event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
def get_keyboard(key, direction):
    if direction != 'DOWN' and (key == pygame.K_UP or key == ord('w')):
        return 'UP'
    if direction != 'UP' and (key == pygame.K_DOWN or key == ord('s')):
        return 'DOWN'
    if direction != 'RIGHT' and (key == pygame.K_LEFT or key == ord('a')):
        return 'LEFT'
    if direction != 'LEFT' and (key == pygame.K_RIGHT or key == ord('d')):
        return 'RIGHT'
    return direction
#  게임 실행 함수
def gameLoop():
    fps = 20

   

    snake_pos = [100, 50]
    snake_body = [[100, 50], [90, 50], [80, 50]]
    food_pos = [random.randrange(1, (frame[0] // 10)) * 10, random.randrange(1, (frame[1] // 10)) * 10]
    bad_food_pos = [random.randrange(1, (frame[0] // 10)) * 10, random.randrange(1, (frame[1] // 10)) * 10]
    special_food_pos = [random.randrange(1, (frame[0] // 10)) * 10, random.randrange(1, (frame[1] // 10)) * 10]
    direction = 'RIGHT'
    reverse_controls = False
    reverse_start_time = 0
    score = 0
    start_time = pygame.time.get_ticks()
    main_window = Init(frame)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.event.post(pygame.event.Event(pygame.QUIT))
                else:
                    direction = get_keyboard(event.key, direction)
                    if reverse_controls:
                        direction = {'UP': 'DOWN', 'DOWN': 'UP', 'LEFT': 'RIGHT', 'RIGHT': 'LEFT'}.get(direction, direction)

        if reverse_controls and (pygame.time.get_ticks() - reverse_start_time) > 5000:
            reverse_controls = False

        if direction == 'UP':
            snake_pos[1] -= 10
        if direction == 'DOWN':
            snake_pos[1] += 10
        if direction == 'LEFT':
            snake_pos[0] -= 10
        if direction == 'RIGHT':
            snake_pos[0] += 10

        snake_body.insert(0, list(snake_pos))
        if snake_pos == food_pos:
            score += 1
            fps +=2
            food_pos = [random.randrange(1, (frame[0] // 10)) * 10, random.randrange(1, (frame[1] // 10)) * 10]
        elif snake_pos == bad_food_pos:
            reverse_controls = True
            reverse_start_time = pygame.time.get_ticks()
            bad_food_pos = [random.randrange(1, (frame[0] // 10)) * 10, random.randrange(1, (frame[1] // 10)) * 10]
        elif snake_pos == special_food_pos:
            special_food_pos = [random.randrange(1, (frame[0] // 10)) * 10, random.randrange(1, (frame[1] // 10)) * 10]
            score += random.randint(-5, 5) # 특별한 먹이를 먹었을 때 점수 -5~+5사이로 점수 추가
        elif score<0:
            game_over(main_window, frame, score, start_time)
        else:
            snake_body.pop()

        

        main_window.blit(background_img, (0, 0))
        for pos in snake_body:
            pygame.draw.rect(main_window, green, pygame.Rect(pos[0], pos[1], 10, 10))
        pygame.draw.rect(main_window, red, pygame.Rect(food_pos[0], food_pos[1], 10, 10))
        pygame.draw.rect(main_window, blue, pygame.Rect(bad_food_pos[0], bad_food_pos[1], 10, 10))
        pygame.draw.rect(main_window, white, pygame.Rect(special_food_pos[0], special_food_pos[1], 10, 10))
        



        # 충돌 감지
        if snake_pos[0] < 0:
            snake_pos[0] = frame[0] - 10
        elif snake_pos[0] > frame[0] - 10:
            snake_pos[0] = 0
        elif snake_pos[1] < 0 or snake_pos[1] > frame[1] - 10:
            game_over(main_window, frame, score, start_time)

        for block in snake_body[1:]:
            if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
                game_over(main_window, frame, score, start_time)

        show_score(main_window, frame, 1, white, 'consolas', 20, score, start_time)
        pygame.display.update()
        fps_controller.tick(fps)

# 게임 실행
gameLoop()
