import pygame
import math
from game import Game

pygame.init()

pygame.display.set_caption("Galaxy Shooter")
screen = pygame.display.set_mode((1080, 720))

# permet de stocker l'image redimensionnée dans la variable "background" avec la fonction scale() et de la charger avec la fonction load()
background = pygame.transform.scale(pygame.image.load("assets/galaxy_shooter_background.png"), size=(1080, 720))

# importer notre bannière
banner = pygame.image.load("assets/galaxy_shooter_logo.png")
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width() / 5)
banner_rect.y = math.ceil(screen.get_height() / 5.5)

# import charger notre bouton avant la partie
play_button = pygame.image.load("assets/play_button.png")
play_button = pygame.transform.scale(play_button, (270, 100))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width() / 2.65)
play_button_rect.y = math.ceil(screen.get_height() / 1.5)

#charger notre jeu
game = Game()

running = True

while running:
    
    # intégration de l'image de fond dans la fenêtre avec blit()
    screen.blit(background, (0, 0))
    
    # vérifier si le jeu a commencé
    if game.is_playing:
        # déclencher les instructions de la partie
        game.update(screen)

    # vérifier si notre jeu n'a pas commencé
    else:
        # ajout de l'écran de bienvenue
        screen.blit(banner, (banner_rect))
        screen.blit(play_button, (play_button_rect))
       
    # permet la mise à jour du contenu de la fenêtre
    pygame.display.flip()
    
    # écouteur d'évènement qui récupère le type d'évènement produit dans la fenêtre
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fermeture du jeu")
            
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
  
            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()
                
        elif event.type == pygame.KEYUP:        
            game.pressed[event.key] = False   

        elif event.type == pygame.MOUSEBUTTONDOWN:
            # verifie pour savoir si la souris est en collision avec le bouton jouer
            if play_button_rect.collidepoint(event.pos):
                # mettre le jeu en mode "lancé"
                game.start()