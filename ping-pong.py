from pygame import *
from random import randint
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QInputDialog
o1 = 0
o2 = 0
font.init()
window = display.set_mode((800,500))
app = QApplication([])
window1 = QWidget()
window.fill((0, 128, 1))
display.set_caption('Ping-pong')
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, speed, rect_x, rect_y, size_x, size_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = rect_x
        self.rect.y = rect_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(sprite.Sprite):
    def __init__(self, speed, rect_x, rect_y, width, height, color1, color2, color3):
        super().__init__()
        self.color1 = color1
        self.color2 = color2
        self.color3 = color3
        self.image = Surface((width, height))
        self.image.fill((self.color1, self.color2, self.color3))
        self.rect = self.image.get_rect()
        self.speed = speed
        self.rect.x = rect_x
        self.rect.y = rect_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    def move(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 10:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 370:
            self.rect.y += self.speed

    def move2(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 10:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 370:
            self.rect.y += self.speed

class Ball(GameSprite):
    def move(self):
        pass

text = []
text1 = 'игрок1'
text2 = 'игрок2'
font = font.SysFont('Arial', 20)
start = GameSprite('start.png', 5, 300, 200, 150, 150)
ball = Ball('ball.png', 10, 350, 250, 50, 50)
player1 = Player(10, 10, 200, 40, 120, 255, 255, 255)
player2 = Player(10, 750, 200, 40, 120, 255, 255, 255)
play1 = font.render('Очки у '+ str(text1) + ' : ' + str(o1), True, (255, 255, 255, 255))
play2 = font.render('Очки у '+ str(text2) + ' : ' + str(o2), True, (255, 255, 255, 255))
win1 = font.render('Выиграл(а) '+ str(text1), True, (255, 255, 255, 255))
win1 = font.render('Выиграл(а) '+ str(text2), True, (255, 255, 255, 255))
FPS = 60
clock = time.Clock()
game = True
speed_x = 3
speed_y = 3
finish = False
win11 = False
win22 = False
handled = False
start1 = False
def name1():
    text1 = 'игрок1'
    text_p1, result1 = QInputDialog.getText(window1, 'Первое Имя ', 'Имя:')
    if result1 and text_p1 != '':
        text1 = text_p1
        text.append(text_p1)
    else:
        text.append(text1)

def name2():
    text2 = 'игрок2'
    text_p2, result2 = QInputDialog.getText(window1, 'Второе имя', 'Имя:')
    if result2 and text_p2 != '':
        text.append(text_p2)
    else:
        text.append(text2)

name1()
name2()
while game:
    window.fill((0, 128, 1))
    play1 = font.render('Очки у '+ str(text[0]) + ': ' + str(o1), True, (255, 255, 255, 255))
    play2 = font.render('Очки у '+ str(text[1]) + ': ' + str(o2), True, (255, 255, 255, 255))
    win1 = font.render('Выиграл(а) '+ str(text[0]), True, (255, 255, 255, 255))
    win2 = font.render('Выиграл(а) '+ str(text[1]), True, (255, 255, 255, 255))
    if o1 != 3 and o2 != 3:
        if win11:
            window.blit(win1, (250, 250))
        if win22:
            window.blit(win2, (250, 250))
    if start1:
        start.reset()
        handled = False
    window.blit(play1, (0, 0))
    window.blit(play2, (600, 0))
    ball.reset()
    player1.move2()
    player1.reset()
    player2.move()
    player2.reset()
    display.update()
    if mouse.get_pressed()[0] and start.rect.collidepoint(mouse.get_pos()) and not handled:
        o1 = 0
        o2 = 0
        win11 = False
        win22 = False
        time.delay(3000)
        start = GameSprite('start.png', 5, 300, 200, 150, 150)
        ball = Ball('ball.png', 10, 350, 250, 50, 50)
        player1 = Player(10, 10, 200, 40, 120, 255, 255, 255)
        player2 = Player(10, 750, 200, 40, 120, 255, 255, 255)
        handled = mouse.get_pressed()[0]
        finish = False
        start1 = False
        o1 = 0
        o2 = 0

    if finish != True:
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if ball.rect.x > 850:
            win11 = True
            o1 += 1
            finish = True
    
        if ball.rect.x < -50:
            win22 = True
            o2 += 1
            finish = True


    else:
        speed_x = 3
        speed_y = 3
        if o1 != 3 and o2 != 3:
            time.delay(3000)
            win11 = False
            win22 = False
            start = GameSprite('start.png', 5, 300, 200, 150, 150)
            ball = Ball('ball.png', 10, 350, 250, 50, 50)
            player1 = Player(10, 10, 200, 40, 120, 255, 255, 255)
            player2 = Player(10, 750, 200, 40, 120, 255, 255, 255)
            finish = False
        else:
            start1 = True
            
            


    if ball.rect.y > 450 or ball.rect.y < 10:
        speed_y *= -1
    if sprite.collide_rect(player1, ball) or sprite.collide_rect(player2, ball):
        speed_x *= -1
        if speed_x > 0:
            speed_x += 0.1
        else:
            speed_x -= 0.1
        if speed_y > 0:
            speed_y += 0.1
        else:
            speed_y -= 0.1
    for e in event.get():
        if e.type == QUIT:
            game = False
    clock.tick(FPS)
