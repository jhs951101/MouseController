from pynput.mouse import Listener;

def on_click(x, y, button, pressed):
    print(int(x), int(y));

with Listener(on_click=on_click) as listener:
    listener.join();
