import json

pDict = {'/': {'image': True, 'imagename': 'main_cover.jpg', 'header1': "About Me", 'text1': """I am a STEM 
enthusiast and student based in the greater Denver Metropolitan area. I love challenges, especially in the areas of 
math and computer science. If you are curious about my projects, check out the blog page. If you would like to learn 
something, don't hesitate to check out the tutorials page. To see some fun tools I have made in Javascript, 
check out the widgets page.""", 'purl': [], 'ptext': []},
         '/blog': {'image': True, 'imagename': 'blog_cover.jpg', 'header1': "Welcome!",
                   'text1': """I frequently find myself working on all kinds of projects. I wish to share some of 
                   them that I find cool or that I think will inspire you.""", 'purl': ['1'],
                   'ptext': ['Creation of this Site']},
         '/tutorials': {'image': True, 'imagename': 'tutorials_cover.jpg', 'header1': "Welcome!",
                        'text1': """I have a strong passion to understand things at a deeper level. Here are some of 
                        my attempts to diffuse that passion to you and to inspire you to pursue STEM related 
                        fields.""", 'purl': ['player'], 'ptext': ['Tutorials Media Player']},
         '/widgets': {'image': True, 'imagename': 'widgets_cover.jpg', 'header1': "Welcome!",
                      'text1': """I occasionally create small web widgets to help me speed up tasks, visuallize 
                      mathematical concepts, or challenge my Javascript skills. This page holds a few of those 
                      widgets that I feel are worth sharing.""", 'purl': ['line_motion', 'word_tools', 'the_button',
                                                                          'ceaser_cipher'],
                      'ptext': ['Motion Along a Line', 'Word Tools', 'Self Destruct Button', 'Ceaser Cipher']},
         'widget': {'line_motion': {'header1': "Line Motion", 'text1': """This widget was designed to help one gain 
         an intuitive understanding of how distance, velocity, speed, and acceleration relate to each other. At this 
         widget's current state, only polynomials are fully supported. The key thing to notice as you are playing 
         around with this widgets is how roots correspond to extrema of higher order derivatives. After messing around 
         with the initially example, feel free to enter your own. In case you don't already know the relation 
         between these functions, velocity is the rate of change (derivative) of distance, speed is the absolute 
         value of velocity, and acceleration is the rate of change of velocity. Something interesting you may notice 
         is that the speed function shows whether or not the velocity function is heading towards the x-axis (which 
         signifies no motion). Another way to put this is that the speed function is decreasing when the velocity 
         function is negative and heading towards the x-axis (meaning the acceleration would need to be positive) or 
         the velocity function is positive and heading towards the x-axis (negative acceleration) and increasing when 
         the velocity function is positive and heading away from the x-axis (positive acceleration) or when the 
         velocity is negative and heading away from the x-axis (negative acceleration)."""},
                    'word_tools': {'header1': "Word Tools", 'text1': """Tools for words!"""},
                    'the_button': {'header1': "Self Destruct Button", 'text1': """Don't press it!"""},
                    'ceaser_cipher': {}},
         'blog': {'1': {'header1': "Creation of this Site", 'text1': "Hello World!"}}}

json.dump(pDict, open("pages.json", "w"))


