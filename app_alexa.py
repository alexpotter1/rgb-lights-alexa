#!/usr/bin/env python

import RPi.GPIO as GPIO
import logging
from flask import Flask, render_template
from flask_ask import Ask, statement, question, session

import multiprocessing
import time

app = Flask(__name__)
ask = Ask(app, "/")
logging.getLogger("flask_ask").setLevel(logging.DEBUG)

GPIO.setmode(GPIO.BCM)

RED = 17
GREEN = 27
BLUE = 24

GPIO.setup(RED, GPIO.OUT)
GPIO.setup(GREEN, GPIO.OUT)
GPIO.setup(BLUE, GPIO.OUT)

def resetColor():
    GPIO.output(RED, GPIO.LOW)
    GPIO.output(GREEN, GPIO.LOW)
    GPIO.output(BLUE, GPIO.LOW)

resetColor()

@ask.intent("LightsOnIntent")
def lightsOn():
    # Default to white
    resetColor()
    
    GPIO.output(RED, GPIO.HIGH)
    GPIO.output(GREEN, GPIO.HIGH)
    GPIO.output(BLUE, GPIO.HIGH)

    msg = render_template('voice_lightson')
    return statement(msg)

@ask.launch
def start_lights_daemon():
    lightsOn()

@ask.intent("LightsOffIntent")
def lightsOff():
    resetColor()


    msg = render_template('voice_lightsoff')
    return statement(msg)

@ask.intent("LightsRedIntent")
def lightsRed():
    resetColor()

    GPIO.output(RED, GPIO.HIGH)

    msg = render_template('voice_lightsred')
    return statement(msg)

@ask.intent("LightsGreenIntent")
def lightsGreen():
    resetColor()

    GPIO.output(GREEN, GPIO.HIGH)

    msg = render_template('voice_lightsgreen')
    return statement(msg)

@ask.intent("LightsBlueIntent")
def lightsBlue():
    resetColor()

    GPIO.output(BLUE, GPIO.HIGH)

    msg = render_template('voice_lightsblue')
    return statement(msg)

@ask.intent("LightsPurpleIntent")
def lightsPurple():
    resetColor()

    GPIO.output(RED, GPIO.HIGH)
    GPIO.output(BLUE, GPIO.HIGH)

    msg = render_template('voice_lightspurple')
    return statement(msg)

@ask.intent("LightsTealIntent")
def lightsTeal():
    resetColor()

    GPIO.output(BLUE, GPIO.HIGH)
    GPIO.output(GREEN, GPIO.HIGH)

    msg = render_template('voice_lightsteal')
    return statement(msg)

@ask.intent("LightsYellowIntent")
def lightsYellow():
    resetColor()

    GPIO.output(RED, GPIO.HIGH)
    GPIO.output(GREEN, GPIO.HIGH)

    msg = render_template("voice_lightsyellow")
    return statement(msg)


if __name__ == "__main__":
    app.run(debug=True)
