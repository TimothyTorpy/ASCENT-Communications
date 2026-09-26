import math
# Zenith is height / elevation of the device from gps
# GPS will give Long and Latt, Need to figure out Angle of the Dangle Next
# Once we have a Heading (360 deg) then we calcualte the Angle (Use SIN, COS, DEG ??)
# Putput Rotations. 

# Research 
# https://www.igismap.com/formula-to-find-bearing-or-heading-angle-between-two-points-latitude-longitude/
# https://www.igismap.com/haversine-formula-calculate-geographic-distance-earth/
def Haversine(latitude_1:float , latitude_2:float,longitude_1:float,longitude_2:float):
    """Calculate the distance between two locations using GPS values

    Args:
        latitude_1 (float): the latitude of first location in degrees
        latitude_2 (float): the latitude of second location in degrees
        longitude_1 (float): the longitude of first location in degrees
        longitude_2 (float): the longitude of second location in degrees

    Returns:
        float: The distance between two locations

    Raises:
        No error raised
    """
    
    MeanRadiusEarth = 6371.009
    Latitude_1_Radian = math.radians(latitude_1)
    Latitude_2_Radian = math.radians(latitude_2)
    Longitude_1_Radian = math.radians(longitude_1)
    Longitude_2_Radian = math.radians(longitude_2)
    deltaLatitude = math.sin((Latitude_2_Radian-Latitude_1_Radian)/2)**2
    deltaLongitude = math.sin((Longitude_2_Radian - Longitude_1_Radian)/2)**2
    distance = 2 *math.asin(math.sqrt(deltaLatitude + deltaLongitude *math.cos(Latitude_1_Radian)*math.cos(Latitude_2_Radian)))*MeanRadiusEarth
    return distance



if __name__ == "__main__":
    print(math.sin(90))
    print(math.pi/2)
    print(math.sin(math.pi/2))
    EdsonLatitude = 53.586580
    EdsonLongitude = -116.425632
    EdmontonLatitude = 53.547972
    EdmontonLongitude = -113.486861
    print(Haversine(EdsonLatitude,EdmontonLatitude,EdsonLongitude,EdmontonLongitude))