import pygame, random
from pygame.locals import *
pygame.init()
mainClock = pygame.time.Clock()
pygame.mouse.set_visible(False)

black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
font = pygame.font.SysFont(None, 48)

bonusVel = 10
FPS = 60
windowX = 2500
windowY = 1400
window = pygame.display.set_mode((windowX, windowY), pygame.FULLSCREEN)

# Images
Scale = 0.8
# Ships
pShip1 = pygame.image.load("PlayerShip1.png")
pShip1 = pygame.transform.scale(pShip1, (round(420 * 0.4 * Scale), round(430 * 0.4 * Scale)))
pShip1p = pygame.image.load("PlayerShip1p.png")
pShip1p = pygame.transform.scale(pShip1p, (round(430 * 0.4), round(420 * 0.4)))

pShip2 = pygame.image.load("PlayerShip2.png")
pShip2 = pygame.transform.scale(pShip2, (round(551 * 0.67 * Scale), round(521 * 0.67 * Scale)))
pShip2p = pygame.image.load("PlayerShip2p.png")
pShip2p = pygame.transform.scale(pShip2p, (round(521 * 0.67), round(551 * 0.67)))

pShip3 = pygame.image.load("PlayerShip3.png")
pShip3 = pygame.transform.scale(pShip3, (round(1537 * 0.23 * Scale), round(963 * 0.23 * Scale)))
pShip3p = pygame.image.load("PlayerShip3p.png")
pShip3p = pygame.transform.scale(pShip3p, (round(963 * 0.23), round(1537 * 0.23)))

# Enemies
e1Rate = 20
e1Size = 100
e1Vel = 8
eShip1Img = pygame.image.load("enemy1.png")
eShip1Img = pygame.transform.scale(eShip1Img, (e1Size, e1Size))
eShip1Rect = eShip1Img.get_rect()

e2Rate = 100
e2SizeX = round(161 * 0.2)
e2SizeY = round(341 * 0.2)
e2Vel = 4
eShip2Img = pygame.image.load("enemy2.png")
eShip2Img = pygame.transform.scale(eShip2Img, (e2SizeX, e2SizeY))
eShip2Rect = eShip2Img.get_rect()

e3Rate = 200
e3Size = 200
e3Vel = 10
eShip3Img = pygame.image.load("enemy3.png")
eShip3Img = pygame.transform.scale(eShip3Img, (e3Size, e3Size))
eShip3Rect = eShip3Img.get_rect()

heartImage = pygame.image.load("heart.png")
heartImage = pygame.transform.scale(heartImage, (80, 80))
heartRect = heartImage.get_rect()

ammoImage = pygame.image.load("ammo.png")
ammoImage = pygame.transform.scale(ammoImage, (80, 80))
ammoRect = ammoImage.get_rect()

ammoBagImage = pygame.image.load("ammobag.png")
ammoBagImage = pygame.transform.scale(ammoBagImage, (80, 80))
ammoBagRect = ammoBagImage.get_rect()

blueMissileImage = pygame.image.load("blueMissile.png").convert()
blueMissileRect = blueMissileImage.get_rect()

redMissileImage = pygame.image.load("red missile.png").convert()
redMissileImage = pygame.transform.scale(redMissileImage, (14, 7))



backgroundImage = pygame.image.load("cosmos.png").convert()
bgX = 0
bgY = 0




def drawText (text, font, surface, x, y, textColor):
    textObj = font.render(text, True, textColor)
    textRect = textObj.get_rect()
    textRect.midleft = (x, y)
    surface.blit(textObj, textRect)


def playerCollide (pShipRect, enemies):
    for e in enemies:
        if pShipRect.colliderect(e['rect']):
            return True
        else:
            return False

highScore = 0
rocketChoice = 0
while rocketChoice == 0:
    rocketChoice = 0
    # Set start of game

    pCounter = 0
    missiles = []
    enemies = []
    emissiles = []

    e1Counter = 0
    e2Counter = 0
    e3Counter = 0
    dirCounter = 0
    dirSwitch = 1
    score = 0
    moveUp = moveDown = moveRight = moveLeft = pShoot = ammoBag = heartON = False


    for event in pygame.event.get():
        if event == pygame.QUIT:
            pygame.quit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()

    # Background
    window.fill(black)
    window.blit(backgroundImage, (bgX, bgY))
    window.blit(backgroundImage, (bgX + 2500, bgY))
    bgX -= 1
    if bgX < -2500:
        bgX = 0
    # Rockets to choose

    sk = pygame.Surface((1700, 1000))
    sk.set_alpha(240)
    sk.fill(black)
    window.blit(sk, (400, 100))
    # Text
    sx = pygame.Surface((1000, 200))
    sx.set_alpha(00)
    sx.fill(blue)
    window.blit(sx, (750, 100))
    font = pygame.font.SysFont(None, 100)
    drawText("Choose Your rocket : ", font, window, 880, 200, white)





    font = pygame.font.SysFont(None, 60)
    # 1st rocket
    drawText("Press 1", font, window, 700, 350, white)
    drawText("Press 2", font, window, 1200, 350, white)
    drawText("Press 3", font, window, 1700, 350, white)

    font = pygame.font.SysFont(None, 60)
    s1 = pygame.Surface((400, 600))
    s1.set_alpha(00)
    s1.fill(blue)
    window.blit(s1, (550, 400))
    window.blit(pShip1p, (660, 500))
    drawText("Fire power : 2/5 ", font, window, 640, 810, white)
    drawText("Speed : 5/5", font, window, 640, 860, white)
    drawText("Durability : 1/5", font, window, 640, 910, white)

    # 2nd rocket
    s2 = pygame.Surface((400, 600))
    s2.set_alpha(00)
    s2.fill(blue)
    window.blit(s2, (1050, 400))
    window.blit(pShip2p, (1070, 400))
    drawText("Fire power : 4/5 ", font, window, 1140, 810, white)
    drawText("Speed : 3/5", font, window, 1140, 860, white)
    drawText("Durability : 3/5", font, window, 1140, 910, white)

    # 3rd rocket
    s3 = pygame.Surface((400, 600))
    s3.set_alpha(00)
    s3.fill(blue)
    window.blit(s3, (1550, 400))
    window.blit(pShip3p, (1630, 420))
    drawText("Fire power : 5/5 ", font, window, 1660, 810, white)
    drawText("Speed : 1/5", font, window, 1660, 860, white)
    drawText("Durability : 5/5", font, window, 1660, 910, white)


    pygame.display.update()

    for event in pygame.event.get():
        if event == pygame.QUIT:
            pygame.quit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
            if event.key == K_1:
                rocketChoice = 1
            if event.key == K_2:
                rocketChoice = 2
            if event.key == K_3:
                rocketChoice = 3

    # Settings for different rockets
    if rocketChoice == 1:
        pShipImg = pShip1
        pShipRect = pShipImg.get_rect()
        lives = 1
        pVel = 12
        pShipRect.center = (300, windowY//2 + 100)
        ammo = 20
        mX = 10
        mY = 5
        mVel = 25
        blueMissileImage = pygame.transform.scale(blueMissileImage, (mX, mY))
        pCooldown = 25
        missileLauncherX = pShipRect.right
        missileLauncherY = pShipRect.centery

        pHitbox1 = pygame.rect.Rect(pShipRect.left, pShipRect.top + 38, 30, 70)
        pHitbox2 = pygame.rect.Rect(pShipRect.left + 30, pShipRect.top + 55, 40, 40)
        pHitbox3 = pygame.rect.Rect(pShipRect.left + 60, pShipRect.top + 66, 45, 20)
    if rocketChoice == 2:
        pShipImg = pShip2
        pShipRect = pShipImg.get_rect()
        lives = 3
        pVel = 6
        pShipRect.center = (300, windowY//2 + 100)

        ammo = 50
        mX = 20
        mY = 10
        mVel = 20
        blueMissileImage = pygame.transform.scale(blueMissileImage, (mX, mY))
        pCooldown = 10
        missileLauncherX = pShipRect.right
        missileLauncherY = pShipRect.centery

        pHitbox1 = pygame.rect.Rect(pShipRect.left + 30, pShipRect.top + 125, 250, 30)
        pHitbox2 = pygame.rect.Rect(pShipRect.left + 110, pShipRect.top + 75 , 115, 130)
        pHitbox3 = pygame.rect.Rect(pShipRect.left + 60, pShipRect.top + 10, 100, 262)
    if rocketChoice == 3:
        pShipImg = pShip3
        pShipRect = pShipImg.get_rect()
        lives = 5
        pVel = 3
        pShipRect.center = (300, windowY//2 + 100)

        ammo = 10
        mX = 200
        mY = 100
        mVel = 10
        blueMissileImage = pygame.transform.scale(blueMissileImage, (mX, mY))
        pCooldown = 100
        missileLauncherX = pShipRect.right
        missileLauncherY = pShipRect.centery

        pHitbox1 = pygame.rect.Rect(pShipRect.left + 20, pShipRect.top + 45, 250, 90)
        pHitbox2 = pygame.rect.Rect(pShipRect.left + 70, pShipRect.top + 95, 80, 80)
        pHitbox3 = pygame.rect.Rect(pShipRect.left + 5 , pShipRect.top + 5 , 100, 62)


    while rocketChoice != 0:
        score += 1
        e1Counter += 1
        e2Counter += 1
        e3Counter += 1
        pCounter += 1

        if dirCounter == 40:
            dirSwitch = dirSwitch * -1
            dirCounter = 0
        else:
            dirCounter += 1


        # Handling keyboard
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                if event.key == K_UP:
                    moveUp = True
                    moveDown = False
                if event.key == K_DOWN:
                    moveUp = False
                    moveDown = True
                if event.key == K_RIGHT:
                    moveRight = True
                    moveLeft = False
                if event.key == K_LEFT:
                    moveRight = False
                    moveLeft = True
                if event.key == K_SPACE:
                    pShoot = True
            if event.type == KEYUP:
                if event.key == K_UP:
                    moveUp = False
                if event.key == K_DOWN:
                    moveDown = False
                if event.key == K_RIGHT:
                    moveRight = False
                if event.key == K_LEFT:
                    moveLeft = False
                if event.key == K_SPACE:
                    pShoot = False
        # Spawning enemies
        if e1Counter == e1Rate:
            e1spawn = random.randint(150, windowY - e1Size)
            e1 = {'rect': pygame.Rect(windowX + e1Size, e1spawn, e1Size, e1Size),
                  'velx': e1Vel,
                  'hitbox1': pygame.rect.Rect(windowX + e1Size + 60, e1spawn + 15, 30, 70),
                  'hitbox2': pygame.rect.Rect(windowX + e1Size + 10, e1spawn + 35, 70, 30),
                  'vely': 0,
                  'surface': eShip1Img,
                  }
            enemies.append(e1)
            e1Counter = 0

        if e2Counter == e2Rate:
            e2 = {'rect': pygame.Rect(windowX + e2SizeX, random.randint(150, windowY - e2SizeY), e2SizeX, e2SizeY),
                  'velx': e2Vel,
                  'vely': 0,
                  'surface': eShip2Img,
                  }
            enemies.append(e2)
            e2Counter = 0

        if e3Counter == e3Rate:
            e3 = {'rect': pygame.Rect(windowX + e3Size, random.randint(150, windowY - e3Size), e3Size, e3Size),
                  'velx': e3Vel,
                  'vely': 10,
                  'surface': eShip3Img,
                  }
            enemies.append(e3)
            e3Counter = 0

        # Moving enemies
        for e in enemies[:]:
            e['rect'].move_ip(-1 * e['velx'], e['vely'] * dirSwitch)

        for e in enemies:
            if e['velx'] == e1Vel:
                e['hitbox1'].move_ip(-1 * e['velx'], 0)
                e['hitbox2'].move_ip(-1 * e['velx'], 0)

        # Deleting enemies
        for e in enemies[:]:
            if e['rect'].right < 0:
                enemies.remove(e)



        # Moving player
        if moveUp and pShipRect.top > 150:
            pShipRect.move_ip(0, -1 * pVel)
            missileLauncherY -= (1 * pVel)
            pHitbox1.move_ip(0, -1 * pVel)
            pHitbox2.move_ip(0, -1 * pVel)
            pHitbox3.move_ip(0, -1 * pVel)
        if moveDown and pShipRect.bottom < windowY:
            pShipRect.move_ip(0, 1 * pVel)
            missileLauncherY += (1 * pVel)
            pHitbox1.move_ip(0, 1 * pVel)
            pHitbox2.move_ip(0, 1 * pVel)
            pHitbox3.move_ip(0, 1 * pVel)
        if moveRight and pShipRect.right < windowX:
            pShipRect.move_ip(1 * pVel, 0)
            missileLauncherX += (1 * pVel)
            pHitbox1.move_ip(1 * pVel, 0)
            pHitbox2.move_ip(1 * pVel, 0)
            pHitbox3.move_ip(1 * pVel, 0)
        if moveLeft and pShipRect.left > 0:
            pShipRect.move_ip(-1 * pVel, 0)
            missileLauncherX -= (1 * pVel)
            pHitbox1.move_ip(-1 * pVel, 0)
            pHitbox2.move_ip(-1 * pVel, 0)
            pHitbox3.move_ip(-1 * pVel, 0)

        # Spawning missiles
        if rocketChoice == 1:
            if pShoot:
                if pCounter >= pCooldown:
                    if ammo > 0:
                        missile = {
                            'rect': pygame.Rect(missileLauncherX, missileLauncherY + 1, mX, mY),
                            'vel': mVel,
                            'surface': blueMissileImage,
                        }
                        missiles.append(missile)
                        pCounter = 0
                        ammo -= 1

        if rocketChoice == 2:
            if pShoot:
                if pCounter >= pCooldown:
                    if ammo > 1:
                        missile = {
                            'rect': pygame.Rect(missileLauncherX - 60, missileLauncherY + 56, mX, mY),
                            'vel': mVel,
                            'surface': blueMissileImage,
                        }
                        missiles.append(missile)
                        missile = {
                            'rect': pygame.Rect(missileLauncherX - 60, missileLauncherY - 65, mX, mY),
                            'vel': mVel,
                            'surface': blueMissileImage,
                        }
                        missiles.append(missile)
                        pCounter = 0
                        ammo -= 2
        if rocketChoice == 3:
            if pShoot:
                if pCounter >= pCooldown:
                    if ammo > 0:
                        missile = {
                            'rect': pygame.Rect(missileLauncherX, missileLauncherY - 50 , mX, mY),
                            'vel': mVel,
                            'surface': blueMissileImage,
                        }
                        missiles.append(missile)
                        pCounter = 0
                        ammo -= 1
        if pCounter > pCooldown:
            pCounter = pCooldown
        for e in enemies:
            if e['velx'] == e2Vel:
                eShoot = random.randint(0, 500)
                if eShoot == 66:
                    emissile = {
                        'rect': pygame.Rect(e['rect'].left, e['rect'].centery, 14, 7),
                        'vel': 10,
                        'surface': blueMissileImage,
                    }
                    emissiles.append(emissile)

        # Moving missiles
        for m in missiles:
            m['rect'].move_ip(mVel, 0)

        for em in emissiles:
            em['rect'].move_ip(em['vel'] * -1, 0)

        # Deleting missiles
        for m in missiles:
            if m['rect'].left > windowX:
                missiles.remove(m)
        for em in emissiles:
            if em['rect'].right < 0:
                emissiles.remove(em)


        # Spawning bonuses
        if not ammoBag:
            ammoBagRect.center = (-100, 0)
            randomBag = random.randint(0, 250)
            if randomBag == 33:
                ammoBagRect.left = windowX
                ammoBagRect.top = random.randint(150, windowY - 80)
                window.blit(ammoBagImage, ammoBagRect)
                ammoBag = True



        if not heartON:
            heartRect.center = (-100, 0)
            if lives < 5:
                randHeart = random.randint(0, 1000)
                if randHeart == 666:
                    heartON = True
                    heartRect.left = windowX
                    heartRect.top = random.randint(150, windowY - 80)
                    window.blit(heartImage, heartRect)
            else:
                heartRect.center = (-100, 0)



        # Moving bonuses
        if ammoBag:
            if ammoBagRect.right < 0:
                ammoBag = False
            else:
                ammoBagRect.move_ip(-1 * bonusVel, 0)

        if heartON:
            heartRect.move_ip(-1 * bonusVel, 0)


        # Drawing
        # Background

        window.blit(backgroundImage, (bgX, bgY))
        window.blit(backgroundImage, (bgX + 2500, bgY))
        bgX -= 1
        if bgX < -2500:
            bgX = 0
        # Interface
        if lives == 5:
            window.blit(heartImage, (50, 30))
            window.blit(heartImage, (80, 30))
            window.blit(heartImage, (110, 30))
            window.blit(heartImage, (140, 30))
            window.blit(heartImage, (170, 30))
        if lives == 4:
            window.blit(heartImage, (50, 30))
            window.blit(heartImage, (80, 30))
            window.blit(heartImage, (110, 30))
            window.blit(heartImage, (140, 30))
        if lives == 3:
            window.blit(heartImage, (50, 30))
            window.blit(heartImage, (80, 30))
            window.blit(heartImage, (110, 30))
        if lives == 2:
            window.blit(heartImage, (50, 30))
            window.blit(heartImage, (80, 30))
        if lives == 1:
            window.blit(heartImage, (50, 30))

        window.blit(ammoImage, (300, 25))
        drawText(str(ammo), font, window, 390, 70, white)

        drawText("Score : ", font, window, 2000, 50, white)
        drawText(str(score), font, window, 2150, 50, white)
        drawText("High score : ", font, window, 2000, 100, white)
        drawText(str(highScore), font, window, 2250, 102, white)
        # Player
        window.blit(pShipImg, pShipRect)
        # Enemies
        for e in enemies[:]:
            window.blit(e['surface'], e['rect'])

        # Missiles
        for m in missiles:
            window.blit(blueMissileImage, m['rect'])
        for em in emissiles:
            window.blit(redMissileImage, em['rect'])

        # Bonuses
        if ammoBag:
            window.blit(ammoBagImage, ammoBagRect)
        if heartON:
            window.blit(heartImage, heartRect)
        # Collisions
        # Player v enemies
        for e in enemies[:]:
            if e['velx'] == e1Vel:
                if pHitbox1.colliderect(e['hitbox1']) or pHitbox2.colliderect(e['hitbox1']) or pHitbox3.colliderect(e['hitbox1']) or pHitbox1.colliderect(e['hitbox2']) or pHitbox2.colliderect(e['hitbox2']) or pHitbox3.colliderect(e['hitbox2']):
                    if lives > 1:
                        lives -= 1
                        enemies.remove(e)
                    else:
                        if score > highScore:
                            highScore = score
                        rocketChoice = 0
            else:
                if pHitbox1.colliderect(e['rect']) or pHitbox2.colliderect(e['rect']) or pHitbox3.colliderect(e['rect']):
                    if lives > 1:
                        lives -= 1
                        enemies.remove(e)
                    else:
                        if score > highScore:
                            highScore = score
                        rocketChoice = 0

        # Player vs bonuses
        if rocketChoice == 3:
            if pHitbox1.colliderect(ammoBagRect) or pHitbox2.colliderect(ammoBagRect) or pHitbox3.colliderect(ammoBagRect):
                ammoBag = False
                ammo += 2
        else:
            if pHitbox1.colliderect(ammoBagRect) or pHitbox2.colliderect(ammoBagRect) or pHitbox3.colliderect(ammoBagRect):
                ammoBag = False
                ammo += 10

        if heartON:
            if pHitbox1.colliderect(heartRect) or pHitbox2.colliderect(heartRect) or pHitbox3.colliderect(heartRect):
                heartON = False
                lives += 1

        # Player v eMissiles
        for em in emissiles:
            if pHitbox1.colliderect(em['rect']) or pHitbox2.colliderect(em['rect']) or pHitbox3.colliderect(em['rect']):
                if lives > 1:
                    lives -= 1
                    emissiles.remove(em)
                else:
                    if score > highScore:
                        highScore = score
                    rocketChoice = 0
        # Missiles v enemies
        if rocketChoice == 1 or rocketChoice == 2:
            for m in missiles[:]:
                for e in enemies[:]:
                    if e['rect'].colliderect(m['rect']):
                        try:
                            enemies.remove(e)
                            missiles.remove(m)
                            score += 10
                        except ValueError:
                            pass
        else:
            for m in missiles[:]:
                for e in enemies[:]:
                    if e['rect'].colliderect(m['rect']):
                        try:
                            enemies.remove(e)

                            score += 10
                        except ValueError:
                            pass

        # Missiles v eMissiles
        if rocketChoice == 3:
            for m in missiles:
                for em in emissiles:
                    if em['rect'].colliderect(m['rect']):
                        emissiles.remove(em)
        else:
            for m in missiles:
                for em in emissiles:
                    if em['rect'].colliderect(m['rect']):
                        missiles.remove(m)
                        emissiles.remove(em)

        #pygame.draw.rect(window, green, pHitbox1)
        #pygame.draw.rect(window, green, pHitbox2)
        #pygame.draw.rect(window, green, pHitbox3)
        #for e in enemies:
        #    if e['velx'] == e1Vel:
         #       pygame.draw.rect(window, green, (e['hitbox1']))
          #      pygame.draw.rect(window, green, (e['hitbox2']))
        #
        pygame.display.update()
        mainClock.tick(FPS)












