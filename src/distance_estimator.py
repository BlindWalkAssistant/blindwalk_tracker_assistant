def estimate_distance(box_height):

    # Approximate parameters
    focal_length = 700
    real_object_height = 1.7   # meters (approx human height)

    if box_height == 0:
        return 0

    distance = (real_object_height * focal_length) / box_height

    return distance