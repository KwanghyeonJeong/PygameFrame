# Use pygame
import pygame
################################################################
# 기본, 수정없이 그대로 사용하면 된다.
# You can use it as it is without any modification.
pygame.init() 

# 화면 크기 설정 (Set screen size)
screen_width = 480 # 가로
screen_height = 640 # 세로
screen = pygame.display.set_mode((screen_width,screen_height))

# 화면 타이틀 설정(set game title)
pygame.display.set_caption("set title") # game name

# FPS init
clock = pygame.time.Clock()
################################################################

# 1. 사용자 게임 초기화 (배경화면, 게임이미지, 좌표, 속도, 폰트 등)
# 이곳에 게임 초기화 코드 추가한다. (Add game initialization code here.)
# Background, gameimg, Coordinates, speed, font, etc ...

running = True
while running:
    dt = clock.tick(60)
    # 2. 이벤트 처리,키보드,마우스 (Event Handler)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # 이곳에 이벤트 처리 코드를 추가(Add Event Handler Code here)

    # 3. 게임캐릭터 위치 정의
    # 여기에 게임캐릭터 위치 코드 추가(Add Game Character Location Code here)

    # 4. 충돌 처리
    # 여기에 충돌처리 코드 추가(Add Conflict Handling Code here)

    # 5. 화면에 그리기
    # 여기에 화면 그리기 코드 추가(Add Screen Drawing Code here)


    ################################################################
    # You can use it as it is without any modification.
    pygame.display.update()
    ################################################################

################################################################
# You can use it as it is without any modification.

# pygame End
pygame.quit()
################################################################
