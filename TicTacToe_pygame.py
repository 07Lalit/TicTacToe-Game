#part - 1
"""
    #import module
    #create blank game window
    # setup game loop with exit functionality
    # create grid and setup the grid list
"""
import pygame

pygame.init()
pygame.mixer.init()
# colors:
white = (255,255,255)
red = (255,0,0)
black = (0,0,0)



# local variable
screen_width= 700
screen_height= 500
white = (255,255,255)
red = (255,0,0)
black = (0,0,0)
running = True
game_over= True

window= pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Tic Tac Toe")
Icon = pygame.image.load('tic.png')
# We use set_icon to set new icon
pygame.display.set_icon(Icon)
pygame.display.flip()
aa = pygame.image.load('tic.png')
aa = pygame.transform.scale(aa, (screen_width, screen_height)).convert_alpha()
pygame.display.update()
pygame.mixer.music.load('snake_music.mp3')
pygame.mixer.music.play()

clock = pygame.time.Clock()
font = pygame.font.SysFont(None,55)
def text_screen(text,color,x,y):
    screen_text = font.render(text,True,color)
    window.blit(screen_text,[x,y])

def welcome():
    running = True
    while running:

        window.fill((255, 255, 255))
        window.blit(aa, (0, 0))
        text_screen("Welcome to tic tac toe Game",black,10,50)
        text_screen("Press Space Bar to play", black, 120,200)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running=False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.music.load('snake_music.mp3')
                    pygame.mixer.music.play()
                    gameloop()

        pygame.display.update()
        clock.tick(30)


