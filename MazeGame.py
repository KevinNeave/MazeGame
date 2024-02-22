import pygame
import math

black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)
green = (0, 255, 0)
red = (255,0,0)
gold = (255, 240, 16)
pink = (204, 0, 204)
#Initializes wall class
class Wall(pygame.sprite.Sprite):
  
  def __init__(self, x, y, width, height):
    pygame.sprite.Sprite.__init__(self)
    self.height = height
    self.width = width
    self.image = pygame.Surface([width, height])
    self.image.fill(pink)
    self.rect = self.image.get_rect()
    self.rect.x = x
    self.rect.y = y
#Initializes endwall sub classs
class EndWall (Wall, pygame.sprite.Sprite):

  def __init__ (self, x, y, width, height):
    pygame.sprite.Sprite.__init__(self)
    super().__init__(x, y, width, height)
    self.image.fill(gold)
#Initializes player class
class Player(pygame.sprite.Sprite):
  
  def __init__(self, x, y, lives):
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.image.load("luigi.png")
    self.image = pygame.transform.scale(self.image,[20,25])
    self.rect = self.image.get_rect()
    self.rect.x = x
    self.rect.y = y
    self.xvel = 0
    self.yvel = 0
    self.lives = lives
#Changes the player speed
  def changespeed(self, x, y):
    self.xvel += x
    self.yvel += y
#Updates player class. Checks for collisions, updates lives, removes instances
  def update(self, walls, enemies, keys, endwalls, endArea, endwall):
    self.rect.x += self.xvel

    hit_list = pygame.sprite.spritecollide(self, walls, False)
    for block in hit_list:
      if self.xvel > 0:
        self.rect.right = block.rect.left
      else:
        self.rect.left = block.rect.right

    self.rect.y += self.yvel
    hit_list1 = pygame.sprite.spritecollide(self, walls, False)
    for block in hit_list1:
      if self.yvel > 0:
        self.rect.bottom = block.rect.top
      else:
        self.rect.top = block.rect.bottom
    
    
    if keyOne.flag == True and keyTwo.flag == True and keyThree.flag == True: 
        walls.remove(endwall)
        all_sprites.remove(endwall)
        endwalls.remove(endwall)
    
    hit_list3 = pygame.sprite.spritecollide(self,enemies, False)
    for enemy in hit_list3:
      self.rect.x = 45
      self.rect.y = 35
      self.lives -=1

    hit_list4 = pygame.sprite.spritecollide(self, keys, False)
    for key in hit_list4:
      key.flag = True
      all_sprites.remove(key)
      keys.remove(key)
      keyOne.count +=1

    if self.rect in endArea.rect:
      self.lives=0
#Initializes enemy class
class Enemy(pygame.sprite.Sprite):

  def __init__(self, x, y):
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.image.load("ghost.png")
    self.image = pygame.transform.scale(self.image,[25, 25])
    self.rect = self.image.get_rect()
    self.rect.x = x
    self.rect.y = y
    self.xvel = 2
    self.yvel = 2
#Updates enemy class. Checks for collisions with vertical and horizontal walls
  def update(self, vertWalls, horizWalls):
    self.rect.x += self.xvel
    hit_list = pygame.sprite.spritecollide(self, vertWalls, False)
    for block in hit_list:
      if self.xvel > 0:
        self.rect.right = block.rect.left
      else:
        self.rect.left = block.rect.right
      self.xvel= self.xvel*(-1)
      
   
    self.rect.y += self.yvel
    hit_list = pygame.sprite.spritecollide(self, horizWalls, False)
    for block in hit_list:
      if self.yvel > 0:
        self.rect.bottom = block.rect.top
      else:
        self.rect.top = block.rect.bottom
      self.yvel = self.yvel*(-1)
#Initializes bullet classes
class Bullet(pygame.sprite.Sprite):
  def __init__(self, x, y,flag):
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.Surface([4, 4])
    self.image.fill(gold)
    self.rect = self.image.get_rect()
    pos =pygame.mouse.get_pos()
    xMouse = pos[0]
    yMouse = pos[1]
    xDistance = xMouse - (x-7)
    yDistance = yMouse - (y-7)
    angle = math.atan2(yDistance,xDistance)
    self.xvel = 7*math.cos(angle)
    self.yvel = 7*math.sin(angle)
    self.rect.x = x+7
    self.rect.y = y+7
    
  #Updates bullet class. Changes bullet speed and checks for colliions with enemies and walls
  def update(self,enemies, walls):
    self.rect.y += self.yvel
    self.rect.x +=self.xvel
    hit_list = pygame.sprite.spritecollide(self, walls, False)
    for wall in hit_list:
      bullets.remove(bullet)
      all_sprites.remove(bullet)
    hit_list = pygame.sprite.spritecollide(self,enemies, True)
    for enemy in hit_list:
      bullets.remove(bullet)
      all_sprites.remove(bullet)
      enemies.remove(enemy)
      all_sprites.remove(enemy)
#Initializes key class
class Key(pygame.sprite.Sprite):
  def __init__(self,x,y):
    pygame.sprite.Sprite.__init__(self)
    keys = pygame.image.load("key.png")
    keys = pygame.transform.scale(keys, [25,25])
    self.image = keys
    self.rect = self.image.get_rect()
    self.rect.x = x
    self.rect.y = y
    self.flag = False
    self.count = 0
#Initializes end class
class End(pygame.sprite.Sprite):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.Surface([60,50])
    self.image.fill(green)
    self.rect = self.image.get_rect()
    self.rect.x = 430
    self.rect.y = 70
#Initializes text and variables
end = "GAME OVER"
option1 = "Press Enter to play again"
option2 = "Press ESC to quit"
livesString = "Lives:"
coolString = "Cooldown Active"
keyString = "Keys: "
directFlag = 0
coolFlag = False
shotTime = 0
lives = 3
key1 = False
key2 = False
key3 = False
#Initializes pygame and sets screen size and fonts
pygame.init()
screen = pygame.display.set_mode([600, 400])
pygame.display.set_caption("Luigi's Mansion")
endFont = pygame.font.SysFont("Arial", 80)
optionFont = pygame.font.SysFont("Arial", 20)
gameFont = pygame.font.SysFont("Droid Serif", 30)
heart = pygame.image.load("heart.png")
heart = pygame.transform.scale(heart, [20,20])
#Creates crosshair image
pygame.mouse.set_visible(0)
crosshair = pygame.image.load("crosshair.png")
crosshair = pygame.transform.scale(crosshair,[30,30])
#Initializes sprite groups
all_sprites = pygame.sprite.Group()


walls = pygame.sprite.Group()
horizWalls = pygame.sprite.Group()
vertWalls = pygame.sprite.Group()
endwalls = pygame.sprite.Group()
keys = pygame.sprite.Group()
gameFlag = False
#Puts game and instances in a loop so it can be ran again
while gameFlag == False:
  #Creates instances of above classes and adds them to respective groups
  wall = Wall(0, 0, 10, 350)
  all_sprites.add(wall)
  walls.add(wall)

  player = Player(45, 35, lives)
  all_sprites.add(player)
  
  enemies = pygame.sprite.Group()
  bullets = pygame.sprite.Group()
  
  menu = pygame.image.load("menu.webp")
  menu = pygame.transform.scale(menu,[600,400])
  
  wall = Wall(100, 0, 10,215)
  all_sprites.add(wall)
  walls.add(wall)
  
  wall = Wall (50, 260, 120,10)
  all_sprites.add(wall)
  walls.add(wall)
  
  wall = Wall(160, 75, 10, 240)
  all_sprites.add(wall)
  walls.add(wall)
  
  wall = Wall(220, 0 ,10, 90)
  all_sprites.add(wall)
  walls.add(wall)
  
  wall = Wall(290, 40, 10, 240)
  all_sprites.add(wall)
  walls.add(wall)
  
  wall = Wall (300, 60, 240, 10)
  all_sprites.add(wall)
  walls.add(wall)
  
  wall = Wall(360 ,130, 10 , 220 )
  all_sprites.add(wall)
  walls.add(wall)
  
  wall = Wall(420, 60 , 10, 210)
  all_sprites.add(wall)
  walls.add(wall)
  
  wall = Wall(220, 140, 10, 210)
  all_sprites.add(wall)
  walls.add(wall)
  
  wall = Wall(420, 270, 110 ,10)
  all_sprites.add(wall)
  walls.add(wall)
  
  wall = Wall(430 ,170,100, 10)
  all_sprites.add(wall)
  walls.add(wall)
  
  wall = Wall(480 , 220 , 120 , 10)
  all_sprites.add(wall)
  walls.add(wall)
  
  wall = Wall(490 , 120 , 100,10)
  all_sprites.add(wall)
  walls.add(wall)
  
  wall = Wall(490 , 70 , 10 ,50)
  all_sprites.add(wall)
  walls.add(wall)
  
  wall = Wall(50, 260, 10,60)
  all_sprites.add(wall)
  walls.add(wall)
  
  wall = Wall (105 ,300 , 10 ,60)
  all_sprites.add(wall)
  walls.add(wall)
  
  wall = Wall(360, 10, 10 ,25)
  all_sprites.add(wall)
  walls.add(wall)
  
  wall = Wall (430, 40, 10, 30)
  all_sprites.add(wall)
  walls.add(wall)
  
  wall = Wall(500, 10, 10 , 25)
  all_sprites.add(wall)
  walls.add(wall)
  
  
  wall = Wall(470, 320 ,10, 40)
  all_sprites.add(wall)
  walls.add(wall)
  
  wall = Wall(520, 280 , 10 ,40)
  all_sprites.add(wall)
  walls.add(wall)
  
  wall = Wall(0, 350, 600, 10)
  all_sprites.add(wall)
  walls.add(wall)
  
  wall = Wall(590, 0, 10, 350)
  all_sprites.add(wall)
  walls.add(wall)
  
  wall = Wall(0, 0, 600, 10)
  all_sprites.add(wall)
  walls.add(wall)
  
  endwall = EndWall(490,130, 10, 40)
  all_sprites.add(endwall)
  walls.add(endwall)
  endwalls.add(endwall)
  
  keyOne = Key(120, 325)
  all_sprites.add(keyOne)
  keys.add(keyOne)
  
  keyTwo = Key(510,95)
  all_sprites.add(keyTwo)
  keys.add(keyTwo)
  
  keyThree = Key(530, 325)
  all_sprites.add(keyThree)
  keys.add(keyThree)
  
  enemy = Enemy(500,100)
  all_sprites.add(enemy)
  enemies.add(enemy)
  
  enemy = Enemy(350,150)
  all_sprites.add(enemy)
  enemies.add(enemy)
  
  enemy = Enemy(250, 300)
  all_sprites.add(enemy)
  enemies.add(enemy)
  
  enemy = Enemy(550, 350)
  all_sprites.add(enemy)
  enemies.add(enemy)
  
  enemy = Enemy(100,350)
  all_sprites.add(enemy)
  enemies.add(enemy)
  
  enemy = Enemy(150, 100)
  all_sprites.add(enemy)
  enemies.add(enemy)
  
  endArea = End()
  all_sprites.add(endArea)

  #Create images for keys and background
  keyPic = pygame.image.load("key.png")
  keyPic = pygame.transform.scale(keyPic, [25,20])
  
  background = pygame.image.load("background.jpg")
  background = pygame.transform.scale(background, [600,350])
  #Sorts walls into groups based on if they are vertical or horizontal walls
  for wall in walls:
    if wall.height > wall.width:
      vertWalls.add(wall)
    else:
      horizWalls.add(wall)
  
  clock = pygame.time.Clock()
  endText2 = optionFont.render(option1, True, white)
  endText3 = optionFont.render(option2, True, white)
  livesText = gameFont.render(livesString, True, black)
  coolText = gameFont.render(coolString, True, black)
  keyText = gameFont.render(keyString, True, black)
  
  done = False
  
  while not done:
    
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        done = True
      #Calls player change speed method
      elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_a:
          player.changespeed(-3, 0)
        elif event.key == pygame.K_d:
          player.changespeed(3, 0)
        elif event.key == pygame.K_w:
          player.changespeed(0, -3)
        elif event.key == pygame.K_s:
          player.changespeed(0, 3)
      elif event.type == pygame.KEYUP:
        if event.key == pygame.K_a:
          player.changespeed(3, 0)
        elif event.key == pygame.K_d:
          player.changespeed(-3, 0)
        elif event.key == pygame.K_w:
          player.changespeed(0, 3)
        elif event.key == pygame.K_s:
          player.changespeed(0, -3)
      #Checks cooldown flag
      if coolFlag == True and (pygame.time.get_ticks()-shotTime) >=1000:
        coolFlag = False
      #Creates bullet instance
      if event.type== pygame.MOUSEBUTTONDOWN and coolFlag == False:
        x = player.rect.x 
        y = player.rect.y
        bullet = Bullet(x,y,directFlag)
        all_sprites.add(bullet)
        bullets.add(bullet)
        coolFlag = True
        shotTime = pygame.time.get_ticks()
    #Calls update method for enemies and player
    enemies.update(vertWalls, horizWalls)
    player.update(walls, enemies, keys, endwalls, endArea, endwall)
    #Calls update method for bulets
    for bullet in bullets:
      bullet.update(enemies,walls)
    pos = pygame.mouse.get_pos()
    x_mouse = pos[0]
    y_mouse = pos[1]
    screen.fill(white)
    #Draws the sprites involved in the game if the player is in the game. Updates the bottom of the screen for lives collectables and cooldown
    if player.lives >0:
      screen.blit(background, (0,0))
      all_sprites.draw(screen)
      screen.blit(livesText,(15,370))
      screen.blit(keyText, (180, 370))
      screen.blit(crosshair,[x_mouse,y_mouse,15,15])
      if player.lives ==1:
        screen.blit(heart, [77,369])
      elif player.lives==2:
        screen.blit(heart, [77,369])
        screen.blit(heart, [98,369])
      elif player.lives==3:
        screen.blit(heart, [77,369])
        screen.blit(heart, [98,369])
        screen.blit(heart, [119,369])
      if coolFlag == True:
        screen.blit(coolText,(427, 369))
      if keyOne.count ==1:
        screen.blit(keyPic,(240, 370))
      elif keyOne.count == 2:
        screen.blit(keyPic,(240, 370))
        screen.blit(keyPic, (270,370))
      elif keyOne.count == 3:
        screen.blit(keyPic,(240, 370))
        screen.blit(keyPic, (270,370))
        screen.blit(keyPic, (300,370))
    #Puts the player in the menu if they are not in the game. Removes all sprites from their groups and re runs the game or quits the game depending on user input
    else:
      screen.blit(menu, (0,0))
      screen.blit(endText2, (300, 255))
      screen.blit(endText3, (340,285))
      for bullet in bullets:
        bullets.remove(bullets)
      for enemy in enemies:
        enemies.remove(enemy)
      for key in keys:
        keys.remove(key)
      for wall in walls:
        walls.remove(wall)
      for endwall in endwalls:
        endwalls.remove(endwall)
      for wall in horizWalls:
        horizWalls.remove(wall)
      for wall in vertWalls:
        vertWalls.remove(wall)
      for sprite in all_sprites:
        all_sprites.remove(sprite)
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RETURN:
          gameFlag = False
          done = True
          player.lives =3
        elif event.key == pygame.K_ESCAPE:
          gameFlag = True
          done = True
          pygame.quit()
      
    pygame.display.flip()
    clock.tick(30)

pygame.quit()