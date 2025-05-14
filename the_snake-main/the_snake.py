import pygame
import random
import sys
from typing import List, Tuple

# Инициализация Pygame
pygame.init()

# Константы
CELL_SIZE = 20
GRID_SIZE = CELL_SIZE  # Добавлено для теста
GRID_WIDTH = 32
GRID_HEIGHT = 24
SCREEN_WIDTH = CELL_SIZE * GRID_WIDTH
SCREEN_HEIGHT = CELL_SIZE * GRID_HEIGHT
BOARD_BACKGROUND_COLOR = (0, 0, 0)  # Добавлено для теста
FPS = 10

# Цвета
BLACK = BOARD_BACKGROUND_COLOR
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Направления движения
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Глобальные переменные для тестов
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()


class GameObject:
    """Базовый класс для всех игровых объектов."""
    
    def __init__(self, position: Tuple[int, int] = None):
        """
        Инициализация игрового объекта.
        
        Args:
            position: Начальная позиция объекта (по умолчанию - центр экрана)
        """
        if position is None:
            position = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.position = position
        self.body_color = None  # Должен быть переопределен в дочерних классах
    
    def draw(self, surface: pygame.Surface):
        """Абстрактный метод для отрисовки объекта."""
        pass


class Apple(GameObject):
    """Класс, представляющий яблоко в игре."""
    
    def __init__(self):
        """Инициализация яблока со случайной позицией."""
        super().__init__()
        self.body_color = RED
        self.randomize_position()
    
    def randomize_position(self):
        """Устанавливает случайную позицию для яблока в пределах игрового поля."""
        x = random.randint(0, GRID_WIDTH - 1) * CELL_SIZE
        y = random.randint(0, GRID_HEIGHT - 1) * CELL_SIZE
        self.position = (x, y)
    
    def draw(self, surface: pygame.Surface):
        """Отрисовывает яблоко на игровой поверхности."""
        rect = pygame.Rect(self.position[0], self.position[1], CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(surface, self.body_color, rect)
        pygame.draw.rect(surface, WHITE, rect, 1)


class Snake(GameObject):
    """Класс, представляющий змейку в игре."""
    
    def __init__(self):
        """Инициализация змейки с начальной позицией и направлением."""
        super().__init__()
        self.body_color = GREEN
        self.length = 1
        self.positions = [self.position]
        self.direction = RIGHT
        self.next_direction = None
        self.score = 0
    
    def update_direction(self):
        """Обновляет направление движения змейки."""
        if self.next_direction:
            # Запрещаем движение в противоположном направлении
            if (self.next_direction[0] * -1, self.next_direction[1] * -1) != self.direction:
                self.direction = self.next_direction
            self.next_direction = None
    
    def move(self):
        """Перемещает змейку в текущем направлении."""
        head_x, head_y = self.get_head_position()
        dir_x, dir_y = self.direction
        new_x = (head_x + dir_x * CELL_SIZE) % SCREEN_WIDTH
        new_y = (head_y + dir_y * CELL_SIZE) % SCREEN_HEIGHT
        new_position = (new_x, new_y)
        
        # Вставляем новую голову в начало списка
        self.positions.insert(0, new_position)
        
        # Если длина не увеличилась, удаляем хвост
        if len(self.positions) > self.length:
            self.positions.pop()
    
    def get_head_position(self) -> Tuple[int, int]:
        """Возвращает позицию головы змейки."""
        return self.positions[0]
    
    def grow(self):
        """Увеличивает длину змейки на 1."""
        self.length += 1
        self.score += 1
    
    def reset(self):
        """Сбрасывает змейку в начальное состояние."""
        self.length = 1
        self.positions = [(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)]
        self.direction = RIGHT
        self.next_direction = None
    
    def check_collision(self) -> bool:
        """Проверяет, столкнулась ли змейка сама с собой."""
        return self.get_head_position() in self.positions[1:]
    
    def draw(self, surface: pygame.Surface):
        """Отрисовывает змейку на игровой поверхности."""
        for position in self.positions:
            rect = pygame.Rect(position[0], position[1], CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(surface, self.body_color, rect)
            pygame.draw.rect(surface, BLACK, rect, 1)


def handle_keys(snake: Snake):
    """Обрабатывает нажатия клавиш для управления змейкой."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.next_direction = UP
            elif event.key == pygame.K_DOWN:
                snake.next_direction = DOWN
            elif event.key == pygame.K_LEFT:
                snake.next_direction = LEFT
            elif event.key == pygame.K_RIGHT:
                snake.next_direction = RIGHT


def main():
    """Основная функция игры."""
    pygame.display.set_caption("Змейка")
    
    # Создание объектов игры
    snake = Snake()
    apple = Apple()
    
    # Основной игровой цикл
    while True:
        # Обработка событий
        handle_keys(snake)
        
        # Обновление состояния игры
        snake.update_direction()
        snake.move()
        
        # Проверка на съедение яблока
        if snake.get_head_position() == apple.position:
            snake.grow()
            apple.randomize_position()
            # Убедимся, что яблоко не появилось на змейке
            while apple.position in snake.positions:
                apple.randomize_position()
        
        # Проверка на столкновение с собой
        if snake.check_collision():
            snake.reset()
        
        # Отрисовка
        screen.fill(BLACK)
        snake.draw(screen)
        apple.draw(screen)
        
        # Отображение счета
        font = pygame.font.SysFont('Arial', 20)
        score_text = font.render(f'Счет: {snake.score}', True, WHITE)
        screen.blit(score_text, (5, 5))
        
        pygame.display.update()
        clock.tick(FPS)


if __name__ == "__main__":
    main()