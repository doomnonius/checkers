# Assets: https://techwithtim.net/wp-content/uploads/2020/09/assets.zip
import pygame
from checker import WIDTH, HEIGHT, Board

FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Checkers')


def main():
    """ Main loop
    """
    
    run = True
    clock = pygame.time.Clock()
    board = Board()
    
    while run:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass
            
            if event.type == pygame.KEYDOWN:
                run = False
    
        board.draw_squares(WIN)
        pygame.display.update()
    
    pygame.quit()

main()