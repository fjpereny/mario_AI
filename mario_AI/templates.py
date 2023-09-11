
TEMPLATES = {
        # Mario 
        "mario-small":  {
            "file": "assets/templates/mario-small.png",
            "height": 50,
            "width": 40,
            "offset_x": -5,
            "offset_y": -20,
            "type": "mario",
            "color": (255, 0, 0),
            "priority": 1,
            "method": "max",
            "thresh": 0.8,
        },
        
        "mario-big":  {
            "file": "assets/templates/mario-big.png",
            "height": 100,
            "width": 40,
            "offset_x": -5,
            "offset_y": -20,
            "type": "mario",
            "color": (255, 0, 0),
            "priority": 1,
            "method": "max",
            "thresh": 0.7,
        },

        # Powerups
        "mushroom":  {
            "file": "assets/templates/mushroom.png",
            "height": 50,
            "width": 40,
            "offset_x": -5,
            "offset_y": -20,
            "type": "powerup",
            "color": (0, 255, 0),
            "priority": 5,
            "method": "max",
            "thresh": None,
        },

        # Enemies
        "goomba_1": {
            "file": "assets/templates/goomba_1.png",
            "width": 45,
            "height": 45,
            "offset_x": -15,
            "offset_y": -15,
            "type": "enemy",
            "color": (0, 0, 255),
            "priority": 1,
            "method": "all_max",
            "thresh": 0.75,
        },
        
        "turtle_green_1": {
            "file": "assets/templates/turtle_green_1.png",
            "width": 45,
            "height": 45,
            "offset_x": -15,
            "offset_y": -15,
            "type": "enemy",
            "color": (0, 0, 255),
            "priority": 1,
            "method": "all_max",
            "thresh": 0.75,
        },

        # Environmental Blocks
        "bricks_1":  {
            "file": "assets/templates/bricks_1.png",
            "width": 55,
            "height": 50,
            "offset_x": 0,
            "offset_y": 0,
            "type": "block",
            "color": (255, 0, 255),
            "priority": 5,
            "method": "all_max",
            "thresh": 0.9,
        },

        "question_block_1":  {
            "file": "assets/templates/question_block_1.png",
            "width": 55,
            "height": 50,
            "offset_x": -5,
            "offset_y": -5,
            "type": "block",
            "color": (255, 0, 255),
            "priority": 5,
            "method": "all_max",
            "thresh": 0.9,
        },

        "question_block_2":  {
            "file": "assets/templates/question_block_2.png",
            "width": 55,
            "height": 50,
            "offset_x": -5,
            "offset_y": -5,
            "type": "block",
            "color": (255, 0, 255),
            "priority": 5,
            "method": "all_max",
            "thresh": 0.9,
        },

         "question_block_3":  {
            "file": "assets/templates/question_block_3.png",
            "width": 55,
            "height": 50,
            "offset_x": 0,
            "offset_y": 0,
            "type": "block",
            "color": (255, 0, 255),
            "priority": 5,
            "method": "all_max",
            "thresh": 0.9,
        },

       "bricks_1":  {
            "file": "assets/templates/bricks_1.png",
            "width": 55,
            "height": 50,
            "offset_x": -5,
            "offset_y": -5,
            "type": "block",
            "color": (255, 0, 255),
            "priority": 5,
            "method": "all_max",
            "thresh": 0.9,
        },

       # Pipes
       "pipe_green_flange":  {
            "file": "assets/templates/pipe_green_flange.png",
            "width": 110,
            "height": 50,
            "offset_x": -5,
            "offset_y": -5,
            "type": "pipe",
            "color": (255, 0, 0),
            "priority": 5,
            "method": "all_max",
            "thresh": 0.8,
        },

       "pipe_green_1":  {
            "file": "assets/templates/pipe_green_1.png",
            "width": 120,
            "height": 50,
            "offset_x": -5,
            "offset_y": -5,
            "type": "pipe",
            "color": (255, 0, 0),
            "priority": 5,
            "method": "all_max",
            "thresh": 0.8,
        },
    } 


def template_color(template: dict):
    return template["color"]
