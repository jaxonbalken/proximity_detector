import tkinter as tk
import serial
import threading

SERIAL_PORT = 'COM4'  # Change to match your Arduino port
BAUD_RATE = 9600

class ProximityGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Arduino Proximity Sensor")
        self.label = tk.Label(master, text="Waiting for data...", font=("Arial", 24))
        self.label.pack(pady=40, padx=40)

        self.serial_conn = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
        self.running = True
        self.thread = threading.Thread(target=self.read_serial)
        self.thread.start()

    def read_serial(self):
        while self.running:
            try:
                line = self.serial_conn.readline().decode('utf-8').strip()
                if "NEAR" in line:
                    self.label.config(text="🔴 Object Detected!", bg='red', fg='white')
                elif "FAR" in line:
                    self.label.config(text="🟢 No Object Nearby", bg='green', fg='black')
            except Exception as e:
                print("Error:", e)

    def close(self):
        self.running = False
        self.serial_conn.close()
        self.master.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    gui = ProximityGUI(root)
    root.protocol("WM_DELETE_WINDOW", gui.close)
    root.mainloop()
