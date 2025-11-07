import math
import random

import pygame
from pygame.math import Vector2

# 窗口配置
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800

# 游戏参数
GAME_DURATION = 60  # 单位：秒
PLAYER_BASE_SPEED = 20
ACCELERATION_MULTIPLIER = 1.8
BALL_RADIUS = 20
BOUNCE_FACTOR = 0.85
COLLISION_FORCE = 28
BLUE_BALL_ACCELERATION = 0.99
BLUE_BALL_MAX_SPEED = 25
ACCELERATION_TIME_THRESHOLD = 27  # 0.45秒

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
# 使用中文字体（确保系统有SimHei字体）
font = pygame.font.SysFont("SimHei", 36)
large_font = pygame.font.SysFont("SimHei", 72, bold=True)

# 游戏状态
game_running = False
start_time = 0
score = 0

# 游戏对象
player = pygame.Rect(750, 750, 50, 50)
blue_ball_pos = Vector2(750, 750)
blue_ball_vel = Vector2()
yellow_ball_pos = Vector2(SCREEN_WIDTH // 2, 200)
yellow_ball_vel = Vector2(3, 0)

# 按键计时
key_timers = {pygame.K_UP: 0, pygame.K_DOWN: 0, pygame.K_LEFT: 0, pygame.K_RIGHT: 0}


def reset_game():
    global player, blue_ball_pos, blue_ball_vel, yellow_ball_pos, yellow_ball_vel, score, start_time, game_running
    player = pygame.Rect(750, 750, 50, 50)
    blue_ball_pos = Vector2(750, 750)
    random_angle = math.radians(random.uniform(0, 360))
    blue_ball_vel = Vector2(15 * math.cos(random_angle), 15 * math.sin(random_angle))
    yellow_ball_pos = Vector2(SCREEN_WIDTH // 2, 200)
    yellow_ball_vel = Vector2(3, 0)
    score = 0
    start_time = pygame.time.get_ticks()
    game_running = True


def check_collision(rect, circle_pos, radius):
    closest_x = max(rect.left, min(circle_pos.x, rect.right))
    closest_y = max(rect.top, min(circle_pos.y, rect.bottom))
    dx = circle_pos.x - closest_x
    dy = circle_pos.y - closest_y
    return dx**2 + dy**2 < radius**2


def ball_collision_detection(pos1, pos2, radius):
    return pos1.distance_to(pos2) < radius * 2


def handle_boundaries(position, velocity, radius):
    if position.x < radius:
        position.x = radius
        velocity.x = abs(velocity.x) * BOUNCE_FACTOR
    elif position.x > SCREEN_WIDTH - radius:
        position.x = SCREEN_WIDTH - radius
        velocity.x = -abs(velocity.x) * BOUNCE_FACTOR

    if position.y < radius:
        position.y = radius
        velocity.y = abs(velocity.y) * BOUNCE_FACTOR
    elif position.y > SCREEN_HEIGHT - radius:
        position.y = SCREEN_HEIGHT - radius
        velocity.y = -abs(velocity.y) * BOUNCE_FACTOR * 1.2
    return position, velocity


def update_blue_ball_ai():
    global blue_ball_vel
    target_direction = (yellow_ball_pos - blue_ball_pos).normalize()
    blue_ball_vel += target_direction * BLUE_BALL_ACCELERATION

    if blue_ball_vel.magnitude() > BLUE_BALL_MAX_SPEED:
        blue_ball_vel = blue_ball_vel.normalize() * BLUE_BALL_MAX_SPEED
    blue_ball_vel *= 0.99


def update_yellow_ball_ai():
    global yellow_ball_vel
    escape_direction = (yellow_ball_pos - player.center).normalize() + (yellow_ball_pos - blue_ball_pos).normalize()
    escape_direction = escape_direction.normalize()

    if yellow_ball_pos.x < 150 or yellow_ball_pos.x > SCREEN_WIDTH - 150:
        escape_direction.y += 0.8 * (-1 if yellow_ball_pos.y < SCREEN_HEIGHT / 2 else 1)
    if yellow_ball_pos.y < 150 or yellow_ball_pos.y > SCREEN_HEIGHT - 150:
        escape_direction.x += 0.8 * (-1 if yellow_ball_pos.x < SCREEN_WIDTH / 2 else 1)

    yellow_ball_vel += escape_direction * 0.035
    if yellow_ball_vel.magnitude() > 35:
        yellow_ball_vel = yellow_ball_vel.normalize() * 35


def draw_interface():
    if game_running:
        remaining_time = GAME_DURATION - (pygame.time.get_ticks() - start_time) // 1000
        score_text = font.render(f"分数: {score:.1f}", True, "white")
        time_text = font.render(f"剩余时间: {remaining_time}秒", True, "white")
        screen.blit(score_text, (10, 10))
        screen.blit(time_text, (10, 50))
    else:
        screen.fill("black")
        final_score_text = large_font.render(f"最终得分: {score:.1f}", True, "yellow")
        prompt_text = font.render("按回车键重新开始", True, "white")
        screen.blit(
            final_score_text,
            (
                SCREEN_WIDTH // 2 - final_score_text.get_width() // 2,
                SCREEN_HEIGHT // 2 - 50,
            ),
        )
        screen.blit(
            prompt_text,
            (SCREEN_WIDTH // 2 - prompt_text.get_width() // 2, SCREEN_HEIGHT // 2 + 50),
        )


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                running = False
            elif event.key == pygame.K_RETURN and not game_running:
                reset_game()

    if game_running:
        # 更新按键计时
        keys = pygame.key.get_pressed()
        for key in [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT]:
            key_timers[key] = key_timers[key] + 1 if keys[key] else 0

        # 玩家移动
        y_speed = PLAYER_BASE_SPEED
        x_speed = PLAYER_BASE_SPEED

        if keys[pygame.K_UP] and key_timers[pygame.K_UP] > ACCELERATION_TIME_THRESHOLD:
            y_speed *= ACCELERATION_MULTIPLIER
        if keys[pygame.K_DOWN] and key_timers[pygame.K_DOWN] > ACCELERATION_TIME_THRESHOLD:
            y_speed *= ACCELERATION_MULTIPLIER

        if keys[pygame.K_LEFT] and key_timers[pygame.K_LEFT] > ACCELERATION_TIME_THRESHOLD:
            x_speed *= ACCELERATION_MULTIPLIER
        if keys[pygame.K_RIGHT] and key_timers[pygame.K_RIGHT] > ACCELERATION_TIME_THRESHOLD:
            x_speed *= ACCELERATION_MULTIPLIER

        player.y = max(
            0,
            min(
                SCREEN_HEIGHT - 50,
                player.y - keys[pygame.K_UP] * y_speed + keys[pygame.K_DOWN] * y_speed,
            ),
        )
        player.x = max(
            0,
            min(
                SCREEN_WIDTH - 50,
                player.x - keys[pygame.K_LEFT] * x_speed + keys[pygame.K_RIGHT] * x_speed,
            ),
        )

        # 更新蓝球
        update_blue_ball_ai()
        blue_ball_pos += blue_ball_vel
        blue_ball_pos, blue_ball_vel = handle_boundaries(blue_ball_pos, blue_ball_vel, BALL_RADIUS)

        # 更新黄球
        update_yellow_ball_ai()
        yellow_ball_pos += yellow_ball_vel
        yellow_ball_pos, yellow_ball_vel = handle_boundaries(yellow_ball_pos, yellow_ball_vel, BALL_RADIUS)

        # 碰撞处理
        if ball_collision_detection(blue_ball_pos, yellow_ball_pos, BALL_RADIUS):
            collision_direction = (yellow_ball_pos - blue_ball_pos).normalize()
            blue_ball_vel = -collision_direction * COLLISION_FORCE * 0.7
            yellow_ball_vel = collision_direction * COLLISION_FORCE * 1.4
            score += 0.5

        if check_collision(player, yellow_ball_pos, BALL_RADIUS):
            direction = (yellow_ball_pos - player.center).normalize()
            yellow_ball_vel = direction * COLLISION_FORCE * 1.2
            score += 1

        if check_collision(player, blue_ball_pos, BALL_RADIUS):
            direction = (blue_ball_pos - player.center).normalize()
            blue_ball_vel = direction * COLLISION_FORCE * 0.8

        # 检查时间
        if (pygame.time.get_ticks() - start_time) // 1000 >= GAME_DURATION:
            game_running = False

    # 渲染
    screen.fill("black")
    if game_running:
        pygame.draw.rect(screen, "red", player)
        pygame.draw.circle(screen, "blue", blue_ball_pos, BALL_RADIUS)
        pygame.draw.circle(screen, "yellow", yellow_ball_pos, BALL_RADIUS)
    draw_interface()
    pygame.display.flip()
    clock.tick(60)

pygame.quit()