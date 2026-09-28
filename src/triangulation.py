import math
# Zenith is height / elevation of the device from gps
# GPS will give Long and Latt, Need to figure out Angle of the Dangle Next
# Once we have a Heading (360 deg) then we calcualte the Angle (Use SIN, COS, DEG ??)
# Putput Rotations. 

# Research 
# https://www.igismap.com/formula-to-find-bearing-or-heading-angle-between-two-points-latitude-longitude/
# https://www.igismap.com/haversine-formula-calculate-geographic-distance-earth/
def Haversine(GS_Latitude:float , ASCENT_Latitude:float,GS_Longitude:float,ASCENT_Longitude:float):
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
    Latitude_2_Radian = math.radians(ASCENT_Latitude)
    Longitude_1_Radian = math.radians(GS_Longitude)
    Longitude_2_Radian = math.radians(ASCENT_Longitude)
    deltaLatitude = math.sin((Latitude_2_Radian-Latitude_1_Radian)/2)**2
    deltaLongitude = math.sin((Longitude_2_Radian - Longitude_1_Radian)/2)**2
    distance = 2 *math.asin(math.sqrt(deltaLatitude + deltaLongitude *math.cos(Latitude_1_Radian)*math.cos(Latitude_2_Radian)))*MeanRadiusEarth
    return distance


def BearingCalculator(latitude_A :float , Longitude_a :float , Latitude_b :float , longitude_b:float):
    latitude_A_radian = math.radians(latitude_A)
    longitude_A_radian = math.radians(Longitude_a)
    latitude_B_radian = math.radians(Latitude_b)
    longitude_B_radian = math.radians(longitude_b)
    deltaLongitudeRadian = math.radians(longitude_b - Longitude_a)
    bearing_X = math.cos(latitude_B_radian)*math.sin(deltaLongitudeRadian)
    bearing_Y = math.cos(latitude_A_radian) * math.sin(latitude_B_radian) - math.sin(latitude_A_radian) * math.cos(latitude_B_radian) * math.cos(deltaLongitudeRadian)
    bearing = math.atan2(bearing_X,bearing_Y)
    bearing = math.degrees(bearing)
    return bearing

if __name__ == "__main__":
    print(math.sin(90))
    print(math.pi/2)
    print(math.sin(math.pi/2))
    EdsonLatitude = 53.586580
    EdsonLongitude = -116.425632
    EdmontonLatitude = 53.547972
    EdmontonLongitude = -113.486861
    KansasCityLatitude = 39.099912
    KansasCityLongitude = -94.581213
    StLouisLatitude = 38.627089
    StLouisLongitude = -90.200203
    # print(Haversine(EdsonLatitude,EdmontonLatitude,EdsonLongitude,EdmontonLongitude))
    # print(BearingCalculator(EdsonLatitude,EdmontonLatitude,EdsonLongitude,EdmontonLongitude))
    print(BearingCalculator(KansasCityLatitude,KansasCityLongitude,StLouisLatitude,StLouisLongitude))