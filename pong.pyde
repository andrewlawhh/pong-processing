# Set window size
DISPLAY_HEIGHT = 600
DISPLAY_WIDTH = 1200

# Set paddle height and width
PADDLE_HEIGHT = 100
PADDLE_WIDTH = 10

# Paddle Class
class Paddle:

    # Takes initial x and y position
    # Refers to top left corner of the slider
    def __init__(self, x_pos, y_pos):
        self.x = x_pos
        self.y = y_pos
        self.y_vel = 0
        self.score = 0
        
    # Moves the y position by the y velocity
    def move(self):
        self.y += self.y_vel

# Ball Class
class Ball:

    # Takes initial xposition, yposition, xvelocity, yvelocity, and both paddles
    def __init__(self, x_pos, y_pos, x_vel, y_vel, left_paddle, right_paddle):
        self.x = x_pos
        self.y = y_pos
        self.x_vel = x_vel
        self.y_vel = y_vel
        self.left_paddle = left_paddle
        self.right_paddle = right_paddle
    
    # Moves the ball by one unit of time. Bounces off the edges.
    def move(self):
        if self.x <= 0 or self.x >= DISPLAY_WIDTH or self.touching_paddle():
            self.x_vel += 0.1
            self.x_vel *= -1
        if self.y <= 0 or self.y >= DISPLAY_HEIGHT:
            self.y_vel *= -1
        if self.x <= 0:
            self.right_paddle.score += 1
            self.x = DISPLAY_WIDTH // 2
            self.y = DISPLAY_HEIGHT // 2
        if self.x >= DISPLAY_WIDTH:
            self.left_paddle.score += 1
            self.x = DISPLAY_WIDTH // 2
            self.y = DISPLAY_HEIGHT // 2
        self.x += self.x_vel
        self.y += self.y_vel
    
    # Returns a boolean value; True if it is touching the right side of the left paddle, False if it is touching the left side of the right paddle
    def touching_paddle(self):
        return (left_paddle.y + PADDLE_HEIGHT >= self.y >= left_paddle.y and self.x <= left_paddle.x + PADDLE_WIDTH) or \
               (right_paddle.y + PADDLE_HEIGHT >= self.y >= right_paddle.y and self.x >= right_paddle.x)

# Starting y is half the screen width minus half the length of the paddle
STARTING_HEIGHT = DISPLAY_HEIGHT // 2 - PADDLE_HEIGHT // 2

# Starting x is 10 from the left or right
left_paddle = Paddle(35, STARTING_HEIGHT)
right_paddle = Paddle(DISPLAY_WIDTH - 35, STARTING_HEIGHT)

# Initialize ball object at the center of the screen with random x and y velocity
# Ball Constructor Params : (x, y, x_vel, y_vel, left_paddle, right_paddle)
ball = Ball(DISPLAY_WIDTH // 2, DISPLAY_HEIGHT // 2, random(1, DISPLAY_WIDTH // 80), random(1, DISPLAY_WIDTH // 120), left_paddle, right_paddle)

# Draw the paddles to the screen
def show_paddles():
    # rect(x_pos, y_pos, width, height) x and y positions refer to top left
    rect(left_paddle.x, left_paddle.y, PADDLE_WIDTH, PADDLE_HEIGHT)
    rect(right_paddle.x, right_paddle.y , PADDLE_WIDTH, PADDLE_HEIGHT)
    
# Draw the ball to the screen
def show_ball():
    # ellipse(x_pos, y_pos, width, height)
    ellipse(ball.x, ball.y, 8, 8)

# Draw the background (middle line and stylistic circle)
def show_background():
    # line(x1, y1, x2, y2)w
    ellipse(DISPLAY_WIDTH // 2, DISPLAY_HEIGHT // 2, 100, 100)
    line(DISPLAY_WIDTH // 2, 0, DISPLAY_WIDTH // 2, DISPLAY_HEIGHT) 
    show_score()
    
# Draws the score in the background
def show_score():
    text("Score - " + str(left_paddle.score), DISPLAY_WIDTH * 0.25, 40)
    text("Score - " + str(right_paddle.score), DISPLAY_WIDTH * 0.75, 40) 

# Draw the paddles, balls, and background
def show_game():
    fill(0)
    show_paddles()
    show_ball()
    noFill()
    show_background()
    
# Detect keyboard input
def keyPressed():
    # if w or s was pressed, change left paddle's velocity
    if key == 'w':
        left_paddle.y_vel = -DISPLAY_HEIGHT//45
    if key == 's':
        left_paddle.y_vel = DISPLAY_HEIGHT//45
    if key == CODED:
        # if up or down was pressed, change right paddle's velocity
        if keyCode == UP:
            right_paddle.y_vel = -DISPLAY_HEIGHT//45
        if keyCode == DOWN:
            right_paddle.y_vel = DISPLAY_HEIGHT//45

# Detect keyboard input
def keyReleased():
    # reset velocities to 0 when key is released
    if key == 'w' or key == 's': 
        left_paddle.y_vel = 0
    if key == CODED:
        right_paddle.y_vel = 0

def setup():
    frameRate(60)
    size(DISPLAY_WIDTH, DISPLAY_HEIGHT)

def draw():
    background(255,255,255)
    show_game()
    ball.move()
    left_paddle.move()
    right_paddle.move()
    
