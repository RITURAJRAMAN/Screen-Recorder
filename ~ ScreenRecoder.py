from tkinter import *
import cv2
import numpy as np
import pyautogui

window = Tk()
window.title("Future Keys")
window.geometry('500x400')
window.configure(bg='black')
Label(window, text="Screen Recorder", font="algerian 22 bold", bg='OrangeRed1').place(x=70, y=20)


def download():
    size = (1920, 1080)
    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    video = cv2.VideoWriter("output.avi", fourcc, 20.0, size)
    while True:
        screen = pyautogui.screenshot()
        frame = np.array(screen)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        video.write(frame)


Button(window, text='Start Recording', font='arial 12 bold', width='15', bg='lightgreen', command=download).place(x=160,
                                                                                                                 y=150)
Button(window, text='Quit', font='arial 12 bold', width='15', bg='red', command=window.destroy).place(x=160, y=250)
window.mainloop()
