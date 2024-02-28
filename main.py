import pygame

pygame.init()

pygame.display.set_caption("Galaxy Shooter")
screen = pygame.display.set_mode((1080, 720))

# permet de stocker l'image redimensionnée dans la variable "background" avec la fonction scale() et de la charger avec la fonction load()
background = pygame.transform.scale(pygame.image.load("assets/galaxy_shooter_background.png"), size=(1080, 720))


running = True

while running:
    
    # intégration de l'image de fond dans la fenêtre avec blit()
    screen.blit(background, (0, 0))
    
    # permet la mise à jour du contenu de la fenêtre
    pygame.display.flip()
    
    # écouteur d'évènement qui récupère le type d'évènement produit dans la fenêtre
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fermeture du jeu")
