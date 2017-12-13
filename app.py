#!/usr/bin/env python

import RPi.GPIO as GPIO
from flask import Flask, render_template, request
app = Flask(__name__)

GPIO.setmode(GPIO.BCM)

def resetColor():
    GPIO.output(17, GPIO.LOW)
    GPIO.output(27, GPIO.LOW)
    GPIO.output(24, GPIO.LOW)

pins = {
    17 : {'name' : 'RED', 'state' : GPIO.LOW},
    27 : {'name' : 'GREEN', 'state' : GPIO.LOW},
    24 : {'name' : 'BLUE', 'state' : GPIO.LOW}
}

for pin in pins:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)

@app.route("/")
def main():
    for pin in pins:
        pins[pin]['state'] = GPIO.input(pin)

    templateData = { 'pins' : pins }
    return render_template('main.html', **templateData)

@app.route("/<changeColor>/<action>")
def action(changeColor, action):
    if changeColor.upper() == "RED":
        if action.upper() == "ON":
            resetColor()
            GPIO.output(17, GPIO.HIGH)
        else:
            resetColor()
    elif changeColor.upper() == "GREEN":
        if action.upper() == "ON":
            resetColor()
            GPIO.output(27, GPIO.HIGH)
        else:
            resetColor()
    elif changeColor.upper() == "BLUE":
        if action.upper() == "ON":
            resetColor()
            GPIO.output(24, GPIO.HIGH)
        else:
            resetColor()
    elif changeColor.upper() == "WHITE":
        if action.upper() == "ON":
            GPIO.output(17, GPIO.HIGH)
            GPIO.output(27, GPIO.HIGH)
            GPIO.output(24, GPIO.HIGH)
        else:
            GPIO.output(17, GPIO.LOW)
            GPIO.output(27, GPIO.LOW)
            GPIO.output(24, GPIO.LOW)
    else:
        pass

    for pin in pins:
        pins[pin]['state'] = GPIO.input(pin)

    templateData = { 'pins' : pins }
    return render_template('main.html', **templateData)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
