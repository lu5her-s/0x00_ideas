
from iqoptionapi.stable_api import IQ_Option
import logging
import time
import tkinter as tk
from tkinter import ttk

def start_stream():
    global goal, size, maxdict, iq_api
    print("start stream...")
    iq_api.start_candles_stream(goal.get(),size.get(),maxdict)

def stop_stream():
    global goal, size, iq_api
    print("stop candle")
    iq_api.stop_candles_stream(goal.get(),size.get())

def show_candle():
    global goal, size, iq_api
    print("print candles")
    cc=iq_api.get_realtime_candles(goal.get(),size.get())
    for k in cc:
        print(goal.get(),"size",k,cc[k])

def login():
    
    global iq_api, email, password
    print("login...")
    email_val = email.get()
    password_val = password.get()
    iq_api=IQ_Option(email_val, password_val)
    iq_api.connect()#connect to iqoption
    if iq_api.check_connect() == False:
        print("Error connecting to IQ Option")
    else:
        print("Login successful")
        balance = iq_api.get_balance()
        print("Balance:", balance)

root = tk.Tk()
root.title("IQ Option")
root.geometry("300x200")

# Create input fields
email_label = tk.Label(root, text="Email")
email_label.pack()
email = tk.Entry(root)
email.pack()

password_label = tk.Label(root, text="Password")
password_label.pack()
password = tk.Entry(root)
password.pack()

goal_label = tk.Label(root, text="Goal")
goal_label.pack()
goal = tk.Entry(root)
goal.pack()

size_label = tk.Label(root, text="Size")
size_label.pack()
size = ttk.Combobox(root, values=[1, 2, 3, 4, 5])
size.pack()

# Create buttons
login_button = tk.Button(root, text="Login", command=login)
login_button.pack()

start_stream_button = tk.Button(root, text="Start Stream", command=start_stream)
start_stream_button.pack()

stop_stream_button = tk.Button(root, text="Stop Stream", command=stop_stream)
stop_stream_button.pack()

print_candles_button = tk.Button(root, text="Print Candles", command=show_candle)
print_candles_button.pack()

root.mainloop()
