import unittest
import sys
from pathlib import Path


sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from Triangulation import Haversine
from Triangulation import AngleToASCENT

import math

class TriangulationTest(unittest.TestCase):
    GroundStationLatitude = 53.547972 # Edmonton
    GroundStationLongitude = -113.486861 #Edmonton

    destinations = {
        "North": (54.322033 ,-113.229154 , 87.71),
        "East" : (53.428371 ,-112.552217, 63.250),
        "South": (51.790510,-114.203479,201.30),
        "West": (53.586580,-116.425632,194.10)
    }
    
    # Distance, gps_height ,gs_height,test_angle
    test_angles = {
        "Test1": (87.71 , 30 , 10, 12.845),
        "test2": (63.25 , 50 , 20 , 25.375),
        "test3":(201.30,90,0,24.089),
        "test4":(194.10,80,-20,27.257)
    }
    
    
         
    def test_distance(self):

        for direction,(latitude,longitude,expected_km) in self.destinations.items():
            with self.subTest(direction = direction):
                actual_km = Haversine(
                    self.GroundStationLatitude,
                    self.GroundStationLongitude,
                    latitude,
                    longitude
                )
                self.assertAlmostEqual(actual_km,expected_km,places =2)
    def test_Angles(self):    
        for test , (balloon_distance, balloon_height,gs_height, expected_angle) in self.test_angles.items():
            with self.subTest(test = test) :
                angle = AngleToASCENT(balloon_distance,balloon_height,gs_height)
                self.assertAlmostEqual(angle , expected_angle,3) 
                     
        
if __name__ == "__main__":
    unittest.main()