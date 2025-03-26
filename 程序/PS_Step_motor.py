import smbus
import time

from time import sleep
import RPi.GPIO as GPIO
num0=0
num1=0
num2=0
if __name__=="__main__":
    address=0x48
    controlbit0=0x40
    controlbit1=0x41
    controlbit2=0x42
    bus=smbus.SMBus(1)
    bus.write_byte(address,controlbit0)
    
    
    pwm_pin0 = 17             #定义pwm输出引脚
    GPIO.setmode(GPIO.BCM)   #定义树莓派gpio引脚以BCM方式编号
    GPIO.setup(pwm_pin0,GPIO.OUT)  #使能gpio口为输出
    pwm0 = GPIO.PWM(pwm_pin0,500)
    
    pwm_pin1 = 18         #定义pwm输出引脚
    GPIO.setmode(GPIO.BCM)   #定义树莓派gpio引脚以BCM方式编号
    GPIO.setup(pwm_pin1,GPIO.OUT)  #使能gpio口为输出
    pwm1 = GPIO.PWM(pwm_pin1,320)
    
    GPIO.setup(27,GPIO.OUT)
    GPIO.output(27,GPIO.LOW)
    GPIO.setup(26,GPIO.OUT)
    GPIO.output(26,GPIO.LOW)
    while True:
        
        bus.write_byte(address,controlbit0)
        bus.read_byte(address)
        num0=bus.read_byte(address)
        print(f"x=%d"%num0)
        
        bus.write_byte(address,controlbit1)
        bus.read_byte(address)
        num1=bus.read_byte(address)
        print(f"y=%d"%num1)
        
        bus.write_byte(address,controlbit2)
        bus.read_byte(address)
        num2=bus.read_byte(address)
        print(f"S=%d"%num2)
        if(num0>200):
            print("Left")
            pwm0.start(50)
            GPIO.output(27,GPIO.LOW)
        elif(num0<50):
            print("Right") 
            pwm0.start(50)
            GPIO.output(27,GPIO.HIGH)
        else:
            pwm0.stop()
            
        if(num1>200):
            print("UP")
            pwm1.start(50)
            GPIO.output(26,GPIO.LOW)
        elif(num1<50):
            print("Down")
            pwm1.start(50)
            GPIO.output(26,GPIO.HIGH)
        else:
            pwm1.stop()
            
        time.sleep(0.1)
 
