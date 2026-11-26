#para ejecutar se usa pgzrun intro.py
WIDTH = 400
HEIGHT = 400

alien = Actor('uzitransparent2')
alien.pos = WIDTH // 2, HEIGHT // 2

def draw():
    screen.fill((80, 0, 70))
    alien.draw()