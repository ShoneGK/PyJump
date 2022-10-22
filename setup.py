import multiprocessing
from flask import Flask, render_template, request, redirect
from flask.wrappers import Request
import webview
import threading
import tkinter as tk
from multiprocessing import Process
from tkinter import filedialog
import sys
import os
import time
install_dir = ''
req = False

def dir_thread():
    global req
    global install_dir
    root = tk.Tk()
    root.withdraw()
    while True:
        while not req:
            pass
        install_dir = filedialog.askdirectory()
        if install_dir == ():
            install_dir = ''
        print(install_dir)
        req = False
        
        

def backend_thread(window, main_pid):
    req = False
    threading.Thread(target=app.run, kwargs=dict(host='0.0.0.0', port=34620)).start()
    threading.Thread(target=dir_thread).start()

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/phase2')
def phase2():
    return render_template('phase2.html')

@app.route('/phase3')
def phase3():
    return render_template('phase3.html')

@app.route('/install')
def install():
    time.sleep(3)
    print('done')
    return 'OK'

@app.route('/close')
def close():
    global main_pid
    os.system('sudo kill ' + str(main_pid))
    os.system('sudo kill ' + str(os.getpid()))

@app.route('/get_install_directory/')
def get_install_directory():
    print('?')
    global req
    req = True
    print(req)
    while req:
        pass

    global install_dir
    return install_dir
global window
os.system('sudo echo ')
window = webview.create_window('Jumpster Setup', 'http://localhost:34620/')
main_pid = os.getpid()
backend_proccess = Process(target=backend_thread, args=[window, main_pid])
backend_proccess.start()
time.sleep(1)
webview.start()