class Colours:
    background = (0,0,0)
    primary = (255,255,255)

class GameConfig:
    colours = Colours()
    sWidth = 1920
    sHeight = 1080
    dimensions = (1920, 1080)
    caption = 'Pong'

    controls = {
        'KEY_w': 'left_up',
        'KEY_s': 'left_down',
        'KEY_UP': 'right_up',
        'KEY_DOWN': 'right_down'
    }