# 🧭 Animated Compass with Python Turtle 🐢

Welcome to the **Animated Compass** project! This project demonstrates how to use **Python's Turtle Graphics** library to create a visually appealing and fully animated compass, complete with directional labels and a rotating needle. It’s a fun and educational project for beginners and experienced developers alike!

<div align="center">
    <img src="https://www.nio.lk/wp-content/uploads/revslider/cercle.png" alt="Compass GIF" width="300" height="300">
</div>

---

## 🚀 Features
- **Interactive and animated compass needle** that rotates smoothly.
- **Stylish compass design** using vibrant colors and Turtle graphics.
- **Easy-to-follow** code with detailed comments for each step.
- Ideal for **beginners** learning Turtle and Python animations.

---

## 💻 Technologies Used
- **Python 3** 🐍
- **Turtle Graphics** 🐢 (built-in Python library)
- **Time Module** ⏲️ (for smooth animation)

---

## 📂 Project Structure
The following files are included in this repository:

```bash
.
├── compass.py       # Main Python file with the full code
├── README.md        # Project documentation
└── images/          # Folder for screenshots or GIFs (optional)
```

## 📜 How to Run the Project

1️⃣ Clone the repository to your local machine:
```bash
    git clone https://github.com/SE-LAPS/Python-Turtle-Animated-Compass-.git
```

2️⃣ Navigate to the project directory:
```bash
cd animated-compass-turtle
```

3️⃣ Install Python (if you don't have it installed): Download Python

4️⃣ Run the Python file:
```bash
python compass.py
```

## ✨ Code Overview

1️⃣ Setting Up the Screen
This part of the code creates the canvas for the compass animation. It sets up the screen size and background color.
```bash
def setup_screen():
    screen = turtle.Screen()
    screen.setup(500, 500)
    screen.bgcolor("#F0F0F0")
    screen.title("Enhanced Animated Compass")
    return screen
```
2️⃣ Drawing the Compass
The create_compass() function draws the outer and inner circles of the compass, as well as the labels for the four main directions (N, E, S, W) and the intermediate directions (NE, SE, SW, NW).
```bash
def create_compass(t):
    t.penup()
    t.goto(0, -180)
    t.pendown()
    t.color("#FF1493")
    t.begin_fill()
    t.circle(180)
    t.end_fill()
    ...
```

3️⃣ Creating the Needle
This part of the code creates and animates the needle of the compass to rotate smoothly in a loop.
```bash
def create_needle(t):
    t.penup()
    t.goto(0, 0)
    t.color("white")
    t.shape("triangle")
    t.shapesize(0.8, 4)
    t.setheading(90)
    return t
```

## 🧠 How It Works

1️⃣ Turtle graphics is used to draw the compass and animate the needle.<br>
2️⃣ The circle() method is used to draw the outer and inner circles.<br>
3️⃣ The needle is drawn using a turtle shape and is rotated using the setheading() method.<br>
4️⃣ Smooth animations are achieved using Python’s time.sleep() function.

## 🛠️ Requirements

1️⃣ Python 3.x 🐍<br>
2️⃣ Turtle (no need to install separately, it’s built into Python)<br>
3️⃣ Basic knowledge of Python 🧠

## 📝 License
This project is licensed under the MIT License. See the LICENSE file for more details.

## 🤝 Connect with Me

<div align="center">

<a href="https://www.facebook.com/CodeShowLapZ?mibextid=ZbWKwL" target="_blank">
    <img src="https://img.shields.io/badge/FaceBook-%23E4405F.svg?style=for-the-badge&logo=facebook&logoColor=white" alt="Facebook">
</a>

<a href="https://www.linkedin.com/in/lahiru-senavirathna-39b11a215/" target="_blank">
    <img src="https://img.shields.io/badge/LinkedIn-%230A66C2.svg?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn">
</a>

<a href="https://www.youtube.com/@CodeShowLapZ" target="_blank">
    <img src="https://img.shields.io/badge/YouTube-%23FF0000.svg?style=for-the-badge&logo=YouTube&logoColor=white" alt="YouTube">
</a>

</div>
