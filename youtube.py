from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube

Folder_Nmae=""
def openlocation():
    global Folder_Nmae
    Folder_Nmae=filedialog.askdirectory()#لفتح المجلد 
    if(len(Folder_Nmae)>1):
       downloadlabel.config(text=Folder_Nmae,fg="green")
       DownloadVideo()
    else:
        downloadlabel.config(text="Choes Folder to save",fg="black")    


def DownloadVideo():
    try:
         choose=ytbChoice.get()
         url=urlEntry.get()

         if(len(url)>1):
             urlError.config(text="Error")
             yt=YouTube(url)


             if  (choose == chooses[0]):
               select=yt.streams.filter(progressive=True,file_extension="mp4").get_highest_resolution()
             
             
             elif  (choose==chooses[1]):
               select=yt.streams.filter(progressive=True,file_extension="mp4").get_lowest_resolution()


               
             elif  (choose==chooses[2]):
               select=yt.streams.filter(only_audio==True)._first()
             
         else:
             urlError.config(text="paste URL again!" , fg="red")
         select.download(Folder_Nmae)
        
         downloadlabel.config(text="Download Compleated!" ,fg="green" )
    except Exception as err :
        print(err)    
     


root =Tk()
root.geometry('600x380')

#Title
root.title('youtube video Downloader')
root.columnconfigure(0,weight=1)
title =Label(root,text="youtube video Downloader ",
fg="red",font=('jost',15))
title.grid(row=0, padx=100,pady=20)

#URL 
urllable=Label(root,text="pasta video URL",font=('jost',15))
urllable.grid(row=1)


urlEntry=Entry(root,width=40,fg="blue",font=('jost',15))
urlEntry.grid(row=2 ,pady=5 , padx=20)
 
urlError=Label(root,text="",fg="red",font=("jost",13))
urlError.grid(row=3)

choicelable=Label(root,text="choes type and quality",
font=('jost',15))
choicelable.grid(row=4)


#Combobox
chooses=["high quality vido","low quality vidoe","Audio file"]
ytbChoice=ttk.Combobox(root,values=chooses,
font=('jost',15))
ytbChoice.grid(row=5,pady=10)


#Button
downloadBtn=Button(root, command=openlocation,text="Download",width=20,bg="red",fg="white",
font=('jost',15))
downloadBtn.grid(row=6,pady=10)
 
downloadlabel=Label(root,text="",bg="red",
font=('jost',13))
downloadlabel.grid(row=7,pady=10)

#Main
root.mainloop()
