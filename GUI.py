from tkinter import *
from tkinter import filedialog
import cv2
from Stenography import *
from MergingImages import *

def fileselect():
    file1 = filedialog.askopenfile()
    input_image_path = file1.name.replace('/', '\\')
    return input_image_path


def filesave():
    files = [('All Files', '*.*'),
             ('PNG Files', '*.png')]
    file1 = filedialog.asksaveasfile(filetypes=files, defaultextension=files)
    image = file1.name.replace('/', '\\')
    return image

def select_number():
    print(clicked.get())
    return clicked.get()

def select_number1():
    print(clicked1.get())
    return clicked1.get()

def encode():
    file1 = filedialog.askopenfile()
    input_image_path = file1.name.replace('/', '\\')
    image1=cv2.imread(input_image_path)
    if image1 is None:
        raise FileNotFoundError()
    display_image(image1, 'Resized Input Image')
    data = textbox.get('1.0',END).strip()
    if len(data) == 0:
        raise ValueError('Data is empty')
    encoded_image = hide_data(image1, data)
    output_image_path=filesave()
    cv2.imwrite(output_image_path, encoded_image)
    Label(Frame1,text='File Saved').pack()


def decode():
    input_image_path = fileselect()
    image = cv2.imread(input_image_path)  # Read the input image using OpenCV-Python.

    display_image(image, 'Resized Image with Hidden text')

    text = unhide_data(image)
    message='Decoded message is ' + text
    Label(Frame3,text=message).pack()


def Merge():
    pub_image_path=fileselect()
    secret_image_path=fileselect()
    nf_bits=select_number()
    pub_image = cv2.imread(pub_image_path)
    secret_image = cv2.imread(secret_image_path)
    result = merge_images(pub_image, secret_image, nf_bits)
    output_image_path = filesave()
    cv2.imwrite(output_image_path, result)
    display_image(result, "Merged and Saved")


def Unmerge():
    input_image_path = fileselect()
    result=cv2.imread(input_image_path)
    nf_bits = select_number1()
    hidden = unmerge_image(result, nf_bits)
    display_image(hidden, "Reveal")
def raise_frame(frame):
    frame.tkraise()


def get_text():
    text=textbox.get('1.0',END).strip()
    print(text)

window = Tk()
window.title('Steganography')
window.geometry("1000x1000")
Home = Frame(window)
Frame1 = Frame(window)
Frame2 = Frame(window)
Frame3= Frame(window)
Frame4= Frame(window)

for frame in (Home,Frame1, Frame2,Frame3, Frame4):
    frame.grid(row=0,column=0,sticky='news')

#Home Frame
Label(Home,text='Steganography Program').pack()
button1=Button(Home,text='Hide Text', padx=30,pady=20, command=lambda:raise_frame(Frame1))
button1.pack()
button13=Button(Home, text='Unhide Text',padx=30,pady=20,command=lambda:raise_frame(Frame3))
button13.pack()
button2=Button(Home,text='Hide Image', padx=30,pady=20, command=lambda:raise_frame(Frame2))
button2.pack()
button14=Button(Home, text='Unhide Image',padx=30,pady=20,command=lambda:raise_frame(Frame4))
button14.pack()
button3=Button(Home,text='Exit', padx=30,pady=20,command=window.quit)
button3.pack()


#Frame1 for Hinding Text
Label(Frame1,text='Hiding Text').pack()
button4=Button(Frame1,text='Select Input Image Path', command=encode)
button4.pack()
Label(Frame1,text='Input the Data to be hidden first').pack()
textbox=Text(Frame1)
textbox.pack()
button5=Button(Frame1,padx=10,pady=10,text='Enter',command=get_text)
button5.pack()
button6=Button(Frame1,text='Go to Home', padx=30,pady=20, command=lambda:raise_frame(Home))
button6.pack()
button7=Button(Frame1,text='Exit', padx=30,pady=20,command=window.quit)
button7.pack()


#Frame2 for Hiding Image
clicked=IntVar()
clicked1=IntVar()
Label(Frame2,text='Hiding Image').pack()
Label(Frame2,text='Number of bits to use for Hiding').pack()
drop = OptionMenu(Frame2,clicked,'1','2','3','4','5','6','7')
drop.pack()
button15=Button(Frame2,padx=10,pady=10,text='Hide',command=Merge)
button15.pack()
button8=Button(Frame2,text='Go to Home',  padx=30,pady=20,command=lambda:raise_frame(Home))
button8.pack()
button9=Button(Frame2,text='Exit', padx=30,pady=20,command=window.quit)
button9.pack()


#Frame3 for Retrieving Text
Label(Frame3,text='Retrieving Text').pack()
Label(Frame3,text='Select Image Path').pack()
button11=Button(Frame3,padx=10,pady=10,text='Enter',command=decode)
button11.pack()
button12=Button(Frame3,text='Go to Home', padx=30,pady=20, command=lambda:raise_frame(Home))
button12.pack()
button13=Button(Frame3,text='Exit', padx=30,pady=20,command=window.quit)
button13.pack()

#Frame4 for Retrieving Image
Label(Frame4,text='Retrieving Image').pack()
Label(Frame4,text='Select Image Path').pack()
Label(Frame4,text='Number of bits that were use for Hiding').pack()
drop1 = OptionMenu(Frame4,clicked1,'1','2','3','4','5','6','7')
drop1.pack()
button18=Button(Frame4,padx=10,pady=10,text='Unhide',command=Unmerge)
button18.pack()
button16=Button(Frame4,text='Go to Home', padx=30,pady=20, command=lambda:raise_frame(Home))
button16.pack()
button17=Button(Frame4,text='Exit', padx=30,pady=20,command=window.quit)
button17.pack()

raise_frame(Home)
window.mainloop()