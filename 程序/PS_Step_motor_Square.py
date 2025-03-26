import smbus
import time

from time import sleep
import RPi.GPIO as GPIO
if __name__=="__main__":
    pwm_pin0 = 17             #定义pwm输出引脚
    GPIO.setmode(GPIO.BCM)   #定义树莓派gpio引脚以BCM方式编号
    GPIO.setup(pwm_pin0,GPIO.OUT)  #使能gpio口为输出
    pwm0 = GPIO.PWM(pwm_pin0,250)
    
    pwm_pin1 = 18         #定义pwm输出引脚
    GPIO.setmode(GPIO.BCM)   #定义树莓派gpio引脚以BCM方式编号
    GPIO.setup(pwm_pin1,GPIO.OUT)  #使能gpio口为输出
    pwm1 = GPIO.PWM(pwm_pin1,250)
    
    GPIO.setup(27,GPIO.OUT)
    GPIO.output(27,GPIO.LOW)
    GPIO.setup(26,GPIO.OUT)
    GPIO.output(26,GPIO.LOW)
    pwm0.start(50)
    pwm1.start(50)
    time.sleep(0.5)
    pwm0.stop()
    pwm1.stop()
    
    
    while True:
        GPIO.output(27,GPIO.HIGH)
        pwm0.start(50)
        time.sleep(0.5)
        pwm0.stop()
        GPIO.output(26,GPIO.HIGH)
        pwm1.start(50)
        time.sleep(0.5)
        pwm1.stop()
    
        GPIO.output(27,GPIO.LOW)
        pwm0.start(50)
        time.sleep(0.5)
        pwm0.stop()
    
        GPIO.output(26,GPIO.LOW)
        pwm1.start(50)
        time.sleep(0.5)
        pwm1.stop()
        time.sleep(0.1)
 

