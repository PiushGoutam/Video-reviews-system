from moviepy.editor import *
import os

class MakeMovie:
    """A wrapper class to make movie using custom text and scraped reviews"""

    def __init__(self,movie_name):
        self.screensize = (1920,1080)
        self.movie_name = movie_name
        # These are custom texts
        self.text_strings =  ["Hello Dear User!",
                f"So you wanted to watch the movie {self.movie_name}?",
                "You thought the movie would be a bad bad movie didn't you?",
                "You seriously underestimated this film?"
                "This Film?",
                "THISSSSSS FILLLLMM??????",
                "Come Let's See...",
                "What people have got to say about this brilliant film..."]
        self.clip_list = []


    def pre_cast_text(self):
        """Text before introducing reviews"""
        for text in self.text_strings:
            try:
                    
                txt_clip = TextClip(text,fontsize=70,bg_color = "white",size=self.screensize).set_duration(3)
                self.clip_list.append(txt_clip)

            except UnicodeEncodeError:
                txt_clip = TextClip("Issue with text", fontsize = 70, color = 'white').set_duration(2)
                self.clip_list.append(txt_clip)

    def review_screenshots(self):
        image_strings = list(filter(lambda x: x.endswith('.png'),os.listdir(os.getcwd())))
        clips = [ImageClip(m).on_color(size= self.screensize,color=(0,128,128)).set_duration(2) for m in image_strings]
        self.clip_list+=clips

    def post_cast_text(self):
        """text after reviews"""
        post_text = ["So you made up your mind now?",
                    "Still don't wanna watch it?",
                    "Good Luck!",
                    "Bye-bye"]
        for text in post_text:
            try:
                    
                txt_clip = TextClip(text,fontsize=70,bg_color = "white",size=self.screensize).set_duration(3)
                self.clip_list.append(txt_clip)

            except UnicodeEncodeError:
                txt_clip = TextClip("Issue with text", fontsize = 70, color = 'white').set_duration(2)
                self.clip_list.append(txt_clip)             

    def finalize(self,movie_name):
        final_clip = concatenate(self.clip_list, method = "compose")
        
        final_clip.write_videofile(f"my_video_review_of_{movie_name}.mp4", fps = 24, codec = 'mpeg4')
        print(f"Saving video as my_video_review_of_{movie_name}.mp4 .. ")