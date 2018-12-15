#!/usr/bin/env python3

#
# Based on mtrix example from Pimoroni Unicorn HAT
# which was ported from Pimoroni Unicorn Hat example https://github.com/pimoroni/unicorn-hat/blob/master/examples/hat/matrix.py
# to unicornhat hd by aburgess@gmail.com (https://github.com/Mutiny-Games)
#

# brightness
# clear
# get_rotation
# get_shape
# off
# rotation
# set_layout
# set_pixel
# set_pixel_hsv
# show

import argparse
from time import sleep
import unicornhathd as uh

pixels = []

display_width, display_height = uh.get_shape() 
uh.brightness(1.0)  # full brightness
uh.rotation(90)

w = (255,255,255)
b = (0,0,0)
r = (255,0,0)
g = (0,255,0)
B = (0,0,255)
br = (150,75,0)

patterns = {}
patterns['blank'] = [[w]]
patterns['check'] = [
   [r,w,r,w],
   [r,B,r,B],
   [w,B,w,B],
   [w,w,w,w]
   ]
patterns['stripe'] = [
   [w,r,w,w],
   [r,w,w,w],
   [w,w,w,r],
   [w,w,r,w]
   ]
patterns['stripes'] = [
   [w,r,w,w,B],
   [r,w,w,B,w],
   [w,w,B,w,r],
   [w,B,w,r,w],
   [B,w,r,w,w]
   ]
patterns['matrix'] = [
   [(154, 173, 154), (0, 0, 0), (0, 0, 0)],
   [(0, 255, 0), (0, 0, 0), (154, 173, 154)],
   [(0, 235, 0), (154, 173, 154), (0, 255, 0)], 
   [(0, 220, 0), (0, 145, 0), (0, 235, 0)], 
   [(0, 185, 0), (0, 125, 0), (0, 220, 0)], 
   [(0, 165, 0), (0, 100, 0), (0, 185, 0)], 
   [(0, 128, 0), (0, 80, 0), (0, 165, 0)], 
   [(0, 0, 0), (0, 60, 0), (0, 128, 0)], 
   [(0, 0, 0), (0, 40, 0), (0, 0, 0)], 
   [(0, 0, 0), (0, 0, 0), (0, 0, 0)]
   ]
# space invader
patterns['invader'] = [
   [w,w,w,w,w,w],
   [w,r,r,r,r,r],
   [w,r,w,r,w,r],
   [w,r,r,r,r,r],
   [w,w,r,w,r,w]
   ]
patterns['blocks'] = [
   [B,B,r,r,g,g],
   [B,g,r,r,g,B],
   [g,g,B,B,r,r],
   [g,B,B,g,r,r],
   [r,r,g,g,B,B],
   [r,r,g,B,B,g]
   ]
patterns['bird'] = [
   [w,w,w,w,w,w],
   [w,w,w,w,r,w],
   [w,r,w,r,r,r],
   [w,w,r,r,w,w],
   [w,w,w,b,w,w],
   [w,w,b,b,b,w]
   ]
patterns['dog'] = [
   [w,w,w,w,w,w],
   [w,br,w,w,br,w],
   [w,w,br,br,br,b],
   [w,w,br,br,br,w],
   [w,w,br,w,br,w]
   ]
patterns['butterfly'] = [
   [w,w,w,w,w,w,w,w],
   [w,r,r,w,w,w,r,r],
   [w,r,r,r,b,r,r,r],
   [w,br,br,br,b,br,br,br],
   [w,w,br,br,w,br,br,w]
   ]
patterns['heart'] = [
   [w,w,w,w,w,w],
   [w,w,r,w,r,w],
   [w,r,r,r,r,r],
   [w,w,r,r,r,w],
   [w,w,w,r,w,w]
   ]
patterns['note'] = [
   [w,w,w],
   [w,w,B],
   [w,w,B],
   [w,B,B],
   [w,B,B]
   ]

def invert(pattern):
   return [pattern[n] for n in range(len(pattern)-1, -1, -1)]


def shader(x, y):
   py = (display_height-1) - y
   return pixels[py][x][0], pixels[py][x][1], pixels[py][x][2]

#def main(argv):     
   #try:
   #   opts, args = getopt.getopt(argv,"hps",["pattern=","speed="])
   #except getopt.GetoptError:
   #   print('{} -p <pattern> -s <speed>'.format('weave.py'))
   #   sys.exit(2)
   #for opt, arg in opts:
   #   if opt == '-h':
   #      print('{} -p <pattern> -s <speed>'.format('weave.py'))
   #      sys.exit()
   #   elif opt in ("-p", "--pattern"):
   #      pattern_name = arg
   #   elif opt in ("-s", "--speed"):
   #      print('arg={}'.format(arg))
   #      #speed = int(arg) / 1000

def main():
   global pixels
   
   parser = argparse.ArgumentParser(description='Digital Weaving.')
   parser.add_argument('pattern', metavar='pattern name', type=str, default='blank', 
                    help='name of pattern')
   parser.add_argument('--speed', dest='speed', type=int, default=10,
                    help='speed in milliseconds (default: 10ms)')

   args = parser.parse_args()
   #print(args.accumulate(args.integers))
   pattern_name = args.pattern
   speed = args.speed / 1000

   pattern = patterns[pattern_name]
    
   print("""Digital Weaving
""")
   try:
      pat_h = len(pattern)
      pat_w = len(pattern[0])
      pixels = [[b]*display_width]*display_height
            
      for row in range(0, display_height):
         odd_row = row % 2
         row_pat = row % pat_h
         pixel_row = []
         # scroll
         old_row = pixels.pop(0)
         pixels.append(old_row)
         uh.shade_pixels(shader)
         for col in range(display_width-1 if odd_row else 0, 
                 -1 if odd_row else display_width, -1 if odd_row else 1):
            pixel = pattern[row_pat][col % pat_w]
            if odd_row:
               pixel_row.insert(0,pixel)
            else:
               pixel_row.append(pixel)
            # fade in pattern
            for fade in range(0, 100, 12):
               f = fade / 100
               uh.set_pixel(col, 0, int(pixel[0]*f), int(pixel[1]*f), int(pixel[2]*f))
               uh.show()
               sleep(speed)
         pixels[display_height-1] = pixel_row
      sleep(5)
   except KeyboardInterrupt:
      pass
   uh.off()


if __name__ == "__main__":
   #main(sys.argv[1:])
   main()
