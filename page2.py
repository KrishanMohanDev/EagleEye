
from tkinter import BooleanVar
import tkinter as tk 
import os
import sys
# Add the Models directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'Models'))
from Weapon_Detection.weapon import detect as detect_weapon
from Crowd_Detection.crowd import detect as detect_crowd
from Fall_Detection.Fall import detect as fall_detect
from Face_detection.face import detect as face_detect
from Car_Accident_Detection.Car import detect as accident_detect
from License_Plate_Recognition.lpr import detect as lpr_detect


import tkinter.filedialog as fd
import customtkinter as ctk
from PIL import Image, ImageTk
import cv2

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")


class DetectionPage(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        # self.title("Smart Surveillance System - Detection Page")
        # self.pack(fill="both", expand=True)
        # self.geometry("1280x720")
        self.configure(fg_color="#808080")
        # self.resizable(False, False)
        
        self.using_video_file = False  # <- New flag
        self.cap = cv2.VideoCapture(0)  # <- Start webcam by default
        self.video_label = ctk.CTkLabel(self, text="", width=1000, height=625)
        self.video_label.place(x=10, y=80)
        # self.show_frame()  # <-- ensures the loop starts
        
        # Header
        top_frame = ctk.CTkFrame(
            self, fg_color="#f0f0f0", height=60, corner_radius=0)
        top_frame.pack(side="top", fill="x")

        icon_img = ctk.CTkImage(light_image=Image.open(
            "./Src/Image/logo-survillence.png"), size=(40, 40))
        icon_label = ctk.CTkLabel(top_frame, image=icon_img, text="")
        icon_label.place(x=10, y=10)

        title = ctk.CTkLabel(top_frame, text="EagleEye", font=(
            "Arial Black", 18), text_color="black")
        title.place(x=60, y=15)

        admin_btn = ctk.CTkButton(top_frame, text="Admin Details",
                                  corner_radius=20, fg_color="#00bfff", hover_color="#00aadd", command=self.open_admin_popup)
        admin_btn.place(relx=0.87, rely=0.2)
        

        # Right panel: Select Models
        sidebar = ctk.CTkFrame(self, width=6000, height=450, fg_color="#bfbfbf")
        sidebar.place(x=1020, y=80)


        # Create horizontal frame for icon + label inside sidebar
        label_frame = ctk.CTkFrame(sidebar, fg_color="transparent")
        label_frame.pack(pady=(20, 10), padx=19, anchor="w")

        # Load and display icon image
        icon_img = ctk.CTkImage(light_image=Image.open(
            "./Src/Image/AI_model_logo.png"), size=(30, 30))
        icon_label = ctk.CTkLabel(label_frame, image=icon_img, text="")
        icon_label.pack(side="left", padx=(0, 8))

        # Label text next to icon
        model_label = ctk.CTkLabel(label_frame, text="Select ML Models", font=(
            "Arial Black", 18), text_color="black")
        model_label.pack(side="left")


        # Detection model checkboxes
        self.vars = {}
        models = ["Face Detection", "Crash Detection", "Fall Detection",
                  "LPR Detection", "Crowd Detection", "Weapon Detection"]
        for model in models:
            var = BooleanVar(value=False)
            cb = ctk.CTkCheckBox(sidebar, text=model, variable=var)
            cb.pack(pady=5, anchor="w", padx=30)
            self.vars[model] = var
            
            
        # Start upload file frame and button
        # Label text next to icon
        file_label = ctk.CTkLabel(sidebar, text="Select Video File", font=(
            "Arial Black", 18), text_color="black")
        file_label.pack(pady=(140, 0), padx=25, anchor="w")

        # Upload wrapper frame with padding (placed at bottom)
        upload_outer = ctk.CTkFrame(sidebar, fg_color="#bfbfbf")
        upload_outer.pack(pady=(0, 0), padx=25, anchor="s", side="bottom", fill="x")

        # Simulated dotted rectangle with rounded corners
        upload_box = ctk.CTkFrame(
            upload_outer,
            fg_color="transparent",
            border_color="gray",
            border_width=2,
            corner_radius=15,
            width=200,
            height=160,
        )
        upload_box.pack(padx=10, pady=10, fill="x")

        # Upload image or icon
        upload_img = ctk.CTkImage(light_image=Image.open("./Src/Image/image.png"), size=(35, 35))
        upload_icon = ctk.CTkLabel(upload_box, image=upload_img, text="")
        upload_icon.pack(pady=(20, 25))

        # Upload texts
        upload_label = ctk.CTkLabel(
            upload_box,
            text="Drag and Drop file\nor",
            justify="center",
            text_color="black",
            font=("Arial", 12)
        )
        upload_label.pack(pady=(0, 22))
        
        
        # Upload button
        self.browse_btn = ctk.CTkButton(upload_box, text="Browse",
                                        width=100, command=self.browse_file)
        self.browse_btn.pack(pady=(0, 10))
        
        self.show_frame()

    def browse_file(self):
        file_path = fd.askopenfilename(
            filetypes=[("Video files", "*.mp4 *.avi *.webm *.mov *.mkv")])
        if file_path:
            self.using_video_file = True
            if self.cap:
                self.cap.release()
            self.cap = cv2.VideoCapture(file_path)

    def show_frame(self):
        if self.cap and self.cap.isOpened():
            ret, frame = self.cap.read()
            if ret:
                frame = cv2.resize(frame, (1000, 625))
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                
                
                if self.vars["Weapon Detection"].get():
                    frame = detect_weapon(frame)
                if self.vars["Crowd Detection"].get():
                    frame,_ = detect_crowd(frame)
                if self.vars["Fall Detection"].get():
                    frame,_ = fall_detect(frame)
                if self.vars["Face Detection"].get():
                    frame = face_detect(frame)
                if self.vars["Crash Detection"].get():
                    frame = accident_detect(frame)
                if self.vars["LPR Detection"].get():
                    frame = lpr_detect(frame)
                    


                img = Image.fromarray(frame)
                # imgtk = ImageTk.PhotoImage(image=img)
                ctk_img = ctk.CTkImage(light_image=img, size=(1000, 625))

                self.video_label.configure(image=ctk_img)
                self.video_label.image = ctk_img  # Keep a reference

                self.after(30, self.show_frame)
            else:
                # Video file ended
                self.cap.release()
                if self.using_video_file:
                    self.cap = cv2.VideoCapture(0)  # Switch back to webcam
                    self.using_video_file = False
                    self.after(30, self.show_frame)


    def open_admin_popup(self):
        popup = ctk.CTkToplevel(self)
        popup.title("Admin Details")
        popup.geometry("400x300")
        popup.grab_set()  # Lock focus to popup
        
        

        sender_val = tk.StringVar()
        app_pass_val = tk.StringVar()
        receiver_val = tk.StringVar()

        # Try loading saved data
        try:
            with open("admin_details.txt", "r") as f:
                lines = f.read().splitlines()
                if len(lines) == 3:
                    sender_val.set(lines[0])
                    app_pass_val.set(lines[1])
                    receiver_val.set(lines[2])
        except FileNotFoundError:
            pass

        # Entry fields
        ctk.CTkLabel(popup, text="Sender Email ID:").pack(pady=(10, 2))
        sender_entry = ctk.CTkEntry(popup, textvariable=sender_val, width=300)
        sender_entry.pack()

        ctk.CTkLabel(popup, text="App Password:").pack(pady=(10, 2))
        app_pass_entry = ctk.CTkEntry(
            popup, textvariable=app_pass_val, show="*", width=300)
        app_pass_entry.pack()

        ctk.CTkLabel(popup, text="Receiver Email ID:").pack(pady=(10, 2))
        receiver_entry = ctk.CTkEntry(popup, textvariable=receiver_val, width=300)
        receiver_entry.pack()

        def save_details():
            with open("admin_details.txt", "w") as f:
                f.write(sender_val.get() + "\n")
                f.write(app_pass_val.get() + "\n")
                f.write(receiver_val.get() + "\n")
            popup.destroy()

        ctk.CTkButton(popup, text="Save", command=save_details).pack(pady=20)

