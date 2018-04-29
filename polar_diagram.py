#==============================================================================
# reg : dictionary with 17 keys and the values are Hex string(RGB:FFFFFF).
# max_v: the max vaue by color bar.
# min_v :the min value by color bar.
#==============================================================================
def open_website(reg,max_v,min_v):
    HTML= ''' 
    <xml><?xml version="1.0" encoding="UTF-8" standalone="no"?>
    <!-- Created with Inkscape (http://www.inkscape.org/) -->
    
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
       width="1587.4016"
       height="2245.0393"
       id="svg2"
       inkscape:version="0.92.1 r15371"
       sodipodi:docname="without digital.svg"
       viewBox="0 0 1488.189 2104.7244">
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
         inkscape:window-height="1001"
         id="namedview171"
         showgrid="false"
         inkscape:zoom="0.9206365"
         inkscape:cx="824.15729"
         inkscape:cy="1512.9124"
         inkscape:window-x="-9"
         inkscape:window-y="-9"
         inkscape:window-maximized="1"
         inkscape:current-layer="g4980"
         inkscape:measure-start="0,0"
         inkscape:measure-end="0,0" />
      <defs
         id="defs4">
        <inkscape:path-effect
           fuse_tolerance="0"
           vertical_pattern="false"
           prop_units="false"
           tang_offset="0"
           normal_offset="0"
           spacing="0"
           scale_y_rel="false"
           prop_scale="1"
           copytype="single_stretched"
           pattern="M 0,0 H 1"
           is_visible="true"
           id="path-effect3337"
           effect="skeletal" />
        <inkscape:path-effect
           fuse_tolerance="0"
           vertical_pattern="false"
           prop_units="false"
           tang_offset="0"
           normal_offset="0"
           spacing="0"
           scale_y_rel="false"
           prop_scale="1"
           copytype="single_stretched"
           pattern="M 0,0 H 1"
           is_visible="true"
           id="path-effect3327"
           effect="skeletal" />
        <linearGradient
           id="linearGradient7339">
          <stop
             offset="0"
             style="stop-color:#0f0002;stop-opacity:1"
             id="stop7341" />
        </linearGradient>
        <marker
           style="overflow:visible"
           id="Arrow1Lend"
           orient="auto"
           refY="0"
           refX="0">
          <path
             inkscape:connector-curvature="0"
             style="fill-rule:evenodd;stroke:#000000;stroke-width:1.00000003pt"
             id="path4696"
             transform="matrix(-0.8,0,0,-0.8,-10,0)"
             d="M 0,0 5,-5 -12.5,0 5,5 Z" />
        </marker>
        <marker
           style="overflow:visible"
           id="Arrow1Lstart"
           orient="auto"
           refY="0"
           refX="0">
          <path
             inkscape:connector-curvature="0"
             style="fill-rule:evenodd;stroke:#000000;stroke-width:1.00000003pt"
             id="path4693"
             transform="matrix(0.8,0,0,0.8,10,0)"
             d="M 0,0 5,-5 -12.5,0 5,5 Z" />
        </marker>
        <inkscape:path-effect
           fuse_tolerance="0"
           vertical_pattern="false"
           prop_units="false"
           tang_offset="0"
           normal_offset="0"
           spacing="0"
           scale_y_rel="false"
           prop_scale="1"
           copytype="single_stretched"
           pattern="M 0,0 H 1"
           is_visible="true"
           id="path-effect4677"
           effect="skeletal" />
        <inkscape:path-effect
           fuse_tolerance="0"
           vertical_pattern="false"
           prop_units="false"
           tang_offset="0"
           normal_offset="0"
           spacing="0"
           scale_y_rel="false"
           prop_scale="1"
           copytype="single_stretched"
           pattern="M 0,0 H 1"
           is_visible="true"
           id="path-effect4673"
           effect="skeletal" />
        <inkscape:path-effect
           fuse_tolerance="0"
           vertical_pattern="false"
           prop_units="false"
           tang_offset="0"
           normal_offset="0"
           spacing="0"
           scale_y_rel="false"
           prop_scale="1"
           copytype="single_stretched"
           pattern="M 0,0 H 1"
           is_visible="true"
           id="path-effect4641"
           effect="skeletal" />
        <inkscape:path-effect
           fuse_tolerance="0"
           vertical_pattern="false"
           prop_units="false"
           tang_offset="0"
           normal_offset="0"
           spacing="0"
           scale_y_rel="false"
           prop_scale="1"
           copytype="single_stretched"
           pattern="M 0,0 H 1"
           is_visible="true"
           id="path-effect4631"
           effect="skeletal" />
        <inkscape:path-effect
           fuse_tolerance="0"
           vertical_pattern="false"
           prop_units="false"
           tang_offset="0"
           normal_offset="0"
           spacing="0"
           scale_y_rel="false"
           prop_scale="1"
           copytype="single_stretched"
           pattern="M 0,0 H 1"
           is_visible="true"
           id="path-effect4627"
           effect="skeletal" />
        <inkscape:path-effect
           fuse_tolerance="0"
           vertical_pattern="false"
           prop_units="false"
           tang_offset="0"
           normal_offset="0"
           spacing="0"
           scale_y_rel="false"
           prop_scale="1"
           copytype="single_stretched"
           pattern="M 0,0 H 1"
           is_visible="true"
           id="path-effect4623"
           effect="skeletal" />
        <inkscape:path-effect
           is_visible="true"
           id="path-effect4621"
           effect="spiro" />
        <inkscape:path-effect
           fuse_tolerance="0"
           vertical_pattern="false"
           prop_units="false"
           tang_offset="0"
           normal_offset="0"
           spacing="0"
           scale_y_rel="false"
           prop_scale="1"
           copytype="single_stretched"
           pattern="M 0,0 H 1"
           is_visible="true"
           id="path-effect4617"
           effect="skeletal" />
        <inkscape:path-effect
           is_visible="true"
           id="path-effect4615"
           effect="spiro" />
        <inkscape:path-effect
           fuse_tolerance="0"
           vertical_pattern="false"
           prop_units="false"
           tang_offset="0"
           normal_offset="0"
           spacing="0"
           scale_y_rel="false"
           prop_scale="1"
           copytype="single_stretched"
           pattern="M 0,0 H 1"
           is_visible="true"
           id="path-effect4611"
           effect="skeletal" />
        <inkscape:path-effect
           is_visible="true"
           id="path-effect4609"
           effect="spiro" />
        <inkscape:path-effect
           fuse_tolerance="0"
           vertical_pattern="false"
           prop_units="false"
           tang_offset="0"
           normal_offset="0"
           spacing="0"
           scale_y_rel="false"
           prop_scale="1"
           copytype="single_stretched"
           pattern="M 0,0 H 1"
           is_visible="true"
           id="path-effect4605"
           effect="skeletal" />
        <inkscape:path-effect
           is_visible="true"
           id="path-effect4603"
           effect="spiro" />
        <inkscape:path-effect
           fuse_tolerance="0"
           vertical_pattern="false"
           prop_units="false"
           tang_offset="0"
           normal_offset="0"
           spacing="0"
           scale_y_rel="false"
           prop_scale="1"
           copytype="single_stretched"
           pattern="M 0,0 H 1"
           is_visible="true"
           id="path-effect4599"
           effect="skeletal" />
        <inkscape:path-effect
           is_visible="true"
           id="path-effect4597"
           effect="spiro" />
        <inkscape:path-effect
           fuse_tolerance="0"
           vertical_pattern="false"
           prop_units="false"
           tang_offset="0"
           normal_offset="0"
           spacing="0"
           scale_y_rel="false"
           prop_scale="1"
           copytype="single_stretched"
           pattern="M 0,0 H 1"
           is_visible="true"
           id="path-effect4593"
           effect="skeletal" />
        <inkscape:path-effect
           is_visible="true"
           id="path-effect4591"
           effect="spiro" />
        <inkscape:path-effect
           fuse_tolerance="0"
           vertical_pattern="false"
           prop_units="false"
           tang_offset="0"
           normal_offset="0"
           spacing="0"
           scale_y_rel="false"
           prop_scale="1"
           copytype="single_stretched"
           pattern="M 0,0 H 1"
           is_visible="true"
           id="path-effect4587"
           effect="skeletal" />
        <inkscape:path-effect
           is_visible="true"
           id="path-effect4585"
           effect="spiro" />
        <inkscape:path-effect
           fuse_tolerance="0"
           vertical_pattern="false"
           prop_units="false"
           tang_offset="0"
           normal_offset="0"
           spacing="0"
           scale_y_rel="false"
           prop_scale="1"
           copytype="single_stretched"
           pattern="M 0,0 H 1"
           is_visible="true"
           id="path-effect4581"
           effect="skeletal" />
        <inkscape:path-effect
           is_visible="true"
           id="path-effect4579"
           effect="spiro" />
        <inkscape:path-effect
           fuse_tolerance="0"
           vertical_pattern="false"
           prop_units="false"
           tang_offset="0"
           normal_offset="0"
           spacing="0"
           scale_y_rel="false"
           prop_scale="1"
           copytype="single_stretched"
           pattern="M 0,0 H 1"
           is_visible="true"
           id="path-effect4575"
           effect="skeletal" />
        <inkscape:path-effect
           is_visible="true"
           id="path-effect4573"
           effect="spiro" />
        <inkscape:path-effect
           fuse_tolerance="0"
           vertical_pattern="false"
           prop_units="false"
           tang_offset="0"
           normal_offset="0"
           spacing="0"
           scale_y_rel="false"
           prop_scale="1"
           copytype="single_stretched"
           pattern="M 0,0 H 1"
           is_visible="true"
           id="path-effect4569"
           effect="skeletal" />
        <inkscape:path-effect
           is_visible="true"
           id="path-effect4567"
           effect="spiro" />
        <inkscape:path-effect
           fuse_tolerance="0"
           vertical_pattern="false"
           prop_units="false"
           tang_offset="0"
           normal_offset="0"
           spacing="0"
           scale_y_rel="false"
           prop_scale="1"
           copytype="single_stretched"
           pattern="M 0,0 H 1"
           is_visible="true"
           id="path-effect4563"
           effect="skeletal" />
        <inkscape:path-effect
           is_visible="true"
           id="path-effect4561"
           effect="spiro" />
        <inkscape:path-effect
           fuse_tolerance="0"
           vertical_pattern="false"
           prop_units="false"
           tang_offset="0"
           normal_offset="0"
           spacing="0"
           scale_y_rel="false"
           prop_scale="1"
           copytype="single_stretched"
           pattern="M 0,0 H 1"
           is_visible="true"
           id="path-effect4557"
           effect="skeletal" />
        <inkscape:path-effect
           is_visible="true"
           id="path-effect4555"
           effect="spiro" />
        <inkscape:path-effect
           fuse_tolerance="0"
           vertical_pattern="false"
           prop_units="false"
           tang_offset="0"
           normal_offset="0"
           spacing="0"
           scale_y_rel="false"
           prop_scale="1"
           copytype="single_stretched"
           pattern="M 0,0 H 1"
           is_visible="true"
           id="path-effect4551"
           effect="skeletal" />
        <inkscape:path-effect
           is_visible="true"
           id="path-effect4549"
           effect="spiro" />
        <inkscape:path-effect
           fuse_tolerance="0"
           vertical_pattern="false"
           prop_units="false"
           tang_offset="0"
           normal_offset="0"
           spacing="0"
           scale_y_rel="false"
           prop_scale="1"
           copytype="single_stretched"
           pattern="M 0,0 H 1"
           is_visible="true"
           id="path-effect4545"
           effect="skeletal" />
        <inkscape:path-effect
           is_visible="true"
           id="path-effect4543"
           effect="spiro" />
        <inkscape:path-effect
           fuse_tolerance="0"
           vertical_pattern="false"
           prop_units="false"
           tang_offset="0"
           normal_offset="0"
           spacing="0"
           scale_y_rel="false"
           prop_scale="1"
           copytype="single_stretched"
           pattern="M 0,0 H 1"
           is_visible="true"
           id="path-effect4539"
           effect="skeletal" />
        <inkscape:path-effect
           is_visible="true"
           id="path-effect4537"
           effect="spiro" />
        <inkscape:path-effect
           fuse_tolerance="0"
           vertical_pattern="false"
           prop_units="false"
           tang_offset="0"
           normal_offset="0"
           spacing="0"
           scale_y_rel="false"
           prop_scale="1"
           copytype="single_stretched"
           pattern="M 0,0 H 1"
           is_visible="true"
           id="path-effect4533"
           effect="skeletal" />
        <inkscape:path-effect
           is_visible="true"
           id="path-effect4531"
           effect="spiro" />
        <inkscape:path-effect
           fuse_tolerance="0"
           vertical_pattern="false"
           prop_units="false"
           tang_offset="0"
           normal_offset="0"
           spacing="0"
           scale_y_rel="false"
           prop_scale="1"
           copytype="single_stretched"
           pattern="M 0,0 H 1"
           is_visible="true"
           id="path-effect3907"
           effect="skeletal" />
        <inkscape:path-effect
           is_visible="true"
           id="path-effect3905"
           effect="spiro" />
        <inkscape:path-effect
           fuse_tolerance="0"
           vertical_pattern="false"
           prop_units="false"
           tang_offset="0"
           normal_offset="0"
           spacing="0"
           scale_y_rel="false"
           prop_scale="1"
           copytype="single_stretched"
           pattern="M 0,0 H 1"
           is_visible="true"
           id="path-effect3893"
           effect="skeletal" />
        <inkscape:path-effect
           is_visible="true"
           id="path-effect3891"
           effect="spiro" />
        <inkscape:path-effect
           fuse_tolerance="0"
           vertical_pattern="false"
           prop_units="false"
           tang_offset="0"
           normal_offset="0"
           spacing="0"
           scale_y_rel="false"
           prop_scale="1"
           copytype="single_stretched"
           pattern="M 0,0 H 1"
           is_visible="true"
           id="path-effect3887"
           effect="skeletal" />
        <inkscape:path-effect
           is_visible="true"
           id="path-effect3885"
           effect="spiro" />
        <inkscape:path-effect
           fuse_tolerance="0"
           vertical_pattern="false"
           prop_units="false"
           tang_offset="0"
           normal_offset="0"
           spacing="0"
           scale_y_rel="false"
           prop_scale="1"
           copytype="single_stretched"
           pattern="M 0,0 H 1"
           is_visible="true"
           id="path-effect3881"
           effect="skeletal" />
        <inkscape:path-effect
           is_visible="true"
           id="path-effect3879"
           effect="spiro" />
        <inkscape:path-effect
           fuse_tolerance="0"
           vertical_pattern="false"
           prop_units="false"
           tang_offset="0"
           normal_offset="0"
           spacing="0"
           scale_y_rel="false"
           prop_scale="1"
           copytype="single_stretched"
           pattern="M 0,0 H 1"
           is_visible="true"
           id="path-effect3875"
           effect="skeletal" />
        <inkscape:path-effect
           is_visible="true"
           id="path-effect3873"
           effect="spiro" />
        <inkscape:path-effect
           fuse_tolerance="0"
           vertical_pattern="false"
           prop_units="false"
           tang_offset="0"
           normal_offset="0"
           spacing="0"
           scale_y_rel="false"
           prop_scale="1"
           copytype="single_stretched"
           pattern="M 0,0 H 1"
           is_visible="true"
           id="path-effect3869"
           effect="skeletal" />
        <inkscape:path-effect
           fuse_tolerance="0"
           vertical_pattern="false"
           prop_units="false"
           tang_offset="0"
           normal_offset="0"
           spacing="0"
           scale_y_rel="false"
           prop_scale="1"
           copytype="single_stretched"
           pattern="M 0,0 H 1"
           is_visible="true"
           id="path-effect3865"
           effect="skeletal" />
        <inkscape:path-effect
           fuse_tolerance="0"
           vertical_pattern="false"
           prop_units="false"
           tang_offset="0"
           normal_offset="0"
           spacing="0"
           scale_y_rel="false"
           prop_scale="1"
           copytype="single_stretched"
           pattern="M 0,0 H 1"
           is_visible="true"
           id="path-effect3861"
           effect="skeletal" />
        <linearGradient
           id="linearGradient3841">
          <stop
             offset="0"
             style="stop-color:#27221e;stop-opacity:1"
             id="stop3843" />
          <stop
             offset="0.25"
             style="stop-color:#1d1916;stop-opacity:0.74901962"
             id="stop3851" />
          <stop
             offset="0.5"
             style="stop-color:#13110f;stop-opacity:0.49803922"
             id="stop3849" />
          <stop
             offset="1"
             style="stop-color:#000000;stop-opacity:0"
             id="stop3845" />
        </linearGradient>
        <linearGradient
           gradientTransform="matrix(2.429435,0,0,2.3444055,2585.2352,677.546)"
           gradientUnits="userSpaceOnUse"
           xlink:href="#linearGradient3841"
           id="linearGradient3847"
           y2="243.79076"
           x2="-305.21628"
           y1="243.79076"
           x1="-1489.0695" />
        <linearGradient
           gradientTransform="matrix(0.9028961,0,0,0.93666666,33.973593,10.995438)"
           gradientUnits="userSpaceOnUse"
           xlink:href="#linearGradient7339"
           id="linearGradient7343"
           y2="435.48718"
           x2="532.95801"
           y1="435.48718"
           x1="98.292023" />
        <filter
           style="color-interpolation-filters:sRGB;"
           inkscape:label="Neon Draw"
           id="filter4888">
          <feBlend
             mode="normal"
             result="blend"
             in2="SourceGraphic"
             id="feBlend4858" />
          <feGaussianBlur
             in="blend"
             stdDeviation="3"
             result="blur1"
             id="feGaussianBlur4860" />
          <feColorMatrix
             values="1 0 0 0 0 0 1 0 0 0 0 0 1 0 0 0 0 0 50 0"
             result="color1"
             id="feColorMatrix4862" />
          <feComponentTransfer
             result="component1"
             id="feComponentTransfer4870">
            <feFuncR
               type="discrete"
               tableValues="0 0.3 0.3 0.3 0.3 0.6 0.6 0.6 0.6 1 1"
               id="feFuncR4864" />
            <feFuncG
               type="discrete"
               tableValues="0 0.3 0.3 0.3 0.3 0.6 0.6 0.6 0.6 1 1"
               id="feFuncG4866" />
            <feFuncB
               type="discrete"
               tableValues="0 0.3 0.3 0.3 0.3 0.6 0.6 0.6 0.6 1 1"
               id="feFuncB4868" />
          </feComponentTransfer>
          <feGaussianBlur
             in="component1"
             stdDeviation="3"
             result="blur2"
             id="feGaussianBlur4872" />
          <feColorMatrix
             values="1 0 0 0 0 0 1 0 0 0 0 0 1 0 0 0 0 0 50 0"
             result="color2"
             id="feColorMatrix4874" />
          <feComponentTransfer
             in="color2"
             result="component2"
             id="feComponentTransfer4882">
            <feFuncR
               type="table"
               tableValues="0 1 1 1 0 0 0 1 1 1 0 0 0 1 1 1 0 0 0 1"
               id="feFuncR4876" />
            <feFuncG
               type="table"
               tableValues="0 1 1 1 0 0 0 1 1 1 0 0 0 1 1 1 0 0 0 1"
               id="feFuncG4878" />
            <feFuncB
               type="table"
               tableValues="0 1 1 1 0 0 0 1 1 1 0 0 0 1 1 1 0 0 0 1"
               id="feFuncB4880" />
          </feComponentTransfer>
          <feComposite
             in="component2"
             in2="blur2"
             k3="1"
             operator="arithmetic"
             k2="1"
             result="composite1"
             id="feComposite4884" />
          <feComposite
             in="composite1"
             in2="SourceGraphic"
             operator="in"
             result="fbSourceGraphic"
             id="feComposite4886" />
          <feColorMatrix
             result="fbSourceGraphicAlpha"
             in="fbSourceGraphic"
             values="0 0 0 -1 0 0 0 0 -1 0 0 0 0 -1 0 0 0 0 1 0"
             id="feColorMatrix4890" />
          <feBlend
             in2="fbSourceGraphicAlpha"
             id="feBlend4892"
             mode="normal"
             result="blend"
             in="fbSourceGraphic" />
          <feGaussianBlur
             id="feGaussianBlur4894"
             in="blend"
             stdDeviation="3"
             result="blur1" />
          <feColorMatrix
             id="feColorMatrix4896"
             values="1 0 0 0 0 0 1 0 0 0 0 0 1 0 0 0 0 0 50 0"
             result="color1" />
          <feComponentTransfer
             id="feComponentTransfer4898"
             result="component1">
            <feFuncR
               id="feFuncR4900"
               type="discrete"
               tableValues="0 0.3 0.3 0.3 0.3 0.6 0.6 0.6 0.6 1 1" />
            <feFuncG
               id="feFuncG4902"
               type="discrete"
               tableValues="0 0.3 0.3 0.3 0.3 0.6 0.6 0.6 0.6 1 1" />
            <feFuncB
               id="feFuncB4904"
               type="discrete"
               tableValues="0 0.3 0.3 0.3 0.3 0.6 0.6 0.6 0.6 1 1" />
          </feComponentTransfer>
          <feGaussianBlur
             id="feGaussianBlur4906"
             in="component1"
             stdDeviation="3"
             result="blur2" />
          <feColorMatrix
             id="feColorMatrix4908"
             values="1 0 0 0 0 0 1 0 0 0 0 0 1 0 0 0 0 0 50 0"
             result="color2" />
          <feComponentTransfer
             id="feComponentTransfer4910"
             in="color2"
             result="component2">
            <feFuncR
               id="feFuncR4912"
               type="discrete"
               tableValues="0 1 1 1 0 0 0 1 1 1 0 0 0 1 1 1 0 0 0 1" />
            <feFuncG
               id="feFuncG4914"
               type="discrete"
               tableValues="0 1 1 1 0 0 0 1 1 1 0 0 0 1 1 1 0 0 0 1" />
            <feFuncB
               id="feFuncB4916"
               type="discrete"
               tableValues="0 1 1 1 0 0 0 1 1 1 0 0 0 1 1 1 0 0 0 1" />
          </feComponentTransfer>
          <feComposite
             in2="blur2"
             id="feComposite4918"
             in="component2"
             k3="1"
             operator="arithmetic"
             k2="1"
             result="composite1" />
          <feComposite
             in2="fbSourceGraphic"
             id="feComposite4920"
             in="composite1"
             operator="in"
             result="fbSourceGraphic" />
          <feColorMatrix
             result="fbSourceGraphicAlpha"
             in="fbSourceGraphic"
             values="0 0 0 -1 0 0 0 0 -1 0 0 0 0 -1 0 0 0 0 1 0"
             id="feColorMatrix4922" />
          <feBlend
             in2="fbSourceGraphicAlpha"
             id="feBlend4924"
             mode="multiply"
             result="blend"
             in="fbSourceGraphic" />
          <feGaussianBlur
             id="feGaussianBlur4926"
             in="blend"
             stdDeviation="3"
             result="blur1" />
          <feColorMatrix
             id="feColorMatrix4928"
             values="1 0 0 0 0 0 1 0 0 0 0 0 1 0 0 0 0 0 50 0"
             result="color1" />
          <feComponentTransfer
             id="feComponentTransfer4930"
             result="component1">
            <feFuncR
               id="feFuncR4932"
               type="discrete"
               tableValues="0 0.3 0.3 0.3 0.3 0.6 0.6 0.6 0.6 1 1" />
            <feFuncG
               id="feFuncG4934"
               type="discrete"
               tableValues="0 0.3 0.3 0.3 0.3 0.6 0.6 0.6 0.6 1 1" />
            <feFuncB
               id="feFuncB4936"
               type="discrete"
               tableValues="0 0.3 0.3 0.3 0.3 0.6 0.6 0.6 0.6 1 1" />
          </feComponentTransfer>
          <feGaussianBlur
             id="feGaussianBlur4938"
             in="component1"
             stdDeviation="3"
             result="blur2" />
          <feColorMatrix
             id="feColorMatrix4940"
             values="1 0 0 0 0 0 1 0 0 0 0 0 1 0 0 0 0 0 50 0"
             result="color2" />
          <feComponentTransfer
             id="feComponentTransfer4942"
             in="color2"
             result="component2">
            <feFuncR
               id="feFuncR4944"
               type="discrete"
               tableValues="0 1 1 1 0 0 0 1 1 1 0 0 0 1 1 1 0 0 0 1" />
            <feFuncG
               id="feFuncG4946"
               type="discrete"
               tableValues="0 1 1 1 0 0 0 1 1 1 0 0 0 1 1 1 0 0 0 1" />
            <feFuncB
               id="feFuncB4948"
               type="discrete"
               tableValues="0 1 1 1 0 0 0 1 1 1 0 0 0 1 1 1 0 0 0 1" />
          </feComponentTransfer>
          <feComposite
             in2="blur2"
             id="feComposite4950"
             in="component2"
             k3="1"
             operator="arithmetic"
             k2="1"
             result="composite1" />
          <feComposite
             in2="fbSourceGraphic"
             id="feComposite4952"
             in="composite1"
             operator="in"
             result="fbSourceGraphic" />
          <feColorMatrix
             result="fbSourceGraphicAlpha"
             in="fbSourceGraphic"
             values="0 0 0 -1 0 0 0 0 -1 0 0 0 0 -1 0 0 0 0 1 0"
             id="feColorMatrix4954" />
          <feBlend
             in2="fbSourceGraphicAlpha"
             id="feBlend4956"
             mode="multiply"
             result="blend"
             in="fbSourceGraphic" />
          <feGaussianBlur
             id="feGaussianBlur4958"
             in="blend"
             stdDeviation="3"
             result="blur1" />
          <feColorMatrix
             id="feColorMatrix4960"
             values="1 0 0 0 0 0 1 0 0 0 0 0 1 0 0 0 0 0 50 0"
             result="color1" />
          <feComponentTransfer
             id="feComponentTransfer4962"
             result="component1">
            <feFuncR
               id="feFuncR4964"
               type="discrete"
               tableValues="0 0.3 0.3 0.3 0.3 0.6 0.6 0.6 0.6 1 1" />
            <feFuncG
               id="feFuncG4966"
               type="discrete"
               tableValues="0 0.3 0.3 0.3 0.3 0.6 0.6 0.6 0.6 1 1" />
            <feFuncB
               id="feFuncB4968"
               type="discrete"
               tableValues="0 0.3 0.3 0.3 0.3 0.6 0.6 0.6 0.6 1 1" />
          </feComponentTransfer>
          <feGaussianBlur
             id="feGaussianBlur4970"
             in="component1"
             stdDeviation="3"
             result="blur2" />
          <feColorMatrix
             id="feColorMatrix4972"
             values="1 0 0 0 0 0 1 0 0 0 0 0 1 0 0 0 0 0 50 0"
             result="color2" />
          <feComponentTransfer
             id="feComponentTransfer4974"
             in="color2"
             result="component2">
            <feFuncR
               id="feFuncR4976"
               type="discrete"
               tableValues="0 1 1 1 0 0 0 1 1 1 0 0 0 1 1 1 0 0 0 1" />
            <feFuncG
               id="feFuncG4978"
               type="discrete"
               tableValues="0 1 1 1 0 0 0 1 1 1 0 0 0 1 1 1 0 0 0 1" />
            <feFuncB
               id="feFuncB4980"
               type="discrete"
               tableValues="0 1 1 1 0 0 0 1 1 1 0 0 0 1 1 1 0 0 0 1" />
          </feComponentTransfer>
          <feComposite
             in2="blur2"
             id="feComposite4982"
             in="component2"
             k3="1"
             operator="arithmetic"
             k2="1"
             result="composite1" />
          <feComposite
             in2="fbSourceGraphic"
             id="feComposite4984"
             in="composite1"
             operator="in"
             result="composite2" />
        </filter>
      </defs>
      <metadata
         id="metadata7">
        <rdf:RDF>
          <cc:Work
             rdf:about="">
            <dc:format>image/svg+xml</dc:format>
            <dc:type
               rdf:resource="http://purl.org/dc/dcmitype/StillImage" />
            <dc:title />
          </cc:Work>
        </rdf:RDF>
      </metadata>
      <path
         inkscape:connector-curvature="0"
         id="path3869"
         d="m 268.41797,738.41493 c -27.57659,0.80433 -55.21743,-0.49314 -82.81311,0.49438 -4.10422,3.17011 -1.73793,9.89547 -1.7102,14.54224 0.11251,108.58089 49.52764,216.47668 132.70386,286.76885 5.63746,4.5446 11.15451,10.4641 18.09631,12.9144 5.94789,-1.4562 6.54273,-9.0139 10.22726,-13.1342 14.59585,-25.0789 29.91741,-49.79462 43.79252,-75.25815 -1.57616,-7.65 -10.49713,-9.87338 -15.23072,-15.30028 -58.04985,-48.74214 -94.35634,-123.18547 -94.17115,-199.26455 -0.66921,-3.92155 1.15015,-11.53218 -4.7937,-11.51001 -2.01583,-0.32844 -4.06589,-0.31901 -6.10107,-0.25268 z"
         '''
    HTML += 'style="fill:#%s;stroke-width:0.966142"/>'%(reg[2])
    HTML += '''
    	 
      <path
         inkscape:connector-curvature="0"
         id="path3873"
         d="m 332.7594,449.96888 c -12.78798,7.58337 -23.72969,18.32591 -34.53641,28.61511 -69.38964,66.69736 -110.12387,161.19577 -114.20932,256.88477 -1.29652,5.40741 5.85418,5.61304 9.43907,4.87574 27.90158,-0.35439 55.97024,0.75005 83.76528,-0.56727 4.13852,-4.14156 1.72566,-10.73388 3.28938,-15.99426 5.98632,-65.97068 38.63387,-128.91095 88.74158,-172.1846 8.24631,-7.82587 17.76009,-14.41089 26.24236,-21.79368 1.16885,-5.62146 -5.55669,-8.59206 -7.71607,-13.16895 -18.01219,-22.16729 -34.18825,-45.91516 -53.88428,-66.53319 -0.36466,-0.11744 -0.75053,-0.14811 -1.13159,-0.13367 z"
         '''
    HTML += 'style="fill:#%s;stroke-width:0.966142"'%(reg[1])
    HTML +='''
    	 />
      <path
         inkscape:connector-curvature="0"
         id="path3875"
         d="m 541.09315,375.68115 c -55.47814,0.46506 -110.47105,16.28195 -159.54346,41.99524 -16.1628,8.7929 -32.36229,18.44578 -46.6095,30.10255 -0.94463,5.69402 5.65568,8.66673 8.06224,13.18862 18.3093,21.89631 35.46224,44.85323 53.31654,67.0189 5.45616,1.07711 8.93409,-4.76151 13.82374,-6.35578 42.29143,-25.00439 91.27617,-38.83167 140.49023,-38.20661 49.07219,-1.18569 97.6416,13.09184 140.3009,36.85731 3.22472,2.17185 6.74365,0.26136 7.83078,-3.15109 17.3053,-26.59488 35.94608,-52.5202 52.3505,-79.57963 -1.21556,-5.58058 -8.32608,-6.2374 -12.07216,-9.80421 -47.36842,-29.01924 -102.11421,-46.50175 -157.43087,-51.32307 -13.45346,-0.75591 -26.99202,-0.70127 -40.51894,-0.74223 z"
         '''
    HTML += 'style="fill:#%s;stroke-width:0.966142"'%(reg[0])
    HTML +='''	 />
      <path
         inkscape:connector-curvature="0"
         id="path3881"
         d="m 389.75099,963.16407 c -4.34231,1.80338 -5.0358,8.06138 -8.0713,11.42578 -15.21516,25.96615 -31.36638,51.64505 -45.36438,78.16595 1.54748,6.5684 9.27828,8.509 13.81531,12.7038 62.7271,41.8372 138.68495,64.5244 214.2473,60.7528 56.8288,-1.1311 112.96285,-17.5661 162.60939,-45.0972 13.04454,-7.503 26.17764,-15.2832 37.85156,-24.7596 1.18236,-5.959 -5.20486,-9.8066 -7.01752,-15.079 -15.40129,-24.861 -30.14241,-50.28809 -46.16729,-74.66834 -5.20461,-1.88972 -9.17664,3.92756 -13.77922,5.59603 -77.36321,48.73281 -179.31508,55.12691 -262.16943,16.45003 -15.8104,-6.9975 -30.52615,-16.32384 -45.06454,-25.45181 -0.29326,-0.0489 -0.59355,-0.0782 -0.88988,-0.0384 z"
         '''
    HTML += 'style="fill:#%s;stroke-width:0.966142"'%(reg[3])
    HTML +='''
    	 />
      <g
         transform="translate(182,286.3623)"
         style="display:inline"
         id="layer1">
        <path
           inkscape:connector-curvature="0"
           style="opacity:0.33780003;fill:none;stroke:#000000;stroke-width:2.37699533;stroke-linecap:square;stroke-linejoin:bevel;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:0.06802721"
           id="path3053"
           transform="matrix(0.41161835,0,0,0.42654737,-1064.1303,-289.00547)"
           d="m -994.28572,630.93359 a 1.428575,7.1428746 0 1 1 -2.85715,0 1.428575,7.1428746 0 1 1 2.85715,0 z" />
        <path
           inkscape:connector-curvature="0"
           style="opacity:0.02000002;fill:none;stroke:#000000;stroke-width:2.37699533;stroke-linecap:square;stroke-linejoin:bevel;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:0.06802721"
           id="path3059"
           transform="matrix(0.41161835,0,0,0.42654737,-1064.1303,-289.00547)"
           d="m -380.00006,553.79077 a 714.28572,581.4286 0 1 1 -1428.57144,0 714.28572,581.4286 0 1 1 1428.57144,0 z" />
        <path
           inkscape:connector-curvature="0"
           style="opacity:0;fill:none;stroke:url(#linearGradient3847);stroke-width:2.37699533;stroke-linecap:square;stroke-linejoin:bevel;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
           id="path3831"
           transform="matrix(0.41161835,0,0,0.42654737,-1064.1303,-289.00547)"
           d="m -305.71429,243.79076 a 591.42861,442.85716 0 1 1 -1182.85721,0 591.42861,442.85716 0 1 1 1182.85721,0 z" />
        <path
           inkscape:connector-curvature="0"
           style="opacity:0;fill:none;stroke:#272c3c;stroke-width:0.99599999;stroke-linecap:square;stroke-linejoin:miter;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
           id="path3895"
           d="m -1547.6529,-459.62192 c -26.6009,9.73661 -53.9289,17.09352 -80.8686,25.72405 -19.779,6.48257 -39.1691,14.25242 -57.8928,23.52101 -9.0907,4.50003 -20.0558,10.54026 -29.0258,15.39892 -33.3266,19.89353 6.4889,-3.96727 10.9105,-5.99472 4.2109,-1.9309 -7.6805,5.26837 -11.4523,8.00577 -5.0733,3.682 -13.0924,9.82957 -17.9525,14.13562 -2.2086,1.95693 -4.2542,4.10333 -6.3813,6.15498 -5.4739,5.82987 -10.6417,12.16319 -13.2058,19.97337 -1.21,3.68568 -1.1797,4.65606 -1.7144,8.44677 -0.7645,7.66672 -0.8809,15.3733 -0.8192,23.07322 -0.186,6.8463 0.1466,13.69118 0.029,20.53722 0.01,5.55701 -0.5937,11.08308 -0.831,16.62488 -0.4782,2.5761 0.428,6.13165 -1.3538,8.29891 -2.1505,-8.17184 -19.3275,13.70523 -15.8218,7.04241 0,0 17.6143,-8.01325 17.6143,-8.01325 v 0 c -3.7971,5.74188 -13.7052,16.57287 -17.8375,9.441 -1.5342,-0.24287 -1.1144,-5.62939 -1.3504,-6.86954 -0.2345,-5.24126 -0.8541,-10.46527 -0.8601,-15.72279 -0.164,-6.7846 0.1006,-13.57805 -0.3103,-20.35694 -0.161,-7.61632 -0.7263,-15.23255 -0.3253,-22.8486 0.97,-10.61574 2.5714,-18.61938 8.8019,-27.51241 1.4266,-1.85957 2.7542,-3.80561 4.28,-5.5787 3.3208,-3.8592 8.8196,-9.09663 12.5421,-12.28325 21.2858,-18.22166 46.6112,-30.35635 70.2124,-44.98412 4.8243,-2.60791 9.602,-5.31059 14.4729,-7.82372 23.0383,-11.8864 47.0863,-21.613 71.6885,-29.4105 13.6957,-4.17577 27.3582,-8.11434 41.3242,-11.21751 4.0118,-0.89139 16.0425,-3.39765 20.6811,-3.93161 2.0633,-0.23751 4.1498,-0.13725 6.2247,-0.20587 0,0 -20.7789,16.3754 -20.7789,16.3754 z" />
        <path
           inkscape:connector-curvature="0"
           style="opacity:0;fill:none;stroke:#272c3c;stroke-width:0.99599999;stroke-linecap:square;stroke-linejoin:miter;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
           id="path3897"
           d="m -1586.3161,-456.06057 c -0.3077,0.52097 -0.5839,1.06334 -0.923,1.56291 -2.4703,3.6392 -5.4593,6.9369 -8.2536,10.3006 -5.8521,7.04454 -2.7858,3.39868 -9.0815,10.78368 -10.1887,11.44108 -20.2517,22.99841 -30.438,34.44199 -6.6666,7.46775 -13.1555,15.16822 -18.1275,23.968 -4.8857,7.96738 -7.7569,16.87053 -10.6458,25.74366 -2.653,7.42886 -4.0683,15.1969 -5.6692,22.91355 -1.5324,7.62796 -2.6577,15.33409 -3.8526,23.02754 -0.9287,6.43247 -1.873,12.85941 -2.9979,19.25866 -0.4663,3.45226 -1.1919,6.85152 -1.8331,10.27005 0.09,-0.55948 -0.3456,1.71811 -0.7244,1.37411 -0.368,-0.3342 -0.2002,-1.57397 -0.6463,-1.36575 -15.0919,7.04358 -17.4116,14.75115 -15.0044,7.64651 0,0 18.6015,-8.57766 18.6015,-8.57766 v 0 c -4.8931,6.87922 -2.8019,4.39875 -17.8729,12.44354 -0.4833,0.25797 -0.7537,-0.81448 -1.1663,-1.18124 -0.1719,-0.15278 -0.4502,-0.176 -0.5784,-0.36948 -0.1841,-0.27798 -0.2022,-0.64096 -0.3032,-0.96144 0.2946,-3.10971 0.6971,-6.19342 0.2829,-9.32066 -0.174,-6.15412 0.5013,-12.23176 0.9723,-18.35737 0.8315,-7.83935 2.3134,-15.531 3.8662,-23.24828 1.5837,-7.53429 2.851,-15.13825 4.674,-22.61581 0.6874,-2.91511 1.3264,-5.88078 2.2558,-8.7278 1.9793,-6.06363 4.6809,-11.88843 7.7198,-17.44769 4.8918,-7.97809 9.9569,-15.82566 15.5814,-23.28098 8.6378,-11.76557 18.0917,-22.89043 27.9912,-33.5297 8.8426,-9.3969 17.7392,-18.80083 27.7759,-26.85422 0,0 18.3971,-7.89672 18.3971,-7.89672 z" />
        <path
           inkscape:connector-curvature="0"
           style="opacity:0;fill:none;stroke:#272c3c;stroke-width:0.99599999;stroke-linecap:square;stroke-linejoin:miter;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
           id="path3899"
           d="m -1411.3585,-492.32684 c 10.6363,-5.96443 21.0357,-12.37239 31.9088,-17.8933 2.7993,-1.42135 -5.0607,3.7169 -7.6067,5.55371 -3.5287,2.54574 -7.0209,5.14461 -10.6173,7.59381 -15.8541,10.79688 -32.3405,20.65124 -48.7292,30.5998 -46.5101,27.50559 -91.5413,57.47348 -134.2292,90.62684 -10.0127,7.77633 -19.7848,15.85752 -29.6773,23.78628 -46.3625,38.65269 -87.983,82.67427 -124.7158,130.54132 -6.7017,8.73317 -13.005,17.76499 -19.5076,26.64749 -21.4165,31.50143 -41.2645,64.21849 -58.1587,98.390459 -8.3758,16.941741 -10.6924,23.220495 -17.7926,40.247583 -10.8433,26.19982 -17.557,53.6479455 -20.5632,81.776922 -1.3804,16.751654 -1.2461,33.575773 -1.1342,50.368826 0.4373,17.375949 4.5476,34.37072 7.95,51.34041 3.897,18.17675 8.482,36.20906 13.2619,54.17294 3.6473,13.75788 7.8022,27.30916 12.8611,40.60921 1.9362,3.57223 3.1418,15.413 9.0782,14.1331 12.1314,-9.7479 19.4865,-11.78043 -31.7894,17.46546 -0.652,0.3719 1.2835,-0.78423 1.8789,-1.24142 1.205,-0.92536 2.2813,-2.0072 3.4266,-3.00554 2.281,-2.17158 4.3648,-4.49229 6.3949,-6.89781 0,0 39.7866,-16.84944 39.7866,-16.84944 v 0 c -2.0796,2.41056 -3.8825,5.11629 -6.3526,7.13187 -3.3504,4.1984 0.4696,-0.32597 -3.2796,3.3426 -12.289,12.02463 -27.9814,25.68884 -45.4047,24.73955 -7.1591,-3.11564 -9.3024,-10.73884 -11.8271,-17.58998 -5.3448,-13.34024 -9.6666,-26.97433 -13.4357,-40.84628 -4.8574,-18.0287 -9.6196,-36.10373 -13.5141,-54.36708 -3.3847,-17.27066 -7.4607,-34.54875 -8.087,-52.200619 -0.155,-16.871848 -0.4759,-33.765884 0.6124,-50.616175 2.4017,-28.241571 8.25,-55.942026 18.7683,-82.364585 6.7556,-17.010882 8.9987,-23.448039 17.0833,-40.369824 16.3767,-34.278017 35.9226,-67.041077 56.954,-98.635777 6.4104,-8.92184 12.6038,-18.00356 19.2311,-26.7655 36.3961,-48.11982 77.7747,-92.40303 123.8916,-131.3334 9.8966,-7.98388 19.6699,-16.12318 29.6899,-23.95163 43.1355,-33.70091 88.7098,-64.12485 135.917,-91.80955 16.7537,-10.02284 33.6256,-19.96776 49.9303,-30.71945 6.4935,-4.28194 12.4341,-9.38654 19.0541,-13.47009 14.0266,-8.65231 28.3007,-16.8967 42.4511,-25.34505 0,0 -33.7081,27.20432 -33.7081,27.20432 z" />
        <path
           inkscape:connector-curvature="0"
           style="opacity:0;fill:none;stroke:#272c3c;stroke-width:0.99599999;stroke-linecap:square;stroke-linejoin:miter;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
           id="path3901"
           d="m -1325.4935,-501.46955 c -5.0269,13.79571 -9.3814,27.81689 -13.133,42.03794 -4.3734,17.90767 -6.6891,36.24647 -8.6149,54.58052 -1.3142,13.2997 -2.7149,26.59211 -3.86,39.90907 -0.4056,5.12431 -0.2238,2.68665 -0.5515,7.31246 0,0 -17.208,8.95619 -17.208,8.95619 v 0 c 0.1879,-4.58593 0.076,-2.16913 0.3439,-7.24996 0.8619,-13.26093 2.1526,-26.48661 3.3682,-39.71638 1.8076,-18.42483 4.0943,-36.84005 8.3966,-54.84503 3.821,-14.45718 8.1132,-28.81791 13.9463,-42.55939 0,0 17.3124,-8.42542 17.3124,-8.42542 z" />
        <path
           inkscape:connector-curvature="0"
           style="opacity:0;fill:#000000;stroke:#000000;stroke-width:0.99599999;stroke-linecap:square;stroke-linejoin:miter;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
           id="path4679"
           transform="translate(0,-84)"
           d="m 592.5,388.61218 a 254.375,281.25 0 1 1 -508.75,0 254.375,281.25 0 1 1 508.75,0 z" />
        <path
           inkscape:connector-curvature="0"
           id="path3898"
           d="m 569.06934,151.38062 c -15.98564,20.43298 -29.3644,42.75044 -44.20898,64.00453 -3.76636,6.24672 -8.70125,12.13702 -11.25,18.82141 1.85493,6.13352 9.31696,7.64797 13.64868,11.72607 63.2999,43.54664 106.71296,115.67229 112.98778,192.51742 1.27969,4.81855 -0.0607,11.09966 3.26955,14.95206 5.91069,1.85378 12.34634,-0.38335 18.46069,0.55299 24.40946,-0.33296 49.04924,0.87365 73.31543,-0.64271 3.50493,-3.99416 -0.0481,-9.76362 0.64559,-14.56599 -6.7546,-109.4228 -63.56232,-215.15 -152.5556,-279.67902 -4.15538,-2.8462 -8.24824,-7.38595 -13.31903,-7.90502 l -0.9157,0.20105 z"
           '''
    HTML += 'style="fill:#%s;stroke-width:0.966142"'%(reg[5])
    HTML +='''/>
        <path
           d="m 731.04297,452.01172 c -1.9524,0.011 -3.95845,0.29454 -5.79688,0.17383 -27.37157,0.56543 -54.76485,-0.76297 -82.12304,0.57617 -3.68354,7.97371 -0.21056,16.93434 -2.00977,25.29101 -4.58119,74.83711 -43.12451,146.18905 -102.30664,192.03907 -2.71132,3.4145 -9.22538,5.12374 -9.6582,9.55664 0.98692,6.92521 7.1866,11.52 9.72851,17.83203 14.43098,23.63376 28.01133,47.87595 44.5918,70.11133 7.869,0.23274 11.79922,-8.11597 17.99805,-11.52735 71.8049,-59.7522 119.78598,-147.07816 131.84765,-239.70703 3.00323,-20.79501 4.48127,-41.88083 3.20117,-62.88086 -1.62149,-1.21433 -3.52025,-1.47585 -5.47265,-1.46484 z"
           id="path3885"
           '''
    HTML += 'style="fill:#%s;stroke-width:0.966142"'%(reg[4])
    HTML +='''
           inkscape:original="M 731.04297 452.01172 C 729.09057 452.02273 727.08452 452.30626 725.24609 452.18555 C 697.87452 452.75098 670.48124 451.42258 643.12305 452.76172 C 639.43951 460.73543 642.91249 469.69606 641.11328 478.05273 C 636.53209 552.88984 597.98877 624.24178 538.80664 670.0918 C 536.09532 673.5063 529.58126 675.21554 529.14844 679.64844 C 530.13536 686.57365 536.33504 691.16844 538.87695 697.48047 C 553.30793 721.11423 566.88828 745.35642 583.46875 767.5918 C 591.33775 767.82454 595.26797 759.47583 601.4668 756.06445 C 673.2717 696.31225 721.25278 608.98629 733.31445 516.35742 C 736.31768 495.56241 737.79572 474.47659 736.51562 453.47656 C 734.89413 452.26223 732.99537 452.00071 731.04297 452.01172 z "
           inkscape:radius="0"
           sodipodi:type="inkscape:offset" />
        <path
           inkscape:connector-curvature="0"
           style="opacity:0;fill:#000000;fill-opacity:1;stroke:#bac4b1;stroke-width:0.99599999;stroke-linecap:square;stroke-linejoin:miter;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:0"
           id="path4683"
           transform="translate(0,-84)"
           d="m 551.25,389.86218 a 236.25,270 0 1 1 -472.5,0 236.25,270 0 1 1 472.5,0 z" />
        <path
           inkscape:connector-curvature="0"
           style="opacity:0;fill:#000000;fill-opacity:1;stroke:#bac4b1;stroke-width:1.29700005;stroke-linecap:square;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:3.891, 1.297;stroke-dashoffset:0;stroke-opacity:0;marker-start:url(#Arrow1Lend);marker-end:none"
           id="path4687"
           transform="translate(0,-84)"
           d="m 552.5,405.48718 a 232.5,271.875 0 1 1 -465,0 232.5,271.875 0 1 1 465,0 z" />
        <path
           inkscape:connector-curvature="0"
           style="fill:none;stroke:url(#linearGradient7343);stroke-width:1.92751741;stroke-linecap:round;stroke-linejoin:bevel;stroke-miterlimit:4;stroke-dasharray:none;stroke-dashoffset:0.3663837;stroke-opacity:0.97857139"
           id="path5894"
           transform="matrix(1.6916427,0,0,1.4319809,-164.54971,-158.99715)"
           d="m 532.5,435.48718 a 216.875,261.875 0 1 1 -433.75,0 216.875,261.875 0 1 1 433.75,0 z" />
        <path
           inkscape:connector-curvature="0"
           id="path3904"
           d="m 367.26148,195.1996 c -52.70598,0.53624 -105.81322,15.46965 -149.74182,45.03295 -4.48884,4.37922 1.29516,8.97004 3.79856,12.4119 14.70819,19.04885 28.93037,38.74452 44.82509,56.70859 6.04406,1.24896 10.10484,-5.04553 15.58874,-6.58493 53.12383,-28.73855 120.10019,-29.39279 173.92686,-2.06281 4.25687,1.28336 10.08514,6.9765 13.53922,1.44071 13.69944,-22.26406 29.5707,-43.23902 43.0426,-65.61951 -0.11804,-5.39106 -7.46839,-5.504 -10.86182,-8.37708 -40.95235,-22.18777 -87.73048,-33.3153 -134.11743,-32.94982 z"
           '''
    HTML +='style="fill:#%s;stroke-width:0.966142"'%(reg[6])
    HTML +='''/>
        <path
           inkscape:connector-curvature="0"
           id="path3908"
           d="m 214.19263,242.77223 c -6.24343,2.06623 -10.94157,7.67421 -16.40947,11.35829 -44.69408,35.54838 -79.20515,84.82471 -93.43184,140.30614 -4.81927,18.782 -8.561264,38.49026 -8.497926,57.82837 3.777881,3.94308 10.025486,0.65056 14.897446,1.71538 25.69771,-0.35266 51.57024,0.75758 77.157,-0.57098 4.22847,-4.34118 1.01868,-11.21907 2.63047,-16.64718 4.36144,-50.29909 34.19123,-96.4795 75.43472,-124.76883 2.65836,-4.99167 -4.12896,-8.60585 -6.35743,-12.3761 -14.83565,-18.99592 -29.1279,-38.6859 -44.9176,-56.81396 -0.16611,-0.0326 -0.33651,-0.0423 -0.50537,-0.0311 z"
           '''
    HTML += 'style="fill:#%s;stroke-width:0.966142"'%(reg[7])
    HTML +='''
    	   />
        <path
           inkscape:connector-curvature="0"
           id="path3912"
           d="m 183.33936,452.04896 c -28.60403,0.77929 -57.2827,-0.46839 -85.909429,0.49989 -4.063997,3.00656 -1.751859,9.54157 -1.708369,14.02221 0.311147,70.00676 31.452188,138.85632 82.669728,186.54309 8.66321,8.1495 17.43387,16.87097 27.66413,22.81969 5.85116,-1.31897 6.32039,-8.77425 10.0263,-12.7215 14.02801,-23.83744 28.81665,-47.28493 41.89693,-71.64434 -1.4839,-7.67076 -9.91014,-10.77361 -14.55031,-16.38903 -33.0593,-30.74909 -52.87766,-75.1311 -53.86339,-120.24061 -0.61922,-2.75807 -3.91861,-2.94066 -6.22559,-2.8894 z"
           '''
    HTML += 'style="fill:#%s;stroke-width:0.966142"'%(reg[8])
    HTML +='''/>
        <path
           inkscape:connector-curvature="0"
           id="path3916"
           d="m 259.40503,590.40712 c -6.37458,2.82826 -7.07916,10.90765 -11.40796,15.80627 -13.28631,23.12695 -27.86312,45.71285 -40.20032,69.26454 1.65433,6.11578 9.14808,7.38787 13.48106,11.28684 68.80168,43.34578 156.17146,54.05269 233.30067,29.00307 25.66337,-8.16469 50.79801,-19.413 72.17519,-35.94479 2.25803,-5.7524 -4.32811,-9.99112 -6.25401,-14.96325 -14.52195,-23.14907 -28.32037,-46.89867 -43.29433,-69.67363 -5.24762,-2.03104 -9.25456,3.86098 -13.91805,5.48304 -44.67912,25.21184 -99.67977,31.10327 -148.64077,15.68915 -19.15405,-5.63498 -36.88286,-15.2077 -53.66494,-25.78096 -0.51009,-0.1462 -1.04631,-0.21963 -1.57654,-0.17028 z"
           '''
    HTML += 'style="fill:#%s;stroke-width:0.966142"'%(reg[9])
    HTML +='''/>
        <path
           inkscape:connector-curvature="0"
           id="path3920"
           d="m 637.07288,452.02333 c -22.89314,0.84027 -45.87851,-0.24893 -68.81083,0.22707 -5.17219,0.49279 -11.08148,-0.69662 -15.79488,1.0272 -2.31847,7.11533 -0.50295,14.8534 -2.51141,22.09324 -6.31223,46.46971 -33.52011,89.01152 -71.55841,116.04519 -4.72821,4.43272 1.32603,9.42657 3.32443,13.42356 15.23576,24.43131 29.53458,49.62025 45.70206,73.30065 5.3866,1.27022 8.27249,-5.34019 12.73498,-7.3425 56.27864,-43.75841 95.22178,-110.56707 101.72145,-181.91707 0.81071,-11.64518 1.80908,-23.45986 0.8231,-35.02629 -1.15812,-1.86502 -3.68491,-1.8598 -5.63049,-1.83105 z"
           '''
    HTML += 'style="fill:#%s;stroke-width:0.966142"'%(reg[10])
    HTML +='''/>
        <path
           inkscape:connector-curvature="0"
           id="path3924"
           d="m 513.81178,236.29029 c -7.44792,4.1845 -10.21739,13.06358 -15.59642,19.31371 -10.44014,15.98574 -22.26897,31.50349 -31.18887,48.22475 2.2827,7.10597 10.90182,8.58451 15.71807,13.64155 40.14043,30.11961 67.11093,78.20877 68.58404,128.7036 0.40192,3.39561 0.415,8.2386 5.08815,7.76105 12.28763,0.19553 24.60915,-0.21715 36.92504,0.0251 16.05715,-0.24197 32.43761,0.82269 48.3069,-0.73011 3.50268,-4.55804 0.18721,-10.83977 0.60871,-16.1292 -7.79259,-81.71348 -56.67111,-159.2043 -127.44221,-200.84526 -0.32889,-4.2e-4 -0.69897,-0.12311 -1.00341,0.0348 z"
           '''
    HTML += 'style="fill:#%s;stroke-width:0.966142"'%(reg[11])
    HTML +='''/>
        <path
           inkscape:connector-curvature="0"
           style="fill:none;stroke:#0f0002;stroke-width:2.59552097;stroke-linecap:round;stroke-linejoin:bevel;stroke-miterlimit:4;stroke-dasharray:none;stroke-dashoffset:0.52440941;stroke-opacity:0.97857139"
           id="path7345"
           transform="matrix(-1.1007557,0,0,-1.2136752,786.97421,1225.8019)"
           d="m 627.5,629.23718 a 248.125,219.375 0 1 1 -496.25,0 248.125,219.375 0 1 1 496.25,0 z" />
        <path
           inkscape:connector-curvature="0"
           id="path3932"
           d="m 232.1095,341.2024 c -7.09144,3.46161 -9.72698,11.74582 -14.85057,17.32631 -20.05188,28.86151 -30.34741,64.40158 -28.7114,99.54961 -0.0839,25.30986 7.10347,50.21274 18.9584,72.56368 7.57277,14.26543 16.627,28.10638 28.62823,38.88011 6.02287,-0.0162 8.62019,-6.98082 13.27895,-9.94246 14.23266,-14.09563 29.41355,-27.50514 42.744,-42.35429 0.17329,-5.91499 -6.5545,-8.87284 -8.25417,-14.2567 -8.72773,-14.5101 -14.67999,-31.2264 -13.23938,-48.36706 -0.70646,-14.34307 1.8634,-28.8843 8.808,-41.54861 3.22862,-7.09341 9.01744,-13.22053 11.51368,-20.39795 -2.48244,-5.65331 -8.98757,-8.04055 -12.76001,-12.76443 -14.92161,-12.85214 -28.43647,-27.71894 -44.89259,-38.55637 -0.39783,-0.10215 -0.81191,-0.16141 -1.22314,-0.13184 z"
           '''
    HTML += 'style="fill:#%s;stroke-width:0.966142"'%(reg[13])
    HTML +='''/>
        <path
           inkscape:connector-curvature="0"
           id="path3928"
           d="m 369.87989,279.04726 c -48.42134,-0.44384 -96.61097,19.34986 -131.38706,53.4313 -2.92966,2.4231 -7.78568,6.90872 -3.52139,10.44321 15.96297,14.20694 31.57763,28.90334 47.59659,43.10353 3.48097,2.28386 7.44519,9.29376 11.93099,4.80967 31.37386,-34.53184 86.73441,-43.18403 127.43409,-20.61218 7.8813,3.85498 14.13354,10.11557 21.21643,15.07507 4.94266,2.03458 7.397,-4.90803 11.0302,-6.93563 15.69197,-14.90679 32.34914,-29.05433 47.21748,-44.6763 0.23847,-5.34028 -6.43487,-6.98517 -9.26696,-10.6714 -33.7325,-28.75626 -78.08745,-44.511 -122.25037,-43.96727 z"
           '''
    HTML += 'style="fill:#%s;stroke-width:0.966142"'%(reg[12])
    HTML += '''/>
        <path
           inkscape:connector-curvature="0"
           id="path3936"
           d="m 292.15894,516.95802 c -5.60395,3.14061 -9.5928,9.10856 -14.65576,13.22937 -13.3784,13.11159 -27.68724,25.64281 -39.73388,39.88769 0.45074,5.60008 7.29566,7.51733 10.41562,11.67238 50.21201,43.51793 124.18606,56.77501 186.35683,33.65722 25.20528,-9.07845 48.61631,-23.2963 67.70691,-41.9989 4.22211,-5.05856 -3.16023,-8.98141 -5.96786,-12.44897 -14.40631,-14.07723 -29.90301,-27.12576 -44.8201,-40.55457 -6.71714,-3.24343 -10.45218,5.2837 -15.41776,8.11551 -35.46568,28.35777 -89.587,29.19405 -126.08249,2.2629 -6.17024,-3.92787 -11.05189,-9.75502 -16.96289,-13.78784 -0.27479,-0.0587 -0.55989,-0.0696 -0.83862,-0.0348 z"
           '''
    HTML += 'style="fill:#%s;stroke-width:0.966142"'%(reg[14])
    HTML +='''/>
        <path
           inkscape:connector-curvature="0"
           id="path3940"
           d="m 501.71034,333.53395 c -10.8013,7.4466 -20.20394,17.40161 -30.03213,26.2943 -8.30492,8.41337 -17.67719,15.90058 -25.51292,24.68959 -2.82903,4.8088 4.15273,7.51103 5.99487,11.25 18.803,23.42979 25.62967,56.09809 16.47603,84.86951 -3.82042,13.50326 -11.21524,25.73676 -19.89095,36.57153 0.45476,6.19582 7.88747,8.65434 11.44583,13.0188 14.5946,12.80929 28.45587,26.91363 44.05894,38.24341 6.20198,-0.39597 8.27254,-7.665 12.38342,-11.36903 25.00747,-31.57002 38.57594,-71.96823 36.17798,-112.22351 -1.27808,-41.58135 -19.88614,-81.79634 -49.20227,-111.01318 -0.58264,-0.29922 -1.25285,-0.37202 -1.8988,-0.33142 z"
           '''
    HTML +='style="fill:#%s;stroke-width:0.966142"'%(reg[15])
    HTML +='''/>
        <path
           inkscape:connector-curvature="0"
           style="fill:none;stroke:#0f0002;stroke-width:2.52945733;stroke-linecap:round;stroke-linejoin:bevel;stroke-miterlimit:4;stroke-dasharray:none;stroke-dashoffset:0.52440941;stroke-opacity:0.97857139"
           id="path7347"
           transform="matrix(1.1781377,0,0,1.1939654,-111.6751,-251.53792)"
           d="m 563.75,589.86218 a 154.375,145 0 1 1 -308.75,0 154.375,145 0 1 1 308.75,0 z" />
        <path
           inkscape:connector-curvature="0"
           style="fill:none;stroke:#000000;stroke-width:3;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
           id="path7357"
           d="M 552.5,453.36218 H 736.25 735" />
        <path
           inkscape:connector-curvature="0"
           style="fill:none;stroke:#000000;stroke-width:3;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
           id="path7359"
           d="m 152.5,163.36218 115,147.5" />
        <path
           inkscape:connector-curvature="0"
           style="fill:none;stroke:#000000;stroke-width:3;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
           id="path7361"
           d="m 466.25,304.61218 103.75,-155" />
        <path
           inkscape:connector-curvature="0"
           style="fill:none;stroke:#000000;stroke-width:3;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
           id="path7363"
           d="m 476.2494,594.61158 107.5012,174.5803" />
        <path
           inkscape:connector-curvature="0"
           style="fill:none;stroke:#000000;stroke-width:3;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
           id="path7365"
           d="m 258.75,589.61218 -106.25,180" />
        <path
           inkscape:connector-curvature="0"
           style="fill:none;stroke:#000000;stroke-width:3;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
           id="path7367"
           d="m 232.5,339.61218 58.75,53.125" />
        <path
           inkscape:connector-curvature="0"
           style="fill:none;stroke:#000000;stroke-width:3;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
           id="path7369"
           d="m 501.24999,333.36218 -56.25,52.5" />
        <path
           inkscape:connector-curvature="0"
           style="fill:none;stroke:#000000;stroke-width:3;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
           id="path7371"
           d="m 293.76858,515.21861 -56.28712,55.03711" />
        <path
           inkscape:connector-curvature="0"
           style="fill:none;stroke:#000000;stroke-width:3;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
           id="path7373"
           d="m 447.5,517.73717 57.50001,51.875" />
        <text
           style="font-style:normal;font-weight:normal;font-size:40px;line-height:0%;font-family:sans-serif;letter-spacing:0px;word-spacing:0px;fill:#000000;fill-opacity:1;stroke:none"
           xml:space="preserve"
           id="text3281"
           y="531.11218"
           x="375"><tspan
             style="font-family:sans-serif"
             id="tspan3283"
             y="531.11218"
             x="375" /></text>
        <flowRoot
           style="font-style:normal;font-weight:normal;line-height:0.01%;font-family:sans-serif;letter-spacing:0px;word-spacing:0px;fill:#000000;fill-opacity:1;stroke:none"
           xml:space="preserve"
           id="flowRoot3285"><flowRegion
             style="font-family:sans-serif"
             id="flowRegion3287"><rect
               style="font-family:sans-serif"
               id="rect3289"
               y="507.36218"
               x="363.75"
               height="51.25"
               width="78.75" /></flowRegion><flowPara
             style="font-size:40px;line-height:1.25;font-family:sans-serif"
             id="flowPara3291"> </flowPara></flowRoot>    <flowRoot
           style="font-style:normal;font-weight:normal;line-height:0.01%;font-family:sans-serif;letter-spacing:0px;word-spacing:0px;fill:#000000;fill-opacity:1;stroke:none"
           xml:space="preserve"
           id="flowRoot3293"><flowRegion
             style="font-family:sans-serif"
             id="flowRegion3295"><rect
               style="font-family:sans-serif"
               id="rect3297"
               y="548.61218"
               x="398.75"
               height="48.75"
               width="8.75" /></flowRegion><flowPara
             style="font-size:40px;line-height:1.25;font-family:sans-serif"
             id="flowPara3299"> </flowPara></flowRoot>    <flowRoot
           style="font-style:normal;font-weight:normal;line-height:0.01%;font-family:sans-serif;letter-spacing:0px;word-spacing:0px;fill:#000000;fill-opacity:1;stroke:none"
           xml:space="preserve"
           id="flowRoot3301"><flowRegion
             style="font-family:sans-serif"
             id="flowRegion3303"><rect
               style="font-family:sans-serif"
               id="rect3305"
               y="514.86218"
               x="330"
               height="81.25"
               width="103.75" /></flowRegion><flowPara
             style="font-size:40px;line-height:1.25;font-family:sans-serif"
             id="flowPara3307"> </flowPara></flowRoot>    <flowRoot
           style="font-style:normal;font-weight:normal;line-height:0.01%;font-family:sans-serif;letter-spacing:0px;word-spacing:0px;fill:#000000;fill-opacity:1;stroke:none"
           xml:space="preserve"
           id="flowRoot3309"><flowRegion
             style="font-family:sans-serif"
             id="flowRegion3311"><rect
               style="font-family:sans-serif"
               id="rect3313"
               y="486.11218"
               x="325"
               height="111.25"
               width="110" /></flowRegion><flowPara
             style="font-size:40px;line-height:1.25;font-family:sans-serif"
             id="flowPara3315"> </flowPara></flowRoot>    <text
           style="font-style:normal;font-weight:normal;font-size:40px;line-height:0%;font-family:sans-serif;letter-spacing:0px;word-spacing:0px;fill:#000000;fill-opacity:1;stroke:none"
           xml:space="preserve"
           id="text3317"
           y="539.86218"
           x="376.25"><tspan
             style="font-family:sans-serif"
             id="tspan3319"
             y="539.86218"
             x="376.25" /></text>
        <flowRoot
           style="font-style:normal;font-weight:normal;line-height:0.01%;font-family:sans-serif;letter-spacing:0px;word-spacing:0px;fill:#000000;fill-opacity:1;stroke:none"
           xml:space="preserve"
           id="flowRoot3321"><flowRegion
             style="font-family:sans-serif"
             id="flowRegion3323"><rect
               style="font-family:sans-serif"
               id="rect3325"
               y="502.36218"
               x="307.5"
               height="116.25"
               width="130" /></flowRegion><flowPara
             style="font-size:40px;line-height:1.25;font-family:sans-serif"
             id="flowPara3327"> </flowPara></flowRoot>    <text
           style="font-style:normal;font-weight:normal;font-size:40px;line-height:0%;font-family:sans-serif;letter-spacing:0px;word-spacing:0px;fill:#008080;fill-opacity:1;stroke:none"
           xml:space="preserve"
           id="text3337"
           y="465.86218"
           x="482.91666"><tspan
             style="font-family:sans-serif;fill:#008080"
             id="tspan3339"
             y="465.86218"
             x="482.91666" /></text>
        <text
           style="font-style:normal;font-weight:normal;font-size:40px;line-height:0%;font-family:sans-serif;letter-spacing:0px;word-spacing:0px;fill:#808000;fill-opacity:1;stroke:none"
           xml:space="preserve"
           id="text3345"
           y="467.11218"
           x="203.91667"><tspan
             style="font-family:sans-serif;fill:#808000"
             id="tspan3347"
             y="467.11218"
             x="203.91667" /></text>
        <text
           style="font-style:normal;font-weight:normal;font-size:40px;line-height:0%;font-family:sans-serif;letter-spacing:0px;word-spacing:0px;fill:#000000;fill-opacity:1;stroke:none"
           xml:space="preserve"
           id="text3361"
           y="688.36218"
           x="343.75"><tspan
             style="font-family:sans-serif"
             id="tspan3363"
             y="688.36218"
             x="343.75" /></text>
        <text
           style="font-style:normal;font-weight:normal;font-size:40px;line-height:0%;font-family:sans-serif;letter-spacing:0px;word-spacing:0px;fill:#000000;fill-opacity:1;stroke:none"
           xml:space="preserve"
           id="text3365"
           y="622.36218"
           x="167.5"><tspan
             style="font-family:sans-serif"
             id="tspan3367"
             y="622.36218"
             x="167.5" /></text>
        <text
           style="font-style:normal;font-weight:normal;font-size:40px;line-height:0%;font-family:sans-serif;letter-spacing:0px;word-spacing:0px;fill:#000000;fill-opacity:1;stroke:none"
           xml:space="preserve"
           id="text3385"
           y="625.52887"
           x="638"><tspan
             style="font-family:sans-serif"
             id="tspan3387"
             y="625.52887"
             x="638" /></text>
        <path
           inkscape:connector-curvature="0"
           '''
    HTML += 'style="fill:#%s;fill-rule:evenodd;stroke:#000000;stroke-width:2.99999976;stroke-linecap:butt;stroke-linejoin:round;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"'%(reg[16])
    HTML +='''
           id="path3331"
           d="m 473.70725,454.07054 a 102.41556,97.415554 0 1 1 -204.83112,0 102.41556,97.415554 0 1 1 204.83112,0 z" />
        <path
           inkscape:connector-curvature="0"
           style="fill:none;stroke:#000000;stroke-width:3;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
           id="path3355"
           d="M 187.82524,453.50006 H 1.3258252" />
        <text
           id="text4421"
           y="345.08618"
           x="555.06897"
           style="font-style:normal;font-weight:normal;line-height:0%;font-family:sans-serif;letter-spacing:0px;word-spacing:0px;fill:#ff00ff;fill-opacity:1;stroke:none;stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1"
           xml:space="preserve"><tspan
             style="font-size:40px;line-height:1.25"
             y="345.08618"
             x="555.06897"
             id="tspan4423"
             sodipodi:role="line"> </tspan></text>
        <text
           id="text4433"
           y="320.08618"
           x="348.17242"
           style="font-style:normal;font-weight:normal;line-height:0%;font-family:sans-serif;letter-spacing:0px;word-spacing:0px;fill:#ffff00;fill-opacity:1;stroke:none;stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1"
           xml:space="preserve"><tspan
             style="font-size:40px;line-height:1.25"
             y="320.08618"
             x="348.17242"
             id="tspan4435"
             sodipodi:role="line"> </tspan></text>
      </g>
      <text
         id="text4127"
         y="441.99405"
         x="544.05249"
         style="font-style:normal;font-weight:normal;font-size:37.5px;line-height:1.25;font-family:sans-serif;letter-spacing:0px;word-spacing:0px;fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.9375"
         xml:space="preserve"><tspan
           style="font-style:italic;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:40px;font-family:sans-serif;-inkscape-font-specification:'sans-serif, Italic';font-variant-ligatures:normal;font-variant-caps:normal;font-variant-numeric:normal;font-feature-settings:normal;text-align:start;writing-mode:lr-tb;text-anchor:start;stroke-width:0.9375"
           y="441.99405"
           x="544.05249"
           id="tspan4125"
           sodipodi:role="line">1</tspan></text>
      <text
         id="text4127-3"
         y="616.53247"
         x="258.58746"
         style="font-style:normal;font-weight:normal;font-size:37.5px;line-height:1.25;font-family:sans-serif;letter-spacing:0px;word-spacing:0px;fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.9375"
         xml:space="preserve"><tspan
           style="font-style:italic;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:40px;font-family:sans-serif;-inkscape-font-specification:'sans-serif, Italic';font-variant-ligatures:normal;font-variant-caps:normal;font-variant-numeric:normal;font-feature-settings:normal;text-align:start;writing-mode:lr-tb;text-anchor:start;stroke-width:0.9375"
           y="616.53247"
           x="258.58746"
           id="tspan4125-8"
           sodipodi:role="line">2</tspan></text>
      <text
         id="text4127-1"
         y="912.17188"
         x="262.45203"
         style="font-style:normal;font-weight:normal;font-size:37.5px;line-height:1.25;font-family:sans-serif;letter-spacing:0px;word-spacing:0px;fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.9375"
         xml:space="preserve"><tspan
           style="font-style:italic;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:40px;font-family:sans-serif;-inkscape-font-specification:'sans-serif, Italic';font-variant-ligatures:normal;font-variant-caps:normal;font-variant-numeric:normal;font-feature-settings:normal;text-align:start;writing-mode:lr-tb;text-anchor:start;stroke-width:0.9375"
           y="912.17188"
           x="262.45203"
           id="tspan4125-5"
           sodipodi:role="line">3</tspan></text>
      <text
         id="text4127-5"
         y="1077.3822"
         x="539.90662"
         style="font-style:normal;font-weight:normal;font-size:37.5px;line-height:1.25;font-family:sans-serif;letter-spacing:0px;word-spacing:0px;fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.9375"
         xml:space="preserve"><tspan
           style="font-style:italic;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:40px;font-family:sans-serif;-inkscape-font-specification:'sans-serif, Italic';font-variant-ligatures:normal;font-variant-caps:normal;font-variant-numeric:normal;font-feature-settings:normal;text-align:start;writing-mode:lr-tb;text-anchor:start;stroke-width:0.9375"
           y="1077.3822"
           x="539.90662"
           id="tspan4125-81"
           sodipodi:role="line">4</tspan></text>
      <text
         id="text4127-31"
         y="908.30737"
         x="822.92896"
         style="font-style:normal;font-weight:normal;font-size:37.5px;line-height:1.25;font-family:sans-serif;letter-spacing:0px;word-spacing:0px;fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.9375"
         xml:space="preserve"><tspan
           style="font-style:italic;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:40px;font-family:sans-serif;-inkscape-font-specification:'sans-serif, Italic';font-variant-ligatures:normal;font-variant-caps:normal;font-variant-numeric:normal;font-feature-settings:normal;text-align:start;writing-mode:lr-tb;text-anchor:start;stroke-width:0.9375"
           y="908.30737"
           x="822.92896"
           id="tspan4125-9"
           sodipodi:role="line">5</tspan></text>
      <text
         id="text4127-6"
         y="606.07672"
         x="826.67896"
         style="font-style:normal;font-weight:normal;font-size:37.5px;line-height:1.25;font-family:sans-serif;letter-spacing:0px;word-spacing:0px;fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.9375"
         xml:space="preserve"><tspan
           style="font-style:italic;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:40px;font-family:sans-serif;-inkscape-font-specification:'sans-serif, Italic';font-variant-ligatures:normal;font-variant-caps:normal;font-variant-numeric:normal;font-feature-settings:normal;text-align:start;writing-mode:lr-tb;text-anchor:start;stroke-width:0.9375"
           y="606.07672"
           x="826.67896"
           id="tspan4125-3"
           sodipodi:role="line">6</tspan></text>
      <text
         id="text4127-4"
         y="538.33228"
         x="545.47437"
         style="font-style:normal;font-weight:normal;font-size:37.5px;line-height:1.25;font-family:sans-serif;letter-spacing:0px;word-spacing:0px;fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.9375"
         xml:space="preserve"><tspan
           style="font-style:italic;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:40px;font-family:sans-serif;-inkscape-font-specification:'sans-serif, Italic';font-variant-ligatures:normal;font-variant-caps:normal;font-variant-numeric:normal;font-feature-settings:normal;text-align:start;writing-mode:lr-tb;text-anchor:start;stroke-width:0.9375"
           y="538.33228"
           x="545.47437"
           id="tspan4125-7"
           sodipodi:role="line">7</tspan></text>
      <text
         id="text4127-8"
         y="654.21204"
         x="346.50638"
         style="font-style:normal;font-weight:normal;font-size:37.5px;line-height:1.25;font-family:sans-serif;letter-spacing:0px;word-spacing:0px;fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.9375"
         xml:space="preserve"><tspan
           style="font-style:italic;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:40px;font-family:sans-serif;-inkscape-font-specification:'sans-serif, Italic';font-variant-ligatures:normal;font-variant-caps:normal;font-variant-numeric:normal;font-feature-settings:normal;text-align:start;writing-mode:lr-tb;text-anchor:start;stroke-width:0.9375"
           y="654.21204"
           x="346.50638"
           id="tspan4125-84"
           sodipodi:role="line">8</tspan></text>
      <text
         id="text4127-16"
         y="850.33881"
         x="344.5741"
         style="font-style:normal;font-weight:normal;font-size:37.5px;line-height:1.25;font-family:sans-serif;letter-spacing:0px;word-spacing:0px;fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.9375"
         xml:space="preserve"><tspan
           style="font-style:italic;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:40px;font-family:sans-serif;-inkscape-font-specification:'sans-serif, Italic';font-variant-ligatures:normal;font-variant-caps:normal;font-variant-numeric:normal;font-feature-settings:normal;text-align:start;writing-mode:lr-tb;text-anchor:start;stroke-width:0.9375"
           y="850.33881"
           x="344.5741"
           id="tspan4125-842"
           sodipodi:role="line">9</tspan></text>
      <text
         id="text4127-18"
         y="969.91132"
         x="527.80505"
         style="font-style:normal;font-weight:normal;font-size:37.5px;line-height:1.25;font-family:sans-serif;letter-spacing:0px;word-spacing:0px;fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.9375"
         xml:space="preserve"><tspan
           style="font-style:italic;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:40px;font-family:sans-serif;-inkscape-font-specification:'sans-serif, Italic';font-variant-ligatures:normal;font-variant-caps:normal;font-variant-numeric:normal;font-feature-settings:normal;text-align:start;writing-mode:lr-tb;text-anchor:start;stroke-width:0.9375"
           y="969.91132"
           x="527.80505"
           id="tspan4125-810"
           sodipodi:role="line">10</tspan></text>
      <text
         id="text4127-89"
         y="853.2373"
         x="736.94232"
         style="font-style:normal;font-weight:normal;font-size:37.5px;line-height:1.25;font-family:sans-serif;letter-spacing:0px;word-spacing:0px;fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.9375"
         xml:space="preserve"><tspan
           style="font-style:italic;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:40px;font-family:sans-serif;-inkscape-font-specification:'sans-serif, Italic';font-variant-ligatures:normal;font-variant-caps:normal;font-variant-numeric:normal;font-feature-settings:normal;text-align:start;writing-mode:lr-tb;text-anchor:start;stroke-width:0.9375"
           y="853.2373"
           x="736.94232"
           id="tspan4125-4"
           sodipodi:role="line">11</tspan></text>
      <text
         id="text4127-9"
         y="651.3136"
         x="730.40845"
         style="font-style:normal;font-weight:normal;font-size:37.5px;line-height:1.25;font-family:sans-serif;letter-spacing:0px;word-spacing:0px;fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.9375"
         xml:space="preserve"><tspan
           style="font-style:italic;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:40px;font-family:sans-serif;-inkscape-font-specification:'sans-serif, Italic';font-variant-ligatures:normal;font-variant-caps:normal;font-variant-numeric:normal;font-feature-settings:normal;text-align:start;writing-mode:lr-tb;text-anchor:start;stroke-width:0.9375"
           y="651.3136"
           x="730.40845"
           id="tspan4125-31"
           sodipodi:role="line">12</tspan></text>
      <text
         id="text4127-13"
         y="619.37366"
         x="533.14362"
         style="font-style:normal;font-weight:normal;font-size:37.5px;line-height:1.25;font-family:sans-serif;letter-spacing:0px;word-spacing:0px;fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.9375"
         xml:space="preserve"><tspan
           style="font-style:italic;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:40px;font-family:sans-serif;-inkscape-font-specification:'sans-serif, Italic';font-variant-ligatures:normal;font-variant-caps:normal;font-variant-numeric:normal;font-feature-settings:normal;text-align:start;writing-mode:lr-tb;text-anchor:start;stroke-width:0.9375"
           y="619.37366"
           x="533.14362"
           id="tspan4125-36"
           sodipodi:role="line">13</tspan></text>
      <text
         id="text4127-88"
         y="749.86005"
         x="395.95145"
         style="font-style:normal;font-weight:normal;font-size:37.5px;line-height:1.25;font-family:sans-serif;letter-spacing:0px;word-spacing:0px;fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.9375"
         xml:space="preserve"><tspan
           style="font-style:italic;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:40px;font-family:sans-serif;-inkscape-font-specification:'sans-serif, Italic';font-variant-ligatures:normal;font-variant-caps:normal;font-variant-numeric:normal;font-feature-settings:normal;text-align:start;writing-mode:lr-tb;text-anchor:start;stroke-width:0.9375"
           y="749.86005"
           x="395.95145"
           id="tspan4125-1"
           sodipodi:role="line">14</tspan></text>
      <text
         id="text4127-44"
         y="883.18768"
         x="530.70349"
         style="font-style:normal;font-weight:normal;font-size:37.5px;line-height:1.25;font-family:sans-serif;letter-spacing:0px;word-spacing:0px;fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.9375"
         xml:space="preserve"><tspan
           style="font-style:italic;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:40px;font-family:sans-serif;-inkscape-font-specification:'sans-serif, Italic';font-variant-ligatures:normal;font-variant-caps:normal;font-variant-numeric:normal;font-feature-settings:normal;text-align:start;writing-mode:lr-tb;text-anchor:start;stroke-width:0.9375"
           y="883.18768"
           x="530.70349"
           id="tspan4125-44"
           sodipodi:role="line">15</tspan></text>
      <text
         id="text4127-92"
         y="752.75848"
         x="669.48425"
         style="font-style:normal;font-weight:normal;font-size:37.5px;line-height:1.25;font-family:sans-serif;letter-spacing:0px;word-spacing:0px;fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.9375"
         xml:space="preserve"><tspan
           style="font-style:italic;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:40px;font-family:sans-serif;-inkscape-font-specification:'sans-serif, Italic';font-variant-ligatures:normal;font-variant-caps:normal;font-variant-numeric:normal;font-feature-settings:normal;text-align:start;writing-mode:lr-tb;text-anchor:start;stroke-width:0.9375"
           y="752.75848"
           x="669.48425"
           id="tspan4125-0"
           sodipodi:role="line">16</tspan></text>
      <text
         id="text4127-49"
         y="753.72461"
         x="530.30249"
         style="font-style:normal;font-weight:normal;font-size:37.5px;line-height:1.25;font-family:sans-serif;letter-spacing:0px;word-spacing:0px;fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.9375"
         xml:space="preserve"><tspan
           style="font-style:italic;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:40px;font-family:sans-serif;-inkscape-font-specification:'sans-serif, Italic';font-variant-ligatures:normal;font-variant-caps:normal;font-variant-numeric:normal;font-feature-settings:normal;text-align:start;writing-mode:lr-tb;text-anchor:start;stroke-width:0.9375"
           y="753.72461"
           x="530.30249"
           id="tspan4125-32"
           sodipodi:role="line">17</tspan></text>
      <text
         id="text4462"
         y="294.17435"
         x="161.66637"
         style="font-style:normal;font-weight:normal;font-size:37.5px;line-height:1.25;font-family:sans-serif;letter-spacing:0px;word-spacing:0px;fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.9375"
         xml:space="preserve"><tspan
           style="font-style:italic;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:50px;font-family:sans-serif;-inkscape-font-specification:'sans-serif, Italic';font-variant-ligatures:normal;font-variant-caps:normal;font-variant-numeric:normal;font-feature-settings:normal;text-align:start;writing-mode:lr-tb;text-anchor:start;stroke-width:0.9375"
           y="294.17435"
           x="161.66637"
           id="tspan4460"
           sodipodi:role="line">Use polar svg diagram to analyze data</tspan></text>
      <rect
         y="58.60807"
         x="39.434502"
         height="1278.2747"
         width="1250.6052"
         id="rect5129"
         style="opacity:0.18200001;fill:#e6ff2a;fill-opacity:1;stroke:#000000;stroke-width:1.63910151;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:0.95266269" />
      <g
         transform="matrix(0.87848444,0,0,1.2997746,501.12401,-147.27316)"
         id="g4980">
        <path
           inkscape:connector-curvature="0"
           id="path5003-4-7"
           d="m 584.57439,445.27731 c -3.6075,8.94563 -0.8082,20.35842 -1.6908,30.33801 1.7707,11.21143 11.5932,5.31069 17.2472,6.77266 10.291,-0.91024 21.0328,1.90246 31.0147,-1.5623 3.6074,-8.94563 0.8082,-20.35841 1.6907,-30.33799 -1.7706,-11.21147 -11.5931,-5.31072 -17.2471,-6.77269 -10.2618,0.91174 -21.0759,-1.90453 -31.0147,1.56231 z"
           style="fill:#ff5555;stroke-width:1.16134155"
           inkscape:transform-center-x="-10.183172"
           inkscape:transform-center-y="0.76373793" />
        <rect
           y="430.65439"
           x="557.72827"
           height="26.523605"
           width="41.544106"
           id="rect4986"
           style="fill:none;stroke-width:1.34916127" />
        <rect
           y="441.12427"
           x="589.12793"
           height="26.523605"
           width="41.544106"
           id="rect4986-3"
           style="fill:#ff0000;stroke-width:1.34916139" />
        <path
           inkscape:connector-curvature="0"
           id="path5003"
           d="m 586.67079,436.47317 c -3.339,8.94563 -0.7481,20.35841 -1.565,30.338 1.6388,11.21144 10.7302,5.3107 15.9634,6.77269 9.5249,-0.91027 19.4671,1.90245 28.7058,-1.56231 3.3389,-8.94565 0.7481,-20.35843 1.5649,-30.33801 -1.6387,-11.21145 -10.7301,-5.3107 -15.9633,-6.77267 -9.4979,0.91172 -19.5069,-1.90453 -28.7058,1.5623 z"
           style="fill:#ff0000;stroke-width:1.11728036" />
        <path
           inkscape:connector-curvature="0"
           id="path5003-7"
           d="m 586.85499,453.26523 c -3.339,8.94565 -0.7481,20.35843 -1.565,30.33801 1.6389,11.21144 10.7302,5.3107 15.9634,6.77267 9.525,-0.91024 19.4671,1.90246 28.7059,-1.56229 3.3389,-8.94564 0.7481,-20.35842 1.5649,-30.33801 -1.6388,-11.21145 -10.7301,-5.31072 -15.9633,-6.77267 -9.4979,0.91172 -19.507,-1.90454 -28.7059,1.56229 z"
           style="opacity:0.87000002;fill:#ff2a2a;stroke-width:1.11728036" />
        <path
           inkscape:connector-curvature="0"
           id="path5003-4"
           d="m 585.30579,464.463 c -3.6075,8.94563 -0.8082,20.35842 -1.6908,30.33801 1.7707,11.21144 11.5932,5.31069 17.2472,6.77266 10.291,-0.91023 21.0328,1.90246 31.0147,-1.56229 3.6074,-8.94564 0.8082,-20.35842 1.6907,-30.338 -1.7706,-11.21146 -11.5931,-5.31072 -17.2471,-6.77269 -10.2618,0.91174 -21.0759,-1.90453 -31.0147,1.56231 z"
           style="opacity:0.80199998;fill:#ff5555;stroke-width:1.16134155" />
        <path
           inkscape:connector-curvature="0"
           id="path5003-9"
           d="m 585.48999,481.431 c -3.6075,8.94563 -0.8082,20.35842 -1.6908,30.338 1.7707,11.21145 11.5931,5.3107 17.2472,6.77268 10.291,-0.91025 21.0328,1.90245 31.0147,-1.5623 3.6074,-8.94564 0.8082,-20.35843 1.6906,-30.338 -1.7705,-11.21147 -11.593,-5.31072 -17.247,-6.77269 -10.2618,0.91174 -21.0759,-1.90451 -31.0147,1.56231 z"
           style="fill:#ff8080;stroke-width:1.16134155" />
        <path
           inkscape:connector-curvature="0"
           id="path5003-56-0"
           d="m 585.36939,493.81154 c -3.6075,8.94563 -0.8082,20.35841 -1.6907,30.338 1.7706,11.21143 11.5931,5.3107 17.2471,6.77269 10.2911,-0.91027 21.0329,1.90244 31.0147,-1.56231 3.6074,-8.94565 0.8082,-20.35843 1.6907,-30.33802 -1.7706,-11.21144 -11.593,-5.3107 -17.2471,-6.77266 -10.2618,0.91172 -21.0759,-1.90454 -31.0147,1.5623 z"
           style="fill:#ffaaaa;fill-opacity:1;stroke-width:1.16134155" />
        <path
           inkscape:connector-curvature="0"
           id="path5003-5"
           d="m 584.54979,509.33415 c -3.6075,8.94565 -0.8082,20.35844 -1.6908,30.338 1.7707,11.21145 11.5932,5.31071 17.2472,6.77269 10.2911,-0.91024 21.0328,1.90246 31.0147,-1.5623 3.6074,-8.94565 0.8082,-20.35844 1.6907,-30.338 -1.7706,-11.21146 -11.5931,-5.31072 -17.2471,-6.77269 -10.2618,0.91173 -21.0759,-1.90452 -31.0147,1.5623 z"
           style="opacity:1;fill:#ffccaa;stroke-width:1.16134155" />
        <path
           inkscape:connector-curvature="0"
           id="path5003-56"
           d="m 585.21299,522.99705 c -3.6075,8.94563 -0.8082,20.35841 -1.6907,30.338 1.7706,11.21143 11.5931,5.3107 17.2471,6.77268 10.2911,-0.91026 21.0329,1.90245 31.0147,-1.5623 3.6074,-8.94565 0.8082,-20.35843 1.6907,-30.33802 -1.7706,-11.21145 -11.593,-5.3107 -17.2471,-6.77266 -10.2618,0.91172 -21.0759,-1.90454 -31.0147,1.5623 z"
           style="fill:#ffdd55;stroke-width:1.16134155" />
        <path
           inkscape:connector-curvature="0"
           id="path5003-56-7-0"
           d="m 584.02369,535.9787 c -3.6075,8.94563 -0.8082,20.35841 -1.6907,30.338 1.7706,11.21143 11.5931,5.3107 17.2471,6.77268 10.2911,-0.91026 21.0329,1.90245 31.0147,-1.5623 3.6074,-8.94565 0.8082,-20.35843 1.6907,-30.33802 -1.7706,-11.21145 -11.593,-5.3107 -17.2471,-6.77267 -10.2618,0.91173 -21.0759,-1.90454 -31.0147,1.56231 z"
           style="fill:#ffd42a;stroke-width:1.16134167" />
        <path
           inkscape:connector-curvature="0"
           id="path5003-56-7"
           d="m 584.51019,550.30785 c -3.6075,8.94563 -0.8082,20.35841 -1.6907,30.33799 1.7706,11.21144 11.5931,5.3107 17.2471,6.77269 10.2911,-0.91026 21.0329,1.90245 31.0147,-1.56231 3.6074,-8.94564 0.8082,-20.35842 1.6907,-30.33801 -1.7706,-11.21145 -11.593,-5.3107 -17.2471,-6.77267 -10.2618,0.91172 -21.0759,-1.90454 -31.0147,1.56231 z"
           style="fill:#ffcc00;stroke-width:1.16134167;opacity:0.666" />
        <path
           inkscape:connector-curvature="0"
           id="path5003-56-5"
           d="m 584.91119,566.30357 c -3.6075,8.94564 -0.8082,20.35842 -1.6907,30.338 1.7706,11.21144 11.5931,5.3107 17.2471,6.77269 10.2911,-0.91026 21.0329,1.90245 31.0147,-1.56231 3.6074,-8.94565 0.8082,-20.35843 1.6907,-30.33801 -1.7706,-11.21145 -11.593,-5.3107 -17.2471,-6.77266 -10.2618,0.91171 -21.0759,-1.90454 -31.0147,1.56229 z"
           style="fill:#ffcc00;stroke-width:1.16134167" />
        <path
           inkscape:connector-curvature="0"
           id="path5003-56-1"
           d="m 584.19729,582.24983 c -3.6075,8.94563 -0.8082,20.35841 -1.6907,30.338 1.7706,11.21143 11.5931,5.3107 17.2471,6.77269 10.2911,-0.91027 21.0329,1.90246 31.0147,-1.5623 3.6074,-8.94566 0.8082,-20.35844 1.6907,-30.33803 -1.7706,-11.21144 -11.593,-5.3107 -17.2471,-6.77266 -10.2618,0.91172 -21.0759,-1.90454 -31.0147,1.5623 z"
           style="fill:#ffcc00;stroke-width:1.16134167" />
        <path
           inkscape:connector-curvature="0"
           id="path5003-56-9"
           d="m 586.11169,597.97717 c -3.4,8.94565 -0.7617,20.35843 -1.5935,30.33801 1.6688,11.21143 10.9262,5.3107 16.255,6.77268 9.6991,-0.91025 19.8229,1.90246 29.2305,-1.5623 3.3999,-8.94564 0.7617,-20.35844 1.5934,-30.33801 -1.6687,-11.21145 -10.9261,-5.31071 -16.2549,-6.77267 -9.6715,0.91171 -19.8635,-1.90454 -29.2305,1.56229 z"
           style="fill:#ffff00;stroke-width:1.12744308;opacity:0.714" />
        <path
           inkscape:connector-curvature="0"
           id="path5003-56-78"
           d="m 586.25219,615.5081 c -3.317,8.94564 -0.7432,20.35842 -1.5546,30.33799 1.6281,11.21144 10.6595,5.31073 15.8581,6.77269 9.4623,-0.91025 19.339,1.90246 28.5169,-1.56229 3.3169,-8.94566 0.7431,-20.35844 1.5545,-30.33803 -1.628,-11.21143 -10.6593,-5.3107 -15.858,-6.77266 -9.4353,0.91171 -19.3786,-1.90454 -28.5169,1.5623 z"
           style="fill:#ffff00;stroke-width:1.11359477" />
        <path
           inkscape:connector-curvature="0"
           id="path5003-56-2"
           d="m 584.53039,633.90951 c -3.6075,8.94563 -0.8082,20.35841 -1.6907,30.338 1.7706,11.21142 11.5931,5.3107 17.2471,6.77267 10.2911,-0.91025 21.0329,1.90246 31.0147,-1.56229 3.6074,-8.94565 0.8082,-20.35843 1.6907,-30.33801 -1.7706,-11.21145 -11.593,-5.31072 -17.2471,-6.77268 -10.2618,0.91173 -21.0759,-1.90454 -31.0147,1.56231 z"
           style="opacity:0.55500034;fill:#ccff00;stroke-width:1.16134167" />
        <path
           inkscape:connector-curvature="0"
           id="path5003-56-22"
           d="m 584.71469,658.6532 c -3.6075,8.94563 -0.8082,20.35842 -1.6907,30.33801 1.7706,11.21143 11.5931,5.31071 17.2471,6.77269 10.2911,-0.91027 21.0329,1.90246 31.0147,-1.5623 3.6074,-8.94566 0.8082,-20.35844 1.6907,-30.33804 -1.7706,-11.21143 -11.593,-5.3107 -17.2471,-6.77266 -10.2618,0.91171 -21.0759,-1.90454 -31.0147,1.5623 z"
           style="fill:#99ff55;stroke-width:1.16134167;opacity:0.961" />
        <path
           inkscape:connector-curvature="0"
           id="path5003-56-3"
           d="m 584.85389,703.90606 c -3.6075,8.94564 -0.8082,20.35842 -1.6907,30.338 1.7706,11.21144 11.5931,5.3107 17.2471,6.77269 10.2911,-0.91026 21.0329,1.90245 31.0147,-1.56231 3.6074,-8.94565 0.8082,-20.35843 1.6907,-30.33801 -1.7706,-11.21145 -11.593,-5.3107 -17.2471,-6.77268 -10.2618,0.91173 -21.0759,-1.90454 -31.0147,1.56231 z"
           style="fill:#80ffe6;stroke-width:1.16134167" />
        <path
           inkscape:connector-curvature="0"
           id="path5003-56-58"
           d="m 585.14039,686.3377 c -3.6075,8.94565 -0.8082,20.35843 -1.6907,30.33802 1.7706,11.21142 11.5931,5.3107 17.2471,6.77267 10.2911,-0.91025 21.0329,1.90246 31.0147,-1.56229 3.6074,-8.94565 0.8082,-20.35843 1.6907,-30.33802 -1.7706,-11.21145 -11.593,-5.31071 -17.2471,-6.77267 -10.2618,0.91171 -21.0759,-1.90454 -31.0147,1.56229 z"
           style="fill:#7fff2a;stroke-width:1.16134167;opacity:0.828" />
        <path
           inkscape:connector-curvature="0"
           id="path5003-56-58-2"
           d="m 584.85389,703.90606 c -3.6075,8.94564 -0.8082,20.35842 -1.6907,30.338 1.7706,11.21144 11.5931,5.3107 17.2471,6.77269 10.2911,-0.91026 21.0329,1.90245 31.0147,-1.56231 3.6074,-8.94565 0.8082,-20.35843 1.6907,-30.33801 -1.7706,-11.21145 -11.593,-5.3107 -17.2471,-6.77268 -10.2618,0.91173 -21.0759,-1.90454 -31.0147,1.56231 z"
           style="fill:#66ff00;stroke-width:1.16134167" />
        <path
           inkscape:connector-curvature="0"
           id="path5003-56-10"
           d="m 585.09079,725.8612 c -3.6075,8.94563 -0.8082,20.35841 -1.6907,30.338 1.7706,11.21143 11.5931,5.3107 17.2471,6.77268 10.2911,-0.91026 21.0329,1.90245 31.0147,-1.5623 3.6074,-8.94565 0.8082,-20.35843 1.6907,-30.33802 -1.7706,-11.21145 -11.593,-5.3107 -17.2471,-6.77266 -10.2618,0.91172 -21.0759,-1.90455 -31.0147,1.5623 z"
           style="fill:#55ddff;stroke-width:1.16134167" />
        <path
           inkscape:connector-curvature="0"
           id="path5003-56-90"
           d="m 585.89269,747.03808 c -3.6075,8.94563 -0.8082,20.35842 -1.6907,30.338 1.7706,11.21143 11.5931,5.31071 17.2471,6.77268 10.2911,-0.91026 21.0329,1.90246 31.0147,-1.56229 3.6074,-8.94566 0.8082,-20.35844 1.6907,-30.33803 -1.7706,-11.21143 -11.593,-5.3107 -17.2471,-6.77266 -10.2618,0.91172 -21.0759,-1.90454 -31.0147,1.5623 z"
           style="fill:#2ad4ff;stroke-width:1.16134167" />
        <path
           inkscape:connector-curvature="0"
           id="path5003-56-19"
           d="m 585.60629,766.98453 c -3.6075,8.94564 -0.8082,20.35842 -1.6907,30.33801 1.7706,11.21144 11.5931,5.3107 17.2471,6.77269 10.2911,-0.91026 21.0329,1.90245 31.0147,-1.56231 3.6074,-8.94565 0.8082,-20.35842 1.6907,-30.33802 -1.7706,-11.21145 -11.593,-5.3107 -17.2471,-6.77268 -10.2618,0.91173 -21.0759,-1.90454 -31.0147,1.56231 z"
           style="fill:#5599ff;stroke-width:1.16134167;opacity:0.893" />
        <path
           inkscape:connector-curvature="0"
           id="path5003-56-19-5"
           d="m 585.61359,791.90417 c -3.2718,8.94564 -0.733,20.35842 -1.5334,30.33801 1.6059,11.21144 10.5144,5.3107 15.6422,6.77269 9.3335,-0.91026 19.0758,1.90245 28.1288,-1.56231 3.2717,-8.94565 0.733,-20.35842 1.5334,-30.33802 -1.6059,-11.21145 -10.5143,-5.3107 -15.6422,-6.77268 -9.307,0.91173 -19.1148,-1.90454 -28.1288,1.56231 z"
           style="fill:#2a7fff;stroke-width:1.10599101" />
        <path
           inkscape:connector-curvature="0"
           id="path5003-56-19-5-6"
           d="m 585.83329,814.11463 c -3.339,8.94564 -0.7481,20.35842 -1.5649,30.33801 1.6388,11.21144 10.7301,5.31072 15.9633,6.77269 9.525,-0.91026 19.4672,1.90246 28.7059,-1.56229 3.3389,-8.94567 0.7481,-20.35844 1.5649,-30.33804 -1.6388,-11.21145 -10.7301,-5.3107 -15.9633,-6.77266 -9.4979,0.91171 -19.507,-1.90454 -28.7059,1.56229 z"
           style="fill:#0066ff;stroke-width:1.1172806" />
        <path
           inkscape:connector-curvature="0"
           id="path5003-56-19-5-6-8"
           d="m 585.98219,836.32508 c -3.2718,8.94565 -0.733,20.35843 -1.5334,30.33802 1.6058,11.21143 10.5144,5.3107 15.6422,6.77268 9.3336,-0.91025 19.0758,1.90246 28.1288,-1.5623 3.2717,-8.94565 0.733,-20.35844 1.5334,-30.33802 -1.6058,-11.21145 -10.5143,-5.31071 -15.6423,-6.77268 -9.3069,0.91172 -19.1147,-1.90454 -28.1287,1.5623 z"
           style="fill:#2a2aff;stroke-width:1.10599101" />
        <path
           inkscape:connector-curvature="0"
           id="path5003-56-19-5-6-8-7"
           d="m 585.95399,853.71187 c -3.4732,8.94563 -0.7781,20.35841 -1.6278,30.33801 1.7047,11.21144 11.1616,5.3107 16.6052,6.77269 9.908,-0.91027 20.25,1.90244 29.8603,-1.56231 3.4731,-8.94565 0.7781,-20.35843 1.6278,-30.33803 -1.7047,-11.21145 -11.1615,-5.3107 -16.6052,-6.77267 -9.8798,0.91173 -20.2914,-1.90454 -29.8603,1.56231 z"
           style="fill:#0000ff;stroke-width:1.1395241" />
        <path
           inkscape:connector-curvature="0"
           id="path5003-56-19-5-6-8-7-3"
           d="m 585.08729,875.38537 c -3.6075,8.94565 -0.8082,20.35842 -1.6907,30.33802 1.7706,11.21143 11.5931,5.3107 17.2471,6.77268 10.2911,-0.91025 21.0329,1.90246 31.0147,-1.5623 3.6074,-8.94565 0.8082,-20.35843 1.6907,-30.33802 -1.7706,-11.21145 -11.593,-5.31072 -17.2471,-6.77268 -10.2618,0.91172 -21.0759,-1.90454 -31.0147,1.5623 z"
           style="fill:#0000ff;stroke-width:1.16134179" />
        <path
           inkscape:connector-curvature="0"
           id="path5003-56-19-5-6-8-7-3-1"
           d="m 585.08729,875.38537 c -3.6075,8.94565 -0.8082,20.35842 -1.6907,30.33802 1.7706,11.21143 11.5931,5.3107 17.2471,6.77268 10.2911,-0.91025 21.0329,1.90246 31.0147,-1.5623 3.6074,-8.94565 0.8082,-20.35843 1.6907,-30.33802 -1.7706,-11.21145 -11.593,-5.31072 -17.2471,-6.77268 -10.2618,0.91172 -21.0759,-1.90454 -31.0147,1.5623 z"
           style="fill:#0000d4;stroke-width:1.16134179" />
        <path
           inkscape:connector-curvature="0"
           id="path5003-56-19-5-6-8-7-3-0"
           d="m 585.27159,897.59583 c -3.6075,8.94563 -0.8082,20.35841 -1.6907,30.33801 1.7706,11.21144 11.5931,5.3107 17.2471,6.77269 10.2911,-0.91026 21.0329,1.90245 31.0147,-1.56231 3.6074,-8.94565 0.8082,-20.35843 1.6907,-30.33803 -1.7706,-11.21145 -11.593,-5.3107 -17.2471,-6.77267 -10.2618,0.91173 -21.0759,-1.90454 -31.0147,1.56231 z"
           style="fill:#0000aa;stroke-width:1.16134179" />
        <rect
           y="434.28864"
           x="585.13049"
           height="499.13342"
           width="46.420193"
           id="rect4106"
           style="opacity:0.903;fill:none;fill-opacity:1;stroke:#190e0e;stroke-width:5.53763342;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:0.97633134" />
        <text
           xml:space="preserve"
           style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:23.39585686px;line-height:1.25;font-family:sans-serif;-inkscape-font-specification:'sans-serif, Bold';font-variant-ligatures:normal;font-variant-caps:normal;font-variant-numeric:normal;font-feature-settings:normal;text-align:start;letter-spacing:0px;word-spacing:0px;writing-mode:lr-tb;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.87734467"
           x="525.06128"
           y="539.55005"
           id="text5123"
           transform="scale(1.2163736,0.82211583)"><tspan
             sodipodi:role="line"
             id="tspan5121"
             x="525.06128"
             y="539.55005"
             style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:23.39585686px;font-family:sans-serif;-inkscape-font-specification:'sans-serif, Bold';font-variant-ligatures:normal;font-variant-caps:normal;font-variant-numeric:normal;font-feature-settings:normal;text-align:start;writing-mode:lr-tb;text-anchor:start;
             '''
    HTML +='stroke-width:0.87734467">%s</tspan></text>'%(max_v)
    HTML +='''
        <text
           xml:space="preserve"
           style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:23.39585686px;line-height:1.25;font-family:sans-serif;-inkscape-font-specification:'sans-serif, Bold';font-variant-ligatures:normal;font-variant-caps:normal;font-variant-numeric:normal;font-feature-settings:normal;text-align:start;letter-spacing:0px;word-spacing:0px;writing-mode:lr-tb;text-anchor:start;fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.87734467"
           x="528.78351"
           y="1141.118"
           id="text5127"
           transform="scale(1.2163736,0.82211583)"><tspan
             sodipodi:role="line"
             id="tspan5125"
             x="528.78351"
             y="1141.118"
             style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:23.39585686px;font-family:sans-serif;-inkscape-font-specification:'sans-serif, Bold';font-variant-ligatures:normal;font-variant-caps:normal;font-variant-numeric:normal;font-feature-settings:normal;text-align:start;writing-mode:lr-tb;text-anchor:start;
             '''
    HTML += 'stroke-width:0.87734467">%s</tspan></text>'%(min_v)
    HTML +='''
    
    </g>
    </svg>
    </xml>
    '''
    import webbrowser
    f = open('polar_illustration.html','w')
    f.write(HTML)
    f.close()
    webbrowser.open_new_tab('polar_illustration.html')