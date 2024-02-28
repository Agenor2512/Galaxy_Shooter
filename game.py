import pygame
from player import Player
from enemy import Enemy

class Game:
    def __init__(self):
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        self.all_enemies = pygame.sprite.Group()
        self.pressed = {}
        self.spawn_enemy()
        self.spawn_enemy()

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def spawn_enemy(self):
        enemy = Enemy(self)
        self.all_enemies.add(enemy)