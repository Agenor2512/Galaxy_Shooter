import pygame
from enemy.enemy import Enemy

class Boss(Enemy):
    def __init__(self, game):
        self.game = game
        self.loot_amount = 100
        self.set_loot_amount(self.loot_amount)
        image = pygame.image.load("assets/boss.png")
        image = pygame.transform.scale(image, (300, 300))
        self.original_image = image
        max_health = 200
        attack = 1
        velocity = 0
        x = 600
        y = 170
        super().__init__(game, max_health, attack, velocity, image, x, y)
        self.angle = 0


    def damage(self, amount):
        super().damage(amount)
        
        if self.health <= 0:
            self.rect.x = 1800
            self.game.all_bosses.remove(self)
            self.game.add_score(self.loot_amount)

    def forward(self):
        super().forward()
        self.rotate()

    def rotate(self):
        self.angle += 2
        self.image = pygame.transform.rotozoom(self.original_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)
