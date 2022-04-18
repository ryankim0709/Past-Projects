from dis import dis
import math

vehical = input()
ramp = float(input())
accelearation = float(input())
width = float(input())

time = math.sqrt((2 * ramp)/accelearation)
speed = (time * accelearation)
speed = round(speed, 2)
distance = ((speed) ** 2/9.805)
distance = round(distance, 2)

message = ""
if distance < width - 5:
    message = "SPLASH!"
elif distance >= width - 5 and distance <= width:
    message = "BARELY MADE IT!"
else:
    message = "LIKE A BOSS!"
print(vehical+" will reach a speed of "+str(speed)+" m/s on a "+str(ramp)+" meter ramp, crossing "+ str(distance)+" of "+str(width)+" meteres, "+str(message))