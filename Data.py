import tkinter 
import customtkinter
import os
import sys
from pytube import YouTube
from tkinter import filedialog
from tkinter import *

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def startDownload(option):
    try:
        ytLink = Link.get()
        ytObject = YouTube(ytLink, on_progress_callback=on_progress)
        if option == "hq":
            video = ytObject.streams.get_highest_resolution()
            file_path_hq = filedialog.asksaveasfilename(defaultextension=".mp4", filetypes=[("MP4 files", "*.mp4")])
            video.download(file_path_hq)
        elif option == "lq":
            video = ytObject.streams.get_lowest_resolution()
            file_path_lq = filedialog.asksaveasfilename(defaultextension=".mp4", filetypes=[("MP4 files", "*.mp4")])
            video.download(file_path_lq)
        elif option == "audio":
            video = ytObject.streams.get_audio_only()
            file_path_audio = filedialog.asksaveasfilename(defaultextension=".mp3", filetypes=[("Audio files", "*.mp3")])
            video.download(file_path_audio)
        else:
            return 
        

        title.configure(text=ytObject.title, text_color = "White")
        finishLabel.configure(text = "")
        video.download()
        finishLabel.configure(text="Downlaoded!")
    except:
        finishLabel.configure(text="Downlaod Error", text_color="red")


def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percenatge_of_completion = bytes_downloaded / total_size *100
    per = str(int(percenatge_of_completion))
    pPercentage.configure(text= per + "%")
    pPercentage.update()

    #Upgrade Bar
    progressBar.set(float(percenatge_of_completion) / 100)



#System Settings
customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("green")


#Our app frame
app = customtkinter.CTk()
app.geometry("1920x1200")
app.title("Youtube Downloader")



#create a Label
bg_label = Label(app, image=bg)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

#Adding UI elements
title = customtkinter.CTkLabel(app, text="Insert Link", width=200, height=50, font=("Arial Black", 30))
title.pack(padx=10, pady=10)

#Link input
url_var = tkinter.StringVar()
Link = customtkinter.CTkEntry(app, width=550, height=40, textvariable=url_var)
Link.pack()

#Finished Downloading
finishLabel = customtkinter.CTkLabel(app, text="")
finishLabel.pack()

#Progress Bar
pPercentage = customtkinter.CTkLabel(app, text = "0%")
pPercentage.pack()

progressBar = customtkinter.CTkProgressBar(app, width=400)
progressBar.set(0)
progressBar.pack(padx=10, pady=10)



# Download High Quality Video Button
download_hq = customtkinter.CTkButton(app, text="Download High Quality-Mp4", command=lambda: startDownload("hq"))
download_hq.pack(padx=10, pady=10)

# Download Low Quality Video Button
download_lq = customtkinter.CTkButton(app, text="Download Low Quality-Mp4", command=lambda: startDownload("lq"))
download_lq.pack(padx=10, pady=10)

# Download Audio Button
download_a = customtkinter.CTkButton(app, text="Download Mp3", command=lambda: startDownload("audio"))
download_a.pack(padx=10, pady=10)


#Run app
app.mainloop()




