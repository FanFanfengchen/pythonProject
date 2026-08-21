import math
import random

import pygame
from pygame.math import Vector2
from dataclasses import dataclass, field

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


@dataclass
class GameState:
    """
    游戏状态数据类
    封装所有游戏状态，替代全局变量
    """
    running: bool = False
    start_time: int = 0
    score: float = 0.0
    player: pygame.Rect = field(
        default_factory=lambda: pygame.Rect(750, 750, 50, 50)
    )
    blue_ball_pos: Vector2 = field(default_factory=lambda: Vector2(750, 750))
    blue_ball_vel: Vector2 = field(default_factory=Vector2)
    yellow_ball_pos: Vector2 = field(
        default_factory=lambda: Vector2(SCREEN_WIDTH // 2, 200)
    )
    yellow_ball_vel: Vector2 = field(default_factory=lambda: Vector2(3, 0))
    key_timers: dict = field(
        default_factory=lambda: {
            pygame.K_UP: 0,
            pygame.K_DOWN: 0,
            pygame.K_LEFT: 0,
            pygame.K_RIGHT: 0,
        }
    )

    def reset(self) -> None:
        """重置游戏状态到初始值"""
        self.player = pygame.Rect(750, 750, 50, 50)
        self.blue_ball_pos = Vector2(750, 750)
        random_angle = math.radians(random.uniform(0, 360))
        self.blue_ball_vel = Vector2(
            15 * math.cos(random_angle), 15 * math.sin(random_angle)
        )
        self.yellow_ball_pos = Vector2(SCREEN_WIDTH // 2, 200)
        self.yellow_ball_vel = Vector2(3, 0)
        self.score = 0.0
        self.start_time = pygame.time.get_ticks()
        self.running = True


def check_collision(rect: pygame.Rect, circle_pos: Vector2, radius: float) -> bool:
    """检测矩形与圆形的碰撞"""
    closest_x = max(rect.left, min(circle_pos.x, rect.right))
    closest_y = max(rect.top, min(circle_pos.y, rect.bottom))
    dx = circle_pos.x - closest_x
    dy = circle_pos.y - closest_y
    return dx**2 + dy**2 < radius**2


def ball_collision_detection(pos1: Vector2, pos2: Vector2, radius: float) -> bool:
    """检测两个球体之间的碰撞"""
    return pos1.distance_to(pos2) < radius * 2


def handle_boundaries(position: Vector2, velocity: Vector2, radius: float) -> tuple:
    """处理边界碰撞"""
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


def update_blue_ball_ai(state: GameState) -> None:
    """更新蓝球 AI（追击黄球）"""
    target_direction = (state.yellow_ball_pos - state.blue_ball_pos).normalize()
    state.blue_ball_vel += target_direction * BLUE_BALL_ACCELERATION

    if state.blue_ball_vel.magnitude() > BLUE_BALL_MAX_SPEED:
        state.blue_ball_vel = state.blue_ball_vel.normalize() * BLUE_BALL_MAX_SPEED
    state.blue_ball_vel *= 0.99


def update_yellow_ball_ai(state: GameState) -> None:
    """更新黄球 AI（逃离玩家和蓝球）"""
    escape_direction = (
        state.yellow_ball_pos - Vector2(state.player.center)
    ).normalize() + (state.yellow_ball_pos - state.blue_ball_pos).normalize()
    escape_direction = escape_direction.normalize()

    if state.yellow_ball_pos.x < 150 or state.yellow_ball_pos.x > SCREEN_WIDTH - 150:
        escape_direction.y += 0.8 * (
            -1 if state.yellow_ball_pos.y < SCREEN_HEIGHT / 2 else 1
        )
    if state.yellow_ball_pos.y < 150 or state.yellow_ball_pos.y > SCREEN_HEIGHT - 150:
        escape_direction.x += 0.8 * (
            -1 if state.yellow_ball_pos.x < SCREEN_WIDTH / 2 else 1
        )

    state.yellow_ball_vel += escape_direction * 0.035
    if state.yellow_ball_vel.magnitude() > 35:
        state.yellow_ball_vel = state.yellow_ball_vel.normalize() * 35


def update_player_movement(state: GameState, keys: list) -> None:
    """更新玩家移动"""
    # 更新按键计时
    for key in [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT]:
        state.key_timers[key] = state.key_timers[key] + 1 if keys[key] else 0

    y_speed = PLAYER_BASE_SPEED
    x_speed = PLAYER_BASE_SPEED

    if keys[pygame.K_UP] and state.key_timers[pygame.K_UP] > ACCELERATION_TIME_THRESHOLD:
        y_speed *= ACCELERATION_MULTIPLIER
    if keys[pygame.K_DOWN] and state.key_timers[pygame.K_DOWN] > ACCELERATION_TIME_THRESHOLD:
        y_speed *= ACCELERATION_MULTIPLIER
    if keys[pygame.K_LEFT] and state.key_timers[pygame.K_LEFT] > ACCELERATION_TIME_THRESHOLD:
        x_speed *= ACCELERATION_MULTIPLIER
    if keys[pygame.K_RIGHT] and state.key_timers[pygame.K_RIGHT] > ACCELERATION_TIME_THRESHOLD:
        x_speed *= ACCELERATION_MULTIPLIER

    state.player.y = max(
        0,
        min(
            SCREEN_HEIGHT - 50,
            state.player.y - keys[pygame.K_UP] * y_speed + keys[pygame.K_DOWN] * y_speed,
        ),
    )
    state.player.x = max(
        0,
        min(
            SCREEN_WIDTH - 50,
            state.player.x - keys[pygame.K_LEFT] * x_speed + keys[pygame.K_RIGHT] * x_speed,
        ),
    )


def handle_collisions(state: GameState) -> None:
    """处理所有碰撞逻辑"""
    # 蓝球与黄球碰撞
    if ball_collision_detection(state.blue_ball_pos, state.yellow_ball_pos, BALL_RADIUS):
        collision_direction = (state.yellow_ball_pos - state.blue_ball_pos).normalize()
        state.blue_ball_vel = -collision_direction * COLLISION_FORCE * 0.7
        state.yellow_ball_vel = collision_direction * COLLISION_FORCE * 1.4
        state.score += 0.5

    # 玩家与黄球碰撞
    if check_collision(state.player, state.yellow_ball_pos, BALL_RADIUS):
        direction = (state.yellow_ball_pos - Vector2(state.player.center)).normalize()
        state.yellow_ball_vel = direction * COLLISION_FORCE * 1.2
        state.score += 1

    # 玩家与蓝球碰撞
    if check_collision(state.player, state.blue_ball_pos, BALL_RADIUS):
        direction = (state.blue_ball_pos - Vector2(state.player.center)).normalize()
        state.blue_ball_vel = direction * COLLISION_FORCE * 0.8


def update_game(state: GameState) -> None:
    """更新游戏状态（每帧调用）"""
    keys = pygame.key.get_pressed()
    update_player_movement(state, keys)

    # 更新蓝球
    update_blue_ball_ai(state)
    state.blue_ball_pos += state.blue_ball_vel
    state.blue_ball_pos, state.blue_ball_vel = handle_boundaries(
        state.blue_ball_pos, state.blue_ball_vel, BALL_RADIUS
    )

    # 更新黄球
    update_yellow_ball_ai(state)
    state.yellow_ball_pos += state.yellow_ball_vel
    state.yellow_ball_pos, state.yellow_ball_vel = handle_boundaries(
        state.yellow_ball_pos, state.yellow_ball_vel, BALL_RADIUS
    )

    # 处理碰撞
    handle_collisions(state)

    # 检查时间
    if (pygame.time.get_ticks() - state.start_time) // 1000 >= GAME_DURATION:
        state.running = False


def draw_interface(screen: pygame.Surface, font: pygame.Font, large_font: pygame.Font, state: GameState) -> None:
    """绘制游戏界面"""
    if state.running:
        remaining_time = GAME_DURATION - (pygame.time.get_ticks() - state.start_time) // 1000
        score_text = font.render(f"分数: {state.score:.1f}", True, "white")
        time_text = font.render(f"剩余时间: {remaining_time}秒", True, "white")
        screen.blit(score_text, (10, 10))
        screen.blit(time_text, (10, 50))
    else:
        screen.fill("black")
        final_score_text = large_font.render(f"最终得分: {state.score:.1f}", True, "yellow")
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


def main() -> None:
    """游戏主入口"""
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("SimHei", 36)
    large_font = pygame.font.SysFont("SimHei", 72, bold=True)

    state = GameState()
    state.reset()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    running = False
                elif event.key == pygame.K_RETURN and not state.running:
                    state.reset()

        if state.running:
            update_game(state)

        # 渲染
        screen.fill("black")
        if state.running:
            pygame.draw.rect(screen, "red", state.player)
            pygame.draw.circle(screen, "blue", state.blue_ball_pos, BALL_RADIUS)
            pygame.draw.circle(screen, "yellow", state.yellow_ball_pos, BALL_RADIUS)
        draw_interface(screen, font, large_font, state)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
