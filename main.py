import pygame


def main():
    screen = pygame.display.set_mode((1028, 926))
    background = pygame.image.load('Images/UI.png')
    background = pygame.transform.scale(background, (1028, 724))
    back = pygame.image.load('Images/front.png')
    back = pygame.transform.scale(back, (100, 100))
    front = pygame.image.load('Images/back.png')
    front = pygame.transform.scale(front, (100, 100))

    running = True

    while running:
        # Grabs events such as key pressed, mouse pressed and so on.
        # Going through all the events that happened in the last clock tick
        screen.blit(background, (0, 100))
        screen.blit(back, (600, 700))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.flip()


main()
