Basic pong game written with pygame.

WS keys control the left paddle; up and down arrows control the right paddle.

The motivation of this game was to experiment with python and the pygame library. The goal of the architecure that I have implemented so far is to keep the game logic (the sprites, the controls, the movement of the paddles and the behaviour of the ball) separate from the pygame library itself.

With the two decoupled, one can take this game and replace pygame with another library with minimal rework. This is the rationale behind using a dictionary to map pygame's key codes to some custom key codes, as well as the avoidance of directly inheriting from pygame's Sprite class.