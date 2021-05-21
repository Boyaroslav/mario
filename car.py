import pygame
import time
root=pygame.display.set_mode((1920,1080))
clock=pygame.time.Clock()
bg=pygame.image.load("bg.png")
gr=pygame.image.load("ground.png")
fin=pygame.image.load("finish.png")
player=pygame.image.load("player.png")
player2=pygame.image.load("player2.png")
player3=pygame.image.load("player3.png")
player4=pygame.image.load("player4.png")
v=0
playercos=0
left=0
right=0
level="_______________________++++__________++++++__________________F______________________________________________"
pos=10
y=900
while True:
    root.blit(bg,(0,0))
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

        if i.type==pygame.KEYUP:
            right=0
            left=0
    if right:
        if pos+9!="F":
            v+=50
            pos +=1
    if left:
        if pos>=9:
            v-=50
            pos -= 1
    for i in range(-3,20):
        root.blit(gr,(i*108-v,1080-96))
    for i in range(-10,10):
        if level[pos+i]=="+":
            root.blit(gr,(pos+i*108+850,800))
        if level[pos+i]=="F":
            root.blit(fin,(pos+i*108+850,900))
            if pos-3==pos+i:
                time.sleep(3)
                quit()
    if v>=100 or v<=-100:
        v=0
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
    if not left and not right:
        root.blit(player,(600,y))
    pygame.display.update()
    clock.tick(20)