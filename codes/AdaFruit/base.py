# Simple demo of of the PCA9685 PWM servo/LED controller library.
# This will move channel 0 from min to max position repeatedly.
# Author: Tony DiCola
# License: Public Domain
from __future__ import division
import time

# Import the PCA9685 module.
import Adafruit_PCA9685


# Uncomment to enable debug output.
#import logging
#logging.basicConfig(level=logging.DEBUG)

# Initialise the PCA9685 using the default address (0x40).
pwm = Adafruit_PCA9685.PCA9685()

# Alternatively specify a different address and/or bus:
#pwm = Adafruit_PCA9685.PCA9685(address=0x41, busnum=2)

# Configure min and max servo pulse lengths
servo_min = 150  # Min pulse length out of 4096
servo_max = 600  # Max pulse length out of 4096

# Helper function to make setting a servo pulse width simpler.
def set_servo_pulse(channel, pulse):
    pulse_length = 1000000    # 1,000,000 us per second
    pulse_length //= 60       # 60 Hz
    print('{0}us per period'.format(pulse_length))
    pulse_length //= 4096     # 12 bits of resolution
    print('{0}us per bit'.format(pulse_length))
    pulse *= 1000
    pulse //= pulse_length
    pwm.set_pwm(channel, 0, pulse)

# Set frequency to 60hz, good for servos.
pwm.set_pwm_freq(60)

print('Moving servo on channel 0, press Ctrl-C to quit...')
'''
def base_movement():
    i=210
    while i<=430:
        pwm.set_pwm(0, 0, i)
        pwm.set_pwm(2, 0, 500)
        print('0 degree')
        time.sleep(2)
        i=i+22

def shoulder_movement():
    i=270
    while i<=650:
        pwm.set_pwm(0, 0, 340)
        pwm.set_pwm(2, 0, i)
        print('0 degree')
        time.sleep(2)
        i=i+38
def elbow_movement():
    i=170
    while i<=520:
    pwm.set_pwm(0, 0, 340)
    pwm.set_pwm(2, 0, i)
    print('0 degree')
    time.sleep(2)
    i=i+35

Base 8
Shoulder 0
Elbow 6
Wrist 4
Gripper 2
'''
def close_gripper():
    pwm.set_pwm(2, 0, 170)
    time.sleep(2)
def open_gripper():
    pwm.set_pwm(2, 0, 650)
    time.sleep(2)
def wrist_back():
    pwm.set_pwm(4, 0, 170)
    time.sleep(2)
def wrist_front():
    pwm.set_pwm(4, 0, 650)
    time.sleep(2)



while True:
    pwm.set_pwm(8, 0, 210)
    time.sleep(2)
    pwm.set_pwm(8, 0, 340)
    time.sleep(2)
    pwm.set_pwm(0, 0, 270)
    time.sleep(2)
    open_gripper()
    close_gripper()
    pwm.set_pwm(0, 0, 650)
    time.sleep(2)
    pwm.set_pwm(6, 0, 520)
    time.sleep(2)
    wrist_back()
    open_gripper()
    wrist_front()
    #pwm.set_pwm(2, 0, 650)
    #print('0 degree')
    #time.sleep(2)
    #pwm.set_pwm(2, 0, 170)
    #time.sleep(2)
    #pwm.set_pwm(2, 0, 170)
    #print('0 degree')
    #time.sleep(2)

'''
while True:
    open_gripper()
    close_gripper()
'''
    



