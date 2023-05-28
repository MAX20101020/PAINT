import pygame

pygame.init()


class Kvadrat:
    # Создаём класс квадрата
    def __init__(self, x, y, color='white'):
        self.x = x  # координаты левого верхнего угла квадрата
        self.y = y
        self.color = color
        self.rect = pygame.Rect(x, y, 50, 50)  # создам квадрат размером 200 на 50

    def setText(self, text=''):
        font = pygame.font.SysFont('verdana', 25).render(text, True, 'black')  # создём шрифт для текста
        scr.blit(font, self.rect)  # отображаем наш текст

    def draw(self):
        pygame.draw.rect(scr, self.color, self.rect,)  # рисуем квадрат

class Palitra(Kvadrat):
    def __init__(self, x, y, color):
        super().__init__(x, y, color)


    def draw(self):
        pygame.draw.rect(scr, self.color, self.rect, 0, 90)  # рисуем квадрат


width = 500
height = 600
scr = pygame.display.set_mode((width, height))  # создаём переменную для нашего экрана размером 500 на 600

clock = pygame.time.Clock()

GameOver = False
while not GameOver:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GameOver = True

    scr.fill('light blue')

    circle_1 = Palitra(20, 520, 'gray')
    circle_1.draw()  # рисуем его
    circle_1.setText('1')

    circle_2 = Palitra(80, 520, 'yellow')
    circle_2.draw()
    circle_2.setText('2')

    circle_3 = Palitra(140, 520, 'red')
    circle_3.draw()
    circle_3.setText('3')

    circle_4 = Palitra(200, 520, 'white')
    circle_4.draw()
    circle_4.setText('4')

    circle_5 = Palitra(260, 520, 'pink')
    circle_5.draw()
    circle_5.setText('5')

    rect1 = Kvadrat(0, 0)
    rect1.draw()
    rect1.setText('1')

    pygame.display.update()
    clock.tick(40)
