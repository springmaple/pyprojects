import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from functools import partial


def cube():
    glBegin(GL_LINE_STRIP)

    # calculate all points
    points = []
    for x in range(8):
        points.append(((x & 4) >> 2, (x & 2) >> 1, x & 1))

    # traverse path
    paths = (0, 1, 3, 2, 0, 4, 6, 7, 3, 2, 6, 4, 5, 7, 5, 1)

    for pt_idx in paths:
        glVertex3fv(points[pt_idx])

    glEnd()


def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    pygame.key.set_repeat(20, 20)

    gluPerspective(90, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5.0)

    fns = {
        pygame.K_UP: partial(glTranslatef, 0.0, 0.0, -0.1),
        pygame.K_DOWN: partial(glTranslatef, 0.0, 0.0, 0.1),
        pygame.K_LEFT: partial(glRotatef, 1.0, 1.0, 1.0, 1.0),
        pygame.K_RIGHT: partial(glRotatef, -1.0, 1.0, 1.0, 1.0),
    }

    while True:
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        cube()
        pygame.display.flip()

        event = pygame.event.wait()
        if event.type == pygame.KEYDOWN:
            try:
                fns[event.key]()
            except KeyError:
                continue
        elif event.type == pygame.QUIT:
            pygame.quit()
            quit()


if __name__ == '__main__':
    main()
