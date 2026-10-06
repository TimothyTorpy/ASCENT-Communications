

US_Standard_Atmosphere_1976 = {
    "Zone 0" : (0.00, 288.15, 1.000, -6.50),
    "Zone 1" : (11.00,216.65,0.220, 0.00),
    "Zone 2": (20.00,216.65,0.050,1.00),
    "Zone 3":(32.00,228.65,0.010,2.80),
    "Zone 4":(47.00,270.65,0.00,0.00),
    "Zone 5":(51.00,270.65,0.00,-2.80),
    "Zone 6":(71.00,214.65,0.00,-2.00),
    "Zone 7":(84.85,186.95,0.00,0.00)
}

def GeopotentialAltitudeHeight(Re:float,z:float):
    h = (Re*z) / (Re + z)
    return h

if __name__ == "__main__":
    earth = 6371000
    height = 40000
    print(GeopotentialAltitudeHeight(earth,height))