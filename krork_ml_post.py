#Designed for LEGO 10277, but applicable to any other locomotive using LEGO Powered Up-kontrola brzine rel. %
# **********Not for beginners**********
#HUB PORT B for LEDs
#
#1 o-------o--------------------------o--------------------------
#          |                          | 
#2 o----------------------------o----------o-----------------------
#          |                    |     |   _|_   
#3 o----   |  LOCO front lights |     |  / ~ \               WAGON
#      |   |        LED white   |     ---| ~ |            2xLED white
#4 o-  |   |        ---|>|---   |        | G |   ---Res----|>|--|>|---        
#   |  |   o--Res---|       |---o        | + |---|                   |---- 
#5 o-  |   |        ---|<|---   |        \_-_/   ---Res----|>|--|>|---   |
#      |   |         LED red    |          |              2xLED white    | 
#6 o----   |                    |          -------------------------------
#          |        LED white   |
#          |        ---|>|---   |
#          o--Res---|       |---o
#          |        ---|<|---   |
#          |         LED red    |
#          |.  .  .  .  .  .  . |
#          .  LOCO back lights  .                   .
#          .same as front lights.                  . 
#          .                    .
# 1-6 - HUB port pins
# Res - resistor, the values ​​depend on the characteristics of the LED
# G - 4 diode bridge (Greatz)
# LED - SMD
#Wiring:
# LOCO front/back lights - 2 pairs of white/red LEDs (in parallel oposite directions). One pair in each front/back light
# WAGON - 2 white LEDs in serial per WAGON
# -------------
# |  O     O  |
# | w/r   w/r |
# -------------           
#Idea:
# The lighting circuit is presented to the HUB as a DCmotor (not as a Light) because it gives the possibility of changing the polarity.
#Mode of operation:
# By changing the direction of movement, the color of lights also change.
# In the direction of travel forward, they always glow white, and behind red.
# The lights in the wagon are always on, regardless of the direction of travel.
# Remote controller A-for speed/direction; B-ligts on/off
#
#Make sure to connect the motor to port A and LEDs to port B after uploading
from pybricks.pupdevices import *
from pybricks.parameters import *
from pybricks.tools import wait
Motor1 = Motor(Port.A)
LEDset1 = DCMotor(Port.B)
remoteControl = Remote()
speed = 0
light = 0
dlight = False
maxSpeed = 10 #max speed = 100%
firstLoop = 1

#main loop
while True:
	#update pressed buttons information
	pressed = remoteControl.buttons.pressed()
	
	#Make sure that lastPressed is initialized
	#(lastPressed is used to not increase val while button is hold)
	if firstLoop == 1:
		lastPressed = pressed
		firstLoop = 0

	#increase/decrease speed variable between -10 and 10
	if Button.LEFT_PLUS in pressed and not (Button.LEFT_PLUS in lastPressed):
		if speed < maxSpeed:
			speed = speed + 1

	if Button.LEFT_MINUS in pressed and not (Button.LEFT_MINUS in lastPressed):
		if speed > -maxSpeed:
			speed = speed - 1

	#emergency stop
	if Button.LEFT in pressed:
		speed = 0
		
	#Light mod fw-bw-stop 
	if speed > 0:
		light = 70
	elif speed < 0:
		light = -70
	else:
		light = 20

	#Light on-off
	if Button.RIGHT_PLUS in pressed:
		dlight = True
	
	if Button.RIGHT_MINUS in pressed:
		dlight = False
	
	#make the LED on-off
	if dlight:
		LEDset1.dc(light)
	else:
		LEDset1.stop()
		
	#make the motor move with the % speed (speed val * 10 = %)
	Motor1.dc(speed*10)
	lastPressed = pressed
	wait(100)

