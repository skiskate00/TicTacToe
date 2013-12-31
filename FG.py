# coding: utf-8
def fgfd(length):
    fred.forward(length)
    george.forward(length)
    
def fgclear():
    fred.clear()
    george.clear()
    
def fgr():
    fred.reset()
    george.reset()
    main()
    
def fgleft(angle):
    fred.left(angle)
    george.left(angle)
    
def fgsq(length):
    fgfd(length)
    fgleft(90)
    fgfd(length)
    fgleft(90)
    fgfd(length)
    fgleft(90)
    fgfd(length)
    fgleft(90)
    
def fc(newcolor):
    fred.color(newcolor)
    
def gc(newcolor):
    george.color(newcolor)
    
def fgmv(x,y):
    fred.up()
    fred.fd(x)
    fred.left(90)
    fred.fd(y)
    fred.left(-90)
    george.up()
    george.fd(x)
    george.left(90)
    george.fd(y)
    george.left(-90)
    george.down()
    fred.down()
    
def main():
    fred.color("green")
    george.color("purple")
    fred.shape("turtle")
    george.shape("turtle")
    fred.up()
    george.up()
    fred.goto(20,20)
    george.goto(0,0)
    fred.down()
    george.down()
    drawgrid()
    
def fgup(x,y):
    fred.up()
    george.up()
    fred.fd(x)
    george.fd(x)
    fred.left(90)
    george.left(90)
    fred.fd(x)
    george.fd(x)
    fred.right(90)
    george.right(90)
    fred.down()
    george.down()
    
def drawgrid():
    fred.color("green")
    fred.shape("turtle")
    fred.pensize(5)
    fred.up()
    fred.goto(0,50)
    fred.down()
    fred.goto(0,-50)
    fred.goto(100,-50)
    fred.goto(-200,-50)
    fred.goto(-100,-50)
    fred.goto(-100,50)
    fred.goto(-100,-250)
    fred.goto(-100,-150)
    fred.goto(-200,-150)
    fred.goto(-100,-150)
    fred.goto(100,-150)
    fred.goto(00,-150)
    fred.goto(00,-50)
    fred.goto(00,-250)         

def makeX(x,y):
    fred.up()
    fred.goto(x,y)
    fred.down()
    fred.left(45)
    fred.fd(35)
    fred.fd(-35)
    fred.fd(35)
    fred.right
    
def fredgoinvis(x,y):
    fred.up()
    fred.goto(x,y)
    fred.down()
    
def drawxo(letter,cellx,celly):
    if cellx==1:
        xpos=-150
    elif cellx==2:
        xpos=-50
    elif cellx==3:
        xpos=50
    if celly==1:
        ypos=-50
    elif celly==2:
        ypos=-150
    elif celly==3:
        ypos=-250    
    george.up()
    george.goto(xpos,ypos)
    george.down()
    george.write(letter, move = False, align='center', font=('Gill Sans', 60, 'normal'))
    
if __name__ == "__main__":
    import turtle
    s=turtle.Screen()
    s.clearscreen()
    fred = turtle.Turtle()
    george = turtle.Turtle()
    main()
    
