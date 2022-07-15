from Animated_ascii_art import Animated_ascii_art
from Ascii_art import Ascii_art


anim = Animated_ascii_art()
ascii = Ascii_art()
dupa = anim.do_animated_ascii_art('ptak.gif')
print(len(dupa))
for d in dupa:
    ascii.do_ascii_art(d)
    
print("DONE")
    
