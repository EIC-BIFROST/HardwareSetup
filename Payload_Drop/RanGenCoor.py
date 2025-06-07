import numpy as np
import random
from shapely.geometry import Polygon, Point


#Defining the randomization generator
def polygon_random_points (poly):
    min_x, min_y, max_x, max_y = poly.bounds
    points = []
    while len(points) < 1:
        random_point = Point([random.uniform(min_x, max_x), random.uniform(min_y, max_y)])
        if (random_point.within(poly)):
            points.append(random_point)
            return points# Choose the number of points desired. This example uses 20 points. 
        
def main(runway, quadrant):
    # Define the boundary
    AirDropArea = {
        'R1Q1': [(38.3154965, -76.5508375), (38.31564275, -76.551695), (38.315751, -76.5516595), (38.315607, -76.550800)],
        'R1Q2': [(38.315386, -76.550875), (38.3155345, -76.5517305), (38.31564275, -76.551695), (38.3154965, -76.5508375)],
        'R1Q3': [(38.3155345, -76.5517305), (38.315683, -76.552586), (38.315789, -76.5525525), (38.31564275, -76.551695)],
        'R1Q4': [(38.31564275, -76.551695), (38.315789, -76.5525525), (38.315895, -76.552519), (38.315751, -76.5516595)],
        'R2Q1': [(38.3143345, -76.5441185), (38.31448225, -76.5444972), (38.314586, -76.54449365), (38.314441, -76.5444081)],
        'R2Q2': [(38.314228, -76.5444156), (38.3143785, -76.54450075), (38.31448225, -76.5444972), (38.3143345, -76.54441185)],
        'R2Q3': [(38.3143758, -76.54450075), (38.314529, -76.5445859), (38.314630, -76.54458255), (38.31448225, -76.5444972)],
        'R2Q4': [(38.31448225, -76.5444972), (38.314630, -76.54458255), (38.314731, -76.5445792), (38.314586, -76.54449365)],
    }

    # Define the Quadiant
    poly = Polygon(AirDropArea['R' + str(runway) + 'Q' + str(quadrant)])
    points = polygon_random_points(poly)# Printing the results.
    for p in points:
        return round(p.x, 6), round(p.y, 6)

