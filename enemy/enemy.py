import pygame
from math import sqrt

class Enemy(pygame.sprite.Sprite):
    def __init__(self, game, max_health, attack, velocity, image, x, y):
        super().__init__()
        self.game = game
        self.health = max_health
        self.max_health = max_health
        self.attack = attack
        self.velocity = velocity
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        height = self.rect.height
        width = self.rect.width
        circle_radius =  sqrt((height/2)**2 + (width/2)**2)
        center_x = self.rect.centerx
        center_y = self.rect.centery
        highest_circle_coordinate = {
            "x": center_x,
            "y": center_y - circle_radius,
        }
        health_bar_margin = 5
        health_bar_height = 5
        self.health_bar_width = self.max_health

        health_bar_left = highest_circle_coordinate["x"]  - self.health_bar_width/2
        health_bar_top = highest_circle_coordinate["y"] + health_bar_height + health_bar_margin
        self.health_bar_background_rect = [health_bar_left, health_bar_top, self.health_bar_width, health_bar_height]
        self.health_bar_foreground_rect = [health_bar_left, health_bar_top, self.health, health_bar_height]
        
    def damage(self, amount):
        self.health -= amount
        
    def update_health_bar(self, surface):
        health_bar_left = self.rect.centerx  - self.health_bar_width/2
        self.health_bar_background_rect[0] = health_bar_left
        self.health_bar_foreground_rect[0] = health_bar_left
        self.health_bar_foreground_rect[2] = self.health
        
        pygame.draw.rect(surface, (60, 63, 60), self.health_bar_background_rect)
        pygame.draw.rect(surface, (111, 210, 46), self.health_bar_foreground_rect)
        
    def forward(self):
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity
            
        else:
            self.game.player.damage(self.attack)
            

    def update_state(self, screen):
        self.forward()
        self.update_health_bar(screen)
