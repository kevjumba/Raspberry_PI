import RPi.GPIO as GPIO
import time

def operate_relay(mode):
    CHANNEL_1=16
    CHANNEL_2=18
    CHANNEL_1_DEFAULT = GPIO.LOW
    CHANNEL_2_DEFAULT = GPIO.LOW
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    GPIO.setup(CHANNEL_1, GPIO.OUT)
    GPIO.setup(CHANNEL_2, GPIO.OUT)
    if(mode == "on"):
        GPIO.output(CHANNEL_1, GPIO.HIGH)
        GPIO.output(CHANNEL_2, GPIO.HIGH)
    elif(mode == "off"):
        GPIO.output(CHANNEL_1, GPIO.LOW)
        GPIO.output(CHANNEL_2, GPIO.LOW)
    else:
        GPIO.output(CHANNEL_1, GPIO.HIGH)
        GPIO.output(CHANNEL_2, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(CHANNEL_1, CHANNEL_1_DEFAULT)
        GPIO.output(CHANNEL_2, CHANNEL_2_DEFAULT)


if __name__ = ('__main__'):
    operate_relay(sys.argv[1])
        
