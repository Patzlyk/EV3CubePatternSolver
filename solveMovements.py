#!/usr/bin/env python3

from sys import stderr
import time

import movements as move

# Rotate the cube to a certain position
def rotateTo(requiredFace, currentRotation):
    if requiredFace == currentRotation[0]:
        move.armTurn2(currentRotation)

    if requiredFace == currentRotation[1]:
        move.armTurn1(currentRotation)

    if requiredFace == currentRotation[2]:
        pass

    if requiredFace == currentRotation[3]:
        move.turn180(currentRotation)
        move.armTurn1(currentRotation)

    if requiredFace == currentRotation[4]:
        move.turnCCW(currentRotation)
        move.armTurn1(currentRotation)

    if requiredFace == currentRotation[5]:
        move.turnCW(currentRotation)
        move.armTurn1(currentRotation)

    return(currentRotation)

#
#   U moves
#

def U(currentRotation):
    rotateTo("Y", currentRotation)
    move.layerCCW(currentRotation)
    return(currentRotation)

def UPrime(currentRotation):
    rotateTo("Y", currentRotation)
    move.layerCW(currentRotation)
    return(currentRotation)

def U180(currentRotation):
    rotateTo("Y", currentRotation)
    move.layer180(currentRotation)
    return(currentRotation)

#
#   D moves
#

def D(currentRotation):
    rotateTo("W", currentRotation)
    move.layerCCW(currentRotation)
    return(currentRotation)

def DPrime(currentRotation):
    rotateTo("W", currentRotation)
    move.layerCW(currentRotation)
    return(currentRotation)

def D180(currentRotation):
    rotateTo("W", currentRotation)
    move.layer180(currentRotation)
    return(currentRotation)

#
#   F moves
#

def F(currentRotation):
    rotateTo("R", currentRotation)
    move.layerCCW(currentRotation)
    return(currentRotation)

def FPrime(currentRotation):
    rotateTo("R", currentRotation)
    move.layerCW(currentRotation)
    return(currentRotation)

def F180(currentRotation):
    rotateTo("R", currentRotation)
    move.layer180(currentRotation)
    return(currentRotation)

#
#   B moves
#

def B(currentRotation):
    rotateTo("O", currentRotation)
    move.layerCCW(currentRotation)
    return(currentRotation)

def BPrime(currentRotation):
    rotateTo("O", currentRotation)
    move.layerCW(currentRotation)
    return(currentRotation)

def B180(currentRotation):
    rotateTo("O", currentRotation)
    move.layer180(currentRotation)
    return(currentRotation)

#
#   L moves
#

def L(currentRotation):
    rotateTo("B", currentRotation)
    move.layerCCW(currentRotation)
    return(currentRotation)

def LPrime(currentRotation):
    rotateTo("B", currentRotation)
    move.layerCW(currentRotation)
    return(currentRotation)

def L180(currentRotation):
    rotateTo("B", currentRotation)
    move.layer180(currentRotation)
    return(currentRotation)

#
#   R moves
#

def R(currentRotation):
    rotateTo("G", currentRotation)
    move.layerCCW(currentRotation)
    return(currentRotation)

def RPrime(currentRotation):
    rotateTo("G", currentRotation)
    move.layerCW(currentRotation)
    return(currentRotation)

def R180(currentRotation):
    rotateTo("G", currentRotation)
    move.layer180(currentRotation)
    return(currentRotation)