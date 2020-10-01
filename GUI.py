from tkinter import *
from tkinter import filedialog
import cv2
from Stenography import *
from MergingImages import *


global Frame1, Frame2, Frame3, Frame4, Home, frame
global button1, button2, button3, button4, button5, button6, button7, button8, button9
global button10, button11, button12, button13, button14, button15, button16, button17, button18
global text1, text2, text3, text4, text5, clicked, clicked1, drop, drop1, message, message1, label1, label2
message = ''
message1 = ''
window = Tk()
window.title('Steganography')
window.geometry("1000x1000")
window.configure(bg='light blue')

Home = Frame(window)
Frame1 = Frame(window)
Frame2 = Frame(window)
Frame3 = Frame(window)
Frame4 = Frame(window)
Home.configure(bg='light blue')
Frame1.configure(bg='light blue')
Frame2.configure(bg='light blue')
Frame3.configure(bg='light blue')
Frame4.configure(bg='light blue')


def home():
    ''' Home Frame '''
    global Home, Frame1, Frame2, Frame3, Frame4, text1, button1, button2, button3, button4, button5
    Label(Home, text='', bg='light blue').grid(row=0, column=1500)
    text1 = Text(Home, height=2, width=80, bg='blue', bd=5, state=DISABLED)
    text1.grid(row=200, column=1500)
    Label(Home, text='STEGANOGRAPHY PROGRAM', bg='blue', fg='white').grid(row=200, column=1500)
    button1 = Button(Home, text='Hide Texts', bd=5, padx=30, pady=20, command=lambda: raise_frame(Frame1))
    button1.grid(row=400, column=500)
    button2 = Button(Home, text='Unhide Texts', bd=5, padx=30, pady=20, command=lambda: raise_frame(Frame3))
    button2.grid(row=400, column=5000)
    button3 = Button(Home, text='Hide Image', bd=5, padx=30, pady=20, command=lambda: raise_frame(Frame2))
    button3.grid(row=1600, column=500)
    button4 = Button(Home, text='Unhide Image', bd=5, padx=30, pady=20, command=lambda: raise_frame(Frame4))
    button4.grid(row=1600, column=5000)
    button5 = Button(Home, text='Exit', bd=5, padx=30, pady=20, command=window.quit)
    button5.grid(row=2000, column=1500)


def frame1():
    # Frame1 for Hiding Text
    global Frame1, Home
    global text2, button6, button7, button8, button9, clicked, message1, label1
    clicked = IntVar()
    Label(Frame1, text='HIDE TEXT').grid(row=0, column=1500)
    Label(Frame1, text='Hiding Text').grid(row=200, column=1500)
    text2 = Text(Frame1, height=2, width=80, bd=5)
    text2.grid(row=800, column=1500)
    button6 = Button(Frame1, bd=5, text='Select Input Image Path', command=encode)
    button6.grid(row=1600, column=1500)
    Label(Frame1, text='Input the Data to be hidden first').grid(row=400, column=1500)
    button7 = Button(Frame1, bd=5, padx=10, pady=10, text='Enter', command=lambda: get_text)
    button7.grid(row=1200, column=1500)
    label1 = Button(Frame1, text=message1, padx=100, pady=100, state=DISABLED).grid(row=1300, column=1500)
    button8 = Button(Frame1, bd=5, text='Go to Home', padx=30, pady=20, command=lambda: raise_frame(Home))
    button8.grid(row=5000, column=400)
    button9 = Button(Frame1, bd=5, text='Clear', padx=30, pady=20, command=lambda: clear_frame(Frame1))
    button9.grid(row=5000, column=5000)


def frame2():
    """ Frame2 for Hiding Image """
    global Home, Frame2, clicked, text3, drop, button10, button11, button12
    Label(Frame2, text='', bg='light blue').grid(row=0, column=1500)
    text3 = Text(Frame2, height=2, width=80, bg='red', bd=5, state=DISABLED).grid(row=200, column=1500)
    Label(Frame2, text='HIDE IMAGE', fg='black', bg='red').grid(row=200, column=1500)
    Label(Frame2, text='Hiding Image').grid(row=400, column=1500)
    Label(Frame2, text='Number of bits to use for Hiding').grid(row=800, column=1500)
    drop = OptionMenu(Frame2, clicked, '1', '2', '3', '4', '5', '6', '7')
    drop.grid(row=1000, column=1500)
    button10 = Button(Frame2, bd=5, padx=10, pady=10, text='Hide', command=merge)
    button10.grid(row=1400, column=1500)
    button11 = Button(Frame2, bd=5, text='Go to Home', padx=30, pady=20, command=lambda: raise_frame(Home))
    button11.grid(row=2000, column=400)
    button12 = Button(Frame2, bd=5, text='Clear', padx=30, pady=20, command=lambda: clear_frame(Frame2))
    button12.grid(row=2000, column=5000)


def frame3():
    """ Frame3 for Retrieving Text """
    global Home, text3, Frame3, button13, button14, button15, message, label2
    Label(Frame3, text='', bg='light blue').grid(row=0, column=1500)
    text3 = Text(Frame3, height=2, width=80, bd=5, bg='green', state=DISABLED).grid(row=200, column=1500)
    Label(Frame3, text='RETRIEVE TEXT', bg='green', fg='black').grid(row=200, column=1500)
    Label(Frame3, text='Retrieving Text').grid(row=600, column=1500)
    Label(Frame3, text='Select Image Path').grid(row=400, column=1500)
    button13 = Button(Frame3, bd=5, padx=10, pady=10, text='Enter', command=decode)
    button13.grid(row=500, column=1500)
    label2 = Button(Frame3, text=message, padx=300, pady=100, state=DISABLED).grid(row=800, column=1500)
    button14 = Button(Frame3, bd=5, text='Go to Home', padx=30, pady=20, command=lambda: raise_frame(Home))
    button14.grid(row=1000, column=200)
    button15 = Button(Frame3, bd=5, text='Clear', padx=30, pady=20, command=lambda: clear_frame(Frame3))
    button15.grid(row=1000, column=5000)


def frame4():
    """ Frame4 for Retrieving Image """
    global Home, clicked1, Frame4, text4, drop1, button16, button17, button18
    clicked1 = IntVar()
    Label(Frame4, text='', bg='light blue').grid(row=0, column=2500)
    text4 = Text(Frame4, height=2, width=80, bd=5, bg='green').grid(row=200, column=2500)
    Label(Frame4, text='RETRIEVE IMAGE', fg='black', bg='green').grid(row=200, column=2500)
    Label(Frame4, text='Select Image Path').grid(row=400, column=2500)
    Label(Frame4, text='Retrieving Image').grid(row=600, column=2500)
    Label(Frame4, text='Number of bits that were use for Hiding').grid(row=800, column=2500)
    drop1 = OptionMenu(Frame4, clicked1, '1', '2', '3', '4', '5', '6', '7')
    drop1.grid(row=1000, column=2500)
    button16 = Button(Frame4, bd=5, padx=10, pady=10, text='Unhide', command=unmerge)
    button16.grid(row=1400, column=2500)
    button17 = Button(Frame4, bd=5, text='Go to Home', padx=30, pady=20, command=lambda: raise_frame(Home))
    button17.grid(row=2000, column=200)
    button18 = Button(Frame4, bd=5, text='Clear', padx=30, pady=20, command=lambda:clear_frame(Frame4))
    button18.grid(row=2000, column=5000)



def clear_frame(frame):
    global message, message1, Frame1, Frame3
    name = frame
    frame.grid_forget()
    message = ''
    message1 = ''
    """ Function to clear the frame """
    raise_frame(name)


def reset_frame(frame):
    global message, message1
    frame.grid_forget()
    name = str(frame)
    """ Function to clear the frame """
    raise_frame(frame)


def raise_frame(frame):
    global Home, Frame1, Frame2, Frame3, Frame4
    for fram in (Home, Frame1, Frame2, Frame3, Frame4):
        fram.grid(row=0, column=0, sticky='news')
    home()
    frame1()
    frame2()
    frame3()
    frame4()
    frame.tkraise()


def file_select():
    file1 = filedialog.askopenfile()
    input_image_path = file1.name.replace('/', '\\')
    return input_image_path


def file_save():
    files = [('All Files', '*.*'),
             ('PNG Files', '*.png')]
    file1 = filedialog.asksaveasfile(filetypes=files, defaultextension=files)
    image = file1.name.replace('/', '\\')
    return image


def select_number():
    return clicked.get()


def select_number1():
    return clicked1.get()


def get_text():
    global text2
    text = text2.get('1.0',END).strip()
    return text


def encode():
    global message1
    file1 = filedialog.askopenfile()
    input_image_path = file1.name.replace('/', '\\')
    image1=cv2.imread(input_image_path)
    if image1 is None:
        raise FileNotFoundError()
    display_image(image1, 'Resized Input Image')
    data = get_text()
    if len(data) == 0:
        raise ValueError('Data is empty')
    encoded_image = hide_data(image1, data)
    output_image_path=file_save()
    cv2.imwrite(output_image_path, encoded_image)
    message1 = 'File Saved'
    clear_frame(Frame1)
    reset_frame(Frame1)
    message1=''



def decode():
    global message
    input_image_path = file_select()
    image = cv2.imread(input_image_path)  # Read the input image using OpenCV-Python.

    display_image(image, 'Resized Image with Hidden text')

    text = unhide_data(image)
    message='Decoded message is ' + text
    reset_frame(Frame3)
    message=''




def merge():
    pub_image_path = file_select()
    secret_image_path = file_select()
    nf_bits = select_number()
    pub_image = cv2.imread(pub_image_path)
    secret_image = cv2.imread(secret_image_path)
    result = merge_images(pub_image, secret_image, nf_bits)
    output_image_path = file_save()
    cv2.imwrite(output_image_path, result)
    display_image(result, "Merged and Saved")


def unmerge():
    """ Un-merge Hidden image """
    input_image_path = file_select()
    result=cv2.imread(input_image_path)
    nf_bits = select_number1()
    hidden = unmerge_image(result, nf_bits)
    display_image(hidden, "Reveal")


for fram in (Home, Frame1, Frame2, Frame3, Frame4):
    fram.grid(row=0,column=0,sticky='news')


home()
frame1()
frame2()
frame3()
frame4()

raise_frame(Home)
window.mainloop()

