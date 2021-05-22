import pygame
import time
pygame.init()
root=pygame.display.set_mode((1280,720))
clock=pygame.time.Clock()
bg=pygame.image.load("bg.png")
gr=pygame.image.load("ground.png")
fin=pygame.image.load("finish.png")
player=pygame.image.load("player.png")
player2=pygame.image.load("player2.png")
player3=pygame.image.load("player3.png")
player4=pygame.image.load("player4.png")
mon=pygame.image.load("money.png")
v=0
playercos=0
score=0
left=0
right=0
jump=0
inertj=3
level=list("_________MMMM_____MMM_____++++__M___M___++++++________MMMMMM_________F______________________________________________")
pos=10
y=525
xont=pygame.font.Font('Pixeboy-z8XGD.ttf',40)
while True:
    root.blit(bg,(0,0))
    text=xont.render(str(score),False,(0,0,0))
    root.blit(text,(0,0))
    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            quit()
        if i.type==pygame.KEYDOWN:
            if i.key==pygame.K_RIGHT:
                right=1
                left=0

            if i.key==pygame.K_LEFT:
                right=0
                left=1
            if i.key==pygame.K_SPACE:
                if y==525:
                    jump=1

        if i.type==pygame.KEYUP:
            right=0
            left=0
    if right:
        if level[pos-2]=="+":
            if y>450:
                pos-=1
                v-=50
        if pos+9!="F":
            v+=50
            pos +=1
    if left:
        if level[pos-3]=="+":
            if y>450:
                pos+=1
                v+=50
        if pos>=9:
            v-=50
            pos -= 1
    if jump:
        y-=45
        inertj-=1
        if inertj==0:
            jump=0
            inertj=3
    for i in range(-3,20):
        root.blit(gr,(i*108-v,720-96))
    for i in range(-10,10):
        if level[pos+i]=="+":
            root.blit(gr,(pos+i*108+850,500))
        if level[pos+i]=="M":
            root.blit(mon,(pos+i*108+850,500))
        if level[pos+i]=="F":
            root.blit(fin,(pos+i*108+850,525))
            if pos-3==pos+i:
                a="You collected "+str(score)+" coins. Cool!"
                finishtxt=xont.render(a,True,(0,0,0))

                pygame.draw.rect(root,(255,255,255),(100,100,1070,520))
                root.blit(finishtxt, (150, 300))
                pygame.display.update()
                time.sleep(3)
                quit()
    if level[pos-2]=="M":
        level[pos-2]="_"
        score+=1
    if v>=100 or v<=-100:
        v=0
    if level[pos+i]!="+":
        if jump==0:
            if y<520:
                if level[pos - 4] != "+":
                    y+=40

    if right:
        if playercos%2==0:
            root.blit(player2,(600,y))
            playercos+=1
        else:
            root.blit(player,(600,y))
            playercos+=1
    if left:
        if playercos%2==0:
            root.blit(player3,(600,y))
            playercos+=1
        else:
            root.blit(player4,(600,y))
            playercos+=1
    if y>525:
        y=525
    if not left and not right:
        root.blit(player,(600,y))
    pygame.display.update()
    clock.tick(10)