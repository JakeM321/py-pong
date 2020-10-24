class Colours:
    background = (0,0,0)
    primary = (255,255,255)

class GameConfig:
    colours = Colours()
    dimensions = (1920, 1080)
    caption = 'Pong'

    controls = {
        'KEY_w': 'left_up',
        'KEY_s': 'left_down',
        'KEY_up': 'right_up',
        'KEY_down': 'right_down'
    }