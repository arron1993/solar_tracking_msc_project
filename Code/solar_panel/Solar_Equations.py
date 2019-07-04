from datetime import datetime
from math import pi, sin, cos, degrees, radians, asin, tan, acos

class Solar_Equations:
    def longitude_time_correction(self,longitude):
        longitude_std_meridian = 0
        correction = 4 * (longitude_std_meridian - longitude)
        return correction


    def analemma_time_correction(self):
        day_of_year = datetime.now().timetuple().tm_yday
        B = (day_of_year - 1) * (360/365) * (180/pi)
        B=radians(B)

        p1 = radians(229.2) * 0.0000075
        p2 = radians(229.2) * ((0.0001868 * cos(B)) - (0.32077 * sin(B)))
        p3 = radians(-229.2) * (0.014615 * cos(2*B))
        p4 = 0.04089 * sin(2*B)

        return(p1 + p2 - p3 + p4)


    def time_correction(self,longitude):
        time_correction = self.longitude_time_correction(longitude) - self.analemma_time_correction()
        return time_correction


    def get_time(self,DST):
        current_time = datetime.now()
        hour_to_minutes = (float(current_time.hour) * 60)
        seconds_to_minutes = float(current_time.second) / 60
        current_time_minutes = hour_to_minutes + float(current_time.minute) + seconds_to_minutes

        if DST:
            current_time_minutes = current_time_minutes + 60
        return current_time_minutes

    def solar_time(self,current_time_minutes,longitude):
        solar_time = current_time_minutes - self.time_correction(longitude)
        return solar_time / 60  #convert to seconds


    def solar_hour_angle(self,current_time,longitude):
        solar_time = self.solar_time(current_time,longitude)
        solar_hour_angle = 15 * (solar_time - 12)
        return radians(solar_hour_angle)


    def solar_declination(self):
        day_of_year = datetime.now().timetuple().tm_yday
        sin_coef = radians(23.45)

        solar_declination = sin_coef * sin( radians((360/365) * (284 + day_of_year)))

        return(solar_declination)

    def get_solar_elevation(self,lat,lng,current_time):

        latitude = radians(lat)
        longitude = radians(lng)
        declination = self.solar_declination()
        hour_angle = self.solar_hour_angle(current_time,longitude)

        p1 = sin(latitude) * sin(declination)
        p2 = cos(latitude) * cos(declination) * cos(hour_angle)
        altitude = p1 + p2
        elevation = degrees((asin(altitude)))
        print("INFO: Solar Elevation {}".format(elevation))
        return elevation


    def get_solar_azimuth(self,latitude,longitude,current_time_minutes):
        
        
        elevation = radians(self.get_solar_elevation(latitude,longitude,current_time_minutes))

        solar_declination = self.solar_declination()

        solar_zenith = 90 - degrees(elevation)

        solar_zenith = radians(solar_zenith)

        hour_angle = self.solar_hour_angle(current_time_minutes,longitude)
        latitude = radians(latitude)

        azimuth_top_1 = sin(solar_declination) * cos(latitude)
        azimuth_top_2 = cos(hour_angle) * cos(solar_declination) * sin(latitude)
        azimuth_top = azimuth_top_1 -azimuth_top_2
        azimuth_bottom = sin(solar_zenith)

        solar_azimuth = azimuth_top / azimuth_bottom
        solar_azimuth = acos(solar_azimuth)

        if(hour_angle > 0):
            solar_azimuth = radians(180) + (radians(180) - solar_azimuth)   
     
        print("INFO: Time {}, Solar Azimuth {}".format(current_time_minutes,degrees(solar_azimuth)))


        azimuth_angle = solar_azimuth
        azimuth_angle = degrees(azimuth_angle)

        azimuth_angle = azimuth_angle - 90 #reduce range to 0-180
        print("INFO: Time {}, Adjusted Solar Azimuth {}".format(current_time_minutes,azimuth_angle))
        #azimuth_angle = 180 - azimuth_angle #reverse so 0 is 180 - makes servo move clockwise


        return azimuth_angle
