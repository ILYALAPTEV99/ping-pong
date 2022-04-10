from pygame import *
window = display.set_mode((800,500))
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

player1 = Player(10, 10, 250, 40, 120, 255, 255, 255)
player2 = Player(10, 750, 250, 40, 120, 255, 255, 255)
FPS = 60
clock = time.Clock()
game = True
while game:
    window.fill((0, 128, 1))
    player1.move()
    player1.reset()
    player2.move2()
    player2.reset()
    display.update()
    for e in event.get():
        if e.type == QUIT:
            game = False
    clock.tick(FPS)
