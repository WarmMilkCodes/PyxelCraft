import pyglet
from pyglet.gl import *
from engine.world import World

win = pyglet.window.Window(800, 600, "Voxel Engine")
world = World()

def draw_voxel(x, y, z, size=1):
    vertices = [
        x, y, z,
        x + size, y, z,
        x + size, y + size, z,
        x, y + size, z,
        x, y, z + size,
        x + size, y, z + size,
        x + size, y + size, z + size,
        x, y + size, z + size
    ]

    glColor3f(1, 0, 0)  # Red color for now
    
    # Front face
    glVertex3f(vertices[0], vertices[1], vertices[2])
    glVertex3f(vertices[3], vertices[4], vertices[5])
    glVertex3f(vertices[7], vertices[8], vertices[9])
    glVertex3f(vertices[6], vertices[7], vertices[8])
    # ... Do this for all 6 faces

@win.event
def on_draw():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glEnable(GL_DEPTH_TEST)
    
    draw_voxel(0, 0, 0)
