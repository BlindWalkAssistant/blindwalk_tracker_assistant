# def estimate_distance(box_height):

#     # Approximate parameters
#     focal_length = 700
#     real_object_height = 1.7   # meters (approx human height)

#     if box_height == 0:
#         return 0

#     distance = (real_object_height * focal_length) / box_height

#     return distance

def estimate_distance(box_height, label):

    focal_length = 700

    # Real object heights in meters
    REAL_HEIGHTS = {
        "Animal": 1.0,
        "Crosswalk": 0.01,
        "Obstacle": 0.5,
        "Over-bridge": 5.0,
        "Person": 1.7,
        "Pole": 3.0,
        "Pothole": 0.1,
        "Railway": 0.2,
        "Road-barrier": 1.0,
        "Sidewalk": 0.15,
        "Stairs": 0.2,
        "Traffic-light": 0.8,
        "Traffic-sign": 0.7,
        "Train": 4.0,
        "Tree": 5.0,
        "Vehicle": 1.5
    }

    # Default height if label not found
    real_object_height = REAL_HEIGHTS.get(label, 0.5)

    if box_height == 0:
        return 0

    distance = (real_object_height * focal_length) / box_height

    return round(distance, 2)