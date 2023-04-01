from pygame import*
from time import*

window = display.set_mode((500, 600))
display.set_caption("Space Shooter")
background = transform.scale(image.load(""), (700, 600))
clock = time.Clock()


while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    window.blit(background, (0, 0)) 
    display.update()
    clock.tick(60)