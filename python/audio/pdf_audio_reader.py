from tkinter import *
from tkinter import filedialog
import PyPDF2
import pyttsx3

def extract_text():
    file = filedialog.askopenfile(parent=root, mode='rb', title='Choose a PDF File')
    if file != None:
        pdfReader = PyPDF2.PdfReader(file)
        #pdfReader = PyPDF2.PdfFileReader(file)
        global text_extracted
        text_extracted = ""
        for pageNum in range(len(pdfReader.pages)):
        #for pageNum in range(pdfReader.numPages):
            pageObject = pdfReader.pages[pageNum]
            #pageObject = pdfReader.getPage(pageNum)
            text_extracted += pageObject.extract_text()
            #text_extracted += pageObject.extractText()
        file.close()

def speak_text():                                                                                                   
    global rate
    global male
    global female
                                                                                                            
    rate = int(rate.get())
    engine.setProperty('rate', rate)
    male = int(male.get())
    female = int(female.get())
    all_voices = engine.getProperty('voices')
    maleVoice = all_voices[0].id
    femaleVoice = all_voices[1].id
                                                                                                                            if(male == 0 and female == 0) or (male == 1 and female == 1): 
        engine.setProperty('voice', maleVoice) # default
    elif male == 0 and female == 1:
        engine.setProperty('voice', femaleVoice)
    else:
        engine.setProperty('voice', maleVoice)

    eigine.say(text_extracted)
    engine.runAndWait()

def stop_speaking():
    engine.stop()

def Application(self):
    root.geometry('{}x{}'.format(700,600))
    root.resizable(width=False, height=False)
    root.title("PDF to AUDIO")
    root.configure(background = 'light gray')
    global rate, male, female
    # frame1
    frame1 = Frame(root,width=500,height=200, bg='indigo')
    # frame2
    frame2 = Frame(root, width=500, height=450, bg = 'light gray')
    frame1.pack(side='top', fill='both')
    frame2.pack(side='top', fill = 'y')

    # frame1 Widgets
    # https://edukoi.tistory.com/108
    name1 = Label(frame1, text='PDF to AUDIO', fg = 'black', bg='blue',
                    font = 'Arial 28 bold')
    name1.pack()

    name2 = Label(frame1, text = "Hear your PDF file", fg='red', bg='indigo',
        font = 'Calibre 25 bold')
    name2.pack()

    # frame2 Widgets
    btn = Button(frame2, text = 'Select PDF file', activeforeground='red',
        command=extract_text(), padx='70', pady='10', fg = 'white', bg='black',
        font = 'Arial 12')

    btn.grid(row=0, pady=20, columnspan=2)

    rate_text = Label(frame2, text = "Enter Rate of Speech", fg='black', bg='aqua',
        font = 'Arial 12')
    rate_text.grid(row=1, column=0, pady= 15, padx=0, sticky=W)
    rate = Entry(frame2, text='200', fg='black', bg='white', font='Arial 12')
    rate.grid(row=1,column=1,padx=30,pady=15, sticky=W)

    voice_text = Label(frame2, text="Select Voice:", fg='black', bg='aqua',
                    font="Arial 12")
    voice_text.grid(row=2, column=0, pady = 15, padx = 0, sticky=E)

    male = IntVar()
    maleOpt = Checkbutton(frame2, text='Male', bg='pink',
            variable=male, onvalue=1, offvalue=0) # onvalue,offvalue will be used in checkbox
    maleOpt.grid(row=2,column=1,pady=0,padx=30,sticky=W) # sticky means order

    female = IntVar()
    femaleOpt = Checkbutton(frame2, text='Female', bg='pink',
            variable=female, onvalue=1, offvalue=0)
    femaleOpt.grid(row=3,column=1,pady=0,padx=30, sticky=W)

    submitBtn = Button(frame2, text='Play PDF File', command=speak_text,
            activeforeground='red', padx='60', pady='10',
            fg='white', bg='black', font='Arial 12')
    submitBtn.grid(row=4, column=0, pady=65)

    stopBtn = Button(frame2, text='Stop Playing', command=stop_speaking,
            activeforeground='red', padx='60', pady='10', fg='white',
            bg='black', font='Arial 12')
    stopBtn.grid(row=4, column=1, pady=65)

if __name__ == '__main__':
     mytest, rate, male, female = "", 100, 0, 0
     engine = pyttsx3.init()
     root = Tk()
     Application(root)
     root.mainloop()


