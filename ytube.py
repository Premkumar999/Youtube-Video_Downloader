import tkinter as tk
from tkinter import *
from pytube import YouTube
  
def Browse():
    download_Directory = filedialog.askdirectory(initialdir="YOUR DIRECTORY PATH")
    download_Path.set(download_Directory)
  
def Download():
    Youtube_link = video_Link.get()

    download_Folder = download_Path.get()
   
    getVideo = YouTube(Youtube_link)
   
    videoStream = getVideo.streams.get_highest_resolution()
  
    if videoStream!=None:
        videoStream.download(download_Folder)
        messagebox.showinfo("SUCCESSFULLY", 
                        "DOWNLOADED AND SAVED IN\n" 
                        + download_Folder)
    else:
        messagebox.showinfo("Download Failed : Try with correct URL")
  
# Creating object of tk class
root = tk.Tk()

root.geometry("600x120")
root.resizable(False, False)
root.title("Youtube Video Downloader")
root.config(background="#E6E6FA")
# Creating the tkinter Variables
video_Link = StringVar()
download_Path = StringVar()

def Reset():
    video_Link.set("")
    download_Path.set("")
  
link_label = Label(root,text="YouTube video link  :",bg="grey")

link_label.grid(row=1,column=1,pady=5,padx=5)

root.linkText = Entry(root,width=55,textvariable=video_Link)

root.linkText.grid(row=1,column=2,pady=5,padx=5,columnspan = 2)
    
destination_label = Label(root, text="Destination Folder    :",bg="grey")
destination_label.grid(row=2,column=1,pady=5,padx=5)
   
root.destinationText = Entry(root,width=55,textvariable=download_Path)
root.destinationText.grid(row=2, column=2,pady=5,padx=5,columnspan=2)
   
browse_B = Button(root, text="Browse",command=Browse,width=15,bg="#05E8E0")
browse_B.grid(row=2,column=5,pady=1,padx=1)

Download_B = Button(root,text="Download", command=Download, width=20,bg="yellow")
Download_B.grid(row=3,column=2,pady=3,padx=3)

reset_B = Button(root,text="Reset", command=Reset,width=20,bg="green")
reset_B.grid(row=3,column=3,pady=3,padx=3)
   
root.mainloop()
