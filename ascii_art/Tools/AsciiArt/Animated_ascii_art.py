
import PIL.Image 
import PIL.ImageDraw
import PIL.ImageFont
from datetime import datetime
import os
from ascii_art.Tools.AsciiArt.Ascii_art import Ascii_art

class Animated_ascii_art:
    
    def __init__(self) -> None:
        self.ascii_art = Ascii_art()
        self.input_png_frames_dir = 'media/animations/input_png_frames'
        self.output_png_ascii_frames = 'media/animations/output_png_ascii_frames'
        self.gif_output_dir = 'media/animations/gif_output'
        
        
    
    def do_animated_ascii_art(self,animation,width_image=100):
    
       #self.frames_directory = self.create_directory()
        message = ""
        animated_ascii_file = ""
        animation_frames = self.extract_animation(animation)
        ascii_frames= self.convert_frames_to_ascii(animation_frames)
        animated_ascii_file = self.convert_ascii_frames_to_png_frames(ascii_frames,640,480)
        
        context = {"animated_ascii_file":animated_ascii_file,
                   "ascii_frames":ascii_frames,
                   "message": message
                   }
    
        return context
    
    # extract frames from gif animation
    def extract_animation(self,animation):
        animation_frames = []
        im = PIL.Image.open(animation)
        frames_quantity  = im.n_frames
        for i in range(frames_quantity):
            frame = im.seek(i)
            
            frame_file = self.input_png_frames_dir + '/frame_' + str(i) + '.png'
            im.save(frame_file)
            animation_frames.append(frame_file)
        im.close()
        return animation_frames
            

    #return list of frames(path to files)
    def convert_frames_to_ascii(self,animation_frames):
        print("converting frames to ascii...")
        print(animation_frames)
        ascii_frames=[]
        
        for frame_file in animation_frames:
            ascii_frames.append(self.ascii_art.do_ascii_art(frame_file)['filepath'])
            
        for asciiframe in ascii_frames:
           print(asciiframe)
           
        return ascii_frames
    
    #save plain ascii in graphics file
    def convert_ascii_frames_to_png_frames(self,ascii_frames,x,y):
        output_png_ascii_frames =[]
        for ascii_frame in ascii_frames:
            #create empty png file with same name as ascii frame file
            ascii_frame_plain_file = ascii_frame.split('/')[2][:-4] + '.png'   
        
            output_png_frame = self.output_png_ascii_frames + '/' + ascii_frame_plain_file

            self.write_text_on_plain_png(ascii_frame,output_png_frame)
            
            output_png_ascii_frames.append(output_png_frame)
        return output_png_ascii_frames
    
    
     #create empty png file with same name as ascii frame file and fill with ascii
    def write_text_on_plain_png(self,ascii_frame,output_png_frame):
        
        with open (ascii_frame) as f:
            
            lines = [line.rstrip() for line in f]
        print("11111111111111111111111111111111111111111111111111LEN")  
        print(len(lines[0]))
        x = 6 * len(lines[0])
        y = 4* len(lines[0])   
        img = PIL.Image.new("RGB", (x, y), (255, 255, 255))        
        for index,l in enumerate(lines):
                        
            draw = PIL.ImageDraw.Draw(img)    
            draw.text((0, index*6),l, (0,0,0), )
        img.save(output_png_frame  , "PNG") 
           
        
            
    
    #łączenie klatek w animacje
    def create_gif_animation_from_list(self,images):
        images[0].save(self.gif_output_dir +  '/output.gif',
               save_all=True, append_images=images[1:], optimize=False, duration=40, loop=0)
        
     
    def create_directory(self,dir_path):
           
        isExist = os.path.exists(dir_path)
        if not isExist:
            os.makedirs(dir_path)
            print("Directory created")
        
    