# Imports
import pygame
import math
import random

# Initialize game engine
pygame.init()


# Window
SIZE = (800, 600)
TITLE = "Major League Soccer"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)


# Timer
clock = pygame.time.Clock()
refresh_rate = 60


# Colors
''' add colors you use as RGB values here '''
RED = (255, 0, 0)
GREEN = (52, 166, 36)
BLUE = (29, 116, 248)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ORANGE = (255, 125, 0)
DARK_BLUE = (18, 0, 91)
DARK_GREEN = (0, 94, 0)
GRAY = (130, 130, 130)
YELLOW = (255, 255, 110)
SILVER = (200, 200, 200)
DAY_GREEN = (41, 129, 29)
NIGHT_GREEN = (0, 64, 0)
BRIGHT_YELLOW = (255, 244, 47)
NIGHT_GRAY = (104, 98, 115)
ck = (127, 33, 33)

DARKNESS = pygame.Surface(SIZE)
DARKNESS.set_alpha(200)
DARKNESS.fill((0, 0, 0))

SEE_THROUGH = pygame.Surface((800, 180))
SEE_THROUGH.set_alpha(150)
SEE_THROUGH.fill((124, 118, 135))


def key_down_handler(event):
    '''key down handler this controls the lights
    param event: this is the event variable'''
    global day, lights_on
    if event.key == pygame.K_t:
        lights_on = not lights_on
    elif event.key == pygame.K_d:
        day = not day


def draw_cloud(x, y):
    '''function draws cloud with x and y coordinates
    param x: x coordinate of the cloud
    param y: y coordinate of the cloud'''
    pygame.draw.ellipse(SEE_THROUGH, cloud_color, [x, y + 8, 10, 10])
    pygame.draw.ellipse(SEE_THROUGH, cloud_color, [x + 6, y + 4, 8, 8])
    pygame.draw.ellipse(SEE_THROUGH, cloud_color, [x + 10, y, 16, 16])
    pygame.draw.ellipse(SEE_THROUGH, cloud_color, [x + 20, y + 8, 10, 10])
    pygame.draw.rect(SEE_THROUGH, cloud_color, [x + 6, y + 8, 18, 10])



def draw_fence(x, y):
    '''function draws fence with x and y coordinates
    param x: x coordinate of the fence
    param y: y coordinate of the fence'''
    y = 170
    for x in range(5, 800, 30):
        pygame.draw.polygon(screen, NIGHT_GRAY, [[x + 2, y], [x + 2, y + 15], [x, y + 15], [x, y]])

    y = 170
    for x in range(5, 800, 3):
        pygame.draw.line(screen, NIGHT_GRAY, [x, y], [x, y + 15], 1)

    x = 0
    for y in range(170, 185, 4):
        pygame.draw.line(screen, NIGHT_GRAY, [x, y], [x + 800, y], 1)

    if day:
        pygame.draw.ellipse(screen, BRIGHT_YELLOW, [520, 50, 40, 40])
    else:
        pygame.draw.ellipse(screen, WHITE, [520, 50, 40, 40]) 
        pygame.draw.ellipse(screen, sky_color, [530, 45, 40, 40])

def make_star(n):
    '''function makes a star with a random x,y coordinate
    param n: the number of stars to create
    return: an array of created stars
    '''
    stars = []
    for n in range(n):
        x = random.randrange(0, 800)
        y = random.randrange(0, 200)
        r = random.randrange(1, 2)
        stars.append([x, y, r, r])
    return stars

def make_cloud(n):
    '''function makes a cloud with a random x,y coordinate
    parm n: the number of clouds to create
    return: an array of created clouds
    '''
    clouds = []
    for i in range(n):
        x = random.randrange(-100, 1600)
        y = random.randrange(0, 150)
        clouds.append([x, y])
    return clouds

def display_star(stars):
    '''function displays stars onto screen from the parameter array
    parm stars: array of stars with specified x,y coordinate
    return: none
    '''
    for s in stars:
        pygame.draw.ellipse(screen, WHITE, s)

def animate_cloud(clouds, speed):
    '''function updates the each clouds' position to shift left by a 
            specified speed and rotate back with a random y coordinate
        param clouds: array of clouds with specified x,y coordinate to animate
        param speed: specifies shift left animation speed
        return: none
    '''
    # shifts clouds to left
    for c in clouds:
        c[0] -= speed
    # rotates clouds back to right with a random y-coordinate
    if c[0] < -100:
        c[0] = random.randrange(800, 1600)
        c[1] = random.randrange(0, 150)

# Config
lights_on = True
day = True

# array of stars
stars = make_star(200)

# array of clouds
clouds = make_cloud(20)

    
# Game loop
done = False

while not done:
    # Event processing (React to key presses, mouse clicks, etc.)
    ''' for now, we'll just check to see if the X is clicked '''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_l:
                lights_on = not lights_on
            elif event.key == pygame.K_d:
                day = not day

    # Game logic (Check for collisions, update points, etc.)
    ''' leave this section alone for now ''' 
    if lights_on:
        light_color = YELLOW
    else:
        light_color = SILVER

    if day:
        sky_color = BLUE
        field_color = GREEN
        stripe_color = DAY_GREEN
        cloud_color = WHITE
    else:
        sky_color = DARK_BLUE
        field_color = DARK_GREEN
        stripe_color = NIGHT_GREEN
        cloud_color = NIGHT_GRAY
    
    # Animates every cloud to shift left with a speed of 0.5 pixels per frame
    animate_cloud(clouds, 0.5)
            
    # Drawing code (Describe the picture. It isn't actually drawn yet.)
    screen.fill(sky_color)
    SEE_THROUGH.fill(ck)
    SEE_THROUGH.set_colorkey(ck)
    
    # Displays stars when display state is night (not day)
    if not day:
        display_star(stars)




    pygame.draw.rect(screen, field_color, [0, 180, 800 , 420])
    pygame.draw.rect(screen, stripe_color, [0, 180, 800, 42])
    pygame.draw.rect(screen, stripe_color, [0, 264, 800, 52])
    pygame.draw.rect(screen, stripe_color, [0, 368, 800, 62])
    pygame.draw.rect(screen, stripe_color, [0, 492, 800, 82])


   

    
    
    for c in clouds:
        draw_cloud(c[0], c[1])
    screen.blit(SEE_THROUGH, (0, 0))   
    

    #out of bounds lines
    pygame.draw.line(screen, WHITE, [0, 580], [800, 580], 5)
    #left
    pygame.draw.line(screen, WHITE, [0, 360], [140, 220], 5)
    pygame.draw.line(screen, WHITE, [140, 220], [660, 220], 3)
    #right
    pygame.draw.line(screen, WHITE, [660, 220], [800, 360], 5)

#safety circle
def draw_safety_circle(screen, color, rect, width=0):
    '''function draws a safety circle by using a rectangle with coordinates and a width for the line thickness
    param screen: the screen surface where the safety circle will be drawn on
    param color: the color to draw the safety circle in
    param rect: the rectangle coordinates from the user
    param width: the line thickness
    return: none
    '''
    pygame.draw.ellipse(screen, color, rect, width)

    # calling the draw_safery_circle function
    draw_safety_circle(screen, WHITE, [240, 500, 320, 160], 5)

    #18 yard line goal box
    pygame.draw.line(screen, WHITE, [260, 220], [180, 300], 5)
    pygame.draw.line(screen, WHITE, [180, 300], [620, 300], 3)
    pygame.draw.line(screen, WHITE, [620, 300], [540, 220], 5)

    #arc at the top of the goal box
    pygame.draw.arc(screen, WHITE, [330, 280, 140, 40], math.pi, 2 * math.pi, 5)
    
#score board pole 
def draw_scoreboard_pole(screen, color, x, y, width, height):
    '''function draws a scoreboard pole by using x,y coordinates, width, and height
    param screen: the screen surface where the scoreboard pole will be drawn on
    param color: the color to draw the scoreboard pole in
    return: none
    '''
    pygame.draw.rect(screen, color, [x, y, width, height])

    # calling the draw_scoreboard pole function
    draw_scoreboard_pole(screen, GRAY, 390, 120, 20, 70)

    #score board
    pygame.draw.rect(screen, BLACK, [300, 40, 200, 90])
    pygame.draw.rect(screen, WHITE, [302, 42, 198, 88], 2)


#goal
def draw_goal(screen, color, x, y):
    '''function draws a soccer goal by using x,y coordinates
    param screen: the screen surface where the goal will be drawn on
    param color: the color to draw the goal in
    return: none
    '''
    pygame.draw.rect(screen, color, [320, 140, 160, 80], 5)
    pygame.draw.line(screen, color, [340, 200], [460, 200], 3)
    pygame.draw.line(screen, color, [320, 220], [340, 200], 3)
    pygame.draw.line(screen, color, [480, 220], [460, 200], 3)
    pygame.draw.line(screen, color, [320, 140], [340, 200], 3)
    pygame.draw.line(screen, color, [480, 140], [460, 200], 3)

#6 yard line goal box
def draw_yard_line(screen, color, x, y):
    '''function draws a yard line by using x,y coordinates
    param screen: the screen surface where the yard line will be drawn on
    param color: the color to draw the goal in
    return: none
    '''
    pygame.draw.line(screen, color, [310, 220], [270, 270], 3)
    pygame.draw.line(screen, color, [270, 270], [530, 270], 2)
    pygame.draw.line(screen, color, [530, 270], [490, 220], 3)

#light pole 1
def draw_light_pole_1(screen, color, x, y):
    '''function  
    param screen: the screen surface where the light pole will be drawn on
    param color: the color to draw the light pole in
    param x: x coordinate to draw the light pole on
    param y: y coordinate to draw the light pole on
    pram width: the width of the light pole
    param height: the height of the light pole
    return: none
    '''
    pygame.draw.rect(screen, GRAY, [150, 60, 20, 140])
    pygame.draw.ellipse(screen, GRAY, [150, 195, 20, 10])


    #lights part 1
    pygame.draw.line(screen, GRAY, [110, 60], [210, 60], 2)
    pygame.draw.ellipse(screen, light_color, [110, 40, 20, 20])
    pygame.draw.ellipse(screen, light_color, [130, 40, 20, 20])
    pygame.draw.ellipse(screen, light_color, [150, 40, 20, 20])
    pygame.draw.ellipse(screen, light_color, [170, 40, 20, 20])
    pygame.draw.ellipse(screen, light_color, [190, 40, 20, 20])
    pygame.draw.line(screen, GRAY, [110, 40], [210, 40], 2)
    pygame.draw.ellipse(screen, light_color, [110, 20, 20, 20])
    pygame.draw.ellipse(screen, light_color, [130, 20, 20, 20])
    pygame.draw.ellipse(screen, light_color, [150, 20, 20, 20])
    pygame.draw.ellipse(screen, light_color, [170, 20, 20, 20])
    pygame.draw.ellipse(screen, light_color, [190, 20, 20, 20])
    pygame.draw.line(screen, GRAY, [110, 20], [210, 20], 2)

#light pole 2
def draw_light_pole_2(screen, color, x, y):
    '''function  
    param screen: the screen surface where the light pole will be drawn on
    param color: the color to draw the light pole in
    param x: x coordinate to draw the light pole on
    param y: y coordinate to draw the light pole on
    pram width: the width of the light pole
    param height: the height of the light pole
    return: none
    '''
    pygame.draw.rect(screen, GRAY, [630, 60, 20, 140])
    pygame.draw.ellipse(screen, GRAY, [630, 195, 20, 10])

    #lights part 2
    pygame.draw.line(screen, GRAY, [590, 60], [690, 60], 2)
    pygame.draw.ellipse(screen, light_color, [590, 40, 20, 20])
    pygame.draw.ellipse(screen, light_color, [610, 40, 20, 20])
    pygame.draw.ellipse(screen, light_color, [630, 40, 20, 20])
    pygame.draw.ellipse(screen, light_color, [650, 40, 20, 20])
    pygame.draw.ellipse(screen, light_color, [670, 40, 20, 20])
    pygame.draw.line(screen, GRAY, [590, 40], [690, 40], 2)
    pygame.draw.ellipse(screen, light_color, [590, 20, 20, 20])
    pygame.draw.ellipse(screen, light_color, [610, 20, 20, 20])
    pygame.draw.ellipse(screen, light_color, [630, 20, 20, 20])
    pygame.draw.ellipse(screen, light_color, [650, 20, 20, 20])
    pygame.draw.ellipse(screen, light_color, [670, 20, 20, 20])
    pygame.draw.line(screen, GRAY, [590, 20], [690, 20], 2)

def draw_net(screen, color, x, y):
    '''function draws net using x and y coordinates
    param screen: the screen surface where the net will be drawn on
    param color: the color to draw the net in
    return: none
    '''
    #net part 1
    pygame.draw.line(screen, WHITE, [325, 140], [341, 200], 1)
    pygame.draw.line(screen, WHITE, [330, 140], [344, 200], 1)
    pygame.draw.line(screen, WHITE, [335, 140], [347, 200], 1)
    pygame.draw.line(screen, WHITE, [340, 140], [350, 200], 1)
    pygame.draw.line(screen, WHITE, [345, 140], [353, 200], 1)
    pygame.draw.line(screen, WHITE, [350, 140], [356, 200], 1)
    pygame.draw.line(screen, WHITE, [355, 140], [359, 200], 1)
    pygame.draw.line(screen, WHITE, [360, 140], [362, 200], 1)
    pygame.draw.line(screen, WHITE, [364, 140], [365, 200], 1)
    pygame.draw.line(screen, WHITE, [368, 140], [369, 200], 1)
    pygame.draw.line(screen, WHITE, [372, 140], [373, 200], 1)
    pygame.draw.line(screen, WHITE, [376, 140], [377, 200], 1)
    pygame.draw.line(screen, WHITE, [380, 140], [380, 200], 1)
    pygame.draw.line(screen, WHITE, [384, 140], [384, 200], 1)
    pygame.draw.line(screen, WHITE, [388, 140], [388, 200], 1)
    pygame.draw.line(screen, WHITE, [392, 140], [392, 200], 1)
    pygame.draw.line(screen, WHITE, [396, 140], [396, 200], 1)
    pygame.draw.line(screen, WHITE, [400, 140], [400, 200], 1)
    pygame.draw.line(screen, WHITE, [404, 140], [404, 200], 1)
    pygame.draw.line(screen, WHITE, [408, 140], [408, 200], 1)
    pygame.draw.line(screen, WHITE, [412, 140], [412, 200], 1)
    pygame.draw.line(screen, WHITE, [416, 140], [416, 200], 1)
    pygame.draw.line(screen, WHITE, [420, 140], [420, 200], 1)
    pygame.draw.line(screen, WHITE, [424, 140], [423, 200], 1)
    pygame.draw.line(screen, WHITE, [428, 140], [427, 200], 1)
    pygame.draw.line(screen, WHITE, [432, 140], [431, 200], 1)
    pygame.draw.line(screen, WHITE, [436, 140], [435, 200], 1)
    pygame.draw.line(screen, WHITE, [440, 140], [438, 200], 1)
    pygame.draw.line(screen, WHITE, [445, 140], [441, 200], 1)
    pygame.draw.line(screen, WHITE, [450, 140], [444, 200], 1)
    pygame.draw.line(screen, WHITE, [455, 140], [447, 200], 1)
    pygame.draw.line(screen, WHITE, [460, 140], [450, 200], 1)
    pygame.draw.line(screen, WHITE, [465, 140], [453, 200], 1)
    pygame.draw.line(screen, WHITE, [470, 140], [456, 200], 1)
    pygame.draw.line(screen, WHITE, [475, 140], [459, 200], 1)

    #net part 2
    pygame.draw.line(screen, WHITE, [320, 140], [324, 216], 1)
    pygame.draw.line(screen, WHITE, [320, 140], [326, 214], 1)
    pygame.draw.line(screen, WHITE, [320, 140], [328, 212], 1)
    pygame.draw.line(screen, WHITE, [320, 140], [330, 210], 1)
    pygame.draw.line(screen, WHITE, [320, 140], [332, 208], 1)
    pygame.draw.line(screen, WHITE, [320, 140], [334, 206], 1)
    pygame.draw.line(screen, WHITE, [320, 140], [336, 204], 1)
    pygame.draw.line(screen, WHITE, [320, 140], [338, 202], 1)

    #net part 3
    pygame.draw.line(screen, WHITE, [480, 140], [476, 216], 1)
    pygame.draw.line(screen, WHITE, [480, 140], [474, 214], 1)
    pygame.draw.line(screen, WHITE, [480, 140], [472, 212], 1)
    pygame.draw.line(screen, WHITE, [480, 140], [470, 210], 1)
    pygame.draw.line(screen, WHITE, [480, 140], [468, 208], 1)
    pygame.draw.line(screen, WHITE, [480, 140], [466, 206], 1)
    pygame.draw.line(screen, WHITE, [480, 140], [464, 204], 1)
    pygame.draw.line(screen, WHITE, [480, 140], [462, 202], 1)

    #net part 4
    pygame.draw.line(screen, WHITE, [324, 144], [476, 144], 1)
    pygame.draw.line(screen, WHITE, [324, 148], [476, 148], 1)
    pygame.draw.line(screen, WHITE, [324, 152], [476, 152], 1)
    pygame.draw.line(screen, WHITE, [324, 156], [476, 156], 1)
    pygame.draw.line(screen, WHITE, [324, 160], [476, 160], 1)
    pygame.draw.line(screen, WHITE, [324, 164], [476, 164], 1)
    pygame.draw.line(screen, WHITE, [324, 168], [476, 168], 1)
    pygame.draw.line(screen, WHITE, [324, 172], [476, 172], 1)
    pygame.draw.line(screen, WHITE, [324, 176], [476, 176], 1)
    pygame.draw.line(screen, WHITE, [335, 180], [470, 180], 1)
    pygame.draw.line(screen, WHITE, [335, 184], [465, 184], 1)
    pygame.draw.line(screen, WHITE, [335, 188], [465, 188], 1)
    pygame.draw.line(screen, WHITE, [335, 192], [465, 192], 1)
    pygame.draw.line(screen, WHITE, [335, 196], [465, 196], 1)

    #stands right
def draw_stands_right(screen, color, vertices):
    '''function draws the stands on the right side using verticies
    param screen: the screen surface where the stands will be drawn on
    param color: the color to draw the stands in
    param vertices: the verticies of the stands
    return: none
    '''
    pygame.draw.polygon(screen, color, vertices)
    
    # calling the draw_stands_right function
    pygame.draw.polygon(screen, RED, [[680, 220], [800, 340], [800, 290], [680, 180]])
    pygame.draw.polygon(screen, WHITE, [[680, 180], [800, 100], [800, 290]])

  
    #stands left
    pygame.draw.polygon(screen, RED, [[120, 220], [0, 340], [0, 290], [120, 180]])
    pygame.draw.polygon(screen, WHITE, [[120, 180], [0, 100], [0, 290]])
    #people
    

    #corner flag right
    pygame.draw.line(screen, BRIGHT_YELLOW, [140, 220], [135, 190], 3)
    pygame.draw.polygon(screen, RED, [[132, 190], [125, 196], [135, 205]])

    #corner flag left
    pygame.draw.line(screen, BRIGHT_YELLOW, [660, 220], [665, 190], 3)
    pygame.draw.polygon(screen, RED, [[668, 190], [675, 196], [665, 205]]) 

    # DARKNESS
    if not day and not lights_on:
        screen.blit(DARKNESS, (0, 0))    
    
    #pygame.draw.polygon(screen, BLACK, [[200, 200], [50,400], [600, 500]], 10)

    ''' angles for arcs are measured in radians (a pre-cal topic) '''
    #pygame.draw.arc(screen, ORANGE, [100, 100, 100, 100], 0, math.pi/2, 1)
    #pygame.draw.arc(screen, BLACK, [100, 100, 100, 100], 0, math.pi/2, 50)


    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()


    # Limit refresh rate of game loop 
    clock.tick(refresh_rate)

    # trying to draw the objects on the screen permanently
    # # calling the draw goal function
    # draw_goal(screen, WHITE)
    # draw_yard_line(screen, WHITE)
    # draw_light_pole_1(screen, GRAY, 150, 60)
    # draw_yard_line(screen, WHITE)
    # pygame.display.update()

# Close window and quit
pygame.quit()