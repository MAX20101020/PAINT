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

    rect1_1 = Kvadrat(80, 0)
    rect1_1.draw()
    rect1_1.setText("1")

    rect1_2 = Kvadrat(100, 20)
    rect1_2.draw()
    rect1_2.setText("1")

    rect1_3 = Kvadrat(80, 40)
    rect1_3.draw()
    rect1_3.setText("1")

    rect1_4 = Kvadrat(120, 40)
    rect1_4.draw()
    rect1_4.setText("1")

    rect1_5 = Kvadrat(100, 60)
    rect1_5.draw()
    rect1_5.setText("1")

    rect1_6 = Kvadrat(100, 80)
    rect1_6.draw()
    rect1_6.setText("1")

    rect1_7 = Kvadrat(140, 20)
    rect1_7.draw()
    rect1_7.setText("1")

    rect1_8 = Kvadrat(160, 20)
    rect1_8.draw()
    rect1_8.setText("1")

    rect1_9 = Kvadrat(180, 0)
    rect1_9.draw()
    rect1_9.setText("1")

    rect1_10 = Kvadrat(200, 0)
    rect1_10.draw()
    rect1_10.setText("1")

    rect1_11 = Kvadrat(220, 0)
    rect1_11.draw()
    rect1_11.setText("1")

    rect1_12 = Kvadrat(240, 0)
    rect1_12.draw()
    rect1_12.setText("1")

    rect1_13 = Kvadrat(260, 0)
    rect1_13.draw()
    rect1_13.setText("1")

    rect1_14 = Kvadrat(280, 20)
    rect1_14.draw()
    rect1_14.setText("1")

    rect1_15 = Kvadrat(300, 20)
    rect1_15.draw()
    rect1_15.setText("1")

    rect1_16 = Kvadrat(320, 40)
    rect1_16.draw()
    rect1_16.setText("1")

    rect1_17 = Kvadrat(340, 60)
    rect1_17.draw()
    rect1_17.setText("1")

    rect1_18 = Kvadrat(340, 80)
    rect1_18.draw()
    rect1_18.setText("1")

    rect1_19 = Kvadrat(360, 100)
    rect1_19.draw()
    rect1_19.setText("1")

    rect1_20 = Kvadrat(360, 120)
    rect1_20.draw()
    rect1_20.setText("1")

    rect1_21 = Kvadrat(380, 140)
    rect1_21.draw()
    rect1_21.setText("1")

    rect1_22 = Kvadrat(400, 140)
    rect1_22.draw()
    rect1_22.setText("1")

    rect1_23 = Kvadrat(420, 140)
    rect1_23.draw()
    rect1_23.setText("1")

    rect1_24 = Kvadrat(420, 160)
    rect1_24.draw()
    rect1_24.setText("1")

    rect1_25 = Kvadrat(420, 180)
    rect1_25.draw()
    rect1_25.setText("1")

    rect1_26 = Kvadrat(420, 200)
    rect1_26.draw()
    rect1_26.setText("1")

    rect1_27 = Kvadrat(400, 200)
    rect1_27.draw()
    rect1_27.setText("1")

    rect1_28 = Kvadrat(400, 220)
    rect1_28.draw()
    rect1_28.setText("1")

    rect1_29 = Kvadrat(380, 220)
    rect1_29.draw()
    rect1_29.setText("1")

    rect1_30 = Kvadrat(360, 220)
    rect1_30.draw()
    rect1_30.setText("1")

    rect1_31 = Kvadrat(340, 220)
    rect1_31.draw()
    rect1_31.setText("1")

    rect1_32 = Kvadrat(340, 240)
    rect1_32.draw()
    rect1_32.setText("1")

    rect1_33 = Kvadrat(320, 240)
    rect1_33.draw()
    rect1_33.setText("1")

    rect1_34 = Kvadrat(320, 260)
    rect1_34.draw()
    rect1_34.setText("1")

    rect1_35 = Kvadrat(300, 260)
    rect1_35.draw()
    rect1_35.setText("1")

    rect1_36 = Kvadrat(280, 260)
    rect1_36.draw()
    rect1_36.setText("1")

    rect1_37 = Kvadrat(260, 260)
    rect1_37.draw()
    rect1_37.setText("1")

    rect1_38 = Kvadrat(280, 280)
    rect1_38.draw()
    rect1_38.setText("1")

    rect1_39 = Kvadrat(280, 300)
    rect1_39.draw()
    rect1_39.setText("1")

    rect1_40 = Kvadrat(280, 320)
    rect1_40.draw()
    rect1_40.setText("1")

    rect1_41 = Kvadrat(280, 340)
    rect1_41.draw()
    rect1_41.setText("1")

    rect1_42 = Kvadrat(280, 360)
    rect1_42.draw()
    rect1_42.setText("1")

    rect1_43 = Kvadrat(260, 360)
    rect1_43.draw()
    rect1_43.setText("1")

    rect1_44 = Kvadrat(260, 380)
    rect1_44.draw()
    rect1_44.setText("1")

    rect1_45 = Kvadrat(260, 400)
    rect1_45.draw()
    rect1_45.setText("1")

    rect1_46 = Kvadrat(240, 400)
    rect1_46.draw()
    rect1_46.setText("1")

    rect1_47 = Kvadrat(240, 420)
    rect1_47.draw()
    rect1_47.setText("1")

    rect1_48 = Kvadrat(240, 440)
    rect1_48.draw()
    rect1_48.setText("1")

    rect1_49 = Kvadrat(220, 440)
    rect1_49.draw()
    rect1_49.setText("1")

    rect1_50 = Kvadrat(260, 440)
    rect1_50.draw()
    rect1_50.setText("1")

    rect1_51 = Kvadrat(260, 460)
    rect1_51.draw()
    rect1_51.setText("1")

    rect1_52 = Kvadrat(260, 480)
    rect1_52.draw()
    rect1_52.setText("1")

    rect1_53 = Kvadrat(240, 480)
    rect1_53.draw()
    rect1_53.setText("1")

    rect1_54 = Kvadrat(220, 480)
    rect1_54.draw()
    rect1_54.setText("1")

    rect1_55 = Kvadrat(200, 480)
    rect1_55.draw()
    rect1_55.setText("1")

    rect1_56 = Kvadrat(180, 480)
    rect1_56.draw()
    rect1_56.setText("1")

    rect1_57 = Kvadrat(180, 460)
    rect1_57.draw()
    rect1_57.setText("1")

    rect1_58 = Kvadrat(180, 440)
    rect1_58.draw()
    rect1_58.setText("1")

    rect1_59 = Kvadrat(160, 440)
    rect1_59.draw()
    rect1_59.setText("1")

    rect1_60 = Kvadrat(140, 440)
    rect1_60.draw()
    rect1_60.setText("1")

    rect1_61 = Kvadrat(160, 480)
    rect1_61.draw()
    rect1_61.setText("1")

    rect1_62 = Kvadrat(140, 480)
    rect1_62.draw()
    rect1_62.setText("1")

    rect1_63 = Kvadrat(120, 480)
    rect1_63.draw()
    rect1_63.setText("1")

    rect1_64 = Kvadrat(100, 480)
    rect1_64.draw()
    rect1_64.setText("1")

    rect1_65 = Kvadrat(100, 460)
    rect1_65.draw()
    rect1_65.setText("1")

    rect1_66 = Kvadrat(100, 440)
    rect1_66.draw()
    rect1_66.setText("1")

    rect1_67 = Kvadrat(80, 420)
    rect1_67.draw()
    rect1_67.setText("1")

    rect1_68 = Kvadrat(60, 400)
    rect1_68.draw()
    rect1_68.setText("1")

    rect1_69 = Kvadrat(40, 380)
    rect1_69.draw()
    rect1_69.setText("1")

    rect1_70 = Kvadrat(20, 360)
    rect1_70.draw()
    rect1_70.setText("1")

    rect1_71 = Kvadrat(20, 340)
    rect1_71.draw()
    rect1_71.setText("1")

    rect1_72 = Kvadrat(0, 320)
    rect1_72.draw()
    rect1_72.setText("1")

    rect1_73 = Kvadrat(0, 300)
    rect1_73.draw()
    rect1_73.setText("1")

    rect1_74 = Kvadrat(0, 280)
    rect1_74.draw()
    rect1_74.setText("1")

    rect1_75 = Kvadrat(20, 260)
    rect1_75.draw()
    rect1_75.setText("1")

    rect1_76 = Kvadrat(20, 240)
    rect1_76.draw()
    rect1_76.setText("1")

    rect1_77 = Kvadrat(40, 240)
    rect1_77.draw()
    rect1_77.setText("1")

    rect1_78 = Kvadrat(60, 240)
    rect1_78.draw()
    rect1_78.setText("1")

    rect1_79 = Kvadrat(80, 260)
    rect1_79.draw()
    rect1_79.setText("1")

    rect1_80 = Kvadrat(100, 260)
    rect1_80.draw()
    rect1_80.setText("1")

    rect1_81 = Kvadrat(120, 260)
    rect1_81.draw()
    rect1_81.setText("1")

    rect1_82 = Kvadrat(140, 240)
    rect1_82.draw()
    rect1_82.setText("1")

    rect1_83 = Kvadrat(160, 240)
    rect1_83.draw()
    rect1_83.setText("1")

    rect1_84 = Kvadrat(180, 260)
    rect1_84.draw()
    rect1_84.setText("1")

    rect1_85 = Kvadrat(180, 300)
    rect1_85.draw()
    rect1_85.setText("1")

    rect1_86 = Kvadrat(180, 320)
    rect1_86.draw()
    rect1_86.setText("1")

    rect1_87 = Kvadrat(160, 340)
    rect1_87.draw()
    rect1_87.setText("1")

    rect1_88 = Kvadrat(140, 360)
    rect1_88.draw()
    rect1_88.setText("1")

    rect1_89 = Kvadrat(120, 360)
    rect1_89.draw()
    rect1_89.setText("1")

    rect1_90 = Kvadrat(100, 340)
    rect1_90.draw()
    rect1_90.setText("1")

    rect1_91 = Kvadrat(120, 220)
    rect1_91.draw()
    rect1_91.setText("1")

    rect1_92 = Kvadrat(100, 220)
    rect1_92.draw()
    rect1_92.setText("1")

    rect1_93 = Kvadrat(100, 200)
    rect1_93.draw()
    rect1_93.setText("1")

    rect1_94 = Kvadrat(80, 200)
    rect1_94.draw()
    rect1_94.setText("1")

    rect1_95 = Kvadrat(80, 180)
    rect1_95.draw()
    rect1_95.setText("1")

    rect1_96 = Kvadrat(80, 160)
    rect1_96.draw()
    rect1_96.setText("1")

    rect1_97 = Kvadrat(80, 140)
    rect1_97.draw()
    rect1_97.setText("1")

    rect1_98 = Kvadrat(80, 120)
    rect1_98.draw()
    rect1_98.setText("1")

    rect1_99 = Kvadrat(80, 100)
    rect1_99.draw()
    rect1_99.setText("1")

    rect1_100 = Kvadrat(240, 140)
    rect1_100.draw()
    rect1_100.setText("1")

    rect1_101 = Kvadrat(260, 140)
    rect1_101.draw()
    rect1_101.setText("1")

    rect1_102 = Kvadrat(240, 160)
    rect1_102.draw()
    rect1_102.setText("1")

    rect1_103 = Kvadrat(240, 180)
    rect1_103.draw()
    rect1_103.setText("1")

    rect1_104 = Kvadrat(260, 180)
    rect1_104.draw()
    rect1_104.setText("1")

    rect1_105 = Kvadrat(280, 180)
    rect1_105.draw()
    rect1_105.setText("1")

    rect1_107 = Kvadrat(280, 160)
    rect1_107.draw()
    rect1_107.setText("1")

    rect2_1 = Kvadrat(80, 20)
    rect2_1.draw()
    rect2_1.setText("2")

    rect2_2 = Kvadrat(100, 40)
    rect2_2.draw()
    rect2_2.setText("2")

    rect2_3 = Kvadrat(80, 60)
    rect2_3.draw()
    rect2_3.setText("2")

    rect2_4 = Kvadrat(180, 20)
    rect2_4.draw()
    rect2_4.setText("2")

    rect2_5 = Kvadrat(200, 20)
    rect2_5.draw()
    rect2_5.setText("2")

    rect2_6 = Kvadrat(220, 20)
    rect2_6.draw()
    rect2_6.setText("2")

    rect2_7 = Kvadrat(240, 20)
    rect2_7.draw()
    rect2_7.setText("2")

    rect2_8 = Kvadrat(260, 20)
    rect2_8.draw()
    rect2_8.setText("2")

    rect2_9 = Kvadrat(140, 40)
    rect2_9.draw()
    rect2_9.setText("2")

    rect2_10 = Kvadrat(160, 40)
    rect2_10.draw()
    rect2_10.setText("2")

    rect2_11 = Kvadrat(180, 40)
    rect2_11.draw()
    rect2_11.setText("2")

    rect2_12 = Kvadrat(200, 40)
    rect2_12.draw()
    rect2_12.setText("2")

    rect2_13 = Kvadrat(220, 40)
    rect2_13.draw()
    rect2_13.setText("2")

    rect2_14 = Kvadrat(240, 40)
    rect2_14.draw()
    rect2_14.setText("2")

    rect2_15 = Kvadrat(260, 40)
    rect2_15.draw()
    rect2_15.setText("2")

    rect2_16 = Kvadrat(280, 40)
    rect2_16.draw()
    rect2_16.setText("2")

    rect2_17 = Kvadrat(300, 40)
    rect2_17.draw()
    rect2_17.setText("2")

    rect2_18 = Kvadrat(120, 60)
    rect2_18.draw()
    rect2_18.setText("2")

    rect2_19 = Kvadrat(140, 60)
    rect2_19.draw()
    rect2_19.setText("2")

    rect2_20 = Kvadrat(160, 60)
    rect2_20.draw()
    rect2_20.setText("2")

    rect2_21 = Kvadrat(180, 60)
    rect2_21.draw()
    rect2_21.setText("2")

    rect2_22 = Kvadrat(200, 60)
    rect2_22.draw()
    rect2_22.setText("2")

    rect2_23 = Kvadrat(220, 60)
    rect2_23.draw()
    rect2_23.setText("2")

    rect2_24 = Kvadrat(240, 60)
    rect2_24.draw()
    rect2_24.setText("2")

    rect2_25 = Kvadrat(240, 60)
    rect2_25.draw()
    rect2_25.setText("2")

    rect2_26 = Kvadrat(260, 60)
    rect2_26.draw()
    rect2_26.setText("2")

    rect2_27 = Kvadrat(280, 60)
    rect2_27.draw()
    rect2_27.setText("2")

    rect2_28 = Kvadrat(300, 60)
    rect2_28.draw()
    rect2_28.setText("2")

    rect2_29 = Kvadrat(320, 60)
    rect2_29.draw()
    rect2_29.setText("2")

    rect2_30 = Kvadrat(120, 80)
    rect2_30.draw()
    rect2_30.setText("2")

    rect2_31 = Kvadrat(140, 80)
    rect2_31.draw()
    rect2_31.setText("2")

    rect2_32 = Kvadrat(160, 80)
    rect2_32.draw()
    rect2_32.setText("2")

    rect2_33 = Kvadrat(180, 80)
    rect2_33.draw()
    rect2_33.setText("2")

    rect2_34 = Kvadrat(200, 80)
    rect2_34.draw()
    rect2_34.setText("2")

    rect2_35 = Kvadrat(220, 80)
    rect2_35.draw()
    rect2_35.setText("2")

    rect2_36 = Kvadrat(240, 80)
    rect2_36.draw()
    rect2_36.setText("2")

    rect2_37 = Kvadrat(260, 80)
    rect2_37.draw()
    rect2_37.setText("2")

    rect2_38 = Kvadrat(280, 80)
    rect2_38.draw()
    rect2_38.setText("2")

    rect2_39 = Kvadrat(300, 80)
    rect2_39.draw()
    rect2_39.setText("2")

    rect2_40 = Kvadrat(320, 80)
    rect2_40.draw()
    rect2_40.setText("2")

    rect2_41 = Kvadrat(100, 100)
    rect2_41.draw()
    rect2_41.setText("2")

    rect2_42 = Kvadrat(120, 100)
    rect2_42.draw()
    rect2_42.setText("2")

    rect2_43 = Kvadrat(140, 100)
    rect2_43.draw()
    rect2_43.setText("2")

    rect2_44 = Kvadrat(160, 100)
    rect2_44.draw()
    rect2_44.setText("2")

    rect2_45 = Kvadrat(180, 100)
    rect2_45.draw()
    rect2_45.setText("2")

    rect2_46 = Kvadrat(200, 100)
    rect2_46.draw()
    rect2_46.setText("2")

    rect2_47 = Kvadrat(220, 100)
    rect2_47.draw()
    rect2_47.setText("2")

    rect2_48 = Kvadrat(240, 100)
    rect2_48.draw()
    rect2_48.setText("2")

    rect2_49 = Kvadrat(260, 100)
    rect2_49.draw()
    rect2_49.setText("2")

    rect2_50 = Kvadrat(280, 100)
    rect2_50.draw()
    rect2_50.setText("2")

    rect2_51 = Kvadrat(300, 100)
    rect2_51.draw()
    rect2_51.setText("2")

    rect2_52 = Kvadrat(320, 100)
    rect2_52.draw()
    rect2_52.setText("2")

    rect2_53 = Kvadrat(340, 100)
    rect2_53.draw()
    rect2_53.setText("2")

    rect2_54 = Kvadrat(100, 120)
    rect2_54.draw()
    rect2_54.setText("2")

    rect2_55 = Kvadrat(120, 120)
    rect2_55.draw()
    rect2_55.setText("2")

    rect2_56 = Kvadrat(140, 120)
    rect2_56.draw()
    rect2_56.setText("2")

    rect2_57 = Kvadrat(160, 120)
    rect2_57.draw()
    rect2_57.setText("2")

    rect2_58 = Kvadrat(180, 120)
    rect2_58.draw()
    rect2_58.setText("2")

    rect2_59 = Kvadrat(200, 120)
    rect2_59.draw()
    rect2_59.setText("2")

    rect2_60 = Kvadrat(220, 120)
    rect2_60.draw()
    rect2_60.setText("2")

    rect2_61 = Kvadrat(240, 120)
    rect2_61.draw()
    rect2_61.setText("2")

    rect2_62 = Kvadrat(260, 120)
    rect2_62.draw()
    rect2_62.setText("2")

    rect2_63 = Kvadrat(280, 120)
    rect2_63.draw()
    rect2_63.setText("2")

    rect2_64 = Kvadrat(300, 120)
    rect2_64.draw()
    rect2_64.setText("2")

    rect2_65 = Kvadrat(320, 120)
    rect2_65.draw()
    rect2_65.setText("2")

    rect2_66 = Kvadrat(340, 120)
    rect2_66.draw()
    rect2_66.setText("2")

    rect2_67 = Kvadrat(340, 140)
    rect2_67.draw()
    rect2_67.setText("2")

    rect2_68 = Kvadrat(320, 140)
    rect2_68.draw()
    rect2_68.setText("2")

    rect2_69 = Kvadrat(300, 140)
    rect2_69.draw()
    rect2_69.setText("2")

    rect2_70 = Kvadrat(300, 160)
    rect2_70.draw()
    rect2_70.setText("2")

    rect2_71 = Kvadrat(320, 160)
    rect2_71.draw()
    rect2_71.setText("2")

    rect2_72 = Kvadrat(320, 180)
    rect2_72.draw()
    rect2_72.setText("2")

    rect2_73 = Kvadrat(300, 180)
    rect2_73.draw()
    rect2_73.setText("2")

    rect2_74 = Kvadrat(300, 200)
    rect2_74.draw()
    rect2_74.setText("2")

    rect2_75 = Kvadrat(280, 200)
    rect2_75.draw()
    rect2_75.setText("2")

    rect2_76 = Kvadrat(260, 200)
    rect2_76.draw()
    rect2_76.setText("2")

    rect2_77 = Kvadrat(100, 140)
    rect2_77.draw()
    rect2_77.setText("2")

    rect2_78 = Kvadrat(120, 140)
    rect2_78.draw()
    rect2_78.setText("2")

    rect2_79 = Kvadrat(140, 140)
    rect2_79.draw()
    rect2_79.setText("2")

    rect2_80 = Kvadrat(160, 140)
    rect2_80.draw()
    rect2_80.setText("2")

    rect2_81 = Kvadrat(180, 140)
    rect2_81.draw()
    rect2_81.setText("2")

    rect2_82 = Kvadrat(200, 140)
    rect2_82.draw()
    rect2_82.setText("2")

    rect2_83 = Kvadrat(220, 140)
    rect2_83.draw()
    rect2_83.setText("2")

    rect2_84 = Kvadrat(100, 160)
    rect2_84.draw()
    rect2_84.setText("2")

    rect2_85 = Kvadrat(120, 160)
    rect2_85.draw()
    rect2_85.setText("2")

    rect2_86 = Kvadrat(140, 160)
    rect2_86.draw()
    rect2_86.setText("2")

    rect2_87 = Kvadrat(160, 160)
    rect2_87.draw()
    rect2_87.setText("2")

    rect2_88 = Kvadrat(180, 160)
    rect2_88.draw()
    rect2_88.setText("2")

    rect2_89 = Kvadrat(200, 160)
    rect2_89.draw()
    rect2_89.setText("2")

    rect2_90 = Kvadrat(220, 160)
    rect2_90.draw()
    rect2_90.setText("2")

    rect2_91 = Kvadrat(100, 180)
    rect2_91.draw()
    rect2_91.setText("2")

    rect2_92 = Kvadrat(120, 180)
    rect2_92.draw()
    rect2_92.setText("2")

    rect2_93 = Kvadrat(140, 180)
    rect2_93.draw()
    rect2_93.setText("2")

    rect2_94 = Kvadrat(160, 180)
    rect2_94.draw()
    rect2_94.setText("2")

    rect2_95 = Kvadrat(180, 180)
    rect2_95.draw()
    rect2_95.setText("2")

    rect2_96 = Kvadrat(200, 180)
    rect2_96.draw()
    rect2_96.setText("2")

    rect2_97 = Kvadrat(220, 180)
    rect2_97.draw()
    rect2_97.setText("2")

    rect2_98 = Kvadrat(120, 200)
    rect2_98.draw()
    rect2_98.setText("2")

    rect2_99 = Kvadrat(140, 200)
    rect2_99.draw()
    rect2_99.setText("2")

    rect2_100 = Kvadrat(160, 200)
    rect2_100.draw()
    rect2_100.setText("2")

    rect2_101 = Kvadrat(180, 200)
    rect2_101.draw()
    rect2_101.setText("2")

    rect2_102 = Kvadrat(200, 200)
    rect2_102.draw()
    rect2_102.setText("2")

    rect2_103 = Kvadrat(140, 220)
    rect2_103.draw()
    rect2_103.setText("2")

    rect2_104 = Kvadrat(160, 220)
    rect2_104.draw()
    rect2_104.setText("2")

    rect2_105 = Kvadrat(180, 220)
    rect2_105.draw()
    rect2_105.setText("2")

    rect2_106 = Kvadrat(200, 220)
    rect2_106.draw()
    rect2_106.setText("2")

    rect2_107 = Kvadrat(220, 220)
    rect2_107.draw()
    rect2_107.setText("2")

    rect2_108 = Kvadrat(240, 220)
    rect2_108.draw()
    rect2_108.setText("2")

    rect2_109 = Kvadrat(260, 220)
    rect2_109.draw()
    rect2_109.setText("2")

    rect2_110 = Kvadrat(280, 220)
    rect2_110.draw()
    rect2_110.setText("2")

    rect2_111 = Kvadrat(300, 220)
    rect2_111.draw()
    rect2_111.setText("2")

    rect2_112 = Kvadrat(320, 220)
    rect2_112.draw()
    rect2_112.setText("2")

    rect2_113 = Kvadrat(180, 240)
    rect2_113.draw()
    rect2_113.setText("2")

    rect2_114 = Kvadrat(200, 240)
    rect2_114.draw()
    rect2_114.setText("2")

    rect2_115 = Kvadrat(220, 240)
    rect2_115.draw()
    rect2_115.setText("2")

    rect2_116 = Kvadrat(240, 240)
    rect2_116.draw()
    rect2_116.setText("2")

    rect2_117 = Kvadrat(260, 240)
    rect2_117.draw()
    rect2_117.setText("2")

    rect2_118 = Kvadrat(280, 240)
    rect2_118.draw()
    rect2_118.setText("2")

    rect2_119 = Kvadrat(300, 240)
    rect2_119.draw()
    rect2_119.setText("2")

    rect2_120 = Kvadrat(200, 260)
    rect2_120.draw()
    rect2_120.setText("2")

    rect2_121 = Kvadrat(220, 260)
    rect2_121.draw()
    rect2_121.setText("2")

    rect2_122 = Kvadrat(240, 260)
    rect2_122.draw()
    rect2_122.setText("2")

    rect2_123 = Kvadrat(40, 260)
    rect2_123.draw()
    rect2_123.setText("2")

    rect2_124 = Kvadrat(60, 260)
    rect2_124.draw()
    rect2_124.setText("2")

    rect2_125 = Kvadrat(140, 260)
    rect2_125.draw()
    rect2_125.setText("2")

    rect2_126 = Kvadrat(160, 260)
    rect2_126.draw()
    rect2_126.setText("2")

    rect2_127 = Kvadrat(20, 280)
    rect2_127.draw()
    rect2_127.setText("2")

    rect2_128 = Kvadrat(40, 280)
    rect2_128.draw()
    rect2_128.setText("2")

    rect2_129 = Kvadrat(60, 280)
    rect2_129.draw()
    rect2_129.setText("2")

    rect2_130 = Kvadrat(80, 280)
    rect2_130.draw()
    rect2_130.setText("2")

    rect2_131 = Kvadrat(100, 280)
    rect2_131.draw()
    rect2_131.setText("2")

    rect2_132 = Kvadrat(120, 280)
    rect2_132.draw()
    rect2_132.setText("2")

    rect2_133 = Kvadrat(140, 280)
    rect2_133.draw()
    rect2_133.setText("2")

    rect2_134 = Kvadrat(160, 280)
    rect2_134.draw()
    rect2_134.setText("2")

    rect2_135 = Kvadrat(180, 280)
    rect2_135.draw()
    rect2_135.setText("2")

    rect2_136 = Kvadrat(200, 280)
    rect2_136.draw()
    rect2_136.setText("2")

    rect2_137 = Kvadrat(220, 280)
    rect2_137.draw()
    rect2_137.setText("2")

    rect2_138 = Kvadrat(240, 280)
    rect2_138.draw()
    rect2_138.setText("2")

    rect2_139 = Kvadrat(260, 280)
    rect2_139.draw()
    rect2_139.setText("2")

    rect2_140 = Kvadrat(20, 300)
    rect2_140.draw()
    rect2_140.setText("2")

    rect2_141 = Kvadrat(40, 300)
    rect2_141.draw()
    rect2_141.setText("2")

    rect2_142 = Kvadrat(60, 300)
    rect2_142.draw()
    rect2_142.setText("2")

    rect2_143 = Kvadrat(80, 300)
    rect2_143.draw()
    rect2_143.setText("2")

    rect2_144 = Kvadrat(100, 300)
    rect2_144.draw()
    rect2_144.setText("2")

    rect2_145 = Kvadrat(120, 300)
    rect2_145.draw()
    rect2_145.setText("2")

    rect2_146 = Kvadrat(140, 300)
    rect2_146.draw()
    rect2_146.setText("2")

    rect2_147 = Kvadrat(160, 300)
    rect2_147.draw()
    rect2_147.setText("2")

    rect2_148 = Kvadrat(200, 300)
    rect2_148.draw()
    rect2_148.setText("2")

    rect2_149 = Kvadrat(220, 300)
    rect2_149.draw()
    rect2_149.setText("2")

    rect2_150 = Kvadrat(240, 300)
    rect2_150.draw()
    rect2_150.setText("2")

    rect2_151 = Kvadrat(260, 300)
    rect2_151.draw()
    rect2_151.setText("2")

    rect2_152 = Kvadrat(20, 320)
    rect2_152.draw()
    rect2_152.setText("2")

    rect2_153 = Kvadrat(40, 320)
    rect2_153.draw()
    rect2_153.setText("2")

    rect2_154 = Kvadrat(60, 320)
    rect2_154.draw()
    rect2_154.setText("2")

    rect2_155 = Kvadrat(80, 320)
    rect2_155.draw()
    rect2_155.setText("2")

    rect2_156 = Kvadrat(100, 320)
    rect2_156.draw()
    rect2_156.setText("2")

    rect2_157 = Kvadrat(120, 320)
    rect2_157.draw()
    rect2_157.setText("2")

    rect2_158 = Kvadrat(140, 320)
    rect2_158.draw()
    rect2_158.setText("2")

    rect2_159 = Kvadrat(160, 320)
    rect2_159.draw()
    rect2_159.setText("2")

    rect2_160 = Kvadrat(200, 320)
    rect2_160.draw()
    rect2_160.setText("2")

    rect2_161 = Kvadrat(220, 320)
    rect2_161.draw()
    rect2_161.setText("2")

    rect2_162 = Kvadrat(240, 320)
    rect2_162.draw()
    rect2_162.setText("2")

    rect2_163 = Kvadrat(260, 320)
    rect2_163.draw()
    rect2_163.setText("2")

    rect2_164 = Kvadrat(40, 340)
    rect2_164.draw()
    rect2_164.setText("2")

    rect2_165 = Kvadrat(60, 340)
    rect2_165.draw()
    rect2_165.setText("2")

    rect2_166 = Kvadrat(80, 340)
    rect2_166.draw()
    rect2_166.setText("2")

    rect2_167 = Kvadrat(120, 340)
    rect2_167.draw()
    rect2_167.setText("2")

    rect2_168 = Kvadrat(140, 340)
    rect2_168.draw()
    rect2_168.setText("2")

    rect2_169 = Kvadrat(180, 340)
    rect2_169.draw()
    rect2_169.setText("2")

    rect2_170 = Kvadrat(200, 340)
    rect2_170.draw()
    rect2_170.setText("2")

    rect2_171 = Kvadrat(220, 340)
    rect2_171.draw()
    rect2_171.setText("2")

    rect2_171 = Kvadrat(240, 340)
    rect2_171.draw()
    rect2_171.setText("2")

    rect2_172 = Kvadrat(260, 340)
    rect2_172.draw()
    rect2_172.setText("2")

    rect2_173 = Kvadrat(40, 360)
    rect2_173.draw()
    rect2_173.setText("2")

    rect2_174 = Kvadrat(60, 360)
    rect2_174.draw()
    rect2_174.setText("2")

    rect2_175 = Kvadrat(80, 360)
    rect2_175.draw()
    rect2_175.setText("2")

    rect2_176 = Kvadrat(100, 360)
    rect2_176.draw()
    rect2_176.setText("2")

    rect2_177 = Kvadrat(160, 360)
    rect2_177.draw()
    rect2_177.setText("2")

    rect2_178 = Kvadrat(180, 360)
    rect2_178.draw()
    rect2_178.setText("2")

    rect2_179 = Kvadrat(200, 360)
    rect2_179.draw()
    rect2_179.setText("2")

    rect2_180 = Kvadrat(220, 360)
    rect2_180.draw()
    rect2_180.setText("2")

    rect2_181 = Kvadrat(240, 360)
    rect2_181.draw()
    rect2_181.setText("2")

    rect2_182 = Kvadrat(60, 380)
    rect2_182.draw()
    rect2_182.setText("2")

    rect2_183 = Kvadrat(80, 380)
    rect2_183.draw()
    rect2_183.setText("2")

    rect2_184 = Kvadrat(100, 380)
    rect2_184.draw()
    rect2_184.setText("2")

    rect2_185 = Kvadrat(120, 380)
    rect2_185.draw()
    rect2_185.setText("2")

    rect2_186 = Kvadrat(140, 380)
    rect2_186.draw()
    rect2_186.setText("2")

    rect2_187 = Kvadrat(160, 380)
    rect2_187.draw()
    rect2_187.setText("2")

    rect2_188 = Kvadrat(180, 380)
    rect2_188.draw()
    rect2_188.setText("2")

    rect2_189 = Kvadrat(200, 380)
    rect2_189.draw()
    rect2_189.setText("2")

    rect2_190 = Kvadrat(220, 380)
    rect2_190.draw()
    rect2_190.setText("2")

    rect2_191 = Kvadrat(240, 380)
    rect2_191.draw()
    rect2_191.setText("2")

    rect2_192 = Kvadrat(80, 400)
    rect2_192.draw()
    rect2_192.setText("2")

    rect2_193 = Kvadrat(100, 400)
    rect2_193.draw()
    rect2_193.setText("2")

    rect2_194 = Kvadrat(120, 400)
    rect2_194.draw()
    rect2_194.setText("2")

    rect2_195 = Kvadrat(140, 400)
    rect2_195.draw()
    rect2_195.setText("2")

    rect2_196 = Kvadrat(160, 400)
    rect2_196.draw()
    rect2_196.setText("2")

    rect2_197 = Kvadrat(180, 400)
    rect2_197.draw()
    rect2_197.setText("2")

    rect2_198 = Kvadrat(200, 400)
    rect2_198.draw()
    rect2_198.setText("2")

    rect2_199 = Kvadrat(220, 400)
    rect2_199.draw()
    rect2_199.setText("2")

    rect2_200 = Kvadrat(100, 420)
    rect2_200.draw()
    rect2_200.setText("2")

    rect2_201 = Kvadrat(120, 420)
    rect2_201.draw()
    rect2_201.setText("2")

    rect2_203 = Kvadrat(140, 420)
    rect2_203.draw()
    rect2_203.setText("2")

    rect2_204 = Kvadrat(160, 420)
    rect2_204.draw()
    rect2_204.setText("2")

    rect2_205 = Kvadrat(180, 420)
    rect2_205.draw()
    rect2_205.setText("2")

    rect2_205 = Kvadrat(200, 420)
    rect2_205.draw()
    rect2_205.setText("2")

    rect2_206 = Kvadrat(220, 420)
    rect2_206.draw()
    rect2_206.setText("2")

    rect3_1 = Kvadrat(120, 440)
    rect3_1.draw()
    rect3_1.setText("3")

    rect3_2 = Kvadrat(200, 440)
    rect3_2.draw()
    rect3_2.setText("3")

    rect3_3 = Kvadrat(120, 460)
    rect3_3.draw()
    rect3_3.setText("3")

    rect3_4 = Kvadrat(140, 460)
    rect3_4.draw()
    rect3_4.setText("3")

    rect3_5 = Kvadrat(160, 460)
    rect3_5.draw()
    rect3_5.setText("3")

    rect3_6 = Kvadrat(200, 460)
    rect3_6.draw()
    rect3_6.setText("3")

    rect3_7 = Kvadrat(220, 460)
    rect3_7.draw()
    rect3_7.setText("3")

    rect3_8 = Kvadrat(240, 460)
    rect3_8.draw()
    rect3_8.setText("3")

    rect3_9 = Kvadrat(360, 140)
    rect3_9.draw()
    rect3_9.setText("3")

    rect3_10 = Kvadrat(340, 160)
    rect3_10.draw()
    rect3_10.setText("3")

    rect3_11 = Kvadrat(360, 160)
    rect3_11.draw()
    rect3_11.setText("3")

    rect3_12 = Kvadrat(400, 160)
    rect3_12.draw()
    rect3_12.setText("3")

    rect3_13 = Kvadrat(340, 180)
    rect3_13.draw()
    rect3_13.setText("3")

    rect3_14 = Kvadrat(360, 180)
    rect3_14.draw()
    rect3_14.setText("3")

    rect3_15 = Kvadrat(380, 180)
    rect3_15.draw()
    rect3_15.setText("3")

    rect3_16 = Kvadrat(400, 180)
    rect3_16.draw()
    rect3_16.setText("3")

    rect3_17 = Kvadrat(320, 200)
    rect3_17.draw()
    rect3_17.setText("3")

    rect3_18 = Kvadrat(340, 200)
    rect3_18.draw()
    rect3_18.setText("3")

    rect3_19 = Kvadrat(360, 200)
    rect3_19.draw()
    rect3_19.setText("3")

    rect3_20 = Kvadrat(380, 200)
    rect3_20.draw()
    rect3_20.setText("3")

    rect4_1 = Kvadrat(380, 160)
    rect4_1.draw()
    rect4_1.setText("4")

    rect4_2 = Kvadrat(260, 160)
    rect4_2.draw()
    rect4_2.setText("4")

    rect4_3 = Kvadrat(280, 140)
    rect4_3.draw()
    rect4_3.setText("4")

    rect5_1 = Kvadrat(220, 200)
    rect5_1.draw()
    rect5_1.setText("5")

    rect5_2 = Kvadrat(240, 200)
    rect5_2.draw()
    rect5_2.setText("5")

    pygame.display.update()
    clock.tick(40)