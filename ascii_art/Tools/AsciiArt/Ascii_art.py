
import PIL.Image 
from datetime import datetime
import os

class Ascii_art:
    
    def __init__(self):
        
        self.ASCII_CHARS = ["@", "J", "D", "%", "*", "P", "+", "Y", "$", ",", "."]  
    def resize_image(self,image,width_image = 200):
        try:
            new_width = width_image
            image  = PIL.Image.open(image)
            width,height = image.size
            new_height = new_width * height/width
            result = image.resize((int(new_width),int(new_height)))
            
        except Exception as e:
            result = False  
        return  result
       
    
    def grayscale(self,image):
        return image.convert("L")
    
    
    def pixel_to_ascii(self,image):
        pixels = image.getdata()
        
        ascii_str = ""
        for pixel in pixels:

          ascii_str += self.ASCII_CHARS[pixel//25]
        return ascii_str
        
    def do_ascii_art(self,image,width_image=50):
        
       print("do ascii art")
        
       ascii_art_result ={
            "ascii": "incorrect file format",
            "width":0,
            "height":0,
            "filepath":None    
            }        
        
        
       small_image = self.resize_image(image,width_image)
       if small_image != False: # image ok
       
            small_image = self.grayscale(small_image)
            img_width = small_image.width
            ascii_string = self.pixel_to_ascii(small_image)
            ascii_string_len = len(ascii_string)
            ascii_final = ""
        
            #keep image ratio
            for i in range(0,ascii_string_len,img_width):
                    ascii_final += ascii_string[i:i+img_width] + "\n"
                    
                # save ascii image 
                
            current_file_path ='media/ascii/ascii_image_' + datetime.now().strftime("%H_%M_%S") +"_"+ str(datetime.now().microsecond) + ".txt"
            with open(current_file_path,"w") as f:
                    f.write(ascii_final)
                    
            with open (current_file_path) as f:
                lines = [line.rstrip() for line in f]
                
                
            for l in lines:
                print(l)
                
            
            ascii_art_result ={
                "ascii": lines,
                "width":small_image.width,
                "height":small_image.height,
                "filepath":current_file_path    
            }
            
       result = ascii_art_result
            
       return result