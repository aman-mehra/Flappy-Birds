import pygame
pygame.init()

display=pygame.display.set_mode((1000,700))
pygame.display.set_caption("FLAPPY BIRD")
display.fill((0,0,0))
img=pygame.image.load("assets/images/Bird1.png")
img=pygame.transform.scale(img,(50,50))
display.blit(img,(0,0))

for i in range(256):
    for j in range(256):
        for k in range(256):
            if display.get_at((0,0))==(i,j,k):
                print i,j,k
    
