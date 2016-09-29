from flask import Flask, render_template, send_from_directory
import datetime
import RPi.GPIO as GPIO
import os


app = Flask(__name__, static_url_path='')
GPIO.setmode(GPIO.BOARD)

@app.route("/")
def hello():
    return "Python Flask Hello!"

@app.route("/on")
def turnOn():
    pinList=[3]
    print "1"
    for i in pinList:
        GPIO.setwarnings(False)
        GPIO.setup(i, GPIO.OUT)
        GPIO.output(i, GPIO.HIGH)
    return "turned on"

@app.route("/off")
def turnOff():
    pinList=[3]
    for i in pinList:
        GPIO.setwarnings(False)
        GPIO.setup(i, GPIO.OUT)
        GPIO.output(i, GPIO.LOW)
    return "turned Off"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
