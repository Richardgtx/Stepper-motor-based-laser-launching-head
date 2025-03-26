## 基于步进电机的激光发射云台

### 功能介绍
该实验实现了一个搭载激光发射器的二维云台。它可以再远处的平面上投射激光点，并让它沿着任意形状的轨迹运动。
该装置还可以用PS2手柄控制。通过操纵PS2手柄，云台旋转，从而移动激光点。



用PS2手柄控制云台


https://github.com/user-attachments/assets/a274436a-5fd7-49aa-9e58-cdd8887e6abd




https://github.com/user-attachments/assets/ce1925e6-3b8f-45af-ad2d-09f7bb95453c




https://github.com/user-attachments/assets/baa4d4b5-eef2-4a94-9551-da5e8171f5bd

#### 实验原理
该系统由树莓派作为主控制器。PS2手柄作为输入设备。树莓派处理PS2手柄传递过来的信息，给电机驱动器发送指令，然后电机驱动器驱动步进电机运动。


![image](https://github.com/user-attachments/assets/5e958776-3143-4d71-9405-1a9611fc5ddb)


硬件接线图


![image](https://github.com/user-attachments/assets/7cbc00f3-7a22-4371-9c77-1418b397516d)


树莓派输出pwm波给驱动器，控制电机旋转。输出高低电平给驱动器DIR端口控制电机转向。pwm的脉冲数和步进电机旋转的角度线性相关。


$$ \theta=\frac{pulse*2\pi}{6400} $$


从下图可以估计电机的运动范围。在这里将电机的运动估计为匀速运动。
要在距离1m的地方沿着黑框运动。需要把x,y方向电机运动的范围转化为脉冲数。在程序中输出固定的pwm波脉冲数。


![image](https://github.com/user-attachments/assets/c6ed4c35-c5f1-42c5-bcae-f37f3cb6fd43)

