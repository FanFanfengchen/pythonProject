import math
import random

import pygame

# 常量配置
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
SQUARE_SIZE = 50
MOVE_STEP = 20
BALL_MOVE_FORCE = 0.5  # 小球控制力度

# 物理参数
CIRCLE_RADIUS = 20
GRAVITY = 0.7
DAMPING = 0.75  # 摩擦衰减
BOUNCE_STRENGTH = 0.9  # 增加弹跳强度
AIR_RESISTANCE = 0.99  # 空气阻力
MAX_Y_SPEED = 15  # 最大下落速度
SQUARE_MASS = 2.0  # 方块质量

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

# 游戏对象初始化
square = pygame.Rect(
    (SCREEN_WIDTH - SQUARE_SIZE) // 2,
    (SCREEN_HEIGHT - SQUARE_SIZE) // 2,
    SQUARE_SIZE,
    SQUARE_SIZE,
)
prev_square_pos = square.copy()

circle_pos = pygame.Vector2(SCREEN_WIDTH // 2, 50)
circle_vel = pygame.Vector2(3, 0)


def reset_ball():
    """重置小球位置和速度"""
    global circle_pos, circle_vel
    circle_pos = pygame.Vector2(SCREEN_WIDTH // 2, 50)
    # 随机方向（0-360度）初始速度
    angle = math.radians(random.uniform(0, 360))
    speed = 5
    circle_vel = pygame.Vector2(speed * math.cos(angle), speed * math.sin(angle))


def check_collision(rect, circle_pos, radius):
    """碰撞检测函数"""
    closest_x = max(rect.left, min(circle_pos.x, rect.right))
    closest_y = max(rect.top, min(circle_pos.y, rect.bottom))
    dx = circle_pos.x - closest_x
    dy = circle_pos.y - closest_y
    distance_sq = dx**2 + dy**2

    # 处理顶点碰撞
    is_corner = (closest_x in (rect.left, rect.right)) and (
        closest_y in (rect.top, rect.bottom)
    )

    if is_corner and distance_sq < radius**2:
        distance = math.sqrt(distance_sq)
        normal = (
            pygame.Vector2(dx / distance, dy / distance)
            if distance != 0
            else pygame.Vector2(0, 1)
        )
        return True, normal, radius - distance

    if distance_sq < radius**2:
        distance = math.sqrt(distance_sq)
        if distance == 0:
            left = circle_pos.x - rect.left
            right = rect.right - circle_pos.x
            top = circle_pos.y - rect.top
            bottom = rect.bottom - circle_pos.y
            min_side = min(left, right, top, bottom)
            if min_side == left:
                normal = pygame.Vector2(-1, 0)
            elif min_side == right:
                normal = pygame.Vector2(1, 0)
            elif min_side == top:
                normal = pygame.Vector2(0, -1)
            else:
                normal = pygame.Vector2(0, 1)
            return True, normal, radius
        normal = pygame.Vector2(dx / distance, dy / distance)
        return True, normal, radius - distance

    if rect.collidepoint(circle_pos):
        left = circle_pos.x - rect.left
        right = rect.right - circle_pos.x
        top = circle_pos.y - rect.top
        bottom = rect.bottom - circle_pos.y
        min_dist = min(left, right, top, bottom)
        if min_dist < radius:
            if min_dist == left:
                normal = pygame.Vector2(-1, 0)
            elif min_dist == right:
                normal = pygame.Vector2(1, 0)
            elif min_dist == top:
                normal = pygame.Vector2(0, -1)
            else:
                normal = pygame.Vector2(0, 1)
            return True, normal, radius - min_dist

    return False, None, 0


def handle_boundary_collision(pos, vel, radius):
    """边界碰撞处理"""
    # 垂直碰撞（增加底部弹跳强度）
    if pos.y > SCREEN_HEIGHT - radius:
        pos.y = SCREEN_HEIGHT - radius
        vel.y *= -BOUNCE_STRENGTH * 1.2  # 增加底部弹跳力度
        vel.x *= DAMPING
    elif pos.y < radius:
        pos.y = radius
        vel.y *= -BOUNCE_STRENGTH

    # 水平碰撞
    if pos.x > SCREEN_WIDTH - radius:
        pos.x = SCREEN_WIDTH - radius
        vel.x *= -BOUNCE_STRENGTH
    elif pos.x < radius:
        pos.x = radius
        vel.x *= -BOUNCE_STRENGTH

    return pos, vel


# 主循环
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:  # Q键重置小球
                reset_ball()

    # 方块控制
    keys = pygame.key.get_pressed()
    prev_square_pos = square.copy()
    if keys[pygame.K_UP]:
        square.y = max(0, square.y - MOVE_STEP)
    if keys[pygame.K_DOWN]:
        square.y = min(SCREEN_HEIGHT - SQUARE_SIZE, square.y + MOVE_STEP)
    if keys[pygame.K_LEFT]:
        square.x = max(0, square.x - MOVE_STEP)
    if keys[pygame.K_RIGHT]:
        square.x = min(SCREEN_WIDTH - SQUARE_SIZE, square.x + MOVE_STEP)

    # 小球WASD控制
    if keys[pygame.K_w]:
        circle_vel.y -= BALL_MOVE_FORCE
    if keys[pygame.K_s]:
        circle_vel.y += BALL_MOVE_FORCE
    if keys[pygame.K_a]:
        circle_vel.x -= BALL_MOVE_FORCE
    if keys[pygame.K_d]:
        circle_vel.x += BALL_MOVE_FORCE

    # 计算方块速度
    square_vel = pygame.Vector2(
        square.x - prev_square_pos.x, square.y - prev_square_pos.y
    )

    # 小球物理模拟
    circle_vel.y = min(circle_vel.y + GRAVITY, MAX_Y_SPEED)
    circle_vel *= AIR_RESISTANCE

    # 预测新位置
    new_pos = circle_pos + circle_vel

    # 边界碰撞处理
    new_pos, circle_vel = handle_boundary_collision(new_pos, circle_vel, CIRCLE_RADIUS)

    # 方块碰撞处理
    collided, normal, penetration = check_collision(square, new_pos, CIRCLE_RADIUS)
    if collided:
        new_pos += normal * penetration
        vel_normal = circle_vel.dot(normal) * normal
        vel_tangent = circle_vel - vel_normal

        # 加入方块速度影响
        square_effect = square_vel.dot(normal) * (1 / SQUARE_MASS)

        circle_vel = (
            (-vel_normal * BOUNCE_STRENGTH)
            + vel_tangent * DAMPING
            + square_effect * normal * 2
        )

    # 更新位置
    circle_pos = new_pos

    # 速度衰减
    if circle_vel.magnitude() < 0.1:
        circle_vel = pygame.Vector2()

    # 渲染
    screen.fill("black")
    pygame.draw.rect(screen, "red", square)
    pygame.draw.circle(screen, "blue", circle_pos, CIRCLE_RADIUS)
    pygame.display.flip()
    clock.tick(60)


