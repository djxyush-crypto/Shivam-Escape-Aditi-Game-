import pygame
import random
import sys

pygame.init()

screen = pygame.display.set_mode(
    (0,0),
    pygame.FULLSCREEN
)

WIDTH=screen.get_width()
HEIGHT=screen.get_height()

pygame.mouse.set_visible(False)

clock=pygame.time.Clock()

font=pygame.font.SysFont(
    "Arial",
    28
)

bigfont=pygame.font.SysFont(
    "Arial",
    40
)

playerX=120
playerY=HEIGHT//2

vel=0
gravity=0.55
jump=-10

score=0
game_over=False

# FIXED
PIPE_WIDTH=130
PIPE_GAP=500
PIPE_SPEED=8
PIPE_DISTANCE=1000

pipes=[]

for i in range(3):

    pipes.append({

        "x":WIDTH+(i*PIPE_DISTANCE),

        "gapY":random.randint(
            250,
            HEIGHT-1150
        )

    })


while True:

    for event in pygame.event.get():

        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()

        # phone tap
        if event.type==pygame.MOUSEBUTTONDOWN or \
           event.type==pygame.FINGERDOWN:

            if not game_over:
                vel=jump


    vel+=gravity
    playerY+=vel

    screen.fill((10,10,30))

    pygame.draw.rect(
        screen,
        (30,180,50),
        (0,HEIGHT-80,WIDTH,80)
    )


    # player smaller
    player=pygame.Rect(
        playerX,
        int(playerY),
        140,
        45
    )

    pygame.draw.rect(
        screen,
        (0,150,255),
        player,
        border_radius=25
    )

    t=bigfont.render(
        "SHIVAM",
        True,
        (255,255,255)
    )

    screen.blit(
        t,
        (playerX+5,
         playerY+3)
    )


    for p in pipes:

        p["x"]-=PIPE_SPEED

        top=pygame.Rect(
            p["x"],
            0,
            PIPE_WIDTH,
            p["gapY"]
        )

        bottom=pygame.Rect(
            p["x"],
            p["gapY"]+PIPE_GAP,
            PIPE_WIDTH,
            HEIGHT
        )

        pygame.draw.rect(
            screen,
            (255,0,0),
            top,
            border_radius=10
        )

        pygame.draw.rect(
            screen,
            (255,0,0),
            bottom,
            border_radius=10
        )

        txt=font.render(
            "ADITI MUNJAL",
            True,
            (255,255,255)
        )

        screen.blit(
            txt,
            (p["x"]-15,
            p["gapY"]-40)
        )

        screen.blit(
            txt,
            (p["x"]-15,
            p["gapY"]+PIPE_GAP+20)
        )

        if player.colliderect(top) or \
           player.colliderect(bottom):

            game_over=True


        if p["x"]<-200:

            # FIX overlap
            maxX=max(
                pipe["x"]
                for pipe in pipes
            )

            p["x"]=maxX+PIPE_DISTANCE

            p["gapY"]=random.randint(
                250,
                HEIGHT-1150
            )

            score+=1


    s=font.render(
        "Score:"+str(score),
        True,
        (255,255,0)
    )

    screen.blit(
        s,
        (20,20)
    )

    if playerY<0 or \
       playerY>HEIGHT:

        game_over=True


    if game_over:

        over=bigfont.render(
            "GAME OVER",
            True,
            (255,0,0)
        )

        screen.blit(
            over,
            (WIDTH//2-150,
             HEIGHT//2)
        )

    pygame.display.update()

    clock.tick(60)
