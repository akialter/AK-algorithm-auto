import tkinter as tk
import threading
from auto import auto  # Import your 'auto' function here

# Set default variable values here
duration = 1
wait_time = 7
load_game = 12
repeat = 20

# Create a tkinter window
window = tk.Tk()
window.title("AK Algorithm")
window.resizable(False, False)

# Create a label to display the status
status_label = tk.Label(window, text="Stopped...")
status_label.grid(row=5, columnspan=2, pady=10)

# Create tkinter DoubleVars to store the numeric variable values
duration_var = tk.DoubleVar()
wait_time_var = tk.DoubleVar()
load_game_var = tk.DoubleVar()
repeat_var = tk.IntVar()

duration_var.set(duration)
wait_time_var.set(wait_time)
load_game_var.set(load_game)
repeat_var.set(repeat)

def validate_input(new_value):
    try:
        float(new_value)
        return True
    except ValueError:
        return False

# Create labels and input boxes for the variables using the grid layout
tk.Label(window, text='Thoi gian click chuot').grid(row=0, column=0, padx=10, pady=5)
duration_entry = tk.Entry(window, validate="key", validatecommand=(validate_input, "%P"), textvariable=duration_var)
duration_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(window, text='Thoi gian doi chuyen screen').grid(row=1, column=0, padx=10, pady=5)
wait_time_entry = tk.Entry(window, validate="key", validatecommand=(validate_input, "%P"), textvariable=wait_time_var)
wait_time_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(window, text='Thoi gian doi load game').grid(row=2, column=0, padx=10, pady=5)
load_game_entry = tk.Entry(window, validate="key", validatecommand=(validate_input, "%P"), textvariable=load_game_var)
load_game_entry.grid(row=2, column=1, padx=10, pady=5)

tk.Label(window, text='Lap lai bao nhieu lan').grid(row=3, column=0, padx=10, pady=5)
load_game_entry = tk.Entry(window, validate="key", validatecommand=(validate_input, "%P"), textvariable=repeat_var)
load_game_entry.grid(row=3, column=1, padx=10, pady=5)

# Create a threading.Event to signal the thread to stop
stop_event = threading.Event()

def on_closing():
    # Set the stop_event to signal the thread to stop
    stop_event.set()
    # Close the GUI window
    window.destroy()

def run():
    # Update variables
    duration = duration_var.get()
    wait_time = wait_time_var.get()
    load_game = load_game_var.get()
    repeat = repeat_var.get()
    
    status_label.config(text="Running!")
    
    # Function to run 'auto' in a separate thread
    def run_auto():
        for i in range(repeat):
            auto(duration, wait_time, load_game)
        status_label.config(text="Stopped...")
        
        # Bring the GUI window to the front
        window.attributes('-topmost', 1)
        window.attributes('-topmost', 0)
    
    # Create and start a separate thread to run 'auto'
    auto_thread = threading.Thread(target=run_auto)
    auto_thread.start()
    
    # Bind a function to run when the GUI window is closed
    window.protocol("WM_DELETE_WINDOW", on_closing)

# Create a button to update the variables
tk.Button(window, text="Run", command=run).grid(row=4, columnspan=2, pady=10)

if __name__ == "__main__":
    # Start the tkinter main loop
    window.mainloop()
