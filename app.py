from tkinter import *
from tkinter import filedialog
import multiprocessing
from playsound import playsound



class Music:
    def __init__(self,root):
        self.root=root
        self.root.title("Music Player")
        self.root.iconbitmap("logo275.ico")
        self.root.geometry("400x250")
        self.root.resizable(0,0)


        p,file_path=None



        def on_enter1(e):
            but_browser['background']="black"
            but_browser['foreground']="cyan"
            
            

        def on_leave1(e):
            but_browser['background']="SystemButtonFace"
            but_browser['foreground']="SystemButtonText"


        def on_enter2(e):
            but_play['background']="black"
            but_play['foreground']="cyan"
            
            

        def on_leave2(e):
            but_play['background']="SystemButtonFace"
            but_play['foreground']="SystemButtonText"


        def on_enter3(e):
            but_stop['background']="black"
            but_stop['foreground']="cyan"
            
            

        def on_leave3(e):
            but_stop['background']="SystemButtonFace"
            but_stop['foreground']="SystemButtonText"





        def browse():
            file_path= filedialog.askopenfilename(title = "Select file",filetypes = (("mp3","*.mp3"),("all files","*.*")))
            lab_music.config(text=file_path)
            


        def play():
            
            p = multiprocessing.Process(target=playsound, args=("{}".format(file_path),))
            p.start()
            

        def stop():
            
           
            p.terminate()
           



#======================Frame=====================================#
        
        mainframe=Frame(self.root,width=400,height=250,relief="ridge",bd=3,bg="gray88")
        mainframe.place(x=0,y=0)


#======================button===================================#
        
        but_browser=Button(mainframe,text="Browser",font=('times new roman',14),width=17,cursor="hand2",command=browse)
        but_browser.place(x=100,y=10)
        but_browser.bind("<Enter>",on_enter1)
        but_browser.bind("<Leave>",on_leave1)


        lab_music=Label(mainframe,font=('times new roman',8),bg="gray88",fg="white")
        lab_music.place(x=10,y=80)

        but_play=Button(mainframe,text="Play",font=('times new roman',14),width=13,cursor="hand2",command=play)
        but_play.place(x=40,y=140)
        but_play.bind("<Enter>",on_enter2)
        but_play.bind("<Leave>",on_leave2)

        but_stop=Button(mainframe,text="Stop",font=('times new roman',14),width=13,cursor="hand2",command=stop)
        but_stop.place(x=210,y=140)
        but_stop.bind("<Enter>",on_enter3)
        but_stop.bind("<Leave>",on_leave3)







if __name__ == "__main__":
    root=Tk()
    Music(root)
    root.mainloop()