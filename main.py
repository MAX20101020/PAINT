import pygame

pygame.init()


class Kvadrat:
    # Создаём класс квадрата
    def __init__(self, x, y):
        self.x = x  # координаты левого верхнего угла квадрата
        self.y = y
        self.color = 'blue'
        self.rect = pygame.Rect(x, y, 200, 50)  # создам квадрат размером 200 на 50

    def setText(self, text=''):
        font = pygame.font.SysFont('verdana', 25).render(text, True, 'black')  # создём шрифт для текста
        scr.blit(font, (self.rect.x, self.rect.y))  # отображаем наш текст

    def draw(self):
        pygame.draw.rect(scr, self.color, self.rect)  # рисуем квадрат


width = 500
height = 600
scr = pygame.display.set_mode((width, height))  # создаём переменную для нашего экрана размером 500 на 600

clock = pygame.time.Clock()

GameOver = False
while not GameOver:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GameOver = True

    scr.fill('white')  # заливаем экран белым цветом

    rect = Kvadrat(0, 0)  # создаём объект класса Kvadrat
    rect.draw()  # рисуем его
    rect.setText("Hello, World!")  # задаём текст для квадрата

    pygame.display.update()
    clock.tick(40)
