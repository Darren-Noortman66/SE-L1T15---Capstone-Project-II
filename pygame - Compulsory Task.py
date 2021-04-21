import pygame  # This will import a game library that allows you use specific functions.


# Initializing the module for pygame so that we can start working with it.

pygame.init()


# Creating two integer values named 'screen_width' and 'screen_height'.
# These variables are then used to create the screen needed to play the game.

screen_width = 1600
screen_height = 950
screen = pygame.display.set_mode((screen_width, screen_height))  # This creates the screen based on the values given.


# Creating the video-game characters and assigning appropriate variable names and values to them.

player = pygame.image.load(
    "player.jpg")  # Creating the player variable and assigning an image to it. This image will represent the player.

enemy = pygame.image.load(
    "Enemy1.jpg")  # Creating the enemy variables and assigning a different image to each one.
enemy2 = pygame.image.load("enemy2.jpg")
enemy3 = pygame.image.load("enemy3.jpg")
enemy4 = pygame.image.load("enemy4.jpg")
enemy5 = pygame.image.load("enemy5.jpg")
enemy6 = pygame.image.load("enemy6.jpg")

prize = pygame.image.load(
    "prize.jpg")  # Creating the prize variable and assigning an image to it. This image will represent the prize.


# Getting the width and height of all the images so that they can all be scaled to a specific size.
# This will also be used later to create the boundary detection which will be used
# to make sure the game stops as soon as the player touches any other oject in the game.

player_height = player.get_height()
player_width = player.get_width()
player = pygame.transform.scale(player, (150, 150))

enemy_height = enemy.get_height()  # This function will retrieve the height of the chosen variale image.
enemy_width = enemy.get_width()  # This function will retrieve the width of the chosen variale image.
enemy = pygame.transform.scale(enemy, (150, 150))  # This function will scale the image to a wanted size.

enemy2_height = enemy2.get_height()
enemy2_width = enemy2.get_width()
enemy2 = pygame.transform.scale(enemy2, (150, 150))

enemy3_height = enemy3.get_height()
enemy3_width = enemy3.get_width()
enemy3 = pygame.transform.scale(enemy3, (150, 150))

enemy4_height = enemy4.get_height()
enemy4_width = enemy4.get_width()
enemy4 = pygame.transform.scale(enemy4, (150, 150))

enemy5_height = enemy5.get_height()
enemy5_width = enemy5.get_width()
enemy5 = pygame.transform.scale(enemy5, (150, 150))

enemy6_height = enemy6.get_height()
enemy6_width = enemy6.get_width()
enemy6 = pygame.transform.scale(enemy6, (150, 150))

prize_height = prize.get_height()
prize_width = prize.get_width()
prize = pygame.transform.scale(prize, (200, 200))


# Assigning integer values to the appropriate variable names which will be
# used to determine the position of every object in the game.
# These variables will also be used to move the objects from a desired starting place to whichever direction calculated.

playerXPosition = 100
playerYPosition = 50

prizeXPosition = 1350
prizeYPosition = 350

# This will make the enemies start off screen and will come from the inserted location.

enemyXPosition = screen_width
enemyYPosition = 50

enemy2XPosition = screen_width
enemy2YPosition = 400

enemy3XPosition = screen_width  # Width is used here to because the first 3 enemies are moving horizontally.
enemy3YPosition = 750

enemy4XPosition = 400
enemy4YPosition = screen_height

enemy5XPosition = 800
enemy5YPosition = screen_height

enemy6XPosition = 1200
enemy6YPosition = screen_height  # Height is used here to because the last 3 enemies are moving vertically.


# This will check which key is being pressed by the user.
# If the user pressed an arrow-key (Up-Arrow, Down-Arrow, Left-Arrow, Right-Arrow)
# , then the player object must move in that direction.

# An appropriate boolean value is assigned to each direction and is assigned the value 'false'.
# When these values are set to 'true', then the player will move in that direction.

keyUp = False
keyDown = False
keyRight = False
keyLeft = False


# A while-loop is used in order to create the 'game-loop'
# This loop is used to update the screen window with the correct positions of each object as they move.

while 1:  # This is a looping structure created to re-run until it is told to quit.

    screen.fill(0)  # Function to clear the screen.
    screen.blit(player, (playerXPosition, playerYPosition))  # This will draw the images of the objects onto the screen
    screen.blit(enemy,
                (enemyXPosition, enemyYPosition))  # The images will be drawn on the specified 'X' and 'Y' positions.
    screen.blit(enemy2, (enemy2XPosition, enemy2YPosition))
    screen.blit(enemy3, (enemy3XPosition, enemy3YPosition))
    screen.blit(enemy4, (enemy4XPosition, enemy4YPosition))
    screen.blit(enemy5, (enemy5XPosition, enemy5YPosition))
    screen.blit(enemy6, (enemy6XPosition, enemy6YPosition))
    screen.blit(prize, (prizeXPosition, prizeYPosition))

    pygame.display.flip()  # Function to update the screen.

    # Creating a for-loop to loop through events in the game.

    for event in pygame.event.get():

        # This is an event for checking if, and which key has been pressed down.

        if event.type == pygame.KEYDOWN:

            # Test for which key is being pressed.
            # If the keys are pressed then the direction value is changed to 'true'
            # , and the player will move in that direction.

            if event.key == pygame.K_UP:  # pygame.K_UP represents a keyboard key constant.
                keyUp = True
            if event.key == pygame.K_DOWN:
                keyDown = True
            if event.key == pygame.K_LEFT:
                keyLeft = True
            if event.key == pygame.K_RIGHT:
                keyRight = True

        # This is an event for checking if the key been released/ moves up.

        if event.type == pygame.KEYUP:

            # Test for which key is being released.
            # If the key is no longer being pressed then the direction value is changed to 'false'
            # , and the player will stop moving in that direction.

            if event.key == pygame.K_UP:
                keyUp = False
            if event.key == pygame.K_DOWN:
                keyDown = False
            if event.key == pygame.K_LEFT:
                keyLeft = False
            if event.key == pygame.K_RIGHT:
                keyRight = False

    # The player is then moved accordingly to whichever chosen direction after the events have been checked.
    # Down and right have 1 added to them to move further away from the screen start
    # , and left and up have 1 subtracted from them to move them closer to the screen start.

    # This is used to move the player up and down.
    if keyUp == True:
        if playerYPosition > 0:  # This is to ensure that the player image is not moved out of the screen.
            playerYPosition -= 1
    if keyDown == True:
        if playerYPosition < screen_height - 150:  # This is to ensure that the player image does not go out the screen.
            playerYPosition += 1

    # This is the move the player left and right.
    if keyLeft == True:
        if playerXPosition > 0:
            playerXPosition -= 1  # This is what will move the player.
    if keyRight == True:
        if playerXPosition < screen_width - 150:
            playerXPosition += 1

    # Creating bounding boxes to test whether or not the player object is colliding with any other objects.
    # Bounding boxes are created for the player, enemies, and the prize.
    # The game is over once the player collides with any enemy object or the prize object.

    # The bounding box is created to fit the objects images' size by:
    # Assigning the value from the top of the box to the value of the 'YPosition', and then
    # Assigning the value from the left of the box to the value of the 'XPosition'.
    # This bounding box will then follow the objects associated with them.

    # Bounding box for player and prize

    playerBox = pygame.Rect(
        player.get_rect())  # pygame.Rect() is a function used to store and manipulate the area of a rectangle.
    playerBox.top = playerYPosition
    playerBox.left = playerXPosition

    prizeBox = pygame.Rect(prize.get_rect())
    prizeBox.top = prizeYPosition
    prizeBox.left = prizeXPosition

    # Bounding box for the enemy:

    enemyBox = pygame.Rect(enemy.get_rect())
    enemyBox.top = enemyYPosition
    enemyBox.left = enemyXPosition
    enemy2Box = pygame.Rect(enemy2.get_rect())
    enemy2Box.top = enemy2YPosition
    enemy2Box.left = enemy2XPosition
    enemy3Box = pygame.Rect(enemy3.get_rect())
    enemy3Box.top = enemy3YPosition
    enemy3Box.left = enemy3XPosition
    enemy4Box = pygame.Rect(enemy4.get_rect())
    enemy4Box.top = enemy4YPosition
    enemy4Box.left = enemy4XPosition
    enemy5Box = pygame.Rect(enemy5.get_rect())
    enemy5Box.top = enemy5YPosition
    enemy5Box.left = enemy5XPosition
    enemy6Box = pygame.Rect(enemy6.get_rect())
    enemy6Box.top = enemy6YPosition
    enemy6Box.left = enemy6XPosition

    # Testing for collisions from the player touching the enemies.
    # If the player does collide with an enemy's boundary box, then the player loses.

    if playerBox.colliderect(enemyBox) or playerBox.colliderect(enemy2Box) or playerBox.colliderect(
            enemy3Box) or playerBox.colliderect(enemy4Box) or playerBox.colliderect(enemy5Box) or playerBox.colliderect(
            enemy6Box):

        # Display losing status to the user

        print("You lose!")

        # Quite game and exit window

        pygame.quit()
        exit(0)

    elif playerBox.colliderect(
            prizeBox):  # Otherwise, if the player's boundary box touches the prize's boundary box,then the player wins.

        # Display wining status to the user

        print("You win!")

        # Quite game and exit window

        pygame.quit()
        exit(0)

    # Make the enemies approach the player.

    enemyXPosition -= 0.5  # The first 3 enemies only move horizontally.
    enemy2XPosition -= 0.5
    enemy3XPosition -= 0.5

    enemy4YPosition -= 0.5  # The last 3 enemies only move vertically.
    enemy5YPosition -= 0.5
    enemy6YPosition -= 0.5


# ------------------------------------------------------------------------------------------------------------------- #

# References:

# - HyperionDev (2021). SE L1T15 - Capstone Project II - Task 15. Retrieved 15 February 2021,
#   from Dropbox/ Darren Noortman/ Task 15/ SE L1T15 - Capstone Project II.pdf

# - HyperionDev (2021). example - Task 15. Retrieved 15 February 2021,
#   from Dropbox/ Darren Noortman/ Task 15/ game/ example II.pdf

# ------------------------------------------------------------------------------------------------------------------- #
