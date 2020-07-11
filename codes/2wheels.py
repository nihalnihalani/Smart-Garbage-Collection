import RPi.GPIO as GPIO
import time

print("hello")
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

pwmValue=10

#SETUP LEFT WHEEL
GPIO.setup(12, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)

#SETUP RIGHT WHEEL
GPIO.setup(19, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)

#SETUP PWM OF LEFT WHEEL 
pwm=GPIO.PWM(15,255)
pwm.start(pwmValue)

turn=0


#SETUP PWM OF RIGHT WHEEL
pwm1=GPIO.PWM(23,255)
pwm1.start(pwmValue)


while True:
    print("loop")
    #ENABLE PWM OF LEFT WHEEL
    GPIO.output(15, 1)

    #ENABLE PWM OF RIGHT WHEEL
    GPIO.output(23, 1)
    
    #time.sleep(4)

    #RELEASE THE BRAKES OF BOTH WHEELS
    GPIO.output(13,0)
    GPIO.output(21,0)

    #CHANGE THE DUTY CYCLE OF LEFT WHEEL AND MOVE FORWARD DIRECTION
    pwm.ChangeDutyCycle(pwmValue)
    GPIO.output(12,turn)
    #CHANGE THE DUTY CYCLE OF RIGHT WHEEL AND MOVE FORWARD DIRECTION
    pwm1.ChangeDutyCycle(pwmValue)
    GPIO.output(19,not(turn))
    
    GPIO.output(13,1)
    GPIO.output(21,1)
    
    GPIO.output(13,0)
    GPIO.output(21,0)
    time.sleep(2)
    

    #CHANGE THE DUTY CYCLE OF LEFT WHEEL AND MOVE IN REVERSE DIRECTION 
    pwm.ChangeDutyCycle(pwmValue)
    GPIO.output(12,not(turn))
    #CHANGE THE DUTY CYCLE OF RIGHT WHEEL AND MOVE IN REVERSE DIRECTION
    pwm1.ChangeDutyCycle(pwmValue)
    GPIO.output(19,turn)
    
    
    GPIO.output(13,1)
    GPIO.output(13,0)

    GPIO.output(21,1)
    GPIO.output(21,0)
    time.sleep(2)
    
    #pwm.stop()
GPIO.cleanup()
