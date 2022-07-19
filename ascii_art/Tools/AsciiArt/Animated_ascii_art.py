
import PIL.Image 
import PIL.ImageDraw
import PIL.ImageFont
from datetime import datetime
import os
from ascii_art.Tools.AsciiArt.Ascii_art import Ascii_art

class Animated_ascii_art:
    
    def __init__(self,filename) -> None:
        self.ascii_art = Ascii_art()
        self.input_png_frames_dir = 'media/animations/input_png_frames'
        self.output_png_ascii_frames = 'media/animations/output_png_ascii_frames'
        self.gif_output_dir = 'media/animations/gif_output' 
        self.message ="completed"
        self.current_gif_duration_list=[] #keep duration parameter for current gif file uploaded
        self.gif_output_name =  filename.split('.')[0] + self.add_unique_name() +".gif"
        
        
        print("PILLOW VER:")
        print(PIL.__version__)
        
        

  

    def get_file_size(self,filename):
        im = PIL.Image.open(filename)
        im.close()
        width, height = im.size
        return {"width":width,"height":height}

    def add_unique_name(self):
       return datetime.now().strftime("%H_%M_%S") +"_"+ str(datetime.now().microsecond)
        
    
    
    def do_animated_ascii_art(self,animation,width_image=50):
        self.width_image = width_image
        animation_frames = self.extract_animation(animation)
        self.file_size = self.get_file_size(animation_frames[0])
        ascii_frames= self.convert_frames_to_ascii(animation_frames,width_image) #return asci_art_list of dict
        animated_ascii_png_list = self.convert_ascii_frames_to_png_frames(ascii_frames,1280,1024)
        gif_ascii_art_animation = self.create_gif_animation_from_png_list(animated_ascii_png_list[1])
        
        context = {"animated_ascii_file":gif_ascii_art_animation,
                   "ascii_frames":ascii_frames,
                   "message": self.message
                   }
    
        return context
    
    # extract frames from gif animation
    def extract_animation(self,animation):
        animation_frames = []
        im = PIL.Image.open(animation)
        frames_quantity  = im.n_frames
        frame_duration =0
        for i in range(frames_quantity):
            frame = im.seek(i)
            frame_duration = im.info['duration']
            self.current_gif_duration_list.append(frame_duration)
            frame_file = self.input_png_frames_dir + '/frame_' + str(i) + self.add_unique_name() +  '.png'
            im.save(frame_file)
            animation_frames.append(frame_file)
        im.close()
        return animation_frames
            

    #return list of frames(path to files)
    def convert_frames_to_ascii(self,animation_frames,width_image):
        print("converting frames to ascii...")
        print(animation_frames)
        ascii_art_list =[]
        
        for frame_file in animation_frames:

            ascii_art_list.append(self.ascii_art.do_ascii_art(frame_file,width_image))
            
            
        print("path to ascii files:")
        for asciiframe in ascii_art_list:
           print(asciiframe['filepath'])
           
        return ascii_art_list
    
    #save plain ascii in graphics file
    def convert_ascii_frames_to_png_frames(self,ascii_frames,x,y):
        output_png_ascii_frames =[] #path to files
        images_list=[] # PIL.image obj list
        
        
        
        #ascii_frames is a Ascii_art object list
        for a in ascii_frames:
            
            asciiart_image = a['ascii']
            for a in asciiart_image:
                print(a)
            
       
        for ascii_frame in ascii_frames:
            
            #create empty png file with same name as ascii frame file
            ascii_frame_plain_file = ascii_frame['filepath'].split('/')[2][:-4] + '.png'   
        
            output_png_frame = self.output_png_ascii_frames + '/' + ascii_frame_plain_file
            images_list.append(self.write_text_on_plain_png(ascii_frame['filepath'],output_png_frame[0])) #generate tect on in plain file
            
            
            output_png_ascii_frames.append(output_png_frame)
        return output_png_ascii_frames,images_list
    
    
    def crop_image(self,img,x1,y1,x2,y2): 
        area = (x1, y1, x2, y2)
        cropped_img = img.crop(area)
        #cropped_img.show()
        return cropped_img
    
     #create empty png file with same name as ascii frame file and fill with ascii
    def write_text_on_plain_png(self,ascii_frame,output_png_frame):
        
        with open (ascii_frame) as f:
            
            lines = [line.rstrip() for line in f]
        print("line LEN:")  
        print(len(lines[0]))
      
        #zadbac o proporcje obrazka gif zaleznie od ilosci znakow x,y w ascii
        #1 jeli x i y w obrazku wejscowym sa rowne to
        if self.file_size['width'] == self.file_size['height']:
            mx = 6
            my = 6
           
        else:
            mx=6
            my= int( (self.file_size['height'] * mx) // self.file_size['width'])

        
        ratio_factor = int((len(lines) * 190)/270)
        x = mx * len(lines[0])
        y = my * len(lines[0]) + ratio_factor

        img = PIL.Image.new("RGBA", (x, y), (0, 255, 0 ,0))  
        latest_index=None      
        for index,l in enumerate(lines):
                        
            draw = PIL.ImageDraw.Draw(img)    
            draw.text((0, index*6),l, (0,0,0), )
            
        PIL.rgb_im = img.convert('RGB')
        r, g, b = PIL.rgb_im.getpixel((self.file_size['width'],self.file_size['height']))
        print(r, g, b)
      
        crop_val = self.crop_val(img)
        print("crop val")
        print (crop_val)
        if (crop_val >0): # przycinanie gdy obrazek ascii mniejszy niz fizyczna wysokosc zdjecia
            print("crop")
            img = self.crop_image(img,0,0,x,y - crop_val*6)
            
        
        img.save(output_png_frame  , "PNG") 
        return img
        
    #compute how many pixels must be cut from the bootom   
    def crop_val(self,img):
        PIL.rgb_im = img.convert('RGB')
        r, g, b = PIL.rgb_im.getpixel((self.file_size['width'],self.file_size['height']))
        print(r, g, b)
        if g==255:
            i=0
            while g==255:
                r, g, b = PIL.rgb_im.getpixel((self.file_size['width'],self.file_size['height']-i))
                i = i +1
            return  i
        else:
            return 0
                
                
            
    #merge frames in animation
    def create_gif_animation_from_png_list(self,png_list_images):
        #gif_ascii_art_animation = self.gif_output_dir +  '/animated_ascii_art.gif'
        
        gif_ascii_art_animation = self.gif_output_dir + '/' + self.gif_output_name
        
        png_list_images[0].save(gif_ascii_art_animation,
               save_all=True, append_images=png_list_images[1:], optimize=False, duration=self.current_gif_duration_list, loop=0)
        return gif_ascii_art_animation
        
     
    def create_directory(self,dir_path):
           
        isExist = os.path.exists(dir_path)
        if not isExist:
            os.makedirs(dir_path)
            print("Directory created")
            
            
    def clean_up(self):
        pass
        
    