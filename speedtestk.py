# Note: This script is AI generated. It is a simple script that tests the internet speed of the user's internet connection.
import tkinter as tk
from tkinter import messagebox
import speedtest

def test_speed():
    try:
        st = speedtest.Speedtest()
        st.get_best_server()
        download_speed = st.download() / 1_000_000  # Convert to Mbps
        upload_speed = st.upload() / 1_000_000      # Convert to Mbps

        result_label.config(
            text=f"Download Speed: {download_speed:.2f} Mbps\n"
                 f"Upload Speed: {upload_speed:.2f} Mbps"
        )
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

root = tk.Tk()
root.title("Internet Speed Test")
root.geometry("400x300")

test_button = tk.Button(root, text="Test Speed", command=test_speed)
test_button.pack(pady=20)

result_label = tk.Label(root, text="", font=("Helvetica", 14))
result_label.pack(pady=20)

root.mainloop()
