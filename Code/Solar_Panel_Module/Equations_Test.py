import Solar_Equations
from math import degrees
equations = Solar_Equations.Solar_Equations()

latitude = 52.937609
longitude = -1.122017

hours = 0
minutes = 0
current_time_minutes = hours * 60 + minutes

#solar_hour_angle = equations.solar_hour_angle(current_time_minutes,longitude)
for i in range(0,24):
    current_time_minutes = i * 60 + minutes
    elevation = equations.get_solar_elevation(latitude,longitude,current_time_minutes)

    azimuth_angle = equations.get_solar_azimuth(latitude,longitude,current_time_minutes)

    azimuth_angle = degrees(azimuth_angle)

    azimuth_angle = azimuth_angle - 90 #reduce range to 0-180


    azimuth_angle = 180 - azimuth_angle #reverse so 0 is 180 - makes servo move clockwise

