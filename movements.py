#!/usr/bin/env python3

from sys import stderr

from ev3dev2.motor import LargeMotor, SpeedPercent, OUTPUT_A, OUTPUT_B

# Speed of all motors (Percentage)
motorSpeed = 30

# Initialize motors and sensors
turntable_motor = LargeMotor(OUTPUT_A)
arm_motor = LargeMotor(OUTPUT_B)



#                                   #
#           Turntable moves         #
#                                   #

# Turn the cube 90 degrees CW
def turnCW(currentRotation):
    turntable_motor.on_for_degrees(motorSpeed, 90)
    
    # Save new rotation
    uTemp = currentRotation[1]
    currentRotation[1] = currentRotation[5]
    currentRotation[5] = currentRotation[3]
    currentRotation[3] = currentRotation[4]
    currentRotation[4] = uTemp
    return(currentRotation)

# Turn the cube 90 degrees CCW
def turnCCW(currentRotation):
    turntable_motor.on_for_degrees(motorSpeed, 0 - 90)
    
    # Save new rotation
    uTemp = currentRotation[1]
    currentRotation[1] = currentRotation[4]
    currentRotation[4] = currentRotation[3]
    currentRotation[3] = currentRotation[5]
    currentRotation[5] = uTemp
    return(currentRotation)

# Turn the cube 180 degrees CCW
def turn180(currentRotation):
    turntable_motor.on_for_degrees(motorSpeed, 0 - 180)
    
    # Save new rotation
    fTemp = currentRotation[1]
    rTemp = currentRotation[5]
    currentRotation[1] = currentRotation[3]
    currentRotation[5] = currentRotation[4]
    currentRotation[3] = fTemp
    currentRotation[4] = rTemp
    return(currentRotation)



#                                   #
#           Arm moves               #
#                                   #

def armTurn1(currentRotation):
    arm_motor.on_for_degrees(motorSpeed, 0 - 210)
    arm_motor.on_for_degrees(motorSpeed, 210)
    
    # Save new rotation
    uTemp = currentRotation[0]
    currentRotation[0] = currentRotation[3]
    currentRotation[3] = currentRotation[2]
    currentRotation[2] = currentRotation[1]
    currentRotation[1] = uTemp
    return(currentRotation)

def armTurn2(currentRotation):
    arm_motor.on_for_degrees(motorSpeed, 0 - 210)
    arm_motor.on_for_degrees(motorSpeed, 210)
    #
    arm_motor.on_for_degrees(motorSpeed, 0 - 210)
    arm_motor.on_for_degrees(motorSpeed, 210)
    
    # Save new rotation
    uTemp = currentRotation[0]
    fTemp = currentRotation[1]
    currentRotation[0] = currentRotation[2]
    currentRotation[1] = currentRotation[3]
    currentRotation[2] = uTemp
    currentRotation[3] = fTemp
    return(currentRotation)

def armTurn3(currentRotation):
    arm_motor.on_for_degrees(motorSpeed, 0 - 210)
    arm_motor.on_for_degrees(motorSpeed, 210)
    #
    arm_motor.on_for_degrees(motorSpeed, 0 - 210)
    arm_motor.on_for_degrees(motorSpeed, 210)
    #
    arm_motor.on_for_degrees(motorSpeed, 0 - 210)
    arm_motor.on_for_degrees(motorSpeed, 210)
    
    # Save new rotation
    uTemp = currentRotation[0]
    currentRotation[0] = currentRotation[1]
    currentRotation[1] = currentRotation[2]
    currentRotation[2] = currentRotation[3]
    currentRotation[3] = uTemp
    return(currentRotation)



#                                   #
#           Layer moves             #
#                                   #

def layerCW(currentRotation):
    arm_motor.on_for_degrees(motorSpeed, 0 - 210)
    turntable_motor.on_for_degrees(motorSpeed, 90)
    arm_motor.on_for_degrees(motorSpeed, 210)

    # Save new rotation
    uTemp = currentRotation[0]
    currentRotation[0] = currentRotation[3]
    currentRotation[3] = currentRotation[2]
    currentRotation[2] = currentRotation[1]
    currentRotation[1] = uTemp
    return(currentRotation)

def layerCCW(currentRotation):
    arm_motor.on_for_degrees(motorSpeed, 0 - 210)
    turntable_motor.on_for_degrees(motorSpeed, 0 - 90)
    arm_motor.on_for_degrees(motorSpeed, 210)

    # Save new rotation
    uTemp = currentRotation[0]
    currentRotation[0] = currentRotation[3]
    currentRotation[3] = currentRotation[2]
    currentRotation[2] = currentRotation[1]
    currentRotation[1] = uTemp
    return(currentRotation)

def layer180(currentRotation):
    arm_motor.on_for_degrees(motorSpeed, 0 - 210)
    turntable_motor.on_for_degrees(motorSpeed, 180)
    arm_motor.on_for_degrees(motorSpeed, 210)

    # Save new rotation
    uTemp = currentRotation[0]
    currentRotation[0] = currentRotation[3]
    currentRotation[3] = currentRotation[2]
    currentRotation[2] = currentRotation[1]
    currentRotation[1] = uTemp
    return(currentRotation)