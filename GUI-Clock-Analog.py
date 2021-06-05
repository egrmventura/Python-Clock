import tkinter as ui
import time
import datetime as dt
import math
window = ui.Tk()
wsd = 600 #wsd = window square dimension. Used as variable to adjust all corresponding dimensions
center_dim = wsd//2
window.geometry(str(wsd) + "x" + str(wsd))

def update_clock():
    hours = int(time.strftime("%I"))
    minutes = int(time.strftime("%M"))
    seconds = dt.datetime.now().second + (dt.datetime.now().microsecond * 10**(-6))
    secx = second_hand_length * math.sin(math.radians(seconds*6))
    secy = second_hand_length * math.cos(math.radians(seconds*6))
    minx = minute_hand_length * math.sin(math.radians(minutes*6))
    miny = minute_hand_length * math.cos(math.radians(minutes*6))
    hrx = hour_hand_length * math.sin(math.radians(hours*30))
    hry = hour_hand_length * math.cos(math.radians((hours*30) + (minutes/2)))
    canvas.coords(second_hand, center_dim, center_dim, center_dim + secx, center_dim - secy)
    canvas.coords(minute_hand, center_dim, center_dim, center_dim + minx, center_dim - miny)
    canvas.coords(hour_hand, center_dim, center_dim, center_dim + hrx, center_dim - hry)
    canvas.after(20,update_clock) #set at 50fps for smooth second hand
   
# create background
canvas = ui.Canvas(window, width=wsd, height=wsd, bg="grey")
canvas.pack(expand=True, fill='both')
backing = ui.PhotoImage(file='clock-face2.png')
canvas.create_image(center_dim, center_dim, image = backing)

# create hands of clock
second_hand_length = round(0.65 * center_dim)
minute_hand_length = round(0.65 * center_dim)
hour_hand_length = round(0.5 * center_dim)
second_hand = canvas.create_line(center_dim, center_dim, center_dim + second_hand_length, center_dim + second_hand_length, width=1.5, fill="red")
minute_hand = canvas.create_line(center_dim, center_dim, center_dim + minute_hand_length, center_dim - minute_hand_length, width=5, fill="black")
hour_hand = canvas.create_line(center_dim, center_dim, center_dim + hour_hand_length, center_dim + hour_hand_length, width=5, fill="black")

#start clock
update_clock()
window.mainloop()