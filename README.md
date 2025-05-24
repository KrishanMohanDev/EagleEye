# 🦅 EagleEye: Smart Surveillance System

EagleEye is a Python-based smart surveillance system that uses deep learning and computer vision to detect and respond to real-time events. It integrates multiple detection modules into a unified GUI interface for seamless user interaction.

## 🧠 Features

- 🚗 Car Accident Detection  
- 👥 Crowd Detection  
- 🙂 Face Detection  
- 🤕 Fall Detection  
- 🔫 Weapon Detection  
- 🚓 License Plate Recognition (LPR)

---

## 📂 Project Structure

```
EagleEye/
│   app.py                   # Main application file to run
│   page2.py                 # Secondary UI script
│   requirements.txt         # Required Python packages
│   admin_details.txt        # Admin config
│
├───Models/                  # Pretrained models and detection scripts
├───Input Video/             # Sample input videos for testing
├───Output/                  # Output video frames or results
└───Src/                     # UI images and icons
```

---

## 📦 Installation Guide

### 🔧 1. Clone the Repository

```bash
git clone https://github.com/KrishanMohanDev/EagleEye.git
cd EagleEye
```

### 📁 2. Download Pretrained Weights

⚠️ **Weights are not stored in this repo due to size limits.**  
Download all Weapon model weights (~500MB+) from the link below and place them inside the respective folders in the `Models/Weapon_Detection/` directory.

📥 **[Download Model Weights](https://drive.google.com/file/d/15_5JIgPdkNJqjejdFTqibuVjst7VoPQJ/view?usp=sharing)**  

---

### 🐍 3. Install Dependencies

Create a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

Then install required libraries:

```bash
pip install -r requirements.txt
```

---

## 🚀 Run the Application

Start the application by running:

```bash
python app.py
```

The app will open a GUI for selecting the type of detection (car accident, weapon, fall, etc.), input video, and display the detection output.

---

## 📸 Sample Input Videos

A few sample test videos are already included in the `Input Video/` folder for quick testing.
Download all Video input (~500MB+) from the link below.

📥 **[Download sample input video](https://drive.google.com/file/d/1ecGiZQi2qHK8she0C3RqM8BQ9dqxErYe/view?usp=sharing)**  

---

## 🤖 Future Enhancements

- Fire and smoke detection  
- Object theft detection  
- Web app version of EagleEye  
- Real-time camera integration  

---

## 👤 Author

**Krishan Mohan Mandal**  
B.Tech - Artificial Intelligence & Data Science  
[GitHub](https://github.com/KrishanMohanDev)

---

## ⚠️ License

This project is licensed under the MIT License – feel free to use and modify.

---
