from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk

class ChatBot:
    def __init__(self, root):
        self.root = root
        self.root.title("ChatBot")
        self.root.geometry("730x620+0+0")
        self.root.bind('<Return>',self.enter_func) 


        main_frame=Frame(self.root,bd=4,bg='powder blue',width=610)
        main_frame.pack()

        img_chat=Image.open('hlp1.jpg')
        img_chat=img_chat.resize((200,70),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img_chat)

        Title_label=Label(main_frame,bd=3,relief=RAISED,anchor='nw',width=730,compound=LEFT,image=self.photoimg,text='   -: CHAT ME :-',font=('areal',30,'bold'),fg='steelblue4',bg='white')
        Title_label.pack(side=TOP)

        self.scroll_y=ttk.Scrollbar(main_frame,orient=VERTICAL)
        self.text=Text(main_frame,width=65,height=20,bd=3,relief=RAISED,font=('arial',14),yscrollcommand=self.scroll_y.set)
        self.scroll_y.pack(side=RIGHT,fill=Y)
        self.text.pack()


        btn_frame=Frame(self.root,bd=4,bg='white',width=730)
        btn_frame.pack()

        label_1=Label(btn_frame,text="Type somthing",font=('areal',14,'bold'),fg='steel blue',bg='white')
        label_1.grid(row=0,column=0,padx=5,sticky=W)

        self.entry=StringVar()
        self.entry1=ttk.Entry(btn_frame,textvariable=self.entry,width=40,font=('times new roman',16,'bold'))
        self.entry1.grid(row=0,column=1,padx=5,sticky=W)

        self.send=Button(btn_frame,text="> send",command=self.send,font=('areal',15,'bold'),width=8,bg='DeepSkyBlue2')
        self.send.grid(row=0,column=2,padx=5,sticky=W)
        
        self.clear=Button(btn_frame,text="Clear Data",command=self.clear,font=('areal',15,'bold'),width=8,bg='brown4',fg='white')
        self.clear.grid(row=1,column=2,padx=5,sticky=W)

        self.msg=''
        self.label_2=Label(btn_frame,text=self.msg,font=('areal',14,'bold'),fg='Red',bg='white')
        self.label_2.grid(row=1,column=1,padx=5,sticky=W)


    def enter_func(self,event):
        self.send.invoke()
        self.entry.set('')

    def clear(self):
        self.text.delete('1.0',END)
        self.entry.set('')


    def send(self):
        send='\t\t\t\t'+'You: '+self.entry.get()
        self.text.insert(END,'\n'+send)
        self.text.yview(END)

        if (self.entry.get()==''):
            self.msg='please enter some input'
            self.label_2.config(text=self.msg,fg='red')

        else:
            self.msg=''
            self.label_2.config(text=self.msg,fg='red')

        if (self.entry.get()=='hello'):
            self.text.insert(END,'\n\n'+'Bot: Hii')

        elif (self.entry.get()=='hii'):
            self.text.insert(END,'\n\n'+'Bot: Hello')

        elif (self.entry.get()=='hi'):
            self.text.insert(END,'\n\n'+'Bot: Hello')

        elif (self.entry.get()=='how are you'):
            self.text.insert(END,'\n\n'+'Bot: fine and you')

        elif (self.entry.get()=='fantastic'):
            self.text.insert(END,'\n\n'+'Bot: Nice To Here')

        elif (self.entry.get()=='i am Fine'):
            self.text.insert(END,'\n\n'+'Bot:  Nice To Here')

        elif (self.entry.get()=='fine'):
            self.text.insert(END,'\n\n'+'Bot:  Nice To Here')

        elif (self.entry.get()=='who create you'):
            self.text.insert(END,'\n\n'+'Bot: Soumya Ranjan Ghadei Created me by using python and machine Learning')

        elif (self.entry.get()=='what is python'):
            self.text.insert(END,'\n\n'+'Bot: Python is a high-level, interpreted, and general-purpose programming language. It was created by Guido van Rossum and released in 1991. Python is known for its simplicity and readability, and it can be used for various purposes such as web development, software development, data science, and machine learning.')

        elif (self.entry.get()=='what is machine learning'):
            self.text.insert(END,'\n\n'+'Bot: Machine learning (ML) is a subfield of artificial intelligence (AI) that focuses on building computer systems that learn from data and make decisions or predictions without explicitly being programmed')

        elif (self.entry.get()=='how the face recognition work'):
            self.text.insert(END,'\n\n'+'Bot: The face recognition system uses algorithms to detect and analyze facial features, comparing them to a database of known faces to identify individuals.')

        elif (self.entry.get()=='is there any risk to privacy with this system'):
            self.text.insert(END,'\n\n'+'Bot:  Privacy concerns should be addressed by implementing appropriate security measures, such as encryption of stored data and obtaining consent from individuals whose faces are being recognized.')

        elif (self.entry.get()=='How do I enroll students into the system'):
            self.text.insert(END,'\n\n'+'Bot:  You can enroll students by capturing images of their faces and associating them with their respective information, such as name and student ID, in the system database.')

        elif (self.entry.get()=='What if a student''s appearance changes over time'):
            self.text.insert(END,'\n\n'+'Bot: You may need to periodically update the images in the system to account for changes in appearance, such as hairstyles or facial hair.')

        elif (self.entry.get()=='can I integrate this system with other attendance tracking software'):
            self.text.insert(END,'\n\n'+'Bot: Yes, it''s possible to integrate the face recognition system with other software solutions for attendance tracking, such as student management systems or HR software.')

        elif (self.entry.get()=='what if multiple students have similar faces?'):
            self.text.insert(END,'\n\n'+'Bot: The system should be able to distinguish between individuals based on unique facial features, but in cases of similarity, additional verification methods may be necessary to ensure accuracy.')

        elif (self.entry.get()=='how secure is the data stored in the system'):
            self.text.insert(END,'\n\n'+'Bot: It''s essential to implement robust security measures, such as encryption and access controls, to protect the data stored in the system from unauthorized access or tampering.')

        elif (self.entry.get()=='bye'):
            self.text.insert(END,'\n\n'+'Bot: Thank''s for giving your valuable time')
            
        elif (self.entry.get()=='can you speak english'):
            self.text.insert(END,'\n\n'+'Bot: Yes i ccan speak englisg')

        elif (self.entry.get()=='can you speak Hindi'):
            self.text.insert(END,'\n\n'+'Bot: No i cannot speak hindi i am in the process of learning hindi')

        elif (self.entry.get()=='can you speak odia'):
            self.text.insert(END,'\n\n'+'Bot: No i cannot speak odia i am in the process of learning odia')

        elif (self.entry.get()=='what is your name'):
            self.text.insert(END,'\n\n'+'Bot:i am a chatbot')

        else:
            self.text.insert(END,'\n\n'+'Bot: Sorry i did not get it')




if __name__ == '__main__':
    root = Tk()
    obj = ChatBot(root)
    root.mainloop()
