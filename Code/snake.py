import sys
import subprocess
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pygame'])








# %% [markdown]
# #### 1. 모듈 임포트(Module import)
# 설치한 pygame library 및 기타 필요한 모듈을 사용하기 위해 import합니다.
#
# Import `pygame library` and other modules to use in this code








# %%
# Pygame module import
import pygame
# 시간 확인, random 부여 등을 위한 module import
# Modules for time checking and randomization
import random
import time








# %% [markdown]
# ##### 1-1. 게임 사전 설정(Settings on the game)
# 게임에 대한 기본적인 설정에 대한 변수 들을 미리 정의합니다.
#
# Define variables that initializes the game








# %%
# Frame 수 조절(초당 그려지는 수)
# Framerate per seconds
fps = 15








# 창의 크기
# Window size
frame = (720, 480)








# 색깔 정의 (Red, Green, Blue)
# Colors (R, G, B)
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)
yellow = pygame.Color(255, 255, 0)








# 시간을 흐르게 하기 위한 FPS counter
# FPS (frames per second) controller
fps_controller = pygame.time.Clock()








#%%
# Game 관련 변수들
# Game variables
snake_pos = [100, 50]
snake_body = [[100, 50], [100-10, 50], [100-(2*10), 50]]








food_pos = [random.randrange(1, (frame[0]//10)) * 10,
            random.randrange(1, (frame[1]//10)) * 10]
food_spawn = True
food_change_interval = 5000  # 5초마다 음식 위치 변경
last_food_change_time = 0  # 마지막 음식 변경 시간








#무적
shield_pos = [random.randrange(1, (frame[0]//10)) * 10,
              random.randrange(1, (frame[1]//10)) * 10]
shield_spawn = True
shield_active = False
shield_duration = 0








direction = 'RIGHT'








score = 0
# 장애물 변수 설정 및 초기화
obstacle_pos = [[200, 150], [300, 200], [400, 100],[50,350],[130,250],[500,450]]  # 초기 장애물 위치
obstacle_direction = ['LEFT', 'UP', 'RIGHT']  # 각 장애물의 초기 이동 방향






# %% [markdown]
# ##### 1-2. Pygame 초기화(Initialize Pygame)
# Pygame을 사용하기 위해 창 크기, 제목 등을 주어 초기화를 해줍니다.
# 만약 초기화를 실패하였다면 오류를 알려주고 종료하도록 합니다.
# 함수로 만들어서 게임이 동작하기 전에 부를 수 있도록 합니다.
#
# Initialize Pygame with window size, and title.
# When initializing Pygame failed, prints error and exit program.
# Run before executing main logic of the game.
# 색상 변경 관련 변수
color_change_duration = 500  # 색이 일치하는 시간 (밀리초)
color_change_interval = 10000  # 색이 일치하는 주기 (밀리초)
last_color_change_time = 0  # 마지막 색 변경 시간
is_color_changed = False  # 색이 변경되었는지 여부
























# %%
def Init(size):
    # 초기화 후 error가 일어났는지 알아봅니다.
    # Checks for errors encountered
    check_errors = pygame.init()








    # pygame.init() example output -> (6, 0)
    # 두번째 항목이 error의 수를 알려줍니다.
    # second number in tuple gives number of errors
    if check_errors[1] > 0:
        print(
            f'[!] Had {check_errors[1]} errors when initialising game, exiting...')
        sys.exit(-1)
    else:
        print('[+] Game successfully initialised')








    # pygame.display를 통해 제목, window size를 설정하고 초기화합니다.
    # Initialise game window using pygame.display
    pygame.display.set_caption('Snake Example with PyGame')
    game_window = pygame.display.set_mode(size)
    return game_window








# %% [markdown]
# ##### 1-3. 기본 logic 함수 모음(basic logics of the game)
# 게임을 플레이하기 위해 필요한 함수들의 모음입니다.
# 자세한 부분은 각 주석을 확인해주세요.
#
# This is the set of functions that are required in the game.
# You can see more details in comments on each cell.
















# %%
# Score
def show_score(window, size, choice, color, font, fontsize):
    # Score를 띄우기 위한 설정입니다.
    # Settings for showing score on screen
    score_font = pygame.font.SysFont(font, fontsize)
    score_surface = score_font.render('Score : ' + str(score), True, color)
    score_rect = score_surface.get_rect()








    # Game over 상황인지 게임중 상황인지에 따라 다른 위치를 선정합니다.
    # Select different location depending on the situation.
    if choice == 1:
        score_rect.midtop = (size[0]/10, 15)
    else:
        score_rect.midtop = (size[0]/2, size[1]/1.25)








    # 설정한 글자를 window에 복사합니다.
    # Copy the string to windows
    window.blit(score_surface, score_rect)








# %%
# Game Over
def game_over(window, size):
    # 'Game Over'문구를 띄우기 위한 설정입니다.
    # Settings of the 'Game Over' string to show on the screen
    my_font = pygame.font.SysFont('times new roman', 90)
    game_over_surface = my_font.render('Game Over', True, red)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (size[0]/2, size[1]/4)








    # window를 검은색으로 칠하고 설정했던 글자를 window에 복사합니다.
    # Fill window as black and copy 'Game Over' strings to main window.
    window.fill(black)
    window.blit(game_over_surface, game_over_rect)








    # 'show_score' 함수를 부릅니다.
    # Call 'show_score' function.
    show_score(window, size, 0, green, 'times', 20)








    # 그려진 화면을 실제로 띄워줍니다.
    # Show drawn windows to screen
    pygame.display.flip()








    # 3초 기다린 후 게임을 종료합니다.
    # exit program after 3 seconds.
    time.sleep(3)
    pygame.quit()
    sys.exit()
















# %%
# Keyboard input
def get_keyboard(key, cur_dir):
    # WASD, 방향키를 입력 받으면 해당 방향으로 이동합니다.
    # 방향이 반대방향이면 무시합니다.
    # Chnage direction using WASD or arrow key
    # Ignore keyboard input if input key has opposite direction
    if direction != 'DOWN' and key == pygame.K_UP or key == ord('w'):
        return 'UP'
    if direction != 'UP' and key == pygame.K_DOWN or key == ord('s'):
        return 'DOWN'
    if direction != 'RIGHT' and key == pygame.K_LEFT or key == ord('a'):
        return 'LEFT'
    if direction != 'LEFT' and key == pygame.K_RIGHT or key == ord('d'):
        return 'RIGHT'
    # 모두 해당하지 않다면 원래 방향을 돌려줍니다.
    # Return current direction if none of keyboard input occured
    return cur_dir








# %% [markdown]
# #### 2. 메인 프로그램
# Game이 동작하기 위한 메인 코드 입니다.  
#
# This is main code of the game.
#점수에따른 속도 변화 함수
def increase_speed(score):
    if score < 10:
        return 15  # initial speed
    elif 10 <= score < 20:
        return 20  # speed up at score 10
    elif 20 <= score < 30:
        return 25  # speed up at score 20
    elif 30 <= score < 40:
        return 30  # speed up at score 30
    elif 40 <= score < 50:
        return 35  # speed up at score 40
    else:
        return 40  # speed up at score 50 and beyond








# %%
# 초기화합니다.
# Initialize
main_window = Init(frame)








# 주황색 먹이 관련 변수 설정
yellow_food_pos = None  # 초기 위치를 None으로 설정
yellow_food_spawn = True
yellow_food_timer = 0
yellow_food_duration = 5000  # 5초
yellow_food_interval = 3000  # 3초
last_yellow_food_time = 0








# 주황색 먹이의 초기 위치 설정
def spawn_yellow_food():
    return [
        random.randrange(1, (frame[0] // 10)) * 10,
        random.randrange(1, (frame[1] // 10)) * 10
    ]


















while True:
    # 게임에서 event를 받아옵니다.
    # Get event from user
    for event in pygame.event.get():
        # 종료시 실제로 프로그램을 종료합니다.
        # Close program if QUIT event occured
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            # esc 키를 눌렀을떄 종료 신호를 보냅니다.
            # Create quit event when 'esc' key pressed
            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(pygame.QUIT))
            else:
                # 입력 키로 방향을 얻어냅니다.
                # Get direction with key
                direction = get_keyboard(event.key, direction)
 




    # 실제로 뱀의 위치를 옮깁니다.
    # Move the actual snake position
    if direction == 'UP':
        snake_pos[1] -= 10
    if direction == 'DOWN':
        snake_pos[1] += 10
    if direction == 'LEFT':
        snake_pos[0] -= 10
    if direction == 'RIGHT':
        snake_pos[0] += 10
    if shield_active:
        snake_pos[0] = snake_pos[0] % frame[0]
        snake_pos[1] = snake_pos[1] % frame[1]
   




   
# 노란색 먹이의 타이머 관리
    current_time = pygame.time.get_ticks()
    if yellow_food_spawn:
        yellow_food_pos = spawn_yellow_food()  # 노란색 먹이 생성
        yellow_food_timer = current_time
        yellow_food_spawn = False
    # 노란색 먹이가 화면에 나타나고 5초가 지나면 사라짐
    if current_time - yellow_food_timer < yellow_food_duration:
        pygame.draw.rect(main_window, yellow, pygame.Rect(yellow_food_pos[0], yellow_food_pos[1], 10, 10))
    else:
        yellow_food_spawn = True  # 새로운 노란색 먹이를 생성할 수 있도록 설정








    # 뱀이 노란색 먹이를 먹었는지 확인
    if yellow_food_pos and snake_pos[0] == yellow_food_pos[0] and snake_pos[1] == yellow_food_pos[1]:
        score -= 1  # 점수 1 감소
        yellow_food_pos = None  # 노란색 먹이 사라짐
        yellow_food_spawn = True  # 새로운 노란색 먹이를 생성할 수 있도록 설정








    # 우선 증가시키고 음식의 위치가 아니라면 마지막을 뺍니다.
    # Grow snake first, check if food is on sanke head(if not, delete last)
    snake_body.insert(0, list(snake_pos))
    if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
        score += 1
        food_spawn = False
    else:
        snake_body.pop()
            # 음식 위치 변경 로직 추가
    current_time = pygame.time.get_ticks()
    if current_time - last_food_change_time >= food_change_interval:
        food_spawn = False  # 음식 위치 변경
        last_food_change_time = current_time  # 타이머 업데이트








    # 음식이 없다면 음식을 랜덤한 위치에 생성합니다.
    # Spawning food on the screen with random position
    if not food_spawn:
        food_pos = [
            random.randrange(1, (frame[0]//10)) * 10,
            random.randrange(1, (frame[1]//10)) * 10
        ]
    food_spawn = True
        #무적 랜덤 생성
    if not shield_spawn:
        shield_pos = [random.randrange(1, (frame[0]//10)) * 10,
            random.randrange(1, (frame[1]//10)) * 10]
    shield_spawn = True
    #무적 먹을때
    if snake_pos[0] == shield_pos[0] and snake_pos[1] == shield_pos[1]:
        shield_active = True
        shield_duration = 75
        shield_spawn = False
    if not shield_spawn:
        shield_pos = [
            random.randrange(1, (frame[0]//10)) * 10,
            random.randrange(1, (frame[1]//10)) * 10
        ]
    shield_spawn = True
    if shield_active:
        shield_duration -= 1
        if shield_duration <= 0:
            shield_active = False






    # 우선 게임을 검은 색으로 채우고 뱀의 각 위치마다 그림을 그립니다.
    # Fill the screen black and draw each position of snake
    main_window.fill(black)
    # 뱀의 색 결정
    snake_color = green if not is_color_changed else black
    # 색 변경 로직
    current_time = pygame.time.get_ticks()
    if current_time - last_color_change_time >= color_change_interval:
        is_color_changed = not is_color_changed
        last_color_change_time = current_time
    # 뱀의 색 결정
    snake_color = green if not is_color_changed else black
   # 뱀 그리기
    for pos in snake_body:
        pygame.draw.rect(main_window, snake_color, pygame.Rect(pos[0], pos[1], 10, 10))




 
    # 음식을 그립니다.
    # Draw snake food
    pygame.draw.rect(main_window, white,
                     pygame.Rect(food_pos[0], food_pos[1], 10, 10))
    #무적 아이템을 그린다
    pygame.draw.rect(main_window, blue,
                     pygame.Rect(shield_pos[0], shield_pos[1], 10, 10))








# 노란색 음식을 그립니다 (조건에 따라)
    if yellow_food_pos:
        pygame.draw.rect(main_window, yellow, pygame.Rect(yellow_food_pos[0], yellow_food_pos[1], 10, 10))
   #무적 아이템을 그린다
    pygame.draw.rect(main_window, blue,
                     pygame.Rect(shield_pos[0], shield_pos[1], 10, 10))




    # Game Over 상태를 확인합니다.
    # Check Game Over conditions




    # 바깥 벽 처리를 합니다.
    # Check if the snake hit the wall
    if snake_pos[0] < 0 or snake_pos[0] > frame[0] - 10:
        game_over(main_window, frame)
    if snake_pos[1] < 0 or snake_pos[1] > frame[1] - 10:
        game_over(main_window, frame)


    # 게임 중 장애물 그리기
    for obs in obstacle_pos:
        pygame.draw.rect(main_window, red, pygame.Rect(obs[0], obs[1], 10, 10))








    # 장애물과의 충돌 처리
    for obs in obstacle_pos:
     if snake_pos[0] == obs[0] and snake_pos[1] == obs[1]:
        if not shield_active:
            game_over(main_window, frame)




    # 뱀의 몸에 닿았는지 확인합니다.
    # Check if the snake is hit itself
    for block in snake_body[1:]:
        if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
           if not shield_active:
            game_over(main_window, frame)


    # 점수를 띄워줍니다.
    # Show score with defined function
    show_score(main_window, frame, 1, white, 'consolas', 20)








    # 실제 화면에 보이도록 업데이트 해줍니다.
    # Refresh game screen
    pygame.display.update()




    # 해당 FPS만큼 대기합니다.
    # Refresh rate
    fps_controller.tick(increase_speed(score))
    # 색이 일치하는 시간 동안 대기
    if is_color_changed and current_time - last_color_change_time < color_change_duration:
        pygame.time.delay(color_change_duration)
    else:
        is_color_changed = False