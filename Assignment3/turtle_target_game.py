import turtle

# Window Setup 
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600

# Target Dimensions
TARGET_REGION_HEIGHT_PX = 70
TARGET_REGION_WIDTH_PX = 70

TARGET_REGION_X = 200
TARGET_REGION_Y = 200

TARGET_RIGHT = TARGET_REGION_X + TARGET_REGION_WIDTH_PX
TARGET_TOP = TARGET_REGION_Y + TARGET_REGION_HEIGHT_PX

# Projectile Settings
FORCE_MULTIPLIER = 40

# Set the enviroment up
turtle.setup(WINDOW_WIDTH, WINDOW_HEIGHT)
turtle.speed(0)
turtle.hideturtle()
turtle.penup()
turtle.goto(TARGET_REGION_X, TARGET_REGION_Y)

# Draw Target
turtle.pendown()
turtle.goto(TARGET_RIGHT, TARGET_REGION_Y)
turtle.goto(TARGET_RIGHT, TARGET_TOP)
turtle.goto(TARGET_REGION_X, TARGET_TOP)
turtle.goto(TARGET_REGION_X, TARGET_REGION_Y)

# Go back to orgin
turtle.penup()
turtle.goto(0, 0)
turtle.showturtle()
turtle.speed(1)

# Take user input as float
angle = float(input("Enter the projectile's angle: "))
# Set heading early so the user can see the change and debate the force required
turtle.setheading(angle)
force = float(input("Enter the projectile's force (1-10): "))

# Validate and compute distance as force * the FORCE_MULTIPLIER
# and move the turtle to distance
if force >= 1 and force <= 10:
    distance = force * FORCE_MULTIPLIER
    turtle.pendown()
    turtle.forward(distance)

    # Check if both x, and y is within the target region
    if (turtle.xcor() >= TARGET_REGION_X and turtle.xcor() <= TARGET_RIGHT
            and turtle.ycor() >= TARGET_REGION_Y and turtle.ycor() <= TARGET_TOP):
        print("You Hit the target!")
    else:
        # else, hint based on x and y cord
        print("You missed the target..")
        if turtle.xcor() > TARGET_RIGHT:
            print("Try a greater angle...")
        if turtle.xcor() < TARGET_REGION_X:
            print("Try a lesser angle...")
        if turtle.ycor() > TARGET_TOP:
            print("Try lesser force...")
        if turtle.ycor() < TARGET_REGION_Y:
            print("Try more force...")
else:
    # if the input is invalid print error
    print("Invalid force. Please enter a value from 1 to 10.")

turtle.done() 
