# RC-loco-10277-plus-lights
This is Pybricks code for Powered UP train HUB 
Designed for LEGO 10277, but applicable to any other locomotive using LEGO Powered Up-kontrola brzine rel. %
 **********Not for beginners**********
HUB PORT B for LEDs

1 o-------o--------------------------o--------------------------
          |                          | 
2 o----------------------------o----------o-----------------------
          |                    |     |   _|_   
3 o----   |  LOCO front lights |     |  / ~ \               WAGON
      |   |        LED white   |     ---| ~ |            2xLED white
4 o-  |   |        ---|>|---   |        | G |   ---Res----|>|--|>|---        
   |  |   o--Res---|       |---o        | + |---|                   |---- 
5 o-  |   |        ---|<|---   |        \_-_/   ---Res----|>|--|>|---   |
      |   |         LED red    |          |              2xLED white    | 
6 o----   |                    |          -------------------------------
          |        LED white   |
          |        ---|>|---   |
          o--Res---|       |---o
          |        ---|<|---   |
          |         LED red    |
          |.  .  .  .  .  .  . |
          .  LOCO back lights  .                   .
          .same as front lights.                  . 
          .                    .
 1-6 - HUB port pins
 Res - resistor, the values ​​depend on the characteristics of the LED
 G - 4 diode bridge (Greatz)
 LED - SMD
Wiring:
 LOCO front/back lights - 2 pairs of white/red LEDs (in parallel oposite directions). One pair in each front/back light
 WAGON - 2 white LEDs in serial per WAGON
 -------------
 |  O     O  |
 | w/r   w/r |
 -------------           
Idea:
 The lighting circuit is presented to the HUB as a DCmotor (not as a Light) because it gives the possibility of changing the polarity.
Mode of operation:
 By changing the direction of movement, the color of lights also change.
 In the direction of travel forward, they always glow white, and behind red.
 The lights in the wagon are always on, regardless of the direction of travel.
 Remote controller A-for speed/direction; B-ligts on/off
