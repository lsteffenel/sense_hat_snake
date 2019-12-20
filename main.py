from sense_hat import SenseHat
from random import randint
from time import sleep
sense = SenseHat()




white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
black = (0,0,0)
orange = (255,165,0)
blue = (0, 0, 255)

O = black
P = red
W = white

heart = [
  O, O, O, O, O, O, O, O,
  O, P, P, O, P, W, P, O,
  P, P, P, P, W, W, P, P,
  P, P, P, W, W, P, P, P,
  O, P, P, W, W, P, P, O,
  O, O, P, W, P, P, O, O,
  O, O, O, O, P, O, O, O,
  O, O, O, O, O, O, O, O,
  ]
  
skull = [
  O, W, W, W, W, W, W, O,
  W, P, P, W, W, P, P, W,
  W, P, P, W, W, P, P, W,
  O, W, W, W, W, W, W, O,
  O, W, W, O, O, W, W, O,
  O, W, W, W, W, W, W, O,
  O, W, O, W, W, O, W, O,
  O, O, W, W, W, W, O, O,
  ]
  
posx = 5
posy = 4

pommex = 0
pommey = 0
pommevie = 0

vies = 3
energie = 20



def initscreen():
  global sense
  global posx
  global posy
  
  global pommex
  global pommey
  global pommevie
  
  sense.clear()
  sense.set_pixel(posx,posy,white)
  
  
  
  pommex = randint(0,7)
  pommey = randint(1,7)
  pommevie = randint(3,10)
  
  sense.set_pixel(pommex,pommey,blue)
  checkvies()
  
def checkvies():
  global energie
  global vies
  for i in range(0,7):
    sense.set_pixel(i,0,black)
  for i in range(0,int(energie // 4)+1):
    sense.set_pixel(i,0,green)
    
    
    
  for j in range(0,vies):
    sense.set_pixel(5+j,0,red)
  if energie == 0:
    #sense.show_message("X",text_colour=red,back_colour=black)
    sense.set_pixels(heart)
    sleep(0.5)
    energie = 20
    vies = vies - 1
    if vies == 0:
      sense.set_pixels(skull)
    else:
      initscreen()
    
def peutmanger():
  global energie
  global posx
  global posy
  global pommex
  global pommey
  global pommevie
  global sense
  if posx == pommex and posy == pommey:
    energie = energie + 5
    if energie > 20:
      energie = 20
    #sense.flip_v()
    #sleep(0.25)
    #sense.flip_v()
    sense.set_rotation(90)
    sleep(0.1)
    sense.set_rotation(180)
    sleep(0.1)
    sense.set_rotation(270)
    sleep(0.1)
    sense.set_rotation(0)
    

    newpomme()
  pommevie = pommevie - 1
  print(pommevie)
  if pommevie == 0:
    sense.set_pixel(pommex,pommey,black)
    newpomme()

def newpomme():
  global pommex
  global pommey
  global pommevie
  pommex = randint(0,7)
  pommey = randint(1,7)
  pommevie = randint(3,10)
  if pommex == posx and pommey == posx:
    newpomme()
  sense.set_pixel(pommex,pommey,blue)
  
def moinsenergie():
  global energie
  energie = energie-1
  
def deplacer(direction):
  global posx
  global posy
  global sense
  global energie

  newx = posx
  newy = posy
  if direction == "up":
    newy = posy-1
    if newy < 1:
      newy = 7
  if direction == "down":
    newy = posy+1
    if newy > 7:
      newy = 1
  if direction == "left":
    newx = posx-1
    if newx < 0:
      newx = 7
  if direction == "right":
    newx = posx+1
    if newx > 7:
      newx = 0
  
  sense.set_pixel(posx,posy,black)
  sense.set_pixel(newx,newy,white)
  posx = newx
  posy = newy
  peutmanger()
  moinsenergie()
  checkvies()
  


initscreen()
while vies > 0:
  event = sense.stick.wait_for_event()
  if event.action == "pressed":
    if event.direction == "up":
      deplacer("up")      # Up arrow
    elif event.direction == "down":
      deplacer("down")      # Down arrow
    elif event.direction == "left": 
      deplacer("left")      # Left arrow
    elif event.direction == "right":
      deplacer("right")      # Right arrow

