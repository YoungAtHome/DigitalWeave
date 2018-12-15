#!/usr/bin/env python3

#
# Patterns for digital weaving
#

# colours
w = (255,255,255)
b = (0,0,0)
r = (255,0,0)
g = (0,255,0)
B = (0,0,255)
br = (150,75,0)


def invert(pattern):
   return [pattern[n] for n in range(len(pattern)-1, -1, -1)]

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

if __name__ == "__main__":
   print(patterns)
