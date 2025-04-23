import pygame
import sys

# Pygame 초기화
pygame.init()

# 화면 설정
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("캐릭터 이동 게임")

# 색상 정의
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# 캐릭터 설정
player_size = 50
player_x = SCREEN_WIDTH // 2
player_y = SCREEN_HEIGHT // 2
player_speed = 5

# 게임 루프
clock = pygame.time.Clock()

while True:
    # 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 키 입력 처리
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:  # 왼쪽 화살표
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:  # 오른쪽 화살표
        player_x += player_speed
    if keys[pygame.K_UP]:  # 위쪽 화살표
        player_y -= player_speed
    if keys[pygame.K_DOWN]:  # 아래쪽 화살표
        player_y += player_speed

    # 화면 그리기
    screen.fill(WHITE)  # 배경 색상
    pygame.draw.rect(screen, BLUE, (player_x, player_y, player_size, player_size))  # 캐릭터

    # 화면 업데이트
    pygame.display.flip()

    # FPS 설정
    clock.tick(30)