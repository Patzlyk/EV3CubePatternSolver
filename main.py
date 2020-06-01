#!/usr/bin/env python3

from sys import stderr
import time
from ev3dev2.motor import LargeMotor, SpeedPercent, OUTPUT_A, OUTPUT_B
from ev3dev2.sensor import INPUT_2
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.button import Button
from ev3dev2.display import Display
from ev3dev2.sound import Sound
print("EV3dev imported", file = stderr)

from PIL import Image
print("PIL imported", file = stderr)

import movements as moves
import solveMovements as solveMove
print("Move and solveMove imported", file = stderr)

# Start
print("starting", file = stderr)

# Initialize motors, sensors and variables
turntable_motor = LargeMotor(OUTPUT_A)
arm_motor = LargeMotor(OUTPUT_B)

touch_sensor = TouchSensor(INPUT_2)
btn = Button()
lcd = Display()
speaker = Sound()

solution = []
patternNumber = 1
maxPatternNumber = 10

# Load pattern images
imageA = Image.open('/home/robot/CubePatterns/pictures/patternA.png')
imageB = Image.open('/home/robot/CubePatterns/pictures/patternB.png')
imageC = Image.open('/home/robot/CubePatterns/pictures/patternC.png')
imageD = Image.open('/home/robot/CubePatterns/pictures/patternD.png')
imageE = Image.open('/home/robot/CubePatterns/pictures/patternE.png')
imageF = Image.open('/home/robot/CubePatterns/pictures/patternF.png')
imageG = Image.open('/home/robot/CubePatterns/pictures/patternG.png')
imageH = Image.open('/home/robot/CubePatterns/pictures/patternH.png')
imageI = Image.open('/home/robot/CubePatterns/pictures/patternI.png')
imageJ = Image.open('/home/robot/CubePatterns/pictures/patternJ.png')

#                                   #
#           Patterns                #
#                                   #

patternA = ["D2", "U2", "B2", "F2", "L2", "R2"]# Checkerboard
patternB = ["R2", "L'", "D", "F2", "R'", "D'", "R'", "L", "U'", "D", "R", "D", "B2", "R'", "U", "D2"]# Cross
patternC = ["D2", "R2", "L2", "D2", "R2", "L2"]# Plus minus
patternD = ["F", "U", "F", "R", "L2", "B", "D'", "R", "D2", "L", "D'", "B", "R2", "L", "F", "U", "F"]# Vertical stripes
patternE = ["R", "L", "F", "B", "R", "L", "F", "B", "R", "L", "F", "B", "R2", "B2", "L2", "R2", "B2", "L2"]# Wire
patternF = ["U'", "L'", "U'", "F'", "R2", "B'", "R", "F", "U", "B2", "U", "B'", "L", "U'", "F", "U", "R", "F'"]# Cube in a cube in a cube
patternG = ["F", "R'", "U", "L", "F'", "L'", "F", "U'", "R", "U", "L'", "U'", "L", "F'"]# Twister
patternH = ["L2", "B2", "D'", "B2", "D", "L2", "U", "R2", "D", "R2", "B", "U", "R'", "F2", "R", "U'", "B'", "U'"]# Displaced motif
patternI = ["F2", "R'", "B'", "U", "R'", "L", "F'", "L", "F'", "B", "D'", "R", "B", "L2"]# Python
patternJ = ["L", "U", "B'", "U'", "R", "L'", "B", "R'", "F", "B'", "D", "R", "D'", "F'"]# Anaconda

#                                   #
#            Main code              #
#                                   #

while True:


    # Choose pattern
    print("Select pattern", file = stderr)
    while not touch_sensor.is_pressed:
        time.sleep(0.2)



        # Select patterns

        # Go to previous pattern
        if btn.down:
           print("Pervious pattern", file = stderr)
           patternNumber = patternNumber - 1

           # Check if the pattern number is lower the 1
           if patternNumber <= 0:
              patternNumber = maxPatternNumber

           print("Pattern: " + str(patternNumber), file = stderr)



        # Go to next pattern
        elif btn.up:
            print("Next pattern", file = stderr)
            patternNumber = patternNumber + 1

        # Check if the pattern number is higher than maxPatternNumber
        if patternNumber > maxPatternNumber:
            patternNumber = 1
            print("Pattern: " + str(patternNumber), file = stderr)

        # Display the image of currently selected pattern
        if patternNumber == 1:
            lcd.image.paste(imageA, (0,0))
            lcd.update()

        if patternNumber == 2:
            lcd.image.paste(imageB, (0,0))
            lcd.update()

        if patternNumber == 3:
           lcd.image.paste(imageC, (0,0))
           lcd.update()

        if patternNumber == 4:
            lcd.image.paste(imageD, (0,0))
            lcd.update()

        if patternNumber == 5:
            lcd.image.paste(imageE, (0,0))
            lcd.update()

        if patternNumber == 6:
            lcd.image.paste(imageF, (0,0))
            lcd.update()

        if patternNumber == 7:
            lcd.image.paste(imageG, (0,0))
            lcd.update()

        if patternNumber == 8:
            lcd.image.paste(imageH, (0,0))
            lcd.update()

        if patternNumber == 9:
            lcd.image.paste(imageI, (0,0))
            lcd.update()

        if patternNumber == 10:
            lcd.image.paste(imageJ, (0,0))
            lcd.update()

    # Print selected pattern
    print(patternNumber, file = stderr)

    # Copy moves to solution array
    if patternNumber == 1:
       solution = patternA

    if patternNumber == 2:
        solution = patternB

    if patternNumber == 3:
        solution = patternC

    if patternNumber == 4:
        solution = patternD

    if patternNumber == 5:
        solution = patternE

    if patternNumber == 6:
        solution = patternF

    if patternNumber == 7:
        solution = patternG

    if patternNumber == 8:
       solution = patternH

    if patternNumber == 9:
        solution = patternI

    if patternNumber == 10:
       solution = patternJ



    #
    #       Solve the cube
    #



    # Print the selected pattern
    print(solution, file = stderr)

    # This array stores location of the centers --- U, F, D, B, L, R
    currentRotation = ["Y", "R", "W", "O", "B", "G"]

    # Set speed of motors
    moves.motorSpeed = 40

    time.sleep(1)

    # Cycle through solution list and solve the cube
    for move in solution:
        print(move, file = stderr)
        print("A", file = stderr)
        print(currentRotation, file = stderr)
        #time.sleep(0.2)

        #
        #   U moves
        #

        if move == "U":
            solveMove.U(currentRotation)

        if move == "U'":
            solveMove.UPrime(currentRotation)

        if move == "U2":
            solveMove.U180(currentRotation)

        #
        #   D moves
        #

        if move == "D":
            solveMove.D(currentRotation)

        if move == "D'":
            solveMove.DPrime(currentRotation)

        if move == "D2":
            solveMove.D180(currentRotation)

        #
        #   F moves
        #

        if move == "F":
            solveMove.F(currentRotation)

        if move == "F'":
            solveMove.FPrime(currentRotation)

        if move == "F2":
            solveMove.F180(currentRotation)

        #
        #   B moves
        #

        if move == "B":
            solveMove.B(currentRotation)

        if move == "B'":
            solveMove.BPrime(currentRotation)

        if move == "B2":
            solveMove.B180(currentRotation)

        #
        #   L moves
        #

        if move == "L":
            solveMove.L(currentRotation)

        if move == "L'":
            solveMove.LPrime(currentRotation)

        if move == "L2":
            solveMove.L180(currentRotation)

        #
        #   R moves
        #

        if move == "R":
            solveMove.R(currentRotation)

        if move == "R'":
            solveMove.RPrime(currentRotation)

        if move == "R2":
            solveMove.R180(currentRotation)
    

    # Play the fanfare sound
    speaker.play_file("sounds/Fanfare.wav")