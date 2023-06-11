import pygame

pygame.init()


class Kvadrat:
    def __init__(self, x, y, color='white'):
        self.x = x
        self.y = y
        self.color = color
        self.rect = pygame.Rect(x, y, 20, 20)

    def setText(self, text=''):
        font = pygame.font.SysFont('verdana', 18).render(text, True, 'black')
        scr.blit(font, self.rect)

    def draw(self):
        pygame.draw.rect(scr, self.color, self.rect,)

class Palitra(Kvadrat):
    def __init__(self, x, y, color):
        super().__init__(x, y, color)
        self.rect = pygame.Rect(x, y, 50, 50)

    def setText(self, text=''):
        font = pygame.font.SysFont('verdana', 25).render(text, True, 'black')
        scr.blit(font, self.rect)



    def draw(self):
        pygame.draw.rect(scr, self.color, self.rect, 0, 90)


width = 500
height = 600
scr = pygame.display.set_mode((width, height))

clock = pygame.time.Clock()

GameOver = False


scr.fill('light blue')

utochka = [["0", "0", "0", "0", "1", "0", "0", "0", "0", "1", "1", "1", "1", "1", "0", "0", "0", "0", "0", "0", "0", "0"],
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
           [],]




def vidilenie1():


while not GameOver:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GameOver = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            if circle_1.rect.collidepoint(event.pos):


    pygame.display.update()
    clock.tick(40)