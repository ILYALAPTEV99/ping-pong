from pygame import *
window = display.set_mode((700,500))
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

class Player(GameSprite):
    def move(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_LEFT] and self.rect.y > 10:
            self.rect.y -= self.speed
        if keys_pressed[K_RIGHT] and self.rect.y < 400:
            self.rect.x += self.speed
            
background = transform.scale(image.load('galaxy.jpg'), (700, 500))
