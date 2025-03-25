from CPX400DP    import CPX400DP
from CPX400DP       import GuiApp

import tkinter as tk
import threading
import time

# Define a function that performs the task you want to control
def run_task():
    global running
    running = True
    while running:
        print("Task is running...")
        time.sleep(1)

# Function to start the task
def start_task():
    global task_thread
    task_thread = threading.Thread(target=run_task)
    task_thread.start()

# Function to stop the task
def stop_task():
    global running
    running = False

# Create the main application window
root = tk.Tk()
root.title("Task Controller")

# Create Start button
start_button = tk.Button(root, text="Start", command=start_task)
start_button.pack(pady=10)

# Create Stop button
stop_button = tk.Button(root, text="Stop", command=stop_task)
stop_button.pack(pady=5)

# Run the GUI
root.mainloop()
