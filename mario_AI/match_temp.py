
import cv2
import numpy as np


def find_max_template(screen: np.ndarray, template: dict, thresh: float = 0.95, flip_x: bool = False):

    if flip_x:
        img = np.fliplr(template["img"])
    else:
        img = template["img"]
        
    match = cv2.matchTemplate(screen, img, cv2.TM_CCOEFF_NORMED)
    _, max_val, _, max_loc = cv2.minMaxLoc(match)

    result = None
    
    if max_val >= thresh:
        result = {}
        result["found"] = True
        result["match_val"] = max_val
        result["loc"] = max_loc
        result["width"] = template["width"]    
        result["height"] = template["height"]    
    return result
