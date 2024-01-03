#importing the modules...

from moviepy.editor import VideoFileClip
from tkinter.filedialog import *

# This line asks You to open a file...
video = askopenfilename()

clip = VideoFileClip(video)

#gifname you want to save with...
gifname = input("Enter the GIF name to be saved : ") 

#this line used imageio to create gifs
clip.write_gif(gifname,fps=10)