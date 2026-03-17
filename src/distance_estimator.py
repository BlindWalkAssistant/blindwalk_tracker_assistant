def estimate_distance(box_height):

    if box_height > 350:
        return "very close"

    elif box_height > 200:
        return "near"

    elif box_height > 120:
        return "far"

    else:
        return "very far"