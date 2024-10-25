import customtkinter as ctk
from tkinter import messagebox
import threading  
import time       

class VoiceSenseApp:
    def __init__(self, master):
        master.title("VoiceSense")
        master.geometry("700x350")  # Smaller, rectangular window
        ctk.set_appearance_mode("light") 
        ctk.set_default_color_theme("blue")

        # Main frame divided into three vertical sections
        self.main_frame = ctk.CTkFrame(master, corner_radius=15)
        self.main_frame.pack(fill="both", expand=True, padx=20, pady=20)

        # Partition 1: Language Selection and Record Audio
        self.partition1 = ctk.CTkFrame(self.main_frame, corner_radius=15)
        self.partition1.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        self.language_label = ctk.CTkLabel(self.partition1, text="Select Language:", font=ctk.CTkFont(size=14, weight="bold"))
        self.language_label.pack(pady=(20, 10))

        self.languages = [
            "English", "Hindi", "Bengali", "Telugu", "Marathi", "Tamil", 
            "Gujarati", "Kannada", "Malayalam", "Odia", "Punjabi", 
            "Assamese", "Urdu", "Sanskrit"
        ]
        self.language_var = ctk.StringVar(value=self.languages[0])
        self.language_dropdown = ctk.CTkComboBox(self.partition1, values=self.languages, variable=self.language_var, width=150)
        self.language_dropdown.pack(pady=10)

        # Record Audio Button
        self.record_button = ctk.CTkButton(self.partition1, text="Record Audio", command=self.record_audio, fg_color="#2980b9", hover_color="#3498db")
        self.record_button.pack(pady=(20, 10))

        # Partition 2: Recorded Audio Display, Start Analysis, and Progress Bar
        self.partition2 = ctk.CTkFrame(self.main_frame, corner_radius=15)
        self.partition2.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        self.audio_label = ctk.CTkLabel(self.partition2, text="Recorded Audio File: None", font=ctk.CTkFont(size=13))
        self.audio_label.pack(pady=20)

        self.start_button = ctk.CTkButton(self.partition2, text="Start Analysis", command=self.start_analysis, fg_color="#27ae60", hover_color="#2ecc71")
        self.start_button.pack(pady=10)

        self.progress = ctk.CTkProgressBar(self.partition2, width=250)
        self.progress.set(0)  # Initialize at 0
        self.progress.pack(pady=20)

        # Partition 3: Sentiment Result Display
        self.partition3 = ctk.CTkFrame(self.main_frame, corner_radius=15)
        self.partition3.grid(row=0, column=2, padx=10, pady=10, sticky="nsew")

        self.result_label = ctk.CTkLabel(self.partition3, text="Sentiment Result: Waiting for analysis...", font=ctk.CTkFont(size=13, weight="bold"), wraplength=180)
        self.result_label.pack(pady=20)

        # Configure layout weights for responsive resizing
        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_frame.grid_columnconfigure(1, weight=2)
        self.main_frame.grid_columnconfigure(2, weight=1)
        self.main_frame.grid_rowconfigure(0, weight=1)

    def start_analysis(self):
        selected_language = self.language_var.get()
        self.result_label.configure(text=f"Analyzing in {selected_language}... Please wait.")
        self.progress.set(0)  # Reset progress bar
        self.progress.start()  # Start progress animation

        # Simulating analysis with threading to avoid freezing the UI
        threading.Thread(target=self.run_analysis_simulation).start()

    def run_analysis_simulation(self):
        # Simulate analysis duration
        for i in range(1, 101):
            self.progress.set(i / 100)  # Update progress incrementally
            time.sleep(0.05)  # Simulate time delay in analysis

        # Display result once analysis is "complete"
        self.result_label.configure(text="Sentiment Result: Positive")  # Placeholder result
        self.progress.stop()  # Stop progress animation

    def record_audio(self):
        # Simulated recording function
        audio_filename = "audio_sample.wav"  # Placeholder for recorded file
        self.audio_label.configure(text=f"Recorded Audio File: {audio_filename}")
        messagebox.showinfo("Recording", "Audio recorded successfully!")
        # Replace with actual audio recording logic

if __name__ == "__main__":
    root = ctk.CTk()
    app = VoiceSenseApp(root)
    root.mainloop()
