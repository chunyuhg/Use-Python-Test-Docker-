
#!C:/Python27/python

import numpy as np
import cgi, cgitb
import colorsys as cs
import random


#color0~256

browser=1


cgitb.enable()
form = cgi.FieldStorage()
RGB={}
#========================================
#Take the digital to present in RGB
#value: A digital in tuple
#_min: the minimum value in tuple
#_max: the macimum value in tuple
#========================================
def color(value,_min,_max):
    
    _range=np.linspace(_min,_max,10000)
    color_ref={}
    p={}
    temp=0
    #hsv seperate 1000 parts,hue=0~216 degree(red~blue),saturation and bright are set 100%
    for hue in np.linspace(0.,0.6,10000):
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
        RGB[r]=color(p1[r],min(p1),max(p1))

print( RGB)

     



     
     
    
HTML= '''
<xml><?xml version="1.0" encoding="UTF-8" standalone="no"?>
<!-- Created with Inkscape (http://www.inkscape.org/) -->
<note>
  <body>Polar SVG illustration</body>
</note>
<svg
   xmlns:dc="http://purl.org/dc/elements/1.1/"
   xmlns:cc="http://creativecommons.org/ns#"
   xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
   xmlns:svg="http://www.w3.org/2000/svg"
   xmlns="http://www.w3.org/2000/svg"
   xmlns:xlink="http://www.w3.org/1999/xlink"
   xmlns:sodipodi="http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd"
   xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape"
   version="1.2"
   width="1488.189"
   height="2104.7244"
   id="svg2"
   inkscape:version="0.48.5 r10040"
   sodipodi:docname="circle8.svg">
  <sodipodi:namedview
     pagecolor="#ffffff"
     bordercolor="#666666"
     borderopacity="1"
     objecttolerance="10"
     gridtolerance="10"
     guidetolerance="10"
     inkscape:pageopacity="0"
     inkscape:pageshadow="2"
     inkscape:window-width="1920"
     inkscape:window-height="1005"
     id="namedview171"
     showgrid="false"
     inkscape:zoom="0.97035431"
     inkscape:cx="638.84491"
     inkscape:cy="1352.5032"
     inkscape:window-x="-9"
     inkscape:window-y="-9"
     inkscape:window-maximized="1"
     inkscape:current-layer="svg2" />
  <defs
     id="defs4">
    <inkscape:path-effect
       effect="skeletal"
       id="path-effect3337"
       is_visible="true"
       pattern="M 0,0 1,0"
       copytype="single_stretched"
       prop_scale="1"
       scale_y_rel="false"
       spacing="0"
       normal_offset="0"
       tang_offset="0"
       prop_units="false"
       vertical_pattern="false"
       fuse_tolerance="0" />
    <inkscape:path-effect
       effect="skeletal"
       id="path-effect3327"
       is_visible="true"
       pattern="M 0,0 1,0"
       copytype="single_stretched"
       prop_scale="1"
       scale_y_rel="false"
       spacing="0"
       normal_offset="0"
       tang_offset="0"
       prop_units="false"
       vertical_pattern="false"
       fuse_tolerance="0" />
    <linearGradient
       id="linearGradient7339">
      <stop
         id="stop7341"
         style="stop-color:#0f0002;stop-opacity:1"
         offset="0" />
    </linearGradient>
    <marker
       refX="0"
       refY="0"
       orient="auto"
       id="Arrow1Lend"
       style="overflow:visible">
      <path
         d="M 0,0 5,-5 -12.5,0 5,5 0,0 z"
         transform="matrix(-0.8,0,0,-0.8,-10,0)"
         id="path4696"
         style="fill-rule:evenodd;stroke:#000000;stroke-width:1pt"
         inkscape:connector-curvature="0" />
    </marker>
    <marker
       refX="0"
       refY="0"
       orient="auto"
       id="Arrow1Lstart"
       style="overflow:visible">
      <path
         d="M 0,0 5,-5 -12.5,0 5,5 0,0 z"
         transform="matrix(0.8,0,0,0.8,10,0)"
         id="path4693"
         style="fill-rule:evenodd;stroke:#000000;stroke-width:1pt"
         inkscape:connector-curvature="0" />
    </marker>
    <inkscape:path-effect
       effect="skeletal"
       id="path-effect4677"
       is_visible="true"
       pattern="M 0,0 1,0"
       copytype="single_stretched"
       prop_scale="1"
       scale_y_rel="false"
       spacing="0"
       normal_offset="0"
       tang_offset="0"
       prop_units="false"
       vertical_pattern="false"
       fuse_tolerance="0" />
    <inkscape:path-effect
       effect="skeletal"
       id="path-effect4673"
       is_visible="true"
       pattern="M 0,0 1,0"
       copytype="single_stretched"
       prop_scale="1"
       scale_y_rel="false"
       spacing="0"
       normal_offset="0"
       tang_offset="0"
       prop_units="false"
       vertical_pattern="false"
       fuse_tolerance="0" />
    <inkscape:path-effect
       effect="skeletal"
       id="path-effect4641"
       is_visible="true"
       pattern="M 0,0 1,0"
       copytype="single_stretched"
       prop_scale="1"
       scale_y_rel="false"
       spacing="0"
       normal_offset="0"
       tang_offset="0"
       prop_units="false"
       vertical_pattern="false"
       fuse_tolerance="0" />
    <inkscape:path-effect
       effect="skeletal"
       id="path-effect4631"
       is_visible="true"
       pattern="M 0,0 1,0"
       copytype="single_stretched"
       prop_scale="1"
       scale_y_rel="false"
       spacing="0"
       normal_offset="0"
       tang_offset="0"
       prop_units="false"
       vertical_pattern="false"
       fuse_tolerance="0" />
    <inkscape:path-effect
       effect="skeletal"
       id="path-effect4627"
       is_visible="true"
       pattern="M 0,0 1,0"
       copytype="single_stretched"
       prop_scale="1"
       scale_y_rel="false"
       spacing="0"
       normal_offset="0"
       tang_offset="0"
       prop_units="false"
       vertical_pattern="false"
       fuse_tolerance="0" />
    <inkscape:path-effect
       effect="skeletal"
       id="path-effect4623"
       is_visible="true"
       pattern="M 0,0 1,0"
       copytype="single_stretched"
       prop_scale="1"
       scale_y_rel="false"
       spacing="0"
       normal_offset="0"
       tang_offset="0"
       prop_units="false"
       vertical_pattern="false"
       fuse_tolerance="0" />
    <inkscape:path-effect
       effect="spiro"
       id="path-effect4621"
       is_visible="true" />
    <inkscape:path-effect
       effect="skeletal"
       id="path-effect4617"
       is_visible="true"
       pattern="M 0,0 1,0"
       copytype="single_stretched"
       prop_scale="1"
       scale_y_rel="false"
       spacing="0"
       normal_offset="0"
       tang_offset="0"
       prop_units="false"
       vertical_pattern="false"
       fuse_tolerance="0" />
    <inkscape:path-effect
       effect="spiro"
       id="path-effect4615"
       is_visible="true" />
    <inkscape:path-effect
       effect="skeletal"
       id="path-effect4611"
       is_visible="true"
       pattern="M 0,0 1,0"
       copytype="single_stretched"
       prop_scale="1"
       scale_y_rel="false"
       spacing="0"
       normal_offset="0"
       tang_offset="0"
       prop_units="false"
       vertical_pattern="false"
       fuse_tolerance="0" />
    <inkscape:path-effect
       effect="spiro"
       id="path-effect4609"
       is_visible="true" />
    <inkscape:path-effect
       effect="skeletal"
       id="path-effect4605"
       is_visible="true"
       pattern="M 0,0 1,0"
       copytype="single_stretched"
       prop_scale="1"
       scale_y_rel="false"
       spacing="0"
       normal_offset="0"
       tang_offset="0"
       prop_units="false"
       vertical_pattern="false"
       fuse_tolerance="0" />
    <inkscape:path-effect
       effect="spiro"
       id="path-effect4603"
       is_visible="true" />
    <inkscape:path-effect
       effect="skeletal"
       id="path-effect4599"
       is_visible="true"
       pattern="M 0,0 1,0"
       copytype="single_stretched"
       prop_scale="1"
       scale_y_rel="false"
       spacing="0"
       normal_offset="0"
       tang_offset="0"
       prop_units="false"
       vertical_pattern="false"
       fuse_tolerance="0" />
    <inkscape:path-effect
       effect="spiro"
       id="path-effect4597"
       is_visible="true" />
    <inkscape:path-effect
       effect="skeletal"
       id="path-effect4593"
       is_visible="true"
       pattern="M 0,0 1,0"
       copytype="single_stretched"
       prop_scale="1"
       scale_y_rel="false"
       spacing="0"
       normal_offset="0"
       tang_offset="0"
       prop_units="false"
       vertical_pattern="false"
       fuse_tolerance="0" />
    <inkscape:path-effect
       effect="spiro"
       id="path-effect4591"
       is_visible="true" />
    <inkscape:path-effect
       effect="skeletal"
       id="path-effect4587"
       is_visible="true"
       pattern="M 0,0 1,0"
       copytype="single_stretched"
       prop_scale="1"
       scale_y_rel="false"
       spacing="0"
       normal_offset="0"
       tang_offset="0"
       prop_units="false"
       vertical_pattern="false"
       fuse_tolerance="0" />
    <inkscape:path-effect
       effect="spiro"
       id="path-effect4585"
       is_visible="true" />
    <inkscape:path-effect
       effect="skeletal"
       id="path-effect4581"
       is_visible="true"
       pattern="M 0,0 1,0"
       copytype="single_stretched"
       prop_scale="1"
       scale_y_rel="false"
       spacing="0"
       normal_offset="0"
       tang_offset="0"
       prop_units="false"
       vertical_pattern="false"
       fuse_tolerance="0" />
    <inkscape:path-effect
       effect="spiro"
       id="path-effect4579"
       is_visible="true" />
    <inkscape:path-effect
       effect="skeletal"
       id="path-effect4575"
       is_visible="true"
       pattern="M 0,0 1,0"
       copytype="single_stretched"
       prop_scale="1"
       scale_y_rel="false"
       spacing="0"
       normal_offset="0"
       tang_offset="0"
       prop_units="false"
       vertical_pattern="false"
       fuse_tolerance="0" />
    <inkscape:path-effect
       effect="spiro"
       id="path-effect4573"
       is_visible="true" />
    <inkscape:path-effect
       effect="skeletal"
       id="path-effect4569"
       is_visible="true"
       pattern="M 0,0 1,0"
       copytype="single_stretched"
       prop_scale="1"
       scale_y_rel="false"
       spacing="0"
       normal_offset="0"
       tang_offset="0"
       prop_units="false"
       vertical_pattern="false"
       fuse_tolerance="0" />
    <inkscape:path-effect
       effect="spiro"
       id="path-effect4567"
       is_visible="true" />
    <inkscape:path-effect
       effect="skeletal"
       id="path-effect4563"
       is_visible="true"
       pattern="M 0,0 1,0"
       copytype="single_stretched"
       prop_scale="1"
       scale_y_rel="false"
       spacing="0"
       normal_offset="0"
       tang_offset="0"
       prop_units="false"
       vertical_pattern="false"
       fuse_tolerance="0" />
    <inkscape:path-effect
       effect="spiro"
       id="path-effect4561"
       is_visible="true" />
    <inkscape:path-effect
       effect="skeletal"
       id="path-effect4557"
       is_visible="true"
       pattern="M 0,0 1,0"
       copytype="single_stretched"
       prop_scale="1"
       scale_y_rel="false"
       spacing="0"
       normal_offset="0"
       tang_offset="0"
       prop_units="false"
       vertical_pattern="false"
       fuse_tolerance="0" />
    <inkscape:path-effect
       effect="spiro"
       id="path-effect4555"
       is_visible="true" />
    <inkscape:path-effect
       effect="skeletal"
       id="path-effect4551"
       is_visible="true"
       pattern="M 0,0 1,0"
       copytype="single_stretched"
       prop_scale="1"
       scale_y_rel="false"
       spacing="0"
       normal_offset="0"
       tang_offset="0"
       prop_units="false"
       vertical_pattern="false"
       fuse_tolerance="0" />
    <inkscape:path-effect
       effect="spiro"
       id="path-effect4549"
       is_visible="true" />
    <inkscape:path-effect
       effect="skeletal"
       id="path-effect4545"
       is_visible="true"
       pattern="M 0,0 1,0"
       copytype="single_stretched"
       prop_scale="1"
       scale_y_rel="false"
       spacing="0"
       normal_offset="0"
       tang_offset="0"
       prop_units="false"
       vertical_pattern="false"
       fuse_tolerance="0" />
    <inkscape:path-effect
       effect="spiro"
       id="path-effect4543"
       is_visible="true" />
    <inkscape:path-effect
       effect="skeletal"
       id="path-effect4539"
       is_visible="true"
       pattern="M 0,0 1,0"
       copytype="single_stretched"
       prop_scale="1"
       scale_y_rel="false"
       spacing="0"
       normal_offset="0"
       tang_offset="0"
       prop_units="false"
       vertical_pattern="false"
       fuse_tolerance="0" />
    <inkscape:path-effect
       effect="spiro"
       id="path-effect4537"
       is_visible="true" />
    <inkscape:path-effect
       effect="skeletal"
       id="path-effect4533"
       is_visible="true"
       pattern="M 0,0 1,0"
       copytype="single_stretched"
       prop_scale="1"
       scale_y_rel="false"
       spacing="0"
       normal_offset="0"
       tang_offset="0"
       prop_units="false"
       vertical_pattern="false"
       fuse_tolerance="0" />
    <inkscape:path-effect
       effect="spiro"
       id="path-effect4531"
       is_visible="true" />
    <inkscape:path-effect
       effect="skeletal"
       id="path-effect3907"
       is_visible="true"
       pattern="M 0,0 1,0"
       copytype="single_stretched"
       prop_scale="1"
       scale_y_rel="false"
       spacing="0"
       normal_offset="0"
       tang_offset="0"
       prop_units="false"
       vertical_pattern="false"
       fuse_tolerance="0" />
    <inkscape:path-effect
       effect="spiro"
       id="path-effect3905"
       is_visible="true" />
    <inkscape:path-effect
       effect="skeletal"
       id="path-effect3893"
       is_visible="true"
       pattern="M 0,0 1,0"
       copytype="single_stretched"
       prop_scale="1"
       scale_y_rel="false"
       spacing="0"
       normal_offset="0"
       tang_offset="0"
       prop_units="false"
       vertical_pattern="false"
       fuse_tolerance="0" />
    <inkscape:path-effect
       effect="spiro"
       id="path-effect3891"
       is_visible="true" />
    <inkscape:path-effect
       effect="skeletal"
       id="path-effect3887"
       is_visible="true"
       pattern="M 0,0 1,0"
       copytype="single_stretched"
       prop_scale="1"
       scale_y_rel="false"
       spacing="0"
       normal_offset="0"
       tang_offset="0"
       prop_units="false"
       vertical_pattern="false"
       fuse_tolerance="0" />
    <inkscape:path-effect
       effect="spiro"
       id="path-effect3885"
       is_visible="true" />
    <inkscape:path-effect
       effect="skeletal"
       id="path-effect3881"
       is_visible="true"
       pattern="M 0,0 1,0"
       copytype="single_stretched"
       prop_scale="1"
       scale_y_rel="false"
       spacing="0"
       normal_offset="0"
       tang_offset="0"
       prop_units="false"
       vertical_pattern="false"
       fuse_tolerance="0" />
    <inkscape:path-effect
       effect="spiro"
       id="path-effect3879"
       is_visible="true" />
    <inkscape:path-effect
       effect="skeletal"
       id="path-effect3875"
       is_visible="true"
       pattern="M 0,0 1,0"
       copytype="single_stretched"
       prop_scale="1"
       scale_y_rel="false"
       spacing="0"
       normal_offset="0"
       tang_offset="0"
       prop_units="false"
       vertical_pattern="false"
       fuse_tolerance="0" />
    <inkscape:path-effect
       effect="spiro"
       id="path-effect3873"
       is_visible="true" />
    <inkscape:path-effect
       effect="skeletal"
       id="path-effect3869"
       is_visible="true"
       pattern="M 0,0 1,0"
       copytype="single_stretched"
       prop_scale="1"
       scale_y_rel="false"
       spacing="0"
       normal_offset="0"
       tang_offset="0"
       prop_units="false"
       vertical_pattern="false"
       fuse_tolerance="0" />
    <inkscape:path-effect
       effect="skeletal"
       id="path-effect3865"
       is_visible="true"
       pattern="M 0,0 1,0"
       copytype="single_stretched"
       prop_scale="1"
       scale_y_rel="false"
       spacing="0"
       normal_offset="0"
       tang_offset="0"
       prop_units="false"
       vertical_pattern="false"
       fuse_tolerance="0" />
    <inkscape:path-effect
       effect="skeletal"
       id="path-effect3861"
       is_visible="true"
       pattern="M 0,0 1,0"
       copytype="single_stretched"
       prop_scale="1"
       scale_y_rel="false"
       spacing="0"
       normal_offset="0"
       tang_offset="0"
       prop_units="false"
       vertical_pattern="false"
       fuse_tolerance="0" />
    <linearGradient
       id="linearGradient3841">
      <stop
         id="stop3843"
         style="stop-color:#27221e;stop-opacity:1"
         offset="0" />
      <stop
         id="stop3851"
         style="stop-color:#1d1916;stop-opacity:0.74901962"
         offset="0.25" />
      <stop
         id="stop3849"
         style="stop-color:#13110f;stop-opacity:0.49803922"
         offset="0.5" />
      <stop
         id="stop3845"
         style="stop-color:#000000;stop-opacity:0"
         offset="1" />
    </linearGradient>
    <linearGradient
       x1="-1489.0695"
       y1="243.79076"
       x2="-305.21628"
       y2="243.79076"
       id="linearGradient3847"
       xlink:href="#linearGradient3841"
       gradientUnits="userSpaceOnUse"
       gradientTransform="matrix(2.429435,0,0,2.3444055,2585.2352,677.546)" />
    <linearGradient
       x1="98.292023"
       y1="435.48718"
       x2="532.95801"
       y2="435.48718"
       id="linearGradient7343"
       xlink:href="#linearGradient7339"
       gradientUnits="userSpaceOnUse"
       gradientTransform="matrix(0.9028961,0,0,0.93666666,33.973593,10.995438)" />
  </defs>

   <!--<metadata
      id="metadata7">
     <rdf:RDF>
       <cc:Work
          rdf:about="">
         <dc:format>image/svg+xml</dc:format>
         <dc:type
            rdf:resource="http://purl.org/dc/dcmitype/StillImage" />
         <dc:title></dc:title>
       </cc:Work>
     </rdf:RDF>
   </metadata>-->
  <g
     id="layer1"
     style="display:inline"
     transform="translate(182,286.3623)">
    <path
       d="m -994.28572,630.93359 a 1.428575,7.1428746 0 1 1 -2.85715,0 1.428575,7.1428746 0 1 1 2.85715,0 z"
       transform="matrix(0.41161835,0,0,0.42654737,-1064.1303,-289.00547)"
       id="path3053"
       style="opacity:0.33780003;fill:none;stroke:#000000;stroke-width:2.37699533;stroke-linecap:square;stroke-linejoin:bevel;stroke-miterlimit:4;stroke-opacity:0.06802721;stroke-dasharray:none"
       inkscape:connector-curvature="0" />
    <path
       d="m -380.00006,553.79077 a 714.28572,581.4286 0 1 1 -1428.57144,0 714.28572,581.4286 0 1 1 1428.57144,0 z"
       transform="matrix(0.41161835,0,0,0.42654737,-1064.1303,-289.00547)"
       id="path3059"
       style="opacity:0.02000002;fill:none;stroke:#000000;stroke-width:2.37699533;stroke-linecap:square;stroke-linejoin:bevel;stroke-miterlimit:4;stroke-opacity:0.06802721;stroke-dasharray:none"
       inkscape:connector-curvature="0" />
    <path
       d="m -305.71429,243.79076 a 591.42861,442.85716 0 1 1 -1182.85721,0 591.4286,442.85716 0 1 1 1182.85721,0 z"
       transform="matrix(0.41161835,0,0,0.42654737,-1064.1303,-289.00547)"
       id="path3831"
       style="opacity:0;fill:none;stroke:url(#linearGradient3847);stroke-width:2.37699533;stroke-linecap:square;stroke-linejoin:bevel;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none"
       inkscape:connector-curvature="0" />
    <path
       d="m -1547.6529,-459.62192 c -26.6009,9.73661 -53.9289,17.09352 -80.8686,25.72405 -19.779,6.48257 -39.1691,14.25242 -57.8928,23.52101 -9.0907,4.50003 -20.0558,10.54026 -29.0258,15.39892 -33.3266,19.89353 6.4889,-3.96727 10.9105,-5.99472 4.2109,-1.9309 -7.6805,5.26837 -11.4523,8.00577 -5.0733,3.682 -13.0924,9.82957 -17.9525,14.13562 -2.2086,1.95693 -4.2542,4.10333 -6.3813,6.15498 -5.4739,5.82987 -10.6417,12.16319 -13.2058,19.97337 -1.21,3.68568 -1.1797,4.65606 -1.7144,8.44677 -0.7645,7.66672 -0.8809,15.3733 -0.8192,23.07322 -0.186,6.8463 0.1466,13.69118 0.029,20.53722 0.01,5.55701 -0.5937,11.08308 -0.831,16.62488 -0.4782,2.5761 0.428,6.13165 -1.3538,8.29891 -2.1505,-8.17184 -19.3275,13.70523 -15.8218,7.04241 0,0 17.6143,-8.01325 17.6143,-8.01325 l 0,0 c -3.7971,5.74188 -13.7052,16.57287 -17.8375,9.441 -1.5342,-0.24287 -1.1144,-5.62939 -1.3504,-6.86954 -0.2345,-5.24126 -0.8541,-10.46527 -0.8601,-15.72279 -0.164,-6.7846 0.1006,-13.57805 -0.3103,-20.35694 -0.161,-7.61632 -0.7263,-15.23255 -0.3253,-22.8486 0.97,-10.61574 2.5714,-18.61938 8.8019,-27.51241 1.4266,-1.85957 2.7542,-3.80561 4.28,-5.5787 3.3208,-3.8592 8.8196,-9.09663 12.5421,-12.28325 21.2858,-18.22166 46.6112,-30.35635 70.2124,-44.98412 4.8243,-2.60791 9.602,-5.31059 14.4729,-7.82372 23.0383,-11.8864 47.0863,-21.613 71.6885,-29.4105 13.6957,-4.17577 27.3582,-8.11434 41.3242,-11.21751 4.0118,-0.89139 16.0425,-3.39765 20.6811,-3.93161 2.0633,-0.23751 4.1498,-0.13725 6.2247,-0.20587 0,0 -20.7789,16.3754 -20.7789,16.3754 z"
       id="path3895"
       style="opacity:0;fill:none;stroke:#272c3c;stroke-width:0.99599999;stroke-linecap:square;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none"
       inkscape:connector-curvature="0" />
    <path
       d="m -1586.3161,-456.06057 c -0.3077,0.52097 -0.5839,1.06334 -0.923,1.56291 -2.4703,3.6392 -5.4593,6.9369 -8.2536,10.3006 -5.8521,7.04454 -2.7858,3.39868 -9.0815,10.78368 -10.1887,11.44108 -20.2517,22.99841 -30.438,34.44199 -6.6666,7.46775 -13.1555,15.16822 -18.1275,23.968 -4.8857,7.96738 -7.7569,16.87053 -10.6458,25.74366 -2.653,7.42886 -4.0683,15.1969 -5.6692,22.91355 -1.5324,7.62796 -2.6577,15.33409 -3.8526,23.02754 -0.9287,6.43247 -1.873,12.85941 -2.9979,19.25866 -0.4663,3.45226 -1.1919,6.85152 -1.8331,10.27005 0.09,-0.55948 -0.3456,1.71811 -0.7244,1.37411 -0.368,-0.3342 -0.2002,-1.57397 -0.6463,-1.36575 -15.0919,7.04358 -17.4116,14.75115 -15.0044,7.64651 0,0 18.6015,-8.57766 18.6015,-8.57766 l 0,0 c -4.8931,6.87922 -2.8019,4.39875 -17.8729,12.44354 -0.4833,0.25797 -0.7537,-0.81448 -1.1663,-1.18124 -0.1719,-0.15278 -0.4502,-0.176 -0.5784,-0.36948 -0.1841,-0.27798 -0.2022,-0.64096 -0.3032,-0.96144 0.2946,-3.10971 0.6971,-6.19342 0.2829,-9.32066 -0.174,-6.15412 0.5013,-12.23176 0.9723,-18.35737 0.8315,-7.83935 2.3134,-15.531 3.8662,-23.24828 1.5837,-7.53429 2.851,-15.13825 4.674,-22.61581 0.6874,-2.91511 1.3264,-5.88078 2.2558,-8.7278 1.9793,-6.06363 4.6809,-11.88843 7.7198,-17.44769 4.8918,-7.97809 9.9569,-15.82566 15.5814,-23.28098 8.6378,-11.76557 18.0917,-22.89043 27.9912,-33.5297 8.8426,-9.3969 17.7392,-18.80083 27.7759,-26.85422 0,0 18.3971,-7.89672 18.3971,-7.89672 z"
       id="path3897"
       style="opacity:0;fill:none;stroke:#272c3c;stroke-width:0.99599999;stroke-linecap:square;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none"
       inkscape:connector-curvature="0" />
    <path
       d="m -1411.3585,-492.32684 c 10.6363,-5.96443 21.0357,-12.37239 31.9088,-17.8933 2.7993,-1.42135 -5.0607,3.7169 -7.6067,5.55371 -3.5287,2.54574 -7.0209,5.14461 -10.6173,7.59381 -15.8541,10.79688 -32.3405,20.65124 -48.7292,30.5998 -46.5101,27.50559 -91.5413,57.47348 -134.2292,90.62684 -10.0127,7.77633 -19.7848,15.85752 -29.6773,23.78628 -46.3625,38.65269 -87.983,82.67427 -124.7158,130.54132 -6.7017,8.73317 -13.005,17.76499 -19.5076,26.64749 -21.4165,31.50143 -41.2645,64.21849 -58.1587,98.390459 -8.3758,16.941741 -10.6924,23.220495 -17.7926,40.247583 -10.8433,26.19982 -17.557,53.6479455 -20.5632,81.776922 -1.3804,16.751654 -1.2461,33.575773 -1.1342,50.368826 0.4373,17.375949 4.5476,34.37072 7.95,51.34041 3.897,18.17675 8.482,36.20906 13.2619,54.17294 3.6473,13.75788 7.8022,27.30916 12.8611,40.60921 1.9362,3.57223 3.1418,15.413 9.0782,14.1331 12.1314,-9.7479 19.4865,-11.78043 -31.7894,17.46546 -0.652,0.3719 1.2835,-0.78423 1.8789,-1.24142 1.205,-0.92536 2.2813,-2.0072 3.4266,-3.00554 2.281,-2.17158 4.3648,-4.49229 6.3949,-6.89781 0,0 39.7866,-16.84944 39.7866,-16.84944 l 0,0 c -2.0796,2.41056 -3.8825,5.11629 -6.3526,7.13187 -3.3504,4.1984 0.4696,-0.32597 -3.2796,3.3426 -12.289,12.02463 -27.9814,25.68884 -45.4047,24.73955 -7.1591,-3.11564 -9.3024,-10.73884 -11.8271,-17.58998 -5.3448,-13.34024 -9.6666,-26.97433 -13.4357,-40.84628 -4.8574,-18.0287 -9.6196,-36.10373 -13.5141,-54.36708 -3.3847,-17.27066 -7.4607,-34.54875 -8.087,-52.200619 -0.155,-16.871848 -0.4759,-33.765884 0.6124,-50.616175 2.4017,-28.241571 8.25,-55.942026 18.7683,-82.364585 6.7556,-17.010882 8.9987,-23.448039 17.0833,-40.369824 16.3767,-34.278017 35.9226,-67.041077 56.954,-98.635777 6.4104,-8.92184 12.6038,-18.00356 19.2311,-26.7655 36.3961,-48.11982 77.7747,-92.40303 123.8916,-131.3334 9.8966,-7.98388 19.6699,-16.12318 29.6899,-23.95163 43.1355,-33.70091 88.7098,-64.12485 135.917,-91.80955 16.7537,-10.02284 33.6256,-19.96776 49.9303,-30.71945 6.4935,-4.28194 12.4341,-9.38654 19.0541,-13.47009 14.0266,-8.65231 28.3007,-16.8967 42.4511,-25.34505 0,0 -33.7081,27.20432 -33.7081,27.20432 z"
       id="path3899"
       style="opacity:0;fill:none;stroke:#272c3c;stroke-width:0.99599999;stroke-linecap:square;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none"
       inkscape:connector-curvature="0" />
    <path
       d="m -1325.4935,-501.46955 c -5.0269,13.79571 -9.3814,27.81689 -13.133,42.03794 -4.3734,17.90767 -6.6891,36.24647 -8.6149,54.58052 -1.3142,13.2997 -2.7149,26.59211 -3.86,39.90907 -0.4056,5.12431 -0.2238,2.68665 -0.5515,7.31246 0,0 -17.208,8.95619 -17.208,8.95619 l 0,0 c 0.1879,-4.58593 0.076,-2.16913 0.3439,-7.24996 0.8619,-13.26093 2.1526,-26.48661 3.3682,-39.71638 1.8076,-18.42483 4.0943,-36.84005 8.3966,-54.84503 3.821,-14.45718 8.1132,-28.81791 13.9463,-42.55939 0,0 17.3124,-8.42542 17.3124,-8.42542 z"
       id="path3901"
       style="opacity:0;fill:none;stroke:#272c3c;stroke-width:0.99599999;stroke-linecap:square;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none"
       inkscape:connector-curvature="0" />
    <path
       d="m 592.5,388.61218 a 254.375,281.25 0 1 1 -508.75,0 254.375,281.25 0 1 1 508.75,0 z"
       transform="translate(0,-84)"
       id="path4679"
       style="opacity:0;fill:#000000;stroke:#000000;stroke-width:0.99599999;stroke-linecap:square;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none"
       inkscape:connector-curvature="0" />
    <path
       d="m 551.25,389.86218 a 236.25,270 0 1 1 -472.5,0 236.25,270 0 1 1 472.5,0 z"
       transform="translate(0,-84)"
       id="path4683"
       style="opacity:0;fill:#000000;fill-opacity:1;stroke:#bac4b1;stroke-width:0.99599999;stroke-linecap:square;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:0;stroke-dasharray:none"
       inkscape:connector-curvature="0" />
    <path
       d="m 552.5,405.48718 a 232.5,271.875 0 1 1 -465,0 232.5,271.875 0 1 1 465,0 z"
       transform="translate(0,-84)"
       id="path4687"
       style="opacity:0;fill:#000000;fill-opacity:1;stroke:#bac4b1;stroke-width:1.29700005;stroke-linecap:square;stroke-linejoin:round;stroke-miterlimit:4;stroke-opacity:0;stroke-dasharray:3.891, 1.297;stroke-dashoffset:0;marker-start:url(#Arrow1Lend);marker-end:none"
       inkscape:connector-curvature="0" />
    <path
       d="m 532.5,435.48718 a 216.875,261.875 0 1 1 -433.75,0 216.875,261.875 0 1 1 433.75,0 z"
       transform="matrix(1.6916427,0,0,1.4319809,-164.54971,-158.99715)"
       id="path5894"
       style="fill:none;stroke:url(#linearGradient7343);stroke-width:0.84234029;stroke-linecap:round;stroke-linejoin:bevel;stroke-miterlimit:4;stroke-opacity:0.97857139;stroke-dasharray:none;stroke-dashoffset:0.3663837"
       inkscape:connector-curvature="0" />
    <path
       d="m 627.5,629.23718 a 248.125,219.375 0 1 1 -496.25,0 248.125,219.375 0 1 1 496.25,0 z"
       transform="matrix(-1.1007557,0,0,-1.2136752,786.97421,1225.8019)"
       id="path7345"
       style="fill:none;stroke:#0f0002;stroke-width:1.13426316;stroke-linecap:round;stroke-linejoin:bevel;stroke-miterlimit:4;stroke-opacity:0.97857139;stroke-dasharray:none;stroke-dashoffset:0.52440944"
       inkscape:connector-curvature="0" />
    <path
       d="m 563.75,589.86218 a 154.375,145 0 1 1 -308.75,0 154.375,145 0 1 1 308.75,0 z"
       transform="matrix(1.1781377,0,0,1.1939654,-111.6751,-251.53792)"
       id="path7347"
       style="fill:none;stroke:#0f0002;stroke-width:1.10539269;stroke-linecap:round;stroke-linejoin:bevel;stroke-miterlimit:4;stroke-opacity:0.97857139;stroke-dasharray:none;stroke-dashoffset:0.52440944"
       inkscape:connector-curvature="0" />
    <path
       d="m 552.5,453.36218 183.75,0 -1.25,0"
       id="path7357"
       style="fill:none;stroke:#000000;stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1"
       inkscape:connector-curvature="0" />
    <path
       d="m 152.5,163.36218 115,147.5"
       id="path7359"
       style="fill:none;stroke:#000000;stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1"
       inkscape:connector-curvature="0" />
    <path
       d="m 466.25,304.61218 103.75,-155"
       id="path7361"
       style="fill:none;stroke:#000000;stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1"
       inkscape:connector-curvature="0" />
    <path
       d="m 476.2494,594.61158 107.5012,174.5803"
       id="path7363"
       style="fill:none;stroke:#000000;stroke-width:0.9988057px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1"
       inkscape:connector-curvature="0" />
    <path
       d="m 258.75,589.61218 -106.25,180"
       id="path7365"
       style="fill:none;stroke:#000000;stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1"
       inkscape:connector-curvature="0" />
    <path
       d="m 232.5,339.61218 58.75,53.125"
       id="path7367"
       style="fill:none;stroke:#000000;stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1"
       inkscape:connector-curvature="0" />
    <path
       d="m 501.24999,333.36218 -56.25,52.5"
       id="path7369"
       style="fill:none;stroke:#000000;stroke-width:0.99999994px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1"
       inkscape:connector-curvature="0" />
    <path
       d="m 293.76858,515.21861 -56.28712,55.03711"
       id="path7371"
       style="fill:none;stroke:#000000;stroke-width:0.9628703px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1"
       inkscape:connector-curvature="0" />
    <path
       d="m 447.5,517.73717 57.50001,51.875"
       id="path7373"
       style="fill:none;stroke:#000000;stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1"
       inkscape:connector-curvature="0" />
    <text
       x="375"
       y="531.11218"
       id="text3281"
       xml:space="preserve"
       style="font-size:40px;font-style:normal;font-weight:normal;line-height:125%;letter-spacing:0px;word-spacing:0px;fill:#000000;fill-opacity:1;stroke:none;font-family:Sans"
       sodipodi:linespacing="125%"><tspan
         x="375"
         y="531.11218"
         id="tspan3283" /></text>
    <flowRoot
       id="flowRoot3285"
       xml:space="preserve"
       style="font-size:40px;font-style:normal;font-weight:normal;line-height:125%;letter-spacing:0px;word-spacing:0px;fill:#000000;fill-opacity:1;stroke:none;font-family:Sans"><flowRegion
         id="flowRegion3287"><rect
           width="78.75"
           height="51.25"
           x="363.75"
           y="507.36218"
           id="rect3289" /></flowRegion><flowPara
         id="flowPara3291" /></flowRoot>    <flowRoot
       id="flowRoot3293"
       xml:space="preserve"
       style="font-size:40px;font-style:normal;font-weight:normal;line-height:125%;letter-spacing:0px;word-spacing:0px;fill:#000000;fill-opacity:1;stroke:none;font-family:Sans"><flowRegion
         id="flowRegion3295"><rect
           width="8.75"
           height="48.75"
           x="398.75"
           y="548.61218"
           id="rect3297" /></flowRegion><flowPara
         id="flowPara3299" /></flowRoot>    <flowRoot
       id="flowRoot3301"
       xml:space="preserve"
       style="font-size:40px;font-style:normal;font-weight:normal;line-height:125%;letter-spacing:0px;word-spacing:0px;fill:#000000;fill-opacity:1;stroke:none;font-family:Sans"><flowRegion
         id="flowRegion3303"><rect
           width="103.75"
           height="81.25"
           x="330"
           y="514.86218"
           id="rect3305" /></flowRegion><flowPara
         id="flowPara3307" /></flowRoot>    <flowRoot
       id="flowRoot3309"
       xml:space="preserve"
       style="font-size:40px;font-style:normal;font-weight:normal;line-height:125%;letter-spacing:0px;word-spacing:0px;fill:#000000;fill-opacity:1;stroke:none;font-family:Sans"><flowRegion
         id="flowRegion3311"><rect
           width="110"
           height="111.25"
           x="325"
           y="486.11218"
           id="rect3313" /></flowRegion><flowPara
         id="flowPara3315" /></flowRoot>    <text
       x="376.25"
       y="539.86218"
       id="text3317"
       xml:space="preserve"
       style="font-size:40px;font-style:normal;font-weight:normal;line-height:125%;letter-spacing:0px;word-spacing:0px;fill:#000000;fill-opacity:1;stroke:none;font-family:Sans"
       sodipodi:linespacing="125%"><tspan
         x="376.25"
         y="539.86218"
         id="tspan3319" /></text>
    <flowRoot
       id="flowRoot3321"
       xml:space="preserve"
       style="font-size:40px;font-style:normal;font-weight:normal;line-height:125%;letter-spacing:0px;word-spacing:0px;fill:#000000;fill-opacity:1;stroke:none;font-family:Sans"><flowRegion
         id="flowRegion3323"><rect
           width="130"
           height="116.25"
           x="307.5"
           y="502.36218"
           id="rect3325" /></flowRegion><flowPara
         id="flowPara3327" /></flowRoot>    <text
       x="482.91666"
       y="465.86218"
       id="text3337"
       xml:space="preserve"
       style="font-style:normal;font-weight:normal;font-size:40px;line-height:381.99985027%;font-family:Sans;letter-spacing:0px;word-spacing:0px;fill:#008080;fill-opacity:1;stroke:none;"
       sodipodi:linespacing="381.99985%"><tspan
         x="482.91666"
         y="465.86218"
         id="tspan3339"
         style="fill:#008080;" /></text>
    <text
       x="203.91667"
       y="467.11218"
       id="text3345"
       xml:space="preserve"
       style="font-style:normal;font-weight:normal;font-size:40px;line-height:125%;font-family:Sans;letter-spacing:0px;word-spacing:0px;fill:#808000;fill-opacity:1;stroke:none;"
       sodipodi:linespacing="125%"><tspan
         x="203.91667"
         y="467.11218"
         id="tspan3347"
         style="fill:#808000;" /></text>
    <text
       x="343.75"
       y="688.36218"
       id="text3361"
       xml:space="preserve"
       style="font-style:normal;font-weight:normal;font-size:40px;line-height:125%;font-family:Sans;letter-spacing:0px;word-spacing:0px;fill:#000000;fill-opacity:1;stroke:none"
       sodipodi:linespacing="125%"><tspan
         x="343.75"
         y="688.36218"
         id="tspan3363" /></text>
    <text
       x="167.5"
       y="622.36218"
       id="text3365"
       xml:space="preserve"
       style="font-size:40px;font-style:normal;font-weight:normal;line-height:125%;letter-spacing:0px;word-spacing:0px;fill:#000000;fill-opacity:1;stroke:none;font-family:Sans"
       sodipodi:linespacing="125%"><tspan
         x="167.5"
         y="622.36218"
         id="tspan3367" /></text>
    <text
       x="638"
       y="625.52887"
       id="text3385"
       xml:space="preserve"
       style="font-style:normal;font-weight:normal;font-size:40px;line-height:125%;font-family:Sans;letter-spacing:0px;word-spacing:0px;fill:#000000;fill-opacity:1;stroke:none"
       sodipodi:linespacing="125%"><tspan
         x="638"
         y="625.52887"
         id="tspan3387" /></text>
    <path
       d="m 471.25,542.98718 a 87.1875,83.75 0 1 1 -174.375,0 87.1875,83.75 0 1 1 174.375,0 z"
       transform="matrix(1.1746587,0,0,1.1631708,-79.850667,-177.51629)"
       id="path3331"
       '''
HTML +='       style="fill:#%s;fill-rule:evenodd;stroke:#000000;stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1"'%(RGB[16])
HTML +='''       inkscape:connector-curvature="0" />
    <path
       d="m 187.82524,453.50006 -186.4994148,0"
       id="path3355"
       style="fill:none;stroke:#000000;stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1"
       inkscape:connector-curvature="0" />
    <text
       x="346"
       y="465.02887"
       id="text3366"
       xml:space="preserve"
       style="font-size:40px;font-style:normal;font-weight:normal;line-height:125%;letter-spacing:0px;word-spacing:0px;fill:#000000;fill-opacity:1;stroke:none;font-family:Sans"
       sodipodi:linespacing="125%"><tspan
         x="346"
         y="465.02887"
         id="tspan3368">17</tspan></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-weight:normal;font-size:40px;line-height:125%;font-family:sans-serif;letter-spacing:0px;word-spacing:0px;fill:#ff00ff;fill-opacity:1;stroke:none;stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1;"
       x="555.06897"
       y="345.08618"
       id="text4421"
       sodipodi:linespacing="125%"><tspan
         sodipodi:role="line"
         id="tspan4423"
         x="555.06897"
         y="345.08618" /></text>
    <text
       xml:space="preserve"
       style="font-style:normal;font-weight:normal;font-size:40px;line-height:125%;font-family:sans-serif;letter-spacing:0px;word-spacing:0px;fill:#ffff00;fill-opacity:1;stroke:none;stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1;"
       x="348.17242"
       y="320.08618"
       id="text4433"
       sodipodi:linespacing="125%"><tspan
         sodipodi:role="line"
         id="tspan4435"
         x="348.17242"
         y="320.08618" /></text>
    <path'''
HTML +='       style="fill:#%s;fill-opacity:1"'%(c[2])
HTML +='''       d="m 539.67618,1125.2135 c -66.41202,-2.5716 -128.77358,-22.1771 -184.05797,-57.8648 -4.11836,-2.6585 -10.1519,-6.7617 -13.40787,-9.1183 -5.54144,-4.0107 -5.88403,-4.3524 -5.3583,-5.3437 0.3089,-0.5825 3.60535,-6.1678 7.32546,-12.4117 3.7201,-6.244 15.32917,-25.9179 25.79793,-43.71983 10.46876,-17.80193 19.19753,-32.53275 19.39727,-32.73515 0.19974,-0.2024 2.2423,0.94311 4.53902,2.54559 13.0499,9.10521 30.4003,18.72081 45.86108,25.41622 66.59443,28.83927 141.82811,30.80907 209.56522,5.48689 19.68118,-7.35742 41.06829,-18.30637 56.90959,-29.13439 2.99624,-2.04802 3.62225,-2.3087 4.15368,-1.72961 0.99217,1.08116 54.05447,87.57318 54.10693,88.19478 0.0604,0.7156 -8.34825,6.737 -18.55185,13.285 -50.25004,32.2472 -107.5493,51.5338 -166.90821,56.1802 -9.11699,0.7137 -31.50904,1.2533 -39.37198,0.9488 l 0,0 z"
       id="path3396"
       inkscape:connector-curvature="0"
       transform="translate(-182,-286.3623)" />
    <path'''
HTML +='       style="fill:#%s;fill-opacity:1"'%(RGB[3])
HTML +='''       d="m 534.49609,1124.9456 c -1.0628,-0.098 -3.07378,-0.2022 -4.46884,-0.2322 -1.39507,-0.03 -3.1342,-0.1446 -3.86474,-0.2546 -0.73054,-0.11 -3.39347,-0.371 -5.91763,-0.58 -7.11806,-0.5894 -21.23581,-2.4082 -29.10628,-3.75 -3.31774,-0.5656 -14.10294,-2.6759 -16.0628,-3.143 -1.19565,-0.285 -3.58696,-0.8259 -5.31401,-1.2021 -5.03804,-1.0974 -14.69954,-3.6659 -21.73913,-5.7792 -28.66582,-8.6058 -56.22012,-20.789 -82.00483,-36.2584 -14.7697,-8.8611 -29.22706,-18.9067 -29.22706,-20.3083 0,-0.4355 6.10709,-10.9183 24.75568,-42.4929 8.18556,-13.85926 27.66909,-46.66426 27.82221,-46.84506 0.21167,-0.24995 2.74503,1.24131 8.17091,4.80981 27.31351,17.96361 55.77862,30.38799 87.18218,38.05305 67.04352,16.3642 137.2118,7.655 197.77255,-24.54722 7.90135,-4.20141 14.04225,-7.81847 21.16792,-12.46814 4.79822,-3.13094 5.36017,-3.44718 6.1238,-3.44605 0.66103,9.6e-4 3.57601,4.55089 19.65277,30.67551 22.33377,36.2922 34.99686,57.3395 34.80269,57.8455 -0.49872,1.2996 -15.73636,11.6442 -27.9338,18.9638 -11.77761,7.0677 -28.855,15.9109 -39.7343,20.5758 -17.65787,7.5715 -31.332,12.5 -47.34299,17.0637 -23.9921,6.8386 -52.40498,11.725 -74.63768,12.8361 -13.74847,0.6871 -35.08424,0.9446 -40.09662,0.4839 z"
       id="path3398"
       inkscape:connector-curvature="0"
       transform="translate(-182,-286.3623)" />
    <path'''
HTML +='       style="fill:#%s;fill-opacity:1"'%(RGB[4])
HTML +='''       d="m 738.28627,1010.2202 c -15.02101,-24.41989 -27.31093,-44.52664 -27.31093,-44.68169 0,-0.15504 3.07076,-2.57865 6.82391,-5.3858 18.43593,-13.78906 35.14992,-29.96977 49.52199,-47.94193 27.47403,-34.35607 46.51549,-76.18278 54.59483,-119.92366 2.72136,-14.73325 2.83256,-16.01734 3.00522,-34.69819 l 0.16116,-17.43697 46.20275,-0.10689 46.20275,-0.10688 0.0544,4.93882 c 0.42479,38.58906 -4.04376,73.47307 -13.94311,108.84779 -20.54429,73.41377 -62.52414,138.70022 -120.19086,186.9191 -5.05356,4.2256 -17.49412,14.037 -17.73888,13.99 -0.0397,-0.01 -12.36218,-19.9938 -27.38319,-44.4137 z"
       id="path3402"
       inkscape:connector-curvature="0"
       transform="translate(-182,-286.3623)"
       sodipodi:nodetypes="cssssscccsssccc" />
    <text
       xml:space="preserve"
       style="font-size:40px;font-style:normal;font-weight:normal;line-height:125%;letter-spacing:0px;word-spacing:0px;fill:#000000;fill-opacity:1;stroke:none;font-family:Sans"
       x="539.89636"
       y="1076.7451"
       id="text3404"
       sodipodi:linespacing="125%"
       transform="translate(-182,-286.3623)"><tspan
         sodipodi:role="line"
         id="tspan3406"
         x="539.89636"
         y="1076.7451">4</tspan></text>
    <text
       xml:space="preserve"
       style="font-size:40px;font-style:normal;font-weight:normal;line-height:125%;letter-spacing:0px;word-spacing:0px;fill:#000000;fill-opacity:1;stroke:none;font-family:Sans"
       x="648.1347"
       y="605.92682"
       id="text3408"
       sodipodi:linespacing="125%"><tspan
         sodipodi:role="line"
         id="tspan3410"
         x="648.1347"
         y="605.92682">5</tspan></text>
    <path'''
HTML +='       style="fill:#%s;fill-opacity:1"'%(RGB[5])
HTML +='''       d="m 824.85428,738.1348 c -0.0254,-2.74631 -1.56241,-19.27046 -2.30059,-24.7334 -5.85632,-43.33988 -22.73523,-84.78886 -49.16503,-120.73292 -14.20224,-19.3148 -32.94737,-38.409 -52.66867,-53.64934 -4.1667,-3.21997 -16.25355,-10.51502 -22.54508,-14.85898 -2.96601,-2.04787 -3.08852,-3.43987 -3.34965,-3.43987 -1.01534,0 1.75151,0.35671 6.3522,-7.32642 5.60636,-9.3626 49.94668,-75.64767 50.60328,-75.64767 0.78207,0 17.12107,11.91443 25.15686,18.34444 28.40726,22.73065 52.77787,48.88925 73.66064,79.06488 37.90439,54.7719 61.38876,121.48615 65.93428,187.3057 0.27552,3.98964 0.64844,9.41063 0.8287,12.04664 l 0.32776,4.79274 -46.41196,0 -46.41195,0 -0.0108,-1.1658 -1e-5,0 z"
       id="path3412"
       inkscape:connector-curvature="0"
       transform="translate(-182,-286.3623)"
       sodipodi:nodetypes="cssssssssssscccccc" />
    <path'''
HTML +='       style="fill:#%s;fill-opacity:1"'%(RGB[0])
HTML +='''       d="m 394.65761,526.2177 c -0.97868,-1.21114 -14.66694,-18.75648 -30.41834,-38.98964 -15.75141,-20.23316 -28.85833,-37.06749 -29.12648,-37.40963 -0.60279,-0.76909 4.30901,-4.46546 17.73155,-13.3439 51.36732,-33.97728 108.55957,-53.62997 171.50259,-58.93258 10.38147,-0.87459 43.86772,-0.88352 53.88601,-0.0144 44.23043,3.83722 82.20094,13.5813 121.5081,31.1817 14.62878,6.55026 32.91463,16.48568 45.72642,24.84495 l 5.31741,3.46944 -27.47112,41.07876 c -15.10911,22.59332 -27.34918,41.27605 -27.20015,41.51718 0.14902,0.24113 -0.002,0.60714 -0.33569,0.81335 -0.40229,0.24863 -0.47946,0.12979 -0.22909,-0.3528 0.20765,-0.40025 0.0642,-0.3485 -0.31886,0.11501 -0.62774,0.75963 -1.51284,0.39097 -8.97625,-3.73884 -50.40273,-27.8899 -109.4262,-39.50091 -166.82906,-32.81839 -27.08992,3.15366 -54.11393,10.33241 -78.67185,20.89866 -12.31383,5.29813 -32.16707,15.95559 -41.69091,22.38019 -1.22543,0.82666 -2.31733,1.503 -2.42645,1.503 -0.10913,0 -0.99915,-0.99093 -1.97783,-2.20207 l 0,0 z"
       id="path3414"
       inkscape:connector-curvature="0"
       transform="translate(-182,-286.3623)" />
    <path'''
HTML +='       style="fill:#%s;fill-opacity:1"'%(RGB[1])
HTML +='''       d="m 185.33394,735.46897 c 0,-4.37663 1.22337,-19.25665 2.41306,-29.35049 11.61118,-98.514 60.54426,-187.41159 137.35771,-249.54015 4.47597,-3.62026 8.36365,-6.5823 8.63931,-6.5823 0.27566,0 14.03157,17.37245 30.5687,38.60544 16.53713,21.233 30.40033,39.03008 30.80713,39.54908 0.56901,0.72596 0.35153,1.19673 -0.94277,2.04082 -11.51201,7.50761 -29.0428,22.37491 -41.50332,35.19763 -37.85156,38.95182 -62.53825,87.76832 -71.33945,141.06962 -1.26246,7.64568 -1.71327,11.54007 -3.16953,27.38095 l -0.42212,6.59184 -46.20436,0 -46.20436,0 z"
       id="path3416"
       inkscape:connector-curvature="0"
       transform="translate(-182,-286.3623)"
       sodipodi:nodetypes="sssssssssscccs" />
    <text
       xml:space="preserve"
       style="font-size:40px;font-style:normal;font-weight:normal;line-height:125%;letter-spacing:0px;word-spacing:0px;fill:#000000;fill-opacity:1;stroke:none;font-family:Sans"
       x="362.21768"
       y="158.49812"
       id="text3420"
       sodipodi:linespacing="125%"><tspan
         sodipodi:role="line"
         id="tspan3422"
         x="362.21768"
         y="158.49812">1</tspan></text>
    <text
       xml:space="preserve"
       style="font-size:40px;font-style:normal;font-weight:normal;line-height:125%;letter-spacing:0px;word-spacing:0px;fill:#000000;fill-opacity:1;stroke:none;font-family:Sans"
       x="80.915016"
       y="318.19434"
       id="text3424"
       sodipodi:linespacing="125%"><tspan
         sodipodi:role="line"
         id="tspan3426"
         x="80.915016"
         y="318.19434">2</tspan></text>
    <text
       xml:space="preserve"
       style="font-size:40px;font-style:normal;font-weight:normal;line-height:125%;letter-spacing:0px;word-spacing:0px;fill:#000000;fill-opacity:1;stroke:none;font-family:Sans"
       x="640.62775"
       y="319.82193"
       id="text3432"
       sodipodi:linespacing="125%"><tspan
         sodipodi:role="line"
         id="tspan3434"
         x="640.62775"
         y="319.82193">6</tspan></text>
    <path'''
HTML +='       style="fill:#%s;fill-opacity:1"'%(RGB[6])
HTML +='''       d="m 431.26831,573.19407 c -9.52102,-12.32964 -19.98856,-26.03066 -23.2612,-30.44672 -3.27265,-4.41606 -7.08319,-9.21521 -8.46787,-10.66478 l -2.51761,-2.63558 5.70582,-3.64631 c 17.65219,-11.28065 37.04886,-20.56755 58.26247,-27.89539 66.69784,-23.03951 140.25896,-19.584 205.29126,9.64349 12.82846,5.7655 27.01457,13.6514 27.43246,15.24939 0.19245,0.73593 0.088,1.17619 -0.2321,0.97835 -0.80532,-0.49771 -3.09698,3.14902 -2.5426,4.04603 0.24726,0.40007 0.0145,0.63714 -0.51711,0.52683 -0.53463,-0.11093 -0.92194,0.36681 -0.86659,1.06895 0.055,0.69823 -0.15539,1.11164 -0.4676,0.91868 -0.79528,-0.49151 -3.0767,3.16749 -2.52826,4.05488 0.24726,0.40007 0.0145,0.63714 -0.51711,0.52683 -0.53166,-0.11031 -0.92319,0.36137 -0.87006,1.04818 0.0531,0.68681 -0.27533,1.17952 -0.72992,1.09489 -0.4546,-0.0846 -0.78151,0.41743 -0.72646,1.11566 0.055,0.69824 -0.15539,1.11164 -0.46761,0.91868 -0.79528,-0.49151 -3.07669,3.1675 -2.52826,4.05489 0.24726,0.40007 0.0145,0.63714 -0.51711,0.52683 -0.53166,-0.11032 -0.92319,0.36137 -0.87005,1.04818 0.0531,0.68681 -0.27533,1.17951 -0.72993,1.09489 -0.45459,-0.0846 -0.7815,0.41742 -0.72646,1.11566 0.055,0.69823 -0.15539,1.11164 -0.46761,0.91867 -0.79527,-0.4915 -3.07669,3.1675 -2.52825,4.05489 0.24725,0.40007 0.0145,0.63714 -0.51711,0.52683 -0.53464,-0.11093 -0.92194,0.36681 -0.86659,1.06895 0.055,0.69824 -0.15539,1.11164 -0.46761,0.91867 -0.79528,-0.4915 -3.07669,3.16751 -2.52825,4.05489 0.24725,0.40007 0.0145,0.63714 -0.51711,0.52684 -0.53167,-0.11032 -0.92319,0.36136 -0.87006,1.04817 0.0531,0.68682 -0.27533,1.17952 -0.72993,1.09489 -0.45459,-0.0846 -0.7815,0.41743 -0.72646,1.11567 0.055,0.69823 -0.14762,1.11643 -0.45034,0.92934 -0.66157,-0.40888 -18.71657,26.60185 -18.42254,27.56058 0.25605,0.8349 0.62716,0.99914 -9.16105,-4.05439 -20.71744,-10.69617 -42.12808,-17.13407 -66.3857,-19.96131 -12.22846,-1.42523 -36.60596,-1.00892 -48.38117,0.82624 -25.12721,3.91608 -48.68034,12.28088 -69.07947,24.53331 -3.26744,1.96253 -6.22364,3.55576 -6.56935,3.5405 -0.3457,-0.0153 -8.41848,-10.11562 -17.9395,-22.44525 l 0,0 z"
       id="path3436"
       inkscape:connector-curvature="0"
       transform="translate(-182,-286.3623)" />
    <path'''
HTML +='       style="fill:#%s;fill-opacity:1"'%(RGB[2])
HTML +='''       d="M 324.16828,1044.5172 C 248.1161,983.17186 199.52794,894.35349 187.6353,794.93713 c -1.67481,-14.00057 -3.1684,-44.44543 -2.4798,-50.54744 l 0.47363,-4.19708 46.15587,0 46.15586,0 0.40381,16.24087 c 0.87131,35.04355 7.92661,66.0837 22.43925,98.72263 2.32058,5.21898 4.5686,9.41088 4.99561,9.31533 0.44108,-0.0987 0.57654,0.34706 0.31365,1.03215 -0.33532,0.87381 -0.19653,1.04135 0.50401,0.60839 0.63166,-0.39039 0.79209,-0.31488 0.46284,0.21785 -1.04671,1.69361 13.45901,26.92886 14.94966,26.00758 0.35224,-0.21769 0.4779,0.0318 0.27925,0.55451 -0.45279,1.19134 5.37181,9.50208 6.27034,8.94675 0.3631,-0.22441 0.49084,0.0333 0.28385,0.5727 -0.47367,1.23437 12.20673,17.04976 13.452,16.77775 0.51163,-0.11176 0.69623,0.15857 0.41691,0.61052 -0.57721,0.93393 3.96627,5.92763 4.87962,5.36315 0.33325,-0.20596 0.44119,0.0548 0.23985,0.57947 -0.40636,1.05894 14.31461,16.13244 15.40136,15.77019 0.37117,-0.12373 0.67485,0.006 0.67485,0.28732 0,1.15097 5.87261,6.42544 6.77049,6.08089 0.53326,-0.20464 0.79172,-0.0843 0.57437,0.26739 -0.78545,1.27087 15.90133,14.30267 17.29048,13.50327 0.50166,-0.28868 0.6686,-0.25609 0.371,0.0724 -0.29761,0.32852 -0.13338,1.10117 0.36496,1.71699 0.74429,0.91976 0.721,1.00812 -0.13038,0.49487 -0.77304,-0.46603 -0.92027,-0.32207 -0.57932,0.56643 0.25142,0.65519 0.0923,1.41676 -0.3537,1.69238 -0.52004,0.3214 -0.62008,0.13346 -0.27896,-0.52407 0.29254,-0.56385 0.008,-0.37768 -0.63325,0.41372 -0.64082,0.7914 -0.99741,1.87598 -0.79242,2.41017 0.205,0.5342 0.0802,0.79046 -0.2774,0.56948 -0.87647,-0.54169 -3.85795,4.60996 -3.24343,5.60427 0.31113,0.50343 0.1381,0.57154 -0.48056,0.18919 -0.70054,-0.43296 -0.83933,-0.26543 -0.50402,0.60839 0.28532,0.7435 0.12297,1.13926 -0.4234,1.03215 -0.48737,-0.0956 -0.84111,0.39756 -0.78606,1.09579 0.0569,0.72196 -0.23272,1.06385 -0.67149,0.79267 -0.48554,-0.30008 -0.59338,-0.0126 -0.29091,0.77569 0.32391,0.8441 0.20489,1.08212 -0.36497,0.72993 -0.56987,-0.35219 -0.68887,-0.11417 -0.36496,0.72992 0.26435,0.6889 0.18809,1.07174 -0.16947,0.85076 -0.87647,-0.54169 -3.85795,4.60996 -3.24343,5.60427 0.31113,0.50343 0.1381,0.57154 -0.48056,0.18918 -0.70054,-0.43295 -0.83933,-0.26542 -0.50402,0.6084 0.28532,0.7435 0.12297,1.13926 -0.4234,1.03214 -0.48737,-0.0955 -0.84111,0.39757 -0.78606,1.0958 0.0569,0.72196 -0.23272,1.06385 -0.67149,0.79266 -0.49889,-0.30832 -0.58511,0.009 -0.24398,0.89802 0.29018,0.75617 0.29334,1.14062 0.007,0.85431 -0.77807,-0.77806 -2.6438,2.24833 -2.03661,3.30356 0.28835,0.50112 0.25473,0.66687 -0.0747,0.36833 -0.84813,-0.76857 -2.74873,2.18005 -2.11505,3.2813 0.28835,0.50117 0.25473,0.66687 -0.0747,0.36833 -0.82958,-0.75175 -2.76042,2.17424 -2.1193,3.21164 0.34573,0.5594 0.196,0.6411 -0.44672,0.2439 -0.70054,-0.4329 -0.83933,-0.2654 -0.50401,0.6084 0.28531,0.7435 0.12296,1.1393 -0.42341,1.0321 -0.48737,-0.096 -0.8411,0.3976 -0.78606,1.0958 0.0569,0.722 -0.23272,1.0639 -0.67149,0.7927 -0.49889,-0.3083 -0.58511,0.01 -0.24398,0.898 0.29018,0.7562 0.29334,1.1406 0.007,0.8543 -0.77806,-0.778 -2.6438,2.2484 -2.03661,3.3036 0.28835,0.5011 0.25473,0.6669 -0.0747,0.3683 -0.82959,-0.7517 -2.76043,2.1743 -2.1193,3.2116 0.34572,0.5594 0.19599,0.6412 -0.44673,0.244 -0.70054,-0.433 -0.83932,-0.2655 -0.50401,0.6084 0.28531,0.7435 0.12296,1.1392 -0.4234,1.0321 -0.48737,-0.096 -0.84111,0.3976 -0.78607,1.0958 0.0569,0.722 -0.23271,1.0639 -0.67149,0.7927 -0.47973,-0.2965 -0.59653,-0.021 -0.30882,0.729 0.28531,0.7435 0.12296,1.1393 -0.4234,1.0321 -0.48738,-0.096 -0.84111,0.3976 -0.78607,1.0958 0.0569,0.722 -0.23271,1.0639 -0.67149,0.7927 -0.48554,-0.3001 -0.59338,-0.013 -0.29091,0.7757 0.32391,0.8441 0.2049,1.0821 -0.36496,0.7299 -0.56141,-0.3469 -0.69198,-0.1222 -0.38849,0.6687 0.25142,0.6552 0.0923,1.4167 -0.3537,1.6923 -0.52004,0.3214 -0.62008,0.1335 -0.27895,-0.524 0.29253,-0.5639 0.008,-0.3777 -0.63326,0.4137 -0.64082,0.7914 -1.00547,1.855 -0.81032,2.3635 0.19514,0.5085 -0.0439,0.8464 -0.53134,0.7509 -0.48737,-0.096 -0.84111,0.3975 -0.78607,1.0958 0.0569,0.7219 -0.23271,1.0638 -0.67149,0.7926 -0.47973,-0.2965 -0.59653,-0.021 -0.30882,0.7291 0.28531,0.7435 0.12296,1.1392 -0.4234,1.0321 -0.48738,-0.096 -0.84111,0.3976 -0.78607,1.0958 0.0569,0.722 -0.23271,1.0638 -0.67149,0.7927 -0.48554,-0.3001 -0.59338,-0.013 -0.29091,0.7757 0.32391,0.8441 0.2049,1.0821 -0.36496,0.7299 -0.56141,-0.347 -0.69198,-0.1223 -0.38849,0.6686 0.25142,0.6552 0.0923,1.4168 -0.3537,1.6924 -0.52004,0.3214 -0.62008,0.1335 -0.27895,-0.5241 0.29253,-0.5638 0.008,-0.3776 -0.63326,0.4138 -0.64082,0.7913 -1.00799,1.8483 -0.81593,2.3488 0.19206,0.5005 -0.0157,1.1355 -0.46164,1.4111 -0.52004,0.3214 -0.62008,0.1335 -0.27895,-0.524 0.29253,-0.5639 0.008,-0.3777 -0.63326,0.4137 -0.64082,0.7914 -1.00547,1.855 -0.81032,2.3635 0.19514,0.5085 -0.0439,0.8464 -0.53134,0.7509 -0.48738,-0.096 -0.84111,0.3975 -0.78607,1.0958 0.0569,0.7219 -0.23271,1.0638 -0.67149,0.7926 -0.47973,-0.2965 -0.59653,-0.021 -0.30882,0.7291 0.28531,0.7435 0.12296,1.1392 -0.4234,1.0321 -0.48738,-0.096 -0.84111,0.3976 -0.78607,1.0958 0.0569,0.722 -0.23272,1.0638 -0.67149,0.7927 -0.46363,-0.2866 -0.60417,-0.041 -0.35215,0.6161 1.03622,2.7003 -2.63361,0.5117 -12.53851,-7.4778 l -5.2e-4,0 z"
       id="path3440"
       inkscape:connector-curvature="0"
       transform="translate(-182,-286.3623)" />
    <path'''
HTML +='       style="fill:#%s;fill-opacity:1"'%(RGB[8])
HTML +='''       d="m 382.47068,956.91185 c -16.55233,-12.63337 -32.12512,-27.89967 -45.72128,-44.82143 -27.35827,-34.05006 -46.01173,-74.69597 -53.76467,-117.15329 -2.3708,-12.98319 -3.49089,-24.24204 -3.90208,-39.22265 l -0.42545,-15.50003 45.67313,-0.1934 45.67313,-0.19341 0.45721,6.93431 c 1.39743,21.19389 6.33313,42.16536 13.8834,58.9896 1.10703,2.46677 2.29555,4.31027 2.64116,4.09667 0.34562,-0.2136 0.445,0.0896 0.22086,0.67367 -0.52166,1.35941 2.44306,7.23481 3.3636,6.66589 0.38146,-0.23576 0.52932,-6.1e-4 0.32856,0.52255 -0.45599,1.18829 6.05805,12.45026 6.90028,11.92973 0.33875,-0.20936 0.57087,0.19064 0.51584,0.88887 -0.0553,0.70214 0.33195,1.17988 0.86659,1.06895 0.53166,-0.11031 0.75425,0.14314 0.49462,0.56321 -0.91624,1.48251 14.32983,20.91717 15.73014,20.05174 0.37129,-0.22947 0.50951,0.0142 0.30718,0.54149 -0.46292,1.20634 9.26677,10.95839 10.63,10.65443 0.55117,-0.12289 1.01705,0.22664 1.0353,0.77673 0.0477,1.43731 7.8799,8.18391 9.01269,7.76344 0.52267,-0.194 0.7659,-0.0543 0.54049,0.31039 -0.22541,0.36471 0.3478,1.26423 1.2738,1.99894 1.96938,1.56254 3.50548,3.73853 1.96865,2.78871 -0.70781,-0.43745 -0.83801,-0.26201 -0.4861,0.65506 0.32391,0.8441 0.2049,1.08212 -0.36496,0.72992 -0.56351,-0.34825 -0.69124,-0.12031 -0.38288,0.68327 0.28532,0.7435 0.12296,1.13926 -0.4234,1.03214 -0.48737,-0.0955 -0.84111,0.39756 -0.78607,1.0958 0.0569,0.72196 -0.23271,1.06384 -0.67149,0.79266 -0.48554,-0.30007 -0.59337,-0.0125 -0.29091,0.7757 0.27493,0.71646 0.1838,1.06908 -0.21293,0.82389 -0.85589,-0.52897 -3.80654,5.05997 -3.09054,5.85392 0.28389,0.31481 0.0498,0.30159 -0.52029,-0.0293 -0.77878,-0.45214 -0.91696,-0.29034 -0.5558,0.65081 0.32391,0.8441 0.2049,1.08212 -0.36496,0.72993 -0.5614,-0.34697 -0.69197,-0.12224 -0.38848,0.66864 0.25141,0.65519 0.0922,1.41676 -0.35371,1.69237 -0.52004,0.3214 -0.62008,0.13346 -0.27895,-0.52406 0.29253,-0.56386 0.008,-0.37768 -0.63326,0.41372 -0.64081,0.79139 -0.99741,1.87598 -0.79241,2.41017 0.20499,0.53419 0.0802,0.79046 -0.2774,0.56948 -0.87648,-0.54169 -3.85796,4.60995 -3.24344,5.60427 0.31114,0.50342 0.13811,0.57154 -0.48056,0.18918 -0.70781,-0.43745 -0.83801,-0.26201 -0.4861,0.65506 0.32391,0.8441 0.2049,1.08212 -0.36496,0.72993 -0.5614,-0.34697 -0.69197,-0.12224 -0.38848,0.66864 0.25141,0.65519 0.0922,1.41676 -0.35371,1.69237 -0.52004,0.3214 -0.62008,0.13346 -0.27895,-0.52406 0.29253,-0.56386 0.008,-0.37768 -0.63326,0.41372 -0.64081,0.79139 -1.00799,1.84839 -0.81593,2.34888 0.19206,0.50049 -0.0157,1.13548 -0.46164,1.4111 -0.52004,0.3214 -0.62008,0.13346 -0.27895,-0.52407 0.29253,-0.56385 0.008,-0.37768 -0.63326,0.41372 -0.64082,0.7914 -1.00547,1.85498 -0.81032,2.36351 0.19514,0.50852 -0.0439,0.84642 -0.53134,0.75087 -0.48737,-0.0956 -0.84111,0.39756 -0.78607,1.09579 0.0569,0.72196 -0.23271,1.06385 -0.67149,0.79267 -0.47973,-0.29649 -0.59653,-0.0207 -0.30882,0.72902 0.28531,0.74351 0.12296,1.13927 -0.4234,1.03215 -0.48738,-0.0956 -0.84111,0.39756 -0.78607,1.0958 0.0569,0.72196 -0.23271,1.06384 -0.67149,0.79266 -0.48554,-0.30007 -0.59338,-0.0125 -0.29091,0.77569 0.32391,0.84411 0.2049,1.08213 -0.36496,0.72993 -0.56141,-0.34696 -0.69197,-0.12223 -0.38849,0.66864 0.25142,0.65519 0.0923,1.41676 -0.3537,1.69238 -0.52004,0.3214 -0.62008,0.13346 -0.27895,-0.52407 0.29253,-0.56385 0.008,-0.37768 -0.63326,0.41372 -0.64082,0.7914 -1.00799,1.8484 -0.81593,2.34889 0.19206,0.50048 -0.0157,1.13548 -0.46164,1.41109 -0.52004,0.3214 -0.62008,0.13346 -0.27895,-0.52407 0.29253,-0.56385 0.008,-0.37767 -0.63326,0.41373 -0.64082,0.79139 -1.00547,1.85498 -0.81032,2.3635 0.19514,0.50853 -0.0439,0.84642 -0.53134,0.75087 -0.48738,-0.0956 -0.84111,0.39756 -0.78607,1.0958 0.0569,0.72196 -0.23271,1.06384 -0.67149,0.79266 -0.48554,-0.30007 -0.59338,-0.0126 -0.29091,0.77569 0.32391,0.84411 0.2049,1.08213 -0.36496,0.72993 -0.56141,-0.34696 -0.69198,-0.12223 -0.38849,0.66864 0.25142,0.65519 0.0923,1.41676 -0.3537,1.69237 -0.52004,0.32141 -0.62008,0.13346 -0.27895,-0.52406 0.29253,-0.56386 0.008,-0.37768 -0.63326,0.41372 -0.64082,0.7914 -1.00799,1.8484 -0.81593,2.34888 0.19206,0.50049 -0.0157,1.13549 -0.46164,1.4111 -0.52004,0.3214 -0.62008,0.13346 -0.27895,-0.52407 0.29253,-0.56385 0.008,-0.37768 -0.63326,0.41373 -0.64082,0.79139 -1.00547,1.85497 -0.81032,2.3635 0.19514,0.50853 -0.0439,0.84642 -0.53134,0.75087 -0.48738,-0.0956 -0.84111,0.39756 -0.78607,1.09579 0.0569,0.72197 -0.23271,1.06385 -0.67149,0.79267 -0.47973,-0.29648 -0.59653,-0.0207 -0.30882,0.72903 0.28531,0.7435 0.12296,1.13926 -0.4234,1.03214 -0.48738,-0.0955 -0.84111,0.39757 -0.78607,1.0958 0.0569,0.72196 -0.23272,1.06385 -0.67149,0.79266 -0.48554,-0.30007 -0.59338,-0.0126 -0.29091,0.7757 0.32391,0.8441 0.2049,1.08212 -0.36497,0.72992 -0.5614,-0.34696 -0.69197,-0.12223 -0.38848,0.66865 0.25142,0.65519 0.0923,1.41676 -0.3537,1.69237 -0.52004,0.3214 -0.62008,0.13346 -0.27895,-0.52407 0.29253,-0.56385 0.008,-0.37768 -0.63326,0.41373 -0.64082,0.79139 -1.00799,1.84839 -0.81593,2.34888 0.19205,0.50049 -0.0157,1.13548 -0.46164,1.41109 -0.52004,0.32141 -0.62008,0.13346 -0.27896,-0.52406 0.29254,-0.56386 0.008,-0.37768 -0.63325,0.41372 -0.64082,0.79139 -1.00547,1.85498 -0.81032,2.3635 0.19514,0.50853 -0.0439,0.84643 -0.53134,0.75087 -0.48738,-0.0955 -0.84111,0.39756 -0.78607,1.0958 0.0569,0.72196 -0.23272,1.06385 -0.67149,0.79266 -0.48554,-0.30007 -0.59338,-0.0126 -0.29091,0.7757 0.26814,0.69876 0.18145,1.06763 -0.19606,0.83432 -0.37219,-0.23003 -0.96583,0.0984 -1.3192,0.72984 -0.53421,0.95457 -1.80272,0.26254 -7.52661,-4.10616 l 0,-1e-5 z"
       id="path3442"
       inkscape:connector-curvature="0"
       transform="translate(-182,-286.3623)" />
  </g>

   <!--<image
      width="891.01953"
      height="110.766312"
      xlink:href="data:image/png;base64,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 21CBvn37OgWEEF6vd9CgQXIPTlpamutLs0x3gKxd3zU1NX/+859nzZq1evVqIpo0aVJNTU11dXVh YeGaNWuGDh1aV1eXkZGhaZrTlUKI7OzslJQUublPRjkyUunfvz+sXiGE4F143YempqZgMFhbW2s7 RVVVTdM8Hs9bb701fvz4rVu3btu2LSUlxePx5OTkFBcXb9269b333vN4PKmpqc6ihBB5eXn2TVV2 dra9r3PAgAFSJiMjI9rr8UzCkE6vqamRb6oTUe/evZcsWfLTn/70scceW7Zs2ZIlSzRNIyJd130+ n9/vX758eX5+/rx581auXOmMU4UQAwcOFEIEg0F51dtOz8vLk50qIyMDgMzC136XIMdqXdfXrVs3 bNiwU6dOvf7660RUWVl5+eWXv/POO/v371+6dOmKFSuKi4vl1tpPP/30+eefv++++370ox+tXr1a RqWyNDmJO+d6j8cjhPD5fLbT09PTYTm9vXTO6CBvncvLy+XxyZMnA4EAANM05QERmabpFGhqagLg 9/uPHTsm46zKykr7ZW6me6JpWm1t7Z133vnoo49OnTr173//e1lZWVFR0YoVK+RS8HPPPVdaWvrp p5+uXr367NmzcrsuACKqqalpbGyUY1Zpaan9tYZTp07Jwk+dOsW3Wd0KRVGcoacMOM6dO3fPPffc dNNN48aNKyoqmjx5MhH96le/2rp169dff713796SkpK9e/euXLlSvkYkxzIiOnHihBBChqryATms 0UCWby8+d1V9GTicLi9PeaPy7LPPrlq1Sjr3N7/5ja7rcuHtn//854gRI9auXfunP/1pw4YNMsqR u60ByCudiGSII49hdQapTk4Kztt0JpHIObesrOw73/nO3Xfffcstt3z00UdyE+5jjz32wQcfjB8/ Pj09fdWqVTk5OTt37kxJSQGwe/fu66677qGHHpo1a9Zzzz2HmHO93+8H4Pf7T5w4IV18+vRpKXYe Bnc0ZJFBU58+fYLB4KFDh+Q99EcffZSamur1ehVFkTXs06ePYRi2wL59+zweT3p6us/n27dvn+zl X3zxRSAQkEs1THdD+khRlKFDh8r3R/x+f+/evdPS0ioqKsaOHTt79uyNGze+9tprVVVVx44d27Jl iwxQZAcYMGBARUVFZWWlLOq///1vjx49evToQUT79++XGxc+/vhjr9crA3C+3+pWyJUPeQO9ZMmS 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 RK5CYII= "
      id="image2993"
      x="-1187.1758"
      y="986.30841"
      transform="matrix(0,-1,1,0,0,0)" />-->
  <path'''
HTML +='    style="fill:#%s;fill-opacity:1" '%(RGB[7])
HTML +='''     d="m 305.26632,738.91545 -26.52461,-0.20105 0.47575,-6.37768 c 4.26182,-57.13213 24.92206,-108.61027 61.00292,-151.99813 13.10026,-15.75328 36.5505,-37.14986 52.70499,-48.08934 l 3.4702,-2.34994 1.91285,2.04446 c 1.05206,1.12445 1.46127,1.38752 0.90936,0.5846 -0.91287,-1.32802 -0.89205,-1.37264 0.2305,-0.49407 0.67869,0.53117 1.07769,1.37307 0.88666,1.87087 -0.19102,0.4978 0.39766,1.54131 1.30818,2.3189 1.64468,1.40455 1.64843,1.40425 0.57319,-0.0461 -0.99331,-1.33981 -0.98084,-1.38044 0.15168,-0.49408 0.67869,0.53118 1.07432,1.38184 0.87919,1.89036 -0.19514,0.50851 0.23497,1.38778 0.95579,1.95393 1.22329,0.96079 1.23766,0.93211 0.2157,-0.4305 -1.00644,-1.34192 -0.9952,-1.38183 0.1391,-0.49408 0.67869,0.53118 1.07769,1.37307 0.88666,1.87087 -0.19102,0.49781 0.39766,1.54131 1.30818,2.3189 1.6443,1.40423 1.64842,1.40392 0.6084,-0.0461 -0.91103,-1.27013 -0.9105,-1.33764 0.004,-0.51942 0.57817,0.51724 1.05503,1.50179 1.05968,2.18789 0.004,0.68611 0.50118,1.25568 1.10337,1.26573 0.60219,0.01 1.01053,0.53278 0.90742,1.16162 -0.1031,0.62885 0.54817,1.77111 1.44728,2.53836 1.61898,1.38157 1.62465,1.38095 0.58763,-0.0648 -0.91102,-1.27014 -0.91049,-1.33764 0.004,-0.51942 0.57817,0.51723 1.05503,1.50179 1.05969,2.18789 0.004,0.6861 0.50118,1.25568 1.10337,1.26573 0.60218,0.01 1.01053,0.53277 0.90742,1.16162 -0.1031,0.62884 0.54817,1.7711 1.44728,2.53836 1.61898,1.38157 1.62465,1.38094 0.58763,-0.0648 -0.91103,-1.27013 -0.9105,-1.33763 0.004,-0.51942 0.57817,0.51724 1.05503,1.50179 1.05969,2.1879 0.004,0.6861 0.50117,1.25568 1.10336,1.26572 0.60219,0.01 1.01053,0.53278 0.90742,1.16162 -0.1031,0.62885 0.54817,1.77111 1.44728,2.53837 1.61899,1.38157 1.62465,1.38094 0.58764,-0.0648 -0.91103,-1.27013 -0.9105,-1.33764 0.004,-0.51942 0.57816,0.51724 1.05503,1.50179 1.05968,2.18789 0.004,0.6861 0.50118,1.25568 1.10337,1.26573 0.60219,0.01 1.01053,0.53278 0.90742,1.16162 -0.1031,0.62884 0.54817,1.77111 1.44728,2.53836 1.61898,1.38157 1.62465,1.38095 0.58763,-0.0648 -0.91103,-1.27013 -0.91049,-1.33763 0.004,-0.51942 0.57817,0.51724 1.05503,1.50179 1.05969,2.1879 0.004,0.6861 0.50117,1.25568 1.10336,1.26573 0.60219,0.01 1.00844,0.54189 0.90278,1.18188 -0.17401,1.0539 1.61308,3.18318 2.67161,3.18318 0.23667,0 0.34608,0.36677 0.24314,0.81504 -0.17863,0.77786 1.76704,2.8346 2.68152,2.8346 0.23939,0 0.34162,0.28092 0.22717,0.62428 -0.29066,0.87197 1.34623,2.71982 2.0332,2.29525 0.31065,-0.19199 0.51978,0.22221 0.46474,0.92044 -0.055,0.69824 0.31052,1.1874 0.81234,1.08704 0.50183,-0.10037 0.83029,0.2281 0.72993,0.72992 -0.10037,0.50183 0.21628,0.83424 0.70365,0.73869 0.48738,-0.0956 0.71134,0.28181 0.49769,0.83857 -0.21365,0.55677 0.0131,1.26051 0.50401,1.56388 0.6083,0.37595 0.70444,0.24734 0.30195,-0.40391 -0.39368,-0.63699 -0.30565,-0.77943 0.26408,-0.42731 0.47004,0.2905 0.70671,0.76752 0.52591,1.06004 -0.45111,0.72992 0.80862,2.65194 1.73813,2.65194 0.4161,0 0.78894,0.32847 0.82853,0.72993 0.14808,1.50165 1.48559,3.31043 2.14606,2.90224 0.37672,-0.23283 0.49982,0.0591 0.27356,0.64874 -0.22627,0.58963 -1.71232,1.93297 -3.30235,2.9852 -1.59002,1.05223 -2.69794,2.22544 -2.46204,2.60713 0.2359,0.38169 0.001,0.5302 -0.52142,0.33003 -2.39582,-0.91756 -32.56378,26.98333 -31.67635,29.29593 0.20984,0.54683 0.0161,0.91606 -0.43057,0.82051 -1.11014,-0.23749 -9.43839,10.55089 -9.01564,11.67883 0.18628,0.49701 -0.0601,0.82548 -0.54746,0.72993 -0.48737,-0.0956 -0.84111,0.39756 -0.78606,1.09579 0.055,0.69824 -0.16133,1.10797 -0.48082,0.91051 -1.22376,-0.75633 -12.76936,19.50894 -12.10341,21.24437 0.233,0.60719 0.14018,0.92879 -0.20627,0.71468 -0.34645,-0.21412 -1.61842,1.82174 -2.82659,4.52413 -7.48378,16.73936 -12.37381,37.71827 -13.69317,58.74555 l -0.49373,7.84671 -19.09034,-0.17309 c -10.49969,-0.0952 -31.02642,-0.26356 -45.61496,-0.37414 z"
     id="path3438"
     inkscape:connector-curvature="0" />
  <path'''
HTML +='     style="fill:#%s;fill-opacity:1"'%(RGB[9])
HTML +='''     d="m 531.06101,1013.414 c -27.78525,-1.8129 -61.90664,-10.0973 -88.60142,-21.51154 -16.23711,-6.94273 -41.75819,-21.1104 -49.65196,-27.56359 l -2.48695,-2.03309 24.52919,-41.53104 c 13.49105,-22.84207 24.9569,-42.08065 25.47965,-42.7524 0.86096,-1.10633 1.64285,-0.76038 8.30249,3.67354 21.94726,14.61223 48.51954,24.75039 76.22462,29.0821 11.97733,1.87267 43.5486,1.86804 55.47445,-0.008 18.16161,-2.85717 36.13056,-8.19876 51.45985,-15.29734 7.69526,-3.56346 19.73187,-10.14991 23.85387,-13.05285 1.24065,-0.87374 2.12673,-1.10142 2.4227,-0.62252 0.25665,0.41528 0.82316,0.5347 1.25892,0.2654 0.47726,-0.29497 0.58192,-0.1493 0.26322,0.36637 -0.69625,1.12655 2.38935,6.08926 3.39832,5.46568 0.45616,-0.28192 0.56786,-0.13846 0.26886,0.34533 -0.62178,1.00607 0.84287,3.97057 1.70001,3.44084 0.33599,-0.20765 0.56586,0.19373 0.51082,0.89197 -0.0553,0.70213 0.33196,1.17987 0.86659,1.06895 0.53167,-0.11032 0.76283,0.12925 0.51369,0.53236 -0.65941,1.06694 1.00369,3.81265 1.95372,3.2255 0.48112,-0.29734 0.59988,-0.16453 0.29458,0.32944 -0.70189,1.1357 0.89713,3.93704 1.8952,3.3202 0.46587,-0.28792 0.60088,-0.16616 0.3199,0.28848 -0.66592,1.07748 2.40419,6.12296 3.36458,5.5294 0.44732,-0.27646 0.55641,-0.12905 0.25974,0.35097 -0.7019,1.1357 0.89712,3.93704 1.8952,3.3202 0.46587,-0.28792 0.60088,-0.16616 0.3199,0.28848 -0.66592,1.07748 2.40418,6.12296 3.36457,5.5294 0.44732,-0.27646 0.55642,-0.12905 0.25975,0.35097 -0.7019,1.1357 0.89712,3.93704 1.89519,3.3202 0.46587,-0.28792 0.60089,-0.16616 0.3199,0.28848 -0.66592,1.07749 2.40419,6.12296 3.36458,5.5294 0.45277,-0.27983 0.55584,-0.12812 0.2496,0.36739 -0.67838,1.09763 4.63157,9.71389 5.6127,9.10752 0.43041,-0.26601 0.52673,-0.10391 0.22671,0.38153 -0.67837,1.09763 4.63158,9.71389 5.6127,9.10752 0.43042,-0.26601 0.52674,-0.10391 0.22672,0.38153 -0.67837,1.09763 4.63158,9.71389 5.6127,9.10752 0.43555,-0.26918 0.52604,-0.10277 0.21648,0.39809 -0.29955,0.48468 0.75648,2.90056 2.41766,5.53084 l 2.94953,4.67026 -8.18737,5.30382 c -37.16019,24.0726 -81.40762,39.01589 -127.16547,42.94659 -4.28499,0.368 -13.8176,0.5851 -23.10561,0.6173 -8.00907,0.028 -15.83627,-0.082 -19.96008,-0.3511 l 0,0 z"
     id="path3460"
     inkscape:connector-curvature="0"
     sodipodi:nodetypes="csscscsscssscssssccsccssssssssscssssssscscscsccc" />
  <path'''
HTML +='     style="fill:#%s;fill-opacity:1"'%(RGB[10])
HTML +='''     d="m 684.51987,922.70421 c -13.97651,-22.7296 -25.51764,-41.52854 -25.64695,-41.77542 -0.12931,-0.24689 1.73926,-1.85777 4.15238,-3.57974 10.44568,-7.45388 24.40296,-20.54677 33.23081,-31.17278 8.73798,-10.51784 18.1233,-25.63673 23.96666,-38.60812 8.47801,-18.81988 14.58463,-44.91776 14.60443,-62.41497 l 0.006,-4.93197 44.55783,0 44.55782,0 0,8.40462 c 0,44.0945 -12.49146,90.80299 -34.50183,129.01035 -14.81123,25.7105 -36.06898,51.36605 -58.24593,70.29581 -7.57168,6.46302 -20.04779,16.07107 -20.89326,16.09023 -0.20664,0.005 -11.81104,-18.58842 -25.78754,-41.31801 z"
     id="path3462"
     inkscape:connector-curvature="0" />
  <path'''
HTML +='     style="fill:#%s;fill-opacity:1"'%(RGB[11])
HTML +='''     d="m 735.29122,739.09235 c -0.25214,-0.25214 -0.45844,-2.7154 -0.45844,-5.47391 0,-20.5417 -6.40355,-46.07713 -17.02661,-67.897 -13.4847,-27.69768 -34.82939,-51.83568 -61.20468,-69.21435 -3.92857,-2.58853 -7.24068,-4.97262 -7.36024,-5.29796 -0.20351,-0.55378 44.39791,-67.68124 45.36752,-68.28049 0.24572,-0.15187 5.18747,2.88218 10.98165,6.74233 39.43271,26.27052 71.03697,62.33645 91.80722,104.76793 15.06007,30.76618 24.64813,67.52271 25.99658,99.65986 l 0.21407,5.10204 -43.92932,0.17499 c -24.16112,0.0962 -44.13561,-0.0313 -44.38775,-0.28344 z"
     id="path3464"
     inkscape:connector-curvature="0" />
  <path'''
HTML +='     style="fill:#%s;fill-opacity:1"'%(RGB[12])
HTML +='''     d="m 444.42342,652.4139 c -24.7386,-22.38168 -28.53905,-26.07295 -27.95937,-27.15608 0.84999,-1.58822 13.11857,-13.00799 19.38914,-18.04769 7.04349,-5.6609 20.78231,-14.66292 28.92925,-18.95518 18.46229,-9.72695 39.10768,-16.40818 61.2068,-19.80766 9.98196,-1.53552 32.30222,-2.07641 43.57609,-1.05599 34.71906,3.14246 68.02634,15.86581 95.30739,36.40731 8.73504,6.57712 19.09259,15.8969 18.58314,16.72121 -0.20203,0.3269 -0.74415,0.44975 -1.20472,0.27302 -0.79088,-0.30349 -9.66326,8.02791 -9.66326,9.07405 0,0.26971 -0.25322,0.40597 -0.56272,0.3028 -0.93326,-0.31108 -19.51909,17.64213 -19.04982,18.40142 0.25444,0.41169 0.10279,0.49853 -0.36535,0.20921 -0.99593,-0.61552 -10.43884,8.34361 -9.83092,9.32725 0.24751,0.40047 0.0888,0.4821 -0.37718,0.19408 -0.48997,-0.30283 -2.72629,1.31792 -5.72152,4.14659 -2.70444,2.55405 -6.04996,5.6858 -7.43449,6.95945 l -2.51734,2.31573 -4.62135,-3.96009 c -9.84527,-8.43652 -21.66614,-15.02383 -34.75803,-19.36927 -9.98469,-3.31411 -16.62473,-4.67148 -26.43321,-5.40354 -30.04974,-2.24275 -60.70272,8.89609 -81.74839,29.70617 -3.12585,3.09087 -5.78024,5.61976 -5.89864,5.61976 -0.11839,0 -13.09887,-11.65615 -28.8455,-25.90255 z"
     id="path3466"
     inkscape:connector-curvature="0" />
  <path'''
HTML +='     style="fill:#%s;fill-opacity:1"'%(RGB[13])
HTML +='''     d="m 415.71633,851.98261 c -21.09229,-22.28058 -36.47513,-53.69909 -42.10572,-85.99839 -1.89925,-10.89488 -2.56992,-31.68044 -1.39127,-43.1188 2.90762,-28.21737 12.33101,-53.90198 28.44933,-77.54217 5.21302,-7.64576 13.48346,-18.02721 14.36147,-18.02721 0.26847,0 1.53346,1.07851 2.81108,2.39668 1.27762,1.31817 2.73112,2.24005 3.23,2.04861 0.49888,-0.19144 0.75137,-0.0962 0.56109,0.21172 -0.45457,0.7355 5.28896,6.36012 6.22199,6.09319 0.39599,-0.11329 0.76196,0.10014 0.81328,0.47429 0.15117,1.10223 5.6971,6.47351 6.49485,6.29031 0.40203,-0.0923 0.81106,0.13826 0.90894,0.51241 0.35592,1.36045 5.21003,5.80271 6.00666,5.49702 0.4502,-0.17276 1.18453,0.12688 1.63185,0.66587 0.44732,0.53898 0.56063,0.97997 0.25181,0.97997 -0.30882,0 0.63351,1.2238 2.09408,2.71955 1.46056,1.49575 2.98582,2.64371 3.38945,2.55102 0.40364,-0.0927 0.72485,0.0463 0.71379,0.3089 -0.0356,0.84437 5.3296,5.98792 6.06883,5.81817 0.39258,-0.0902 0.71379,0.0506 0.71379,0.3127 0,0.8632 6.04545,6.65622 6.77212,6.48935 0.39098,-0.0898 0.8,0.1408 0.90894,0.51241 0.41888,1.42883 5.22809,5.76634 6.21574,5.60609 0.57126,-0.0927 1.04552,0.18861 1.05392,0.62512 0.008,0.43651 0.23849,1.01688 0.51133,1.28972 0.27284,0.27284 -0.44829,1.75243 -1.60252,3.28798 -16.68832,22.20175 -23.35315,47.91859 -18.99725,73.30255 1.63247,9.51317 3.38345,15.25893 7.31987,24.01977 2.69406,5.99586 8.97875,16.24384 13.26738,21.63413 l 1.49484,1.87883 -3.68704,3.73342 c -2.02788,2.05338 -3.40579,3.73342 -3.06202,3.73342 0.34376,0 -0.5469,1.20016 -1.97925,2.66702 -1.43236,1.46686 -2.94856,2.53501 -3.36936,2.37365 -0.42079,-0.16134 -6.42524,5.37319 -13.34321,12.29898 -6.91798,6.92577 -12.28952,12.59232 -11.93677,12.59232 0.35275,0 -0.54193,1.21181 -1.98819,2.69291 -1.44626,1.48111 -2.918,2.51466 -3.27053,2.29678 -0.35253,-0.21788 -3.15289,2.10273 -6.22302,5.15692 l -5.58205,5.55305 -3.72823,-3.93826 0,0 z m 18.43618,-9.38045 c 1.26924,-1.30952 2.15465,-2.38095 1.96757,-2.38095 -0.18707,0 -1.3786,1.07143 -2.64784,2.38095 -1.26924,1.30953 -2.15465,2.38096 -1.96758,2.38096 0.18708,0 1.37861,-1.07143 2.64785,-2.38096 z m 30.61224,-29.93197 c 1.26924,-1.30952 2.15465,-2.38095 1.96758,-2.38095 -0.18708,0 -1.37861,1.07143 -2.64785,2.38095 -1.26924,1.30953 -2.15464,2.38095 -1.96757,2.38095 0.18708,0 1.37861,-1.07142 2.64784,-2.38095 z"
     id="path3468"
     inkscape:connector-curvature="0" />
  <path'''
HTML +='     style="fill:#%s;fill-opacity:1"'%(RGB[14])
HTML +='''     d="m 535.85319,910.9436 c -31.63739,-3.21231 -60.39777,-13.16059 -85.37415,-29.53113 -9.92876,-6.50771 -20.42426,-14.81088 -26.17574,-20.70806 l -4.06691,-4.16993 3.38663,-3.34472 c 1.86265,-1.8396 14.07875,-13.75961 27.1469,-26.48892 l 23.76027,-23.14419 6.23287,5.95866 c 7.92627,7.57755 13.56736,11.54938 23.86468,16.80283 17.11702,8.73271 33.29955,12.36358 52.07827,11.68479 11.57399,-0.41836 19.05856,-1.6967 29.36794,-5.01597 14.17008,-4.56228 27.02159,-11.91204 38.42214,-21.9736 l 6.10775,-5.39038 1.57162,1.67291 c 0.86438,0.9201 1.98486,1.51433 2.48993,1.32051 0.50508,-0.19382 0.7527,-0.0844 0.55028,0.24312 -0.56643,0.9165 12.37006,12.5008 13.31074,11.91944 0.46904,-0.28989 0.62213,-0.20432 0.36854,0.20598 -0.609,0.98539 12.91419,13.33907 13.92082,12.71693 0.45181,-0.27923 0.61811,-0.20146 0.38291,0.1791 -0.62405,1.00973 5.34452,6.60792 6.36963,5.97436 0.51565,-0.31868 0.67698,-0.24654 0.41101,0.18381 -0.63493,1.02734 12.22417,12.6518 13.30592,12.02838 0.477,-0.2749 0.63488,-0.24385 0.35084,0.069 -0.28403,0.31284 0.17515,1.3145 1.02041,2.2259 l 1.53684,1.6571 -5.44218,5.07795 c -28.25137,26.36057 -62.28074,42.71374 -101.02041,48.54642 -10.58668,1.59394 -34.11556,2.2909 -43.87755,1.29972 l 0,0 z"
     id="path3470"
     inkscape:connector-curvature="0" />
  <path'''
HTML +='     style="fill:#%s;fill-opacity:1"'%(RGB[15])
HTML +='''     d="m 659.93335,830.88442 c -14.68538,-13.28441 -27.20841,-24.6062 -27.82896,-25.15952 l -1.12828,-1.00604 1.53303,-1.7051 c 4.84271,-5.38626 10.06693,-13.29332 13.80514,-20.89463 4.72891,-9.61582 7.31107,-17.78645 9.03761,-28.59738 0.75281,-4.71383 1.03617,-16.67401 0.51547,-21.75712 C 653.666,710.275 644.66997,690.73466 629.52358,674.54312 l -2.0469,-2.18814 1.06697,-0.90024 c 0.58682,-0.49513 13.0053,-12.05373 27.59661,-25.68578 16.26143,-15.19238 26.46273,-24.95996 26.35674,-25.23616 -0.11431,-0.29787 0.0797,-0.43158 0.57226,-0.39447 1.45246,0.10941 11.93533,11.88595 18.23398,20.4842 10.46199,14.28162 19.05603,31.09605 24.42554,47.78912 9.47405,29.45352 10.57651,60.00691 3.24622,89.96599 -5.27425,21.55604 -15.30019,42.71256 -28.6915,60.54421 -3.55714,4.73664 -8.41584,10.58635 -11.49561,13.84034 l -2.15386,2.27572 -26.70068,-24.15349 z"
     id="path3478"
     inkscape:connector-curvature="0" />
  <text
     xml:space="preserve"
     style="font-size:40px;font-style:normal;font-weight:normal;line-height:125%;letter-spacing:0px;word-spacing:0px;fill:#000000;fill-opacity:1;stroke:none;font-family:Sans"
     x="263.82117"
     y="909.28473"
     id="text3480"
     sodipodi:linespacing="125%"><tspan
       sodipodi:role="line"
       id="tspan3482"
       x="263.82117"
       y="909.28473">3</tspan></text>
  <text
     xml:space="preserve"
     style="font-size:40.14570999px;font-style:normal;font-weight:normal;line-height:125%;letter-spacing:0px;word-spacing:0px;fill:#000000;fill-opacity:1;stroke:none;font-family:Sans"
     x="458.41043"
     y="638.09113"
     id="text3484"
     sodipodi:linespacing="125%"><tspan
       sodipodi:role="line"
       id="tspan3486"
       x="537.7043"
       y="540">7</tspan></text>
  <text
     xml:space="preserve"
     style="font-size:40px;font-style:normal;font-weight:normal;line-height:125%;letter-spacing:0px;word-spacing:0px;fill:#000000;fill-opacity:1;stroke:none;font-family:Sans"
     x="343.17361"
     y="648.55524"
     id="text3488"
     sodipodi:linespacing="125%"><tspan
       sodipodi:role="line"
       id="tspan3490"
       x="343.17361"
       y="648.55524">8</tspan></text>
  <text
     xml:space="preserve"
     style="font-size:40px;font-style:normal;font-weight:normal;line-height:125%;letter-spacing:0px;word-spacing:0px;fill:#000000;fill-opacity:1;stroke:none;font-family:Sans"
     x="344.20416"
     y="849.51276"
     id="text3492"
     sodipodi:linespacing="125%"><tspan
       sodipodi:role="line"
       id="tspan3494"
       x="344.20416"
       y="849.51276">9</tspan></text>
  <text
     xml:space="preserve"
     style="font-size:40px;font-style:normal;font-weight:normal;line-height:125%;letter-spacing:0px;word-spacing:0px;fill:#000000;fill-opacity:1;stroke:none;font-family:Sans"
     x="530.73401"
     y="972.14838"
     id="text3496"
     sodipodi:linespacing="125%"><tspan
       sodipodi:role="line"
       id="tspan3498"
       x="530.73401"
       y="972.14838">10</tspan></text>
  <text
     xml:space="preserve"
     style="font-size:40px;font-style:normal;font-weight:normal;line-height:125%;letter-spacing:0px;word-spacing:0px;fill:#000000;fill-opacity:1;stroke:none;font-family:Sans"
     x="735.81372"
     y="838.1767"
     id="text3500"
     sodipodi:linespacing="125%"><tspan
       sodipodi:role="line"
       id="tspan3502"
       x="735.81372"
       y="838.1767">11</tspan></text>
  <text
     xml:space="preserve"
     style="font-size:40px;font-style:normal;font-weight:normal;line-height:125%;letter-spacing:0px;word-spacing:0px;fill:#000000;fill-opacity:1;stroke:none;font-family:Sans"
     x="731.69147"
     y="653.70801"
     id="text3504"
     sodipodi:linespacing="125%"><tspan
       sodipodi:role="line"
       id="tspan3506"
       x="731.69147"
       y="653.70801">12</tspan></text>
  <text
     xml:space="preserve"
     style="font-size:40px;font-style:normal;font-weight:normal;line-height:125%;letter-spacing:0px;word-spacing:0px;fill:#000000;fill-opacity:1;stroke:none;font-family:Sans"
     x="529.70343"
     y="625.88312"
     id="text3508"
     sodipodi:linespacing="125%"><tspan
       sodipodi:role="line"
       id="tspan3510"
       x="529.70343"
       y="625.88312">13</tspan></text>
  <text
     xml:space="preserve"
     style="font-size:40px;font-style:normal;font-weight:normal;line-height:125%;letter-spacing:0px;word-spacing:0px;fill:#000000;fill-opacity:1;stroke:none;font-family:Sans"
     x="390.57898"
     y="755.73254"
     id="text3512"
     sodipodi:linespacing="125%"><tspan
       sodipodi:role="line"
       id="tspan3514"
       x="390.57898"
       y="755.73254">14</tspan></text>
  <text
     xml:space="preserve"
     style="font-size:40px;font-style:normal;font-weight:normal;line-height:125%;letter-spacing:0px;word-spacing:0px;fill:#000000;fill-opacity:1;stroke:none;font-family:Sans"
     x="527.64233"
     y="881.45984"
     id="text3516"
     sodipodi:linespacing="125%"><tspan
       sodipodi:role="line"
       id="tspan3518"
       x="527.64233"
       y="881.45984">15</tspan></text>
  <text
     xml:space="preserve"
     style="font-size:40px;font-style:normal;font-weight:normal;line-height:125%;letter-spacing:0px;word-spacing:0px;fill:#000000;fill-opacity:1;stroke:none;font-family:Sans"
     x="668.82788"
     y="753.67145"
     id="text3520"
     sodipodi:linespacing="125%"><tspan
       sodipodi:role="line"
       id="tspan3522"
       x="668.82788"
       y="753.67145">16</tspan></text>


  </g>
</svg>



</xml>



'''


if browser:
    import webbrowser
    f = open('polar illustration.html','w')
    f.write(HTML)
    f.close()
    webbrowser.open_new_tab('polar illustration.html')
    

    




