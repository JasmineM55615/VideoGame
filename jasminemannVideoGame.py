#*.class
#workspace.xml

# MY_GAME
# The purpose of this program is to create a game 
# that allows the user to move a character away and 
# towards objects and collect them. I have allowed the 
# player to jump with the space bar is presssed. The 
# player is given three lives but will die instantly
# if hit by a babyshrek. There is also a score for the 
# player. Every time a cheese is collected, the score
# increases by one. I have also added different levels k
# and a restart button. Instructions are located on the 
# left side along with the buttons for the different 
# levels and for restarting. The game starts on 
# level one.
# Written by Jasmine Mann.

import simplegui, math, random

# CHANGED
# player_image = simplegui.load_image("https://img.fireden.net/v/image/1524/77/1524777091971.png")
player_image = simplegui.load_image("https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/cf2e5f2d-818a-4555-8e0b-d74131d4b712/deue61v-bcb1ca0a-ee98-42b5-a43a-14f5bdf2619e.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcL2NmMmU1ZjJkLTgxOGEtNDU1NS04ZTBiLWQ3NDEzMWQ0YjcxMlwvZGV1ZTYxdi1iY2IxY2EwYS1lZTk4LTQyYjUtYTQzYS0xNGY1YmRmMjYxOWUucG5nIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.9YTMrSExvXIK0yYTocC3rPfvQkk7daQaCuTqbYq6LRs")

# Dimensions for player image
PLAYER_IMG_WIDTH = 1080
PLAYER_IMG_HEIGHT = 1079

# Dimensions for player on canvas
PLAYER_SIZE = (PLAYER_IMG_WIDTH/10, PLAYER_IMG_HEIGHT/10)

# Dimensions for canvas
WIDTH = 1000
HEIGHT = 520
BGRD = simplegui.load_image("https://s3.amazonaws.com/gameartpartnersimagehost/wp-content/uploads/2017/12/Desert_Game_Background_6.jpg")
B_WIDTH = 1280
B_HEIGHT = 640

# Dimensions for lose image
lose_image = simplegui.load_image("https://i.kym-cdn.com/photos/images/original/001/105/251/e04.jpg")
LOSE_IMG_WIDTH = 800
LOSE_IMG_HEIGHT = 682

# Cheese image
# CHANGED
#cheese_image = simplegui.load_image("http://clipart-library.com/img/1734746.png")
cheese_image = simplegui.load_image("https://www.onlygfx.com/wp-content/uploads/2021/01/cartoon-cheese-1.png")

# Dimensions for cheese image
CHEESE_IMG_WIDTH = 650
CHEESE_IMG_HEIGHT = 572

# Dimensions for cheese on canvas
CHEESE_SIZE = (CHEESE_IMG_WIDTH/17, CHEESE_IMG_HEIGHT/17)

# Bomb image
# CHANGED
#bomb_image = simplegui.load_image("https://www.searchpng.com/wp-content/uploads/2018/12/Cartoon-Bomb-Clipart-715x715.png")
bomb_image = simplegui.load_image("https://freesvg.org/img/bomb.png")

# Dimensions for bomb image
BOMB_IMG_WIDTH = 600
BOMB_IMG_HEIGHT = 600

# Dimensions for bomb on canvas
BOMB_SIZE = (BOMB_IMG_WIDTH/8, BOMB_IMG_HEIGHT/8)

# Heart image
# CHANGED
#heart_image = simplegui.load_image("https://image.spreadshirtmedia.com/image-server/v1/mp/designs/1020424713,width=178,height=178,version=1817257711/funny-dabbing-heart-valentines-shirt-hip-hop-dance.png")
heart_image = simplegui.load_image("https://www.nicepng.com/png/full/11-112096_love-heart-picture-heart-cartoon-transparent-background.png")

# Dimensions for heart image
HEART_IMG_WIDTH = 2285
HEART_IMG_HEIGHT = 2192

# Dimensions for heart on canvas
HEART_SIZE = (HEART_IMG_WIDTH/60,HEART_IMG_HEIGHT/60)

# Shrek image
# CHANGED
#shrek_image = simplegui.load_image("http://www.stickpng.com/assets/images/59f8782b3cec115efb362386.png")
shrek_image = simplegui.load_image("https://assets.stickpng.com/thumbs/59f8782b3cec115efb362386.png")

# Dimensions for shrek image
SHREK_IMG_WIDTH = 400
SHREK_IMG_HEIGHT = 400

# Dimensions for shrek on canvas
SHREK_SIZE = (SHREK_IMG_WIDTH/3, SHREK_IMG_HEIGHT/3)

# Babyshrek image
# CHANGED
#babyshrek_image = simplegui.load_image("http://thecouncil.com/Peggy/Peggy%202007/Baby%20Shrek%20Right%20~%20%2006-01-2007.gif")
babyshrek_image = simplegui.load_image("https://i.pinimg.com/originals/54/1f/0e/541f0ed826a033c3927871d30e21f2c3.png")

# Dimensions for babyshrek image
BABYSHREK_IMG_WIDTH = 236
BABYSHREK_IMG_HEIGHT = 354

# Dimension for babyshrek on canvas
BABYSHREK_SIZE = (BABYSHREK_IMG_WIDTH/5, BABYSHREK_IMG_HEIGHT/5)


cheese_list = []
bomb_list = []
babyshreks = []
character_list = []
time = 0
score = 0
lives = 3
level = 1
bomb_vel = [0, 2]
babyshrek_vel = [-2, 0]
bomb_amount = 120
babyshrek_amount = 300
jump_usage = 3
jump_accel = 2
jump_cooldown = 5
GRAVITY = .5
GROUND = 395
end_game = False


def new_game():
    global time, player, score, lives, time, cheese_list, bomb_list, babyshreks
    player = Character(player_image, [200,400], [0,0], 50)
    score = 0
    lives = 3
    time = 0
    cheese_list =[]
    bomb_list = []
    babyshreks = []

    
# Create level 1
def level_1():
    global level, end_game
    new_game()
    level = 1
    end_game = False
    
    
# Create level 2
def level_2():
    global bomb_vel, babyshrek_vel, bomb_amount, level, end_game
    new_game()
    bomb_vel[1] = 3
    babyshrek_vel[0] = -3
    bomb_amount = 50
    level = 2
    end_game = False
        
        
# Create level 3 (impossible level)
def imp_level():
    global bomb_vel, babyshrek_vel, bomb_amount, babyshrek_amount, level, end_game
    new_game()
    bomb_vel[1] = 4
    babyshrek_vel[0] = -4
    bomb_amount = 10
    babyshrek_amount = 50
    level = 3
    end_game = False
    
    

# This handler makes sure the restart button returns 
# the player to the last level they used
def restart():
    if level == 1:
        level_1()
    if level == 2:
        level_2()
    if level == 3:
        imp_level()
        end_game = False
    

# Use Pythagorean theorem to calculate distance 
# between two points
def distance(pos1, pos2):
    a = pos2[0] - pos1[0]
    b = pos2[1] - pos1[1]
    dist = math.sqrt(a**2 + b**2)
    return dist


# Create Character class
class Character:
    def __init__(self, image, position, velocity, radius):
        self.img = image
        self.pos = position
        self.vel = velocity
        self.rad = radius
        self.on_ground = True
        
        
    
    def jump(self):
        if (self.on_ground == True):
            self.vel[1] = -15
            self.on_ground = False
        
    def draw(self, canvas):
        canvas.draw_image(self.img,
                          (PLAYER_IMG_WIDTH/2,PLAYER_IMG_HEIGHT/2),
                          (PLAYER_IMG_WIDTH,PLAYER_IMG_HEIGHT), 
                          self.pos, 
                          PLAYER_SIZE)
        canvas.draw_circle(self.pos,
                           self.rad,
                           2,
                           "transparent")
        
        
    # Update x and y position
    def update(self):
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]
        if self.pos[0] < self.rad:
            self.pos[0] = self.rad
        if self.pos[0] > WIDTH - self.rad:
            self.pos[0] = WIDTH - self.rad
        if self.on_ground== False:
            self.vel[1] += GRAVITY
        if self.pos[1] > GROUND:
            self.vel[1] = 0
            self.on_ground = True
        
        
    # When character collides with objects
    def has_collided(self, other_obj):
        dist = distance(self.pos, other_obj.pos)
        
        # When you submit project, there shouldnt be 
        # any print statments, they're just here
        # to test if the program works.
        return dist < self.rad + other_obj.rad
        
        
# Create a class for cheese
class Cheese:
    def __init__(self, image, position, velocity, radius):
        self.img = cheese_image
        self.pos = position 
        self.vel = velocity 
        self.rad = radius
      
        
    def draw(self, canvas):
        canvas.draw_image(self.img, 
                          (CHEESE_IMG_WIDTH/2, CHEESE_IMG_HEIGHT/2),
                          (CHEESE_IMG_WIDTH, CHEESE_IMG_HEIGHT),
                          self.pos,
                          CHEESE_SIZE)
        canvas.draw_circle(self.pos,
                           self.rad,
                           2,
                           "transparent")                 
                        
    def update(self):
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]
        # Bounce off top
         
        
# Create a class for bombs
class Bomb:
    def __init__(self, image, position, velocity, radius):
        self.img = image
        self.pos = position
        self.vel = velocity
        self.rad = radius
        
    def draw(self, canvas):
        canvas.draw_image(self.img,
                          (BOMB_IMG_WIDTH/2, BOMB_IMG_WIDTH/2),
                          (BOMB_IMG_WIDTH, BOMB_IMG_HEIGHT),
                          self.pos,
                          BOMB_SIZE)
        canvas.draw_circle(self.pos,
                           self.rad,
                           2,
                           "transparent")
    def update(self):
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]

        
# Create a class for babyshreks (bullets)
class Babyshrek:
    def __init__(self, image, position, velocity, radius):
        self.img = image
        self.pos = position
        self.vel = velocity
        self.rad = radius
    
    def draw(self, canvas):    
        canvas.draw_image(babyshrek_image, 
                          (BABYSHREK_IMG_WIDTH/2, BABYSHREK_IMG_HEIGHT/2),
                          (BABYSHREK_IMG_WIDTH, BABYSHREK_IMG_HEIGHT),
                          self.pos,
                          BABYSHREK_SIZE,
                          math.pi/3) 
        canvas.draw_circle(self.pos,
                           self.rad,
                           2,
                           "transparent")
        
    def update(self):
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]
        
    
# Create a class for shrek
class Shrek:
    def __init__(self, image, position, velocity, radius):
        self.img = image
        self.pos = position
        self.vel = velocity
        self.rad = radius
       
    def draw(self, canvas):    
        canvas.draw_image(self.img, 
                          (SHREK_IMG_WIDTH/2, SHREK_IMG_HEIGHT/2),
                          (SHREK_IMG_WIDTH, SHREK_IMG_HEIGHT),
                          self.pos,
                          SHREK_SIZE,
                          math.pi/3)

    def update(self):
        for i in range(2):
            self.pos[i] += self.vel[i]     
            
    def shoot(self):
        pos = [self.pos[0] + SHREK_SIZE[0]/2, self.pos[1]]
        vel = [10,0]
        babyshrek = Babyshrek(img, pos, vel)
        babyshreks.append(babyshrek)

        
    
# Handler to draw on canvas
def draw(canvas):
    global time, score, lives, end_game

    if (end_game == True):
        canvas.draw_image(lose_image,
                        (LOSE_IMG_WIDTH/2, LOSE_IMG_HEIGHT/2),
                        (LOSE_IMG_WIDTH, LOSE_IMG_HEIGHT),
                        (WIDTH/2, HEIGHT/2),
                        (WIDTH, HEIGHT)) 
        
    else:
        
        # Source is the original file, destination 
        # is the canvas
        canvas.draw_image(BGRD,
                          (B_WIDTH/2,B_HEIGHT/2), 
                          (B_WIDTH,B_HEIGHT),
                          (WIDTH/2,HEIGHT/2),
                          (WIDTH,HEIGHT))
        player.draw(canvas)
        player.update()
    
        # Draw 3 hearts (representing 3 lives)
        # First heart
        if lives == 3:
             canvas.draw_image(heart_image,
                            (HEART_IMG_WIDTH/2, HEART_IMG_HEIGHT/2),
                            (HEART_IMG_WIDTH,HEART_IMG_HEIGHT),
                            (WIDTH*2/90,HEIGHT*1/17), HEART_SIZE)
            # Second heart
             canvas.draw_image(heart_image,
                        (HEART_IMG_WIDTH/2, HEART_IMG_HEIGHT/2),
                        (HEART_IMG_WIDTH,HEART_IMG_HEIGHT),
                        (WIDTH*2/30,HEIGHT*1/17.5), HEART_SIZE)
 
             # Third heart
             canvas.draw_image(heart_image,
                            (HEART_IMG_WIDTH/2, HEART_IMG_HEIGHT/2),
                            (HEART_IMG_WIDTH,HEART_IMG_HEIGHT),
                            (WIDTH*2/18,HEIGHT*1/18), HEART_SIZE)
        
        
        if lives == 2:
            # Only show 2 hearts
            # Second heart
             canvas.draw_image(heart_image,
                            (HEART_IMG_WIDTH/2, HEART_IMG_HEIGHT/2),
                            (HEART_IMG_WIDTH,HEART_IMG_HEIGHT),
                            (WIDTH*2/30,HEIGHT*1/17.5), HEART_SIZE)
 
             # Third heart
             canvas.draw_image(heart_image,
                            (HEART_IMG_WIDTH/2, HEART_IMG_HEIGHT/2),
                            (HEART_IMG_WIDTH,HEART_IMG_HEIGHT),
                            (WIDTH*2/18,HEIGHT*1/18), HEART_SIZE)
        
        if lives == 1:
            # Only show 1 heart
            # Third heart
             canvas.draw_image(heart_image,
                            (HEART_IMG_WIDTH/2, HEART_IMG_HEIGHT/2),
                            (HEART_IMG_WIDTH,HEART_IMG_HEIGHT),
                            (WIDTH*2/18,HEIGHT*1/18), HEART_SIZE)
        
        
        # Make the defeat image appear when all lives 
        # are lost and end the game
        if lives < 1:
            end_game = True
            
            
        # Draw cheese on canvas
        for cheese in cheese_list:
            cheese.draw(canvas)
            cheese.update()
            # Check new position and remove it if it
            # goes off the screen
            if cheese.pos[1] > 420 + cheese.rad:
                cheese_list.remove(cheese)
                return cheese
            # Remove cheese when collided with character
            if player.has_collided(cheese):
                cheese_list.remove(cheese)
                score += 1
    
        if random.randrange(30) == 1:
            x = random.randrange(5, 800)
            y = 5
            # Range for speed and choice for direction
            vx = random.randrange(1,5)*random.choice([10,400])
            vy = random.randrange(1,5)*random.choice([-1,1])
        
            cheese = Cheese(cheese_image, [x,y], [0,2], 18)
            cheese_list.append(cheese)   

        
        # Draw bomb on canvas    
        for bomb in bomb_list:
            bomb.draw(canvas)
            bomb.update()
            # Check new position and remove it if it
            # goes off the screen
            if bomb.pos[1] > 420 + bomb.rad:
                bomb_list.remove(bomb)
                return
            # Remove cheese when collided with character
            if player.has_collided(bomb):
                bomb_list.remove(bomb)
                score = 0
                lives -=1

    
        if random.randrange(bomb_amount) == 1:
            x = random.randrange(5, 800)
            y = 5
            # Range for speed and choice for direction
            vx = random.randrange(1,5)*random.choice([10,400])
            vy = random.randrange(1,5)*random.choice([-1,1])
        
            bomb = Bomb(bomb_image, [x,y], bomb_vel, 18)
            bomb_list.append(bomb)
        
        canvas.draw_text(str(score), (50,105), 80, "Purple")
    
        # Draw shrek on canvas
        shrek = Shrek(shrek_image, [940,400], [0,0], 63)
        shrek.draw(canvas)
        shrek.update()
        for babyshrek in babyshreks:
            babyshrek.draw(canvas)
            babyshrek.update()
            # Check new position and remove it if it
            # goes off the screen
            if babyshrek.pos[1] > HEIGHT + babyshrek.rad:
                babyshreks.remove(babyshrek)
                return
            # Remove babyshrek when collided with 
            # character
            if player.has_collided(babyshrek):
                babyshreks.remove(babyshrek)
                end_game = True
         
        
        if random.randrange(babyshrek_amount) == 1:
            print time/90
            babyshrek = Babyshrek(babyshrek_image, [900,420], babyshrek_vel, 20)
            babyshreks.append(babyshrek)
    
        
    
# Handler for when keyboard key is pressed    
def key_down(key):
    # The key is sent as an integer, so we need to 
    # use a dictionary to look up which key it is
    if key == simplegui.KEY_MAP['right']:
        player.vel[0] = 5
    if key == simplegui.KEY_MAP['left']:
        player.vel[0] = -5
    # Make player jump
    if key == simplegui.KEY_MAP['space']:
        player.jump()
        
    
# Handler for when keyboard key is released        
def key_up(key):
    if key == simplegui.KEY_MAP['right']:
        player.vel[0] = 0
    if key == simplegui.KEY_MAP['left']:
        player.vel[0] = 0
        
# Create the frame and call functions
frame = simplegui.create_frame("Home", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(key_down)
frame.set_keyup_handler(key_up)

# Explain intructions through labels
label1 = frame.add_label('How to Play:')
label2 = frame.add_label('Collect the cheese and avoid the bombs by pressing the left and right keys. Jump over the babyshreks by pressing the spacebar.')
label3 = frame.add_label('Bombs result in you losing a life.')
label4 = frame.add_label('Babyshreks will destroy you.')
label5 = frame.add_label('Goodluck!')

# Buttons for restarting and different levels
button_restart = frame.add_button("Restart", restart)
button_lvl1 = frame.add_button("Level 1", level_1)
button_lvl2 = frame.add_button("Level 2", level_2)
button_lvl3 = frame.add_button("Level Impossible", imp_level)

# Start frame animation
new_game()
frame.start()
