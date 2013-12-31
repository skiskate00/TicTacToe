# coding: utf-8

def main():
    s=turtle.Screen()
    s.clearscreen()
    global fred
    global george
    fred = turtle.Turtle()
    george = turtle.Turtle()
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
    global xturn
    xturn = True
    s.onclick(handleclick)
    
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
    
def handleclick(x,y):
    cellx=0
    celly=0
    global xturn
    if (x > -200) & (x < -100):
        cellx=1
    elif (x > -100) & (x < 0):
        cellx=2
    elif (x > 0) & (x < 100):
        cellx=3
    if (y>-50) & (y<50):
        celly=1
    elif (y>-150) & (y<-50):
        celly=2
    elif (y>-250) & (y<-150):
        celly=3
    if (x > -200) & (x < 100) & (y > -250) & (y < 50):
        if xturn == True:
            drawxo('X',cellx,celly)
            xturn = False
        else:
            drawxo('O',cellx,celly)
            xturn = True    
    
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
    main()
    
