from src.utils import OBJECT_HEIGHTS, FOCAL_LENGTH, MAX_DISTANCE

def estimate_distance(efficient_size, object_name):

    # Approximate parameters
    focal_length = FOCAL_LENGTH
    
    # Handle potentially lowercase labels from models
    normalized_name = object_name
    real_object_height = OBJECT_HEIGHTS.get(normalized_name)
    
    if real_object_height is None:
        return None
    
    try:
        # Convert box_height to float if it's a tensor or numpy array
        efficient_size = float(efficient_size)
    except (TypeError, ValueError):
        return None
    
    if efficient_size <= 0:
        return 0
    
    if efficient_size < 20: # Minimal detectable box height to avoid noise
        return None

    distance = (real_object_height * focal_length) / efficient_size
    if distance > MAX_DISTANCE:
        return None
    
    return round(float(distance), 2)


def smooth_distance(track_id, new_distance, history, alpha=0.3):
    if new_distance is None:
        return history.get(track_id)

    prev = history.get(track_id, new_distance)
    smoothed = alpha * new_distance + (1 - alpha) * prev
    history[track_id] = smoothed
    return round(smoothed, 2)