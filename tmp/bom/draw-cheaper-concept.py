from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
import math

root=Path('/home/hans/repos/fries-machine')
im=Image.new('RGB',(1600,1200),'#FAF9F5')
d=ImageDraw.Draw(im)
fontpath='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
boldpath='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
def f(n,b=False): return ImageFont.truetype(boldpath if b else fontpath,n)
ink='#263D46'; muted='#546A70'; blue='#31768E'; orange='#BE652B'; green='#39775C'
def txt(x,y,s,n=22,b=False,color=ink): d.text((x,y),s,font=f(n,b),fill=color)
def arrow(p,q,color=blue,width=4):
    d.line([p,q],fill=color,width=width)
    a=math.atan2(q[1]-p[1],q[0]-p[0]); L=14
    d.polygon([q,(q[0]-L*math.cos(a-.4),q[1]-L*math.sin(a-.4)),(q[0]-L*math.cos(a+.4),q[1]-L*math.sin(a+.4))],fill=color)
def box(x,y,w,h,label,color='#E5ECEB'):
    d.rounded_rectangle((x,y,x+w,y+h),radius=9,fill=color,outline=ink,width=2)
    txt(x+12,y+15,label,20,True)
def funnel(x,y,w=120):
    d.polygon([(x,y),(x+w,y),(x+w*.65,y+65),(x+w*.35,y+65)],fill='#DDE5E5',outline=ink,width=3)
    d.rectangle((x+w*.35,y+65,x+w*.65,y+90),fill='#DDE5E5',outline=ink,width=2)

txt(45,25,'A simpler layout for the same automatic functions',34,True)
txt(45,75,'Proposed changes to the supplied drawing. Concept sketch; not a measured fabrication plan.',22,color=muted)
for x in [40,820]: d.rounded_rectangle((x,120,x+740,390),radius=15,fill='white',outline='#CCD6D5',width=2)
txt(60,140,'1  Layout shown in the PDF',25,True)
box(70,205,185,105,'Fryer + basket')
box(510,205,180,105,'Funnel + bag')
arrow((270,255),(490,255),orange)
txt(280,290,'Long transfer gap',20,color=orange)
txt(70,340,'Extra basket travel is not shown in the drawing.',21,color=muted)
txt(840,140,'2  Bring the receiving funnel closer',25,True)
box(850,205,200,105,'Fryer + basket')
funnel(1160,215,125)
arrow((1065,245),(1145,245),green)
txt(1060,280,'Short chute',19,color=green)
box(1335,205,175,105,'Flavor coils')
txt(850,340,'Keep the funnel on the right; shorten the path.',21,color=muted)

txt(45,430,'One-motor option: a guide turns the basket near the top',28,True)
txt(45,476,'Use only if the mechanical team can build and verify the hinged basket and captive guide.',21,color=muted)

for index,(x,title,py,angle) in enumerate([(45,'3  Cook',902,0),(575,'4  Lift and drain',782,0),(1105,'5  Lift farther and tip',744,120)]):
    d.rounded_rectangle((x,525,x+475,1120),radius=12,fill='white',outline='#CCD6D5',width=2)
    txt(x+15,543,title,25,True)
    # Tank, oil, support rail and chain; schematic positions only.
    d.rectangle((x+75,880,x+295,1050),fill='#E6ECEE',outline=ink,width=3)
    d.rectangle((x+80,915,x+290,1044),fill='#EDCB81')
    txt(x+120,1005,'Oil tank',20)
    d.line((x+35,620,x+35,1055),fill=muted,width=7)
    d.line((x+55,638,x+55,1026),fill=blue,width=4)
    d.ellipse((x+43,1018,x+68,1043),fill=blue)
    d.line((x+35,py,x+280,py),fill=muted,width=3)
    # Basket pivot is at its right rim; clockwise tip faces the opening toward the chute.
    pivot=(x+280,py)
    points=[(-130,0),(0,0),(0,65),(-130,65)]
    a=math.radians(angle)
    out=[(pivot[0]+u*math.cos(a)-v*math.sin(a),pivot[1]+u*math.sin(a)+v*math.cos(a)) for u,v in points]
    d.polygon(out,fill='#DCE8ED',outline=blue,width=3)
    for v in [18,35,52]:
        p=(pivot[0]-130*math.cos(a)-v*math.sin(a),pivot[1]-130*math.sin(a)+v*math.cos(a))
        q=(pivot[0]-v*math.sin(a),pivot[1]+v*math.cos(a))
        d.line([p,q],fill='#94B7C4',width=1)
    d.ellipse((pivot[0]-6,pivot[1]-6,pivot[0]+6,pivot[1]+6),fill=orange)
    funnel(x+325,897,125)
    d.rectangle((x+360,1006,x+417,1070),fill='#E6C99C',outline=ink,width=2)
    txt(x+365,1077,'Bag',18)
    if index==0:
        txt(x+105,793,'Basket stays upright',19)
        arrow((x+195,825),(x+195,881),orange)
        txt(x+15,1095,'Manual cut; automatic timer',18,color=muted)
    elif index==1:
        arrow((x+55,861),(x+55,786),green)
        txt(x+95,720,'Pause above the tank',19)
        for dx in [165,195,225]: arrow((x+dx,855),(x+dx,890),orange,2)
        txt(x+15,1095,'Oil drains back into the fryer',18,color=muted)
    else:
        d.line([(x+330,709),(x+306,734),(x+299,770)],fill=orange,width=6)
        txt(x+16,810,'Fixed guide causes tipping',18,color=orange)
        for yy in [806,834,863]: d.rounded_rectangle((x+365,yy,x+380,yy+6),radius=2,fill='#D6A13C')
        arrow((x+383,809),(x+383,880),green,3)
        txt(x+15,1095,'Fries fall through a short chute',18,color=muted)

txt(45,1144,'The chain lifts a guided support, not a freely swinging basket. Retention, clearances and drain/dump angles need cold testing.',19,color=muted)
im.save(root/'docs/CHEAPER_DESIGN_CONCEPT.png')
print('Saved concept diagram.')
