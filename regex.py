from tkinter import *
import re
from tkinter.messagebox import showerror


class Window:

    def settings(self):
        self.root.title('Regex')
        self.root.resizable(False,False)
        self.root.config(bg=self.bg)


    def compile(self,event=None):
        self.text_result.configure(state='normal')
        self.text_result.delete(1.0,END)
        try:
            flags = 0
            if self.var_mul.get():
                flags |= re.M
            if self.var_ignore.get():
                flags |= re.I
            
            self.pattern = re.compile(rf'{self.regex_input.get()}',flags)
            text = self.text.get(1.0,END)
            if text:
                matches = self.pattern.finditer(text)
                for match in matches:
                    result = text[match.start():match.end()] 
                    self.text_result.insert(END,f'<{result}>' + '\n')
                self.text_result.configure(state='disabled')
        except re.error as err:
            showerror('Error',err)
            
    def display_label(self):
        self.title = Label(
            self.root,
            text='insert your regular expression here.',
            bg=self.bg,
            font=('Dubai',15)
        )
        self.title_text = Label(
            self.root,
            text='Your text for matching.',
            bg=self.bg,
            font=('Dubai',15)
        )
        self.title_result = Label(
            self.root,
            text='Matches',
            bg=self.bg,
            font=('Dubai',15)
        )
        self.title_name = Label(
            self.root,
            text='Regular Expressions',
            bg=self.bg,
            font=('Dubai',30)
        )

    def display_inputs(self):
        self.regex_input = Entry(
            self.root,
            width=40,
            bg=self.bg_text,
            border=5,
            font=('Arial',15),
        )

    def display_btn(self):
        self.btn_compile = Button(
            self.root,
            text='Compile',
            bg=self.bg_btn,
            font=('Dubai',15),
            border=4,
            command=self.compile
        )

    def display_text(self):
        self.text = Text(
            self.root,
            width=40,
            height=12,
            border=4,
            bg=self.bg_text,
            font=('Arial',15)
        )
        self.text_result = Text(
            self.root,
            width=40,
            height=12,
            border=4,
            bg=self.bg_text,
            font=('Arial',15)
        )
        self.text_result.configure(state='disabled')
        

    def display_radio_btns(self):
        self.var_ignore = BooleanVar(self.root,False)
        self.var_mul = BooleanVar(self.root,False)
        self.radio_ignore = Checkbutton(
            self.root,
            text='IgnoreCase',
            bg=self.bg,
            variable=self.var_ignore,
            width=10,
            font=('Dubai',12,'bold'),
        )
        
        self.radio_mul = Checkbutton(
            self.root,
            text='MultiLine',
            bg=self.bg,
            variable=self.var_mul,
            width=10,
            font=('Dubai',12,'bold'),
        )


        
    def put_items(self):
        self.title.grid(row=0,column=0,sticky='W',padx=5,pady=5)
        self.regex_input.grid(row=1,column=0,padx=5,pady=5)
        self.title_text.grid(row=2,column=0,sticky='W',padx=5,pady=5)
        self.text.grid(row=3,column=0,padx=5,pady=5)
        self.text_result.grid(row=0,column=1,rowspan=4,sticky='S',padx=5,pady=5)
        self.title_result.grid(row=0,column=1,rowspan=3,sticky='S',padx=5,pady=5)
        self.title_name.grid(row=0,column=1,rowspan=2,sticky='S',padx=5,pady=5)
        self.btn_compile.grid(row=4,column=0,sticky='W',padx=5,pady=5)
        self.radio_mul.grid(row=4,column=0,columnspan=1,sticky='S')
        self.radio_ignore.grid(row=4,column=0,columnspan=1,sticky='N')


        
    def __init__(self):
        self.bg = '#6495ED'
        self.bg_text = 'white'
        self.bg_btn = 'white'
        self.root = Tk()
        self.settings()
        self.display_label()
        self.display_inputs()
        self.display_text()
        self.display_btn()
        self.display_radio_btns()
        self.put_items()
    


    def __call__(self):
        self.root.mainloop()



window = Window()
window()
