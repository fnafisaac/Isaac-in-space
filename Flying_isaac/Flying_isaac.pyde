a=0
bg=0
bg2=0
c=0
d=0
people=0
e=0
f=0
g=0
h=0
j=0
k=0
x=260
y=400
x2=0
y2=0
x3=260
y3=400
y4 = 0
x4=0
vertical=0
game = 0
def setup():
    global people, bg, barrier , y,bg2, game
    size(800,800)
    url = " "
    people = loadImage(url, "png")
    url2= "https://cdn.dribbble.com/users/2208405/screenshots/10344568/media/c8d261e7fbe2739731b99a731801d90a.png"
    bg= loadImage(url2, "png")
    bg2= loadImage(url2, "png")
    url3= "https://avatars.mds.yandex.net/i?id=04639948aaa9f9361c2f05de22ef05dd-5139473-images-thumbs&n=13"
    barrier = loadImage(url3,"png")
def draw():
    global x, y, bg, vertical, barrier,people, x2, x3, y3, game
    if game == 0:
        imageMode(CENTER)
        background(0)
        image(bg,x2,0)
        image(bg2,x2+bg.width, 0)
        image(people, width/2, y, 90,30)
        rect(x3,y3-(barrier.height/2+200),50,400)
        rect(x3,y3+(barrier.height/2+200),50,400)
        #image(barrier,x3,y3-(barrier.height/2+100),200,400)
        #image(barrier,x3,y3+(barrier.height/2+100),200,400)
        if x3<0:
            y3 = random(200,height-200)
            x3 = width
        if x3  == width/2:
            pass
        if (y + height or y < 0 or abs(width/2-x3)<50) and (abs(y-y3)>200 ):
            game = 1
            print('game')
        x3 -= 6
        vertical += 1
        y += vertical
        x2 -= 1 
        if x2 == -2*bg.width:
            x2 = 0
    else:
        background(0)
def keyPressed():
    global x,vertical
    if key == ' ':
        vertical = -15
def mousePressed():
    global game, x , score
    y = height/2
    vertical = -15
    #game, x , score = 0,0,0
