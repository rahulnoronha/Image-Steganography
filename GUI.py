from Stenography import *
from MergingImages import *
from tkinter import *

window=Tk()
window.title('Steganography')

btn1=Button(window,text='Hide Text',command=encode_text).pack()
btn2=Button(window,text='Unhide Text',command=decode_text).pack()
btn3=Button(window,text='Unhide Image',command=IHmain).pack()

window.mainloop()
