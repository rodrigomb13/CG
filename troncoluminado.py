from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from math import *
import math 
import sys



rotaçao = 2
N_lados = 5


def figure():
    altura = 3
    angulo = (2*math.pi)/N_lados
    raioBase = 2
    raioTampa = 1
    verticeBase = []
    verticesTampa = []

    glPushMatrix()
    glRotatef(-110,1.0,0.0,0.0)
    

    glBegin(GL_POLYGON)
    for i in range(0,N_lados):
        x = raioBase * math.cos(i*angulo) - rotaçao
        y = raioBase * math.sin(i*angulo) - rotaçao
        verticeBase += [ (x,y) ]
        glVertex3f(x,y,0.0)
    glEnd()

   
    glBegin(GL_POLYGON)
    for i in range(0,N_lados):
        x = raioTampa * math.cos(i*angulo) - rotaçao
        y = raioTampa * math.sin(i*angulo) - rotaçao
        verticesTampa += [ (x,y) ]
        glVertex3f(x,y,altura)
    glEnd()


    
    glBegin(GL_QUADS)
    for i in range(0,N_lados):
        glNormal3fv(calculaNormalFace( (verticeBase[i][0],verticeBase[i][1],0.0), (-rotaçao,-rotaçao,altura), (verticeBase[(i+1)%N_lados][0],verticeBase[(i+1)%N_lados][1],0.0)))
        glVertex3f(verticeBase[i][0],verticeBase[i][1],0.0)
        glVertex3f(verticesTampa[i][0],verticesTampa[i][1],altura)
        glVertex3f(verticesTampa[(i+1)%N_lados][0],verticesTampa[(i+1)%N_lados][1],altura)
        glVertex3f(verticeBase[(i+1)%N_lados][0],verticeBase[(i+1)%N_lados][1],0.0)
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
    glutCreateWindow("Tronco Iluminado")
    glutReshapeFunc(reshape)
    glutDisplayFunc(display)
    glutTimerFunc(50,timer,1)
    init()
    glutMainLoop()

main()