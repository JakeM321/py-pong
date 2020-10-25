class Colours:
    background = (0,0,0)
    primary = (255,255,255)

class GameConfig:
    colours = Colours()
    sWidth = 1280
    sHeight = 720
    dimensions = (1280, 720)
    caption = 'Pong'

    controls = {
        'KEY_w': 'left_up',
        'KEY_s': 'left_down',
        'KEY_UP': 'right_up',
        'KEY_DOWN': 'right_down'
    }

gameConfig = GameConfig()