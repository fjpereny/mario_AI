
from mario import MarioAI


if __name__ == '__main__':
    mario = MarioAI()
    mario.set_screen_corners(0, 1920-896, 896, 672)
    mario.start_screen_capture()
