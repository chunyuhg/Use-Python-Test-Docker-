
#!C:/Python27/python

import numpy as np
import cgi, cgitb
import colorsys as cs
import random
import polar_diagram as svg

#color0~256

browser=1

reg=dict();
cgitb.enable()
form = cgi.FieldStorage()


#========================================
#Take the digital to present in RGB
#value: A digital in tuple
#_min: the minimum value in tuple
#_max: the macimum value in tuple
#========================================
color_ref={}
def color(value,_min,_max):
    
    _range=np.linspace(_min,_max,10000)
   
    p={}
    temp=0
    #hsv seperate 1000 parts,hue=0~256 degree(red~blue),saturation and bright are set 100%
    for hue in np.linspace(0.7,0,10000):
        _range[temp]=("%.3f" %_range[temp])
        color_ref[_range[temp]]=cs.hsv_to_rgb(hue,1.,1.)
   #present in hex      
        for i in range(3):
            p[i]=hex(int(color_ref[_range[temp]][i]*255.))[2:]
            if  len(p[i]) == 1:
                p[i]='0'+p[i]
        color_ref[_range[temp]]=p[0]+p[1]+p[2]   
                
        temp=temp+1
        
    return color_ref[value]
        
           
   


if form.getvalue('x1'):
        browser=0
        #x1v=form.getvalue('x1');

else:
    #p1=[0.81,0.85,0.96,2.,1.13,1.41,1.21,1.29,1.,1.36,1.57,1.77,1.79,1.88,1.46,1.78,1.46]
    
    p1=[round(random.uniform(0,2),2) for _ in range (17)]
    for r in range(17):
        reg[r]=color(p1[r],min(p1),max(p1))


if browser:    
    svg.open_website(reg,round(max(p1),2),round(min(p1),2));
   
    

    




