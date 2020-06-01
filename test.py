#!/usr/bin/env python3

from sys import stderr
import time
from ev3dev2.motor import LargeMotor, MediumMotor, SpeedPercent, OUTPUT_A, OUTPUT_B, OUTPUT_C
from ev3dev2.sensor import INPUT_1, INPUT_2
from ev3dev2.sensor.lego import ColorSensor, TouchSensor
from ev3dev2.button import Button
from ev3dev2.display import Display
print("")
from PIL import Image
from ev3dev2.sound import Sound

import solveMovements
print("import complete", file = stderr)

lcd = Display()
sound = Sound()
touch_sensor = TouchSensor(INPUT_2)

logo = Image.open('/home/robot/CubePatterns/pictures/smiley.png')
lcd.image.paste(logo, (0,0))
lcd.update()

currentRotation = ["R", "R", "O", "Y", "B", "G"]

solveMovements.rotateTo("W", currentRotation)
solveMovements.rotateTo("Y", currentRotation)
solveMovements.rotateTo("G", currentRotation)
solveMovements.rotateTo("B", currentRotation)
solveMovements.rotateTo("R", currentRotation)
solveMovements.rotateTo("O", currentRotation)
#while True:
#    touch_sensor.wait_for_bump()
#    sound.speak("Ah shit, here we go again")
#    sound.speak("hahahahahahahahahahahahahahaha")