import math
# Zenith is height / elevation of the device from gps
# GPS will give Long and Latt, Need to figure out Angle of the Dangle Next
# Once we have a Heading (360 deg) then we calcualte the Angle (Use SIN, COS, DEG ??)
# Putput Rotations. 

# Research 
# https://www.igismap.com/formula-to-find-bearing-or-heading-angle-between-two-points-latitude-longitude/
# https://www.igismap.com/haversine-formula-calculate-geographic-distance-earth/
def Haversine(GS_Latitude:float , GS_longitude:float,ASCENT_latitude:float,ASCENT_Longitude:float):
    """Calculate the distance between two locations using GPS values

    Args:
        GS_Latitude (float): the latitude of the ground station in degrees
        ASCENT_Latitude (float): the latitude of the ASCENT Balloon in degrees
        GS_Longitude (float): the longitude of ground station in degrees
        ASCENT_Longitude (float): the longitude of ASCENT balloon in degrees

    Returns:
        float: The distance between two locations

    Raises:
        No error raised
    """
    
    MeanRadiusEarth = 6371.009
    Latitude_1_Radian = math.radians(GS_Latitude)
    Latitude_2_Radian = math.radians(ASCENT_latitude)
    Longitude_1_Radian = math.radians(GS_longitude)
    Longitude_2_Radian = math.radians(ASCENT_Longitude)
    deltaLatitude = math.sin((Latitude_2_Radian-Latitude_1_Radian)/2)**2
    deltaLongitude = math.sin((Longitude_2_Radian - Longitude_1_Radian)/2)**2
    distance = 2 *math.asin(math.sqrt(deltaLatitude + deltaLongitude *math.cos(Latitude_1_Radian)*math.cos(Latitude_2_Radian)))*MeanRadiusEarth
    return distance


def BearingCalculator(GS_latitude :float , GS_longitude :float , ASCENT_latitude :float , ASCENT_longitude:float):
    
    """Calculate the bearing between two points, the ground station and the balloon. 

    Args:
        GS_Latitude (float): the latitude of the ground station in degrees
        ASCENT_Latitude (float): the latitude of the ASCENT Balloon in degrees
        GS_Longitude (float): the longitude of ground station in degrees
        ASCENT_Longitude (float): the longitude of ASCENT balloon in degrees

    Returns:
        float: The bearing between two locations.

    Raises:
        No error raised
    """
    latitude_A_radian = math.radians(GS_latitude)
    longitude_A_radian = math.radians(GS_longitude)
    latitude_B_radian = math.radians(ASCENT_latitude)
    longitude_B_radian = math.radians(ASCENT_longitude)
    deltaLongitudeRadian = math.radians(ASCENT_longitude - GS_longitude)
    bearing_X = math.cos(latitude_B_radian)*math.sin(deltaLongitudeRadian)
    bearing_Y = math.cos(latitude_A_radian) * math.sin(latitude_B_radian) - math.sin(latitude_A_radian) * math.cos(latitude_B_radian) * math.cos(deltaLongitudeRadian)
    bearing = math.atan2(bearing_X,bearing_Y)
    bearing = math.degrees(bearing)
    return bearing

def AngleToASCENT(distance :float , gps_height:float , GS_height:float):
    """Calculate the angle from the ground station to the height of the balloon. 

    Args:
        distance (float): the distance between the ground station and the hab. 
        gps_height (float): the height reported from the hab, 
        GS_height (float): elevation of the ground station, as height is assumed be to be from sea level

    Returns:
        float: the angle that is between the two locations for pointing.

    Raises:
        No error raised
    """
    height = gps_height - GS_height
    a = height
    b = distance
    c = math.sqrt((a * a) + (b * b) )
    arcsin = math.asin(a/c)
    return math.degrees(arcsin)


if __name__ == "__main__":

    EdsonLatitude = 53.586580
    EdsonLongitude = -116.425632
    EdmontonLatitude = 53.547972
    EdmontonLongitude = -113.486861
    KansasCityLatitude = 39.099912
    KansasCityLongitude = -94.581213
    StLouisLatitude = 38.627089
    StLouisLongitude = -90.200203
    print(AngleToASCENT(63.25,50,0))