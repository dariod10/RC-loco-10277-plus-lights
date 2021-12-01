# RC-loco-10277-plus-lights
This is Pybricks code for Powered UP train HUB
Recomended source for better speed control: krork_ml_post.py

Designed for LEGO 10277, but applicable to any other locomotive using LEGO Powered Up-kontrola brzine rel. %

HUB PORT B for LEDs          
Idea:
 The lighting circuit is presented to the HUB as a DCmotor (not as a Light) because it gives the possibility of changing the polarity.
Mode of operation:
 By changing the direction of movement, the color of lights also change.
 In the direction of travel forward, they always glow white, and behind red.
 The lights in the wagon are always on, regardless of the direction of travel.
 Remote controller A-for speed/direction; B-ligts on/off
