WIDTH = 900
HEIGHT = 900

alien = Actor('uzitransparent2')
alien.pos = 200, 200

def draw():
    screen.fill((80, 0, 70))
    alien.draw()