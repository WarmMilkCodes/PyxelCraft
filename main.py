import pyglet
from pyglet.gl import *
from engine.world import World
from pyglet.gl import gluLookAt

win = pyglet.window.Window(800, 600, "Voxel Engine")
world = World()

chunk_position = [0, 0, 0]
camera_position = [CHUNK_SIZE / 2, CHUNK_SIZE / 2, -CHUNK_SIZE * 1.5]

def draw_voxel(x, y, z, color=(1, 1, 1) size=1):
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

    glColor3f(*color)
    
    # Front face
    glVertex3f(vertices[0], vertices[1], vertices[2])
    glVertex3f(vertices[3], vertices[4], vertices[5])
    glVertex3f(vertices[7], vertices[8], vertices[9])
    glVertex3f(vertices[6], vertices[7], vertices[8])
    # ... Do this for all 6 faces

def draw_chuk(chunk, start_x=0, start_y=0, start_z=0):
    for x in range(CHUNK_SIZE):
        for y in range(CHUNK_SIZE):
            for z in range(CHUNK_SIZE):
                voxel = chunk.voxels[x][y][z]
                if voxel is not None:
                    draw_voxel(x + start_x, y + start_y, z + start_z, color=voxel)

@win.event
def on_draw():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glEnable(GL_DEPTH_TEST)

    # Setup rudimentary camera
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60, win.width/win.height, 0.1, 1000)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(*camera_position, CHUNK_SIZE/2, CHUNK_SIZE/2, CHUNK_SIZE/2, 0, 1, 0)

    draw_chunk(world.get_chunk(0, 0, 0), *chunk_position)
    draw_voxel(0, 0, 0)

@win.event
def on_key_press(symbol, modifiers):
    step = 1
    if symbol == pyglet.window.key.RIGHT:
        chunk_position[0] += step
    elif symbol == pyglet.window.key.LEFT:
        chunk_position[0] -= step
    elif symbol == pyglet.window.key.UP:
        chunk_position[1] += step
    elif symbol == pyglet.window.key.DOWN:
        chunk_position[1] -= step
