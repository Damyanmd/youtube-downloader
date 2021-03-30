from tkinter import *
import pytube

root = Tk()
root.geometry('500x200')
root.title('YouTube Downloader by Damyan Doykov')
root.resizable(0, 0)

variable1 = StringVar()

def download():
    url = variable1.get()
    youtube = pytube.YouTube(url)
    video = youtube.streams.get_highest_resolution()
    #directory for the video
    video.download('.../Video')

def clear_view(tk):
    for el in tk.grid_slaves():
        el.destroy()

def information():
    clear_view(root)
    url = variable1.get()
    youtube = pytube.YouTube(url)
    Label(root, text="Video title: ").grid(row=0, column=0)
    Label(root, text=youtube.title).grid(row=0, column=1, padx=0, pady=0)
    Label(root, text="Video id: ").grid(row=1, column=0, padx=0, pady=0)
    Label(root, text=youtube.video_id).grid(row=1, column=1, padx=0, pady=0)
    Label(root, text="Video age restriction: ").grid(row=2, column=0, padx=10, pady=0)
    Label(root, text=youtube.age_restricted).grid(row=2, column=1, padx=0, pady=0)
    Label(root, text="Video views: ").grid(row=3, column=0, padx=0, pady=0)
    Label(root, text=youtube.views).grid(row=3, column=1, padx=0, pady=0)
    Label(root, text="Video length in seconds: ").grid(row=4, column=0, padx=10, pady=0)
    Label(root, text=youtube.length).grid(row=4, column=1, padx=0, pady=0)
    Label(root, text="Video rating: ").grid(row=6, column=0, padx=0, pady=0)
    Label(root, text=youtube.rating).grid(row=6, column=1, padx=0, pady=0)
    button = Button(root, text='Back', font='arial 10', bg='white smoke', command=lambda: main_windows())
    button.grid(row=7, column=0, padx=30, pady=20)

def main_windows():
    clear_view(root)
    Entry(root, width=50, textvariable=variable1).grid(row=0, column=1, padx=0, pady=20)
    Label(root, text="Link to YouTube: ").grid(row=0, column=0, padx=0, pady=20)
    button = Button(root, text='Download',  font='arial 15 bold', bg='white smoke', command=lambda: download())
    button.grid(row=1, column=0, padx=30, pady=20)
    button = Button(root, text='Information',  font='arial 15 bold', bg='white smoke', command=lambda: information())
    button.grid(row=1, column=1, padx=0, pady=20)

main_windows()
root.mainloop()
