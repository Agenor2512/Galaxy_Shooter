import pygame
from pygame.sprite import Group

# Classe représentant un projectile
class EnemyProjectile(pygame.sprite.Sprite):
    
    def __init__(self, enemy, game):
        super().__init__()
        self.velocity = 20
        self.enemy = enemy
        self.game = game
        self.all_enemies_projectiles = pygame.sprite.Group()
        self.image = pygame.image.load('assets/projectile_enemy.png')
        self.image = pygame.transform.scale(self.image, (100, 70))
        self.rect = self.image.get_rect()
        self.rect.x = enemy.rect.x - 120
        self.rect.y = enemy.rect.y - 40
        
    def remove_shoots(self):
        #supprimer le projectile (en dehors de l'écran)
        self.enemy.all_enemies_projectiles.remove(self)

    def move(self):
        self.rect.x -= self.velocity

        for player in self.enemy.game.check_collision(self, self.enemy.game.all_players):
            self.remove_shoots()
            player.damage(self.enemy.attack)
        
        if self.rect.x < 0:
            self.remove_shoots()
            print("Projectile supprimé !")