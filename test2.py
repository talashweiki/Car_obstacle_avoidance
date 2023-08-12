from gpiozero import DistanceSensor
from time import sleep
from gpiozero import Buzzer

ultrasonic = DistanceSensor(echo = 17 ,trigger = 4)
buzzer = Buzzer(2)


while True:
    print(ultrasonic.distance*100)
    if ultrasonic.distance*100<=10:
        buzzer.on()
    if ultrasonic.distance*100>=10:
        buzzer.off()
