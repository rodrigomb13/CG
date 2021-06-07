from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from math import *
import math
import sys


rotaçao = 2

def figure():
    raio = 2
    N = 6
    H = 3
    pontosBase = []
    pontosTampa = []
    angulo = (2*math.pi)/N

    glPushMatrix()
    glRotatef(-110,1.0,0.0,0.0)

    # BASE
    glBegin(GL_POLYGON)
    for i in range(0,N):
        x = raio * math.cos(i*angulo) -rotaçao
        y = raio * math.sin(i*angulo) -rotaçao
        pontosBase += [(x,y)]
        glVertex3f(x,y,0.0)
    glEnd()

    #TAMPA
    glBegin(GL_POLYGON)
    for i in range(0,N):
        w = raio * math.cos(i*angulo) -rotaçao
        z = raio * math.sin(i*angulo) -rotaçao
        pontosTampa += [(w,z)]
        glVertex3f(w,z,H)
    glEnd()

    # LATERAL
    glBegin(GL_QUADS)
    for i in range(0,N):
        glNormal3fv(calculaNormalFace( (pontosBase[i][0],pontosBase[i][1],0.0), (-rotaçao,-rotaçao,H), (pontosBase[(i+1)%N][0],pontosBase[(i+1)%N][1],0.0)))
        glVertex3f(pontosBase[i][0],pontosBase[i][1],0.0)
        glVertex3f(pontosBase[(i+1)%N][0],pontosBase[(i+1)%N][1],0.0)
        glVertex3f(pontosTampa[(i+1)%N][0],pontosTampa[(i+1)%N][1],H)
        glVertex3f(pontosTampa[i][0],pontosTampa[i][1],H)
    glEnd()

    glPopMatrix()

def calculaNormalFace(a1, a2, a3):
    x = 0
    y = 1
    z = 2
    v0 = a1
    v1 = a2
    v2 = a3
    U = ( v2[x]-v0[x], v2[y]-v0[y], v2[z]-v0[z] )
    V = ( v1[x]-v0[x], v1[y]-v0[y], v1[z]-v0[z] )
    N = ( (U[y]*V[z]-U[z]*V[y]),(U[z]*V[x]-U[x]*V[z]),(U[x]*V[y]-U[y]*V[x]))
    NLength = sqrt(N[x]*N[x]+N[y]*N[y]+N[z]*N[z])
    return ( N[x]/NLength, N[y]/NLength, N[z]/NLength)

def display():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glRotatef(2,1,3,0)
    figure()
    glutSwapBuffers()

def timer(i):
    glutPostRedisplay()
    glutTimerFunc(50,timer,1)

def reshape(w,h):
    glViewport(0,0,w,h)
    glMatrixMode(GL_PROJECTION)
    gluPerspective(45,float(w)/float(h),0.1,50.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt( 10,0,0, 0,0,0,0,1,0 )

def init():
    mat_ambient = (0.0, 0.4, 0.0, 1.0)
    mat_diffuse = (0.0, 1.0, 0.0, 1.0)
    mat_specular = (1.0, 0.5, 0.5, 1.0)
    mat_shininess = (50,)
    light_position = (10,0,0)
    glClearColor(0.0,0.0,0.0,0.0)
    #glShadeModel(GL_FLAT)
    glShadeModel(GL_SMOOTH)

    glMaterialfv(GL_FRONT, GL_AMBIENT, mat_ambient)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, mat_diffuse)
    glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular)
    glMaterialfv(GL_FRONT, GL_SHININESS, mat_shininess)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glLightfv(GL_LIGHT0, GL_POSITION, light_position)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_MULTISAMPLE)

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
    glutInitWindowSize(800,600)
    glutCreateWindow("Prisma Iluminado")
    glutReshapeFunc(reshape)
    glutDisplayFunc(display)
    glutTimerFunc(50,timer,1)
    init()
    glutMainLoop()

main()