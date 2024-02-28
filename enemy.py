import pygame

class Enemy(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 5
        self.velocity = 3
        self.original_image = pygame.image.load("assets/spaceship_enemy.png")
        self.image = pygame.transform.scale(self.original_image, (180, 130))
        self.rect = self.image.get_rect()
        self.rect.x = 1000
        self.rect.y = 300

    def forward(self):
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity
