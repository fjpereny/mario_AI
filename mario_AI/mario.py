
import mss

import cv2
import numpy as np
import pyautogui

from templates import TEMPLATES, template_color
from match_temp import find_max_template


class MarioAI:
    frame = 0
    img = np.zeros(1) 
    img_gray = np.zeros(1) 

    # Templates Priority 1 through 5
    templates_p1 = {} 
    templates_p2 = {} 
    templates_p3 = {} 
    templates_p4 = {} 
    templates_p5 = {} 

    mario_facing_right = True
    mario_position = None
    mario_big = False

    def __init__(self):
        print("Iniitializing Super Mario Bros. AI")
        print("Loading templates...")
        template_count = 0
        for t in TEMPLATES:
            print(f"Loading {t}...")
            template_count += 1
            if TEMPLATES[t]["priority"] == 1:
                self.templates_p1[t] = TEMPLATES[t] 
                self.templates_p1[t]["img"] = cv2.imread(TEMPLATES[t]["file"], cv2.IMREAD_GRAYSCALE)
            if TEMPLATES[t]["priority"] == 2:
                self.templates_p2[t] = TEMPLATES[t] 
                self.templates_p2[t]["img"] = cv2.imread(TEMPLATES[t]["file"], cv2.IMREAD_GRAYSCALE)
            if TEMPLATES[t]["priority"] == 3:
                self.templates_p3[t] = TEMPLATES[t] 
                self.templates_p3[t]["img"] = cv2.imread(TEMPLATES[t]["file"], cv2.IMREAD_GRAYSCALE)
            if TEMPLATES[t]["priority"] == 4:
                self.templates_p4[t] = TEMPLATES[t] 
                self.templates_p4[t]["img"] = cv2.imread(TEMPLATES[t]["file"], cv2.IMREAD_GRAYSCALE)
            if TEMPLATES[t]["priority"] == 5:
                self.templates_p5[t] = TEMPLATES[t] 
                self.templates_p5[t]["img"] = cv2.imread(TEMPLATES[t]["file"], cv2.IMREAD_GRAYSCALE)
        print(f"Total templates found: {template_count}")

    
    def set_screen_corners(self, top: int, left: int, width: int, height: int):
        self.top = top
        self.left = left
        self.width = width
        self.height = height


    def start_screen_capture(self):
        
        with mss.mss() as sct:
            self.frame = 0
            while True:
                self.img = sct.grab({"top": self.top, "left": self.left, "width": self.width, "height": self.height}) 
                self.img = np.array(self.img, dtype=np.uint8)
                self.img_gray = cv2.cvtColor(self.img, cv2.COLOR_BGRA2GRAY)

                self.find_templates()
                # if self.mario_position:
                #     self.img = cv2.circle(self.img, (self.mario_position[0] + 10, self.mario_position[1] + 20), 30, (255, 0, 0), 3, 2) 
                #     self.img = cv2.putText(self.img, "Mario (Small)", (self.mario_position[0] + 45, self.mario_position[1] + 25), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)

                cv2.imshow("Preview", self.img)
                key = cv2.waitKey(1)
                if key == ord('q'):
                    print("Stopping MarioAI...")
                    break
                elif key == ord('a'): # Left Arrow
                    self.mario_facing_right = False
                elif key == ord('d'): # Right Arrow
                    self.mario_facing_right = True

                self.frame += 1
                if self.frame == 100_000:
                    self.frame = 0

    
    def find_templates(self):
        if self.frame % 1 == 0:
            for t in self.templates_p1:
                template = self.templates_p1[t]

                flip_x = False
                if template["type"] == "mario" and not self.mario_facing_right:
                    flip_x = True
                
                    if not self.frame % 10 == 0:
                        if self.mario_big and t == "mario-small":
                            continue
                        if not self.mario_big and t == "mario-big":
                            continue
                    else:
                        self.mario_big = False

                result = find_max_template(self.img_gray, template, thresh=template["thresh"], flip_x=flip_x)
                result_flip = None
                if template["type"] in ["enemy"]:
                    result_flip = find_max_template(self.img_gray, template, thresh=template["thresh"], flip_x=True)

                if result:
                    if result_flip:
                        if result_flip["match_val"] > result["match_val"]:
                            result = result_flip
                    if t == "mario-big" and result["match_val"] >= template["thresh"]:
                        self.mario_big = True

                    color = template_color(template)
                    self.img = cv2.rectangle(
                            self.img, 
                            (result["loc"][0] + template["offset_y"], result["loc"][1] + template["offset_x"]),
                            (result["loc"][0] + result["width"], result["loc"][1] + result["height"]),
                            color,
                            5, 
                            2
                        ) 
                    loc = result["loc"]
                    # print(f"{t}: {loc}")
            

        if self.frame % 5 == 0:
            for t in self.templates_p5:
                template = self.templates_p5[t]
                result = find_max_template(self.img_gray, template)
                if result:
                    color = template_color(template)
                    self.img = cv2.rectangle(
                            self.img, 
                            (result["loc"][0] + template["offset_y"], result["loc"][1] + template["offset_x"]),
                            (result["loc"][0] + result["width"], result["loc"][1] + result["height"]),
                            color,
                            5, 
                            2
                        ) 


    def move_right(self):
        self.mario_facing_right = True
        self.is_moving = True
        pyautogui.keyDown("right") 

    def stop_moving(self):
        self.is_moving = False
        pyautogui.keyUp("right")
        pyautogui.keyUp("left")
