class Colours:
    background = (0,0,0)
    primary = (255,255,255)

class GameConfig:
    colours = Colours()
    dimensions = (1920, 1080)
    caption = 'Pong'

    controls = {
        repr(['KEY_w']): 'left_up',
        repr(['KEY_s']): 'left_down',
        repr(['KEY_up']): 'right_up',
        repr(['KEY_down']): 'right_down'
    }