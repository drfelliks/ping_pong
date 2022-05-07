from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, speed, width, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
 
class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 420:
            self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 420:
            self.rect.y += self.speed
      
back = (194, 148, 23)     
win_width = 600
win_height = 500
window = display.set_mode((win_widht, win_height))
window.fill(back)

finish = False
game = True
clock = time.Clock()
FPS = 60

rocket1 = Player("tennis_staff.png", 30, 200, 6, 50, 150)
rocket2 = Player("thumb_24168_product_big.png", 520, 200, 6, 50, 150)

ball = GameSprite("tennis_ball.png", 200, 200, 4, 50, 50)

font.init()
font = font.Font(None, 35)
lsoe1 = font.render("Player 1 LOSE!", True, (180, 0, 0))
lose2 = font.render("Player 2 LOSE!", True, (180, 0, 0))

speed_x = 3
speed_y = 3

while game:
    for e in enent.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.fill(back)
        racket1.update_l()
        racket2.update_r()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        
        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            speed_x *= -1
            speed_y *= -1
        if ball.rect.y > win_height - 50 or ball.rect.y < 0:
            speed_y *= -1
        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (200, 200))
            game = False
        if ball.rect.x > win_width:
            finish = True
            window.blit(lose2, (200, 200))
            game  = False
        racket1.reset()
        racket2.reset()
        ball.reset()
        
    display.update()
    clocl.tick(FPS)
   
            
         
                
        
        
        
        
        
