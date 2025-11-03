import math
from scipy.optimize import fsolve
import numpy

#"The Deeping Wall has a height of 6.1 m."
wall_height = 6.1 #meters

#"If Legolas is 2 m tall and shoots his bow from shoulder height (assume the shoulders are ⅘ of the body’s height)""
LegoLas_Height = 2.0 #meters
Shoulder_Height = (4/5) * LegoLas_Height 

#"the Bow of the Galadhrim fires its arrows at an initial velocity of 89.4 m/s"
init_v_arrow = 89.4 #m/s

arrow_shot_height = Shoulder_Height + wall_height

print(arrow_shot_height)

#Assume a neck height of 1.9 m from the ground
deadguysneckheight = 1.9 #meters

total_displacement = arrow_shot_height - deadguysneckheight

print(total_displacement)
#it states the son of whoeverthefrick is standing on top of the base and the base to the guy he wants to shoot is 360 meters sooooooooo ya
frombasetodeadguy = 360 #meters
total_displacement = arrow_shot_height - deadguysneckheight
gravity = 9.81

#define time 

def thesuperspecialfunction(theta):
    #define time in python terms
    t = frombasetodeadguy/(init_v_arrow*numpy.cos(theta))
    #now define the whole equation in python
    return total_displacement + (init_v_arrow*numpy.sin(theta)) * t - 1/2 * gravity * t ** 2

final_answer = fsolve(thesuperspecialfunction, 0)
print(f'LegoLas must fire his arrow at {numpy.degrees(final_answer)} degrees to hit the Uruk Hai')