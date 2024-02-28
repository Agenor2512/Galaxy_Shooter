import pygame
from game import Game

pygame.init()

pygame.display.set_caption("Galaxy Shooter")
screen = pygame.display.set_mode((1080, 720))

# permet de stocker l'image redimensionnée dans la variable "background" avec la fonction scale() et de la charger avec la fonction load()
background = pygame.transform.scale(pygame.image.load("assets/galaxy_shooter_background.png"), size=(1080, 720))

game = Game()


running = True

while running:
    
    # intégration de l'image de fond dans la fenêtre avec blit()
    screen.blit(background, (0, 0))
    
    # intégration de l'image du joueur
    screen.blit(game.player.image, game.player.rect)

    for projectile in game.player.all_projectiles:
        projectile.move()

    # intégration de l'image du projectile
    game.player.all_projectiles.draw(screen)

    # intégration de l'image de l'ennemi
    game.all_enemies.draw(screen)

    for enemy in game.all_enemies:
        enemy.forward()
    
    # Vérification des touches utilisées par le joueur et récupération de sa position
    # appels des méthodes permettant de déplacer le sprite du joueur
    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x + game.player.rect.width < screen.get_width():
        game.player.move_right() 

    elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x > 0:
        game.player.move_left()

    elif game.pressed.get(pygame.K_UP) and game.player.rect.y > 0:
        game.player.move_up()
        
    elif game.pressed.get(pygame.K_DOWN) and game.player.rect.y + game.player.rect.height < screen.get_height():
        game.player.move_down()
       
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