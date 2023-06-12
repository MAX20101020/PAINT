import pygame
from tkinter import messagebox
pygame.init()


class Kvadrat:
    def __init__(self, x, y, color='white'):
        self.x = x
        self.y = y
        self.color = color
        self.rect = pygame.Rect(x, y, 20, 20)
        self.text = ''
        self.fill_color = ''

    def setText(self, text=''):
        if text == '0':
            self.text = ''
        else:
            self.text = text

        if text == '1':
            self.fill_color = 'grey'
        elif text == '2':
            self.fill_color = 'yellow'
        elif text == '3':
            self.fill_color = 'red'
        elif text == '4':
            self.fill_color = 'white'
        elif text == '5':
            self.fill_color = 'pink'

    def draw(self):
        pygame.draw.rect(scr, self.color, self.rect, 1, 0)
        font = pygame.font.SysFont('verdana', 18).render(self.text, True, 'black')
        scr.blit(font, (self.rect.x + 4, self.rect.y - 3))

    def fill(self, brush):
        if brush == 'null':
            messagebox.showinfo("Неправильный цвет", f"Выбите для начала цвет соответсувующий номеру квадратика")
        if brush == self.fill_color:
            pygame.draw.rect(scr, self.fill_color, self.rect)


class Palitra(Kvadrat):
    def __init__(self, x, y, color):
        super().__init__(x, y, color)
        self.rect = pygame.Rect(x, y, 50, 50)

    def setText(self, text=''):
        font = pygame.font.SysFont('verdana', 25).render(text, True, 'black')
        scr.blit(font, (self.rect.x + 16, self.rect.y + 9))

    def draw(self):
        pygame.draw.rect(scr, self.color, self.rect, 0, 90)


def createPicture(picture_points):
    _picture = []
    x = 0
    y = 0
    for i in range(len(picture_points)):
        for j in range(len(picture_points[0])):
            _picture.append(Kvadrat(x + 20 * j, y + 20 * i, 'black'))
            _picture[-1].setText(picture_points[i][j])
    return _picture


def drawPicture(pic):
    for el in pic:
        el.draw()
        el.setText()


width = 500
height = 600
scr = pygame.display.set_mode((width, height))

clock = pygame.time.Clock()
brush_color = 'null'

GameOver = False

scr.fill('light blue')

duck = [["0", "0", "0", "0", "1", "0", "0", "0", "0", "1", "1", "1", "1", "1", "0", "0", "0", "0", "0", "0", "0", "0"],
        ["0", "0", "0", "0", "2", "1", "0", "1", "1", "2", "2", "2", "2", "2", "1", "1", "0", "0", "0", "0", "0", "0"],
        ["0", "0", "0", "0", "1", "2", "1", "2", "2", "2", "2", "2", "2", "2", "2", "2", "1", "0", "0", "0", "0", "0"],
        ["0", "0", "0", "0", "2", "1", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "1", "0", "0", "0", "0"],
        ["0", "0", "0", "0", "0", "1", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "1", "0", "0", "0", "0"],
        ["0", "0", "0", "0", "1", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "1", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "1", "2", "2", "2", "2", "2", "2", "2", "1", "1", "4", "2", "2", "2", "3", "1", "1", "1"],
        ["0", "0", "0", "0", "1", "2", "2", "2", "2", "2", "2", "2", "1", "4", "1", "2", "2", "3", "3", "4", "3", "1"],
        ["0", "0", "0", "0", "1", "2", "2", "2", "2", "2", "2", "2", "1", "1", "1", "2", "2", "3", "3", "3", "3", "1"],
        ["0", "0", "0", "0", "1", "1", "2", "2", "2", "2", "2", "5", "5", "2", "2", "2", "3", "3", "3", "3", "1", "1"],
        ["0", "0", "0", "0", "0", "1", "1", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "1", "1", "1", "1", "0"],
        ["0", "1", "1", "1", "0", "0", "0", "1", "1", "2", "2", "2", "2", "2", "2", "2", "1", "1", "0", "0", "0", "0"],
        ["0", "1", "2", "2", "1", "1", "1", "2", "2", "1", "2", "2", "2", "1", "1", "1", "1", "0", "0", "0", "0", "0"],
        ["1", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "1", "0", "0", "0", "0", "0", "0", "0"],
        ["1", "2", "2", "2", "2", "2", "2", "2", "2", "1", "2", "2", "2", "2", "1", "0", "0", "0", "0", "0", "0", "0"],
        ["1", "2", "2", "2", "2", "2", "2", "2", "2", "1", "2", "2", "2", "2", "1", "0", "0", "0", "0", "0", "0", "0"],
        ["0", "1", "2", "2", "2", "1", "2", "2", "1", "2", "2", "2", "2", "2", "1", "0", "0", "0", "0", "0", "0", "0"],
        ["0", "1", "2", "2", "2", "2", "1", "1", "2", "2", "2", "2", "2", "1", "1", "0", "0", "0", "0", "0", "0", "0"],
        ["0", "0", "1", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "1", "0", "0", "0", "0", "0", "0", "0", "0"],
        ["0", "0", "0", "1", "2", "2", "2", "2", "2", "2", "2", "2", "1", "1", "0", "0", "0", "0", "0", "0", "0", "0"],
        ["0", "0", "0", "0", "1", "2", "2", "2", "2", "2", "2", "2", "1", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
        ["0", "0", "0", "0", "0", "1", "3", "1", "1", "1", "3", "1", "1", "1", "0", "0", "0", "0", "0", "0", "0", "0"],
        ["0", "0", "0", "0", "0", "1", "3", "3", "3", "1", "3", "3", "3", "1", "0", "0", "0", "0", "0", "0", "0", "0"],
        ["0", "0", "0", "0", "0", "1", "1", "1", "1", "1", "1", "1", "1", "1", "0", "0", "0", "0", "0", "0", "0", "0"]]

circle_1 = Palitra(20, 520, 'grey')
circle_1.draw()
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

cur_picture = createPicture(duck)
drawPicture(cur_picture)

GameOver = False
while not GameOver:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GameOver = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            if circle_1.rect.collidepoint(event.pos):
                brush_color = circle_1.color
            elif circle_2.rect.collidepoint(event.pos):
                brush_color = circle_2.color
            elif circle_3.rect.collidepoint(event.pos):
                brush_color = circle_3.color
            elif circle_4.rect.collidepoint(event.pos):
                brush_color = circle_4.color
            elif circle_5.rect.collidepoint(event.pos):
                brush_color = circle_5.color

            for pic in cur_picture:
                if pic.rect.collidepoint(event.pos):
                    pic.fill(brush_color)

    drawPicture(cur_picture)
    pygame.display.update()
    clock.tick(40)
