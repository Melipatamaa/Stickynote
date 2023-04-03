from .settings import *
from .button import *
import os
import ffmpeg

# The Save class is a subclass of the Button class. It has the same attributes as the Button class,
# but it also has a screen attribute so as to get the drawing that has to be saved.
class Save(Button) :
    def __init__(self,x,y,width,height,screen,color,unique_id,border_color=LGREY,text=None,text_color=BLACK,icon = None):
        super().__init__(x,y,width,height,color,border_color,text,text_color,icon)
        self.screen = screen
        self.unique_id = unique_id
        self.dossier = f"{os.getcwd()}\\frames_{unique_id}"

    def save(self,frame_speed):
        #TODO: essayer avec la librairie opencv ?????????
        frame_rate = 1 # faire choisir à l'utilisateur? ou faire un rapport avevc frme   
        files = os.listdir(self.dossier)
        # keep only the jpg files just to be sure
        files = [f for f in files if f.endswith('.jpg')]
        # sort by filename
        files.sort()

        # Create the ffmpeg input stream from the list of image files
        input_stream = ffmpeg.input('pipe:', format='image2', framerate=frame_rate)
        for image_file in files:
            input_stream = ffmpeg.concat(input_stream, ffmpeg.input(image_file))

        # Create the ffmpeg output stream for the video
        output_filename = f"animation_{self.unique_id}.mp4"
        output_stream = ffmpeg.output(input_stream, output_filename)

        try:
            ffmpeg.run(output_stream, cmd=r'C:\ffmpeg\bin\ffmpeg.exe', capture_stdout=True, capture_stderr=True)
        except Exception as e:
            print('stdout:', e.stdout.decode('utf8'))
            print('stderr:', e.stderr.decode('utf8'))
            raise e
