# Unitree Go1 EDU Gesture Control Module

## 📌 Overview
The **Unitree Go1 EDU Gesture Control Module** enables users to control the robot using hand gestures. Leveraging computer vision and machine learning, this module recognizes user gestures and translates them into movement commands for the robot.

## ✨ Features
- ✅ Real-time gesture recognition using computer vision
- ✅ Integration with ROS for seamless communication
- ✅ Machine learning-based gesture classification
- ✅ Support for various gestures to control robot movements

## 🛠 Technologies Used
- **🔹 OpenCV**: Image and video processing library for capturing and analyzing video streams.
- **🔹 NumPy**: Library for handling multidimensional arrays and performing mathematical operations.
- **🔹 ROS (Robot Operating System)**: A framework that facilitates communication between system components.
- **🔹 PyTorch**: Deep learning library used for training and implementing gesture recognition models.
- **🔹 MediaPipe**: Multimedia processing library providing tools for gesture recognition and motion tracking.

## 🔧 Installation
### 📌 Prerequisites
Ensure you have the following installed:
- 🐍 Python (version <= 3.12 recommended)
- 🤖 ROS (Robot Operating System)

### 📥 Installing Dependencies
Use the following command to install the required libraries:
```bash
pip install opencv-python numpy torch mediapipe
```

## 🚀 Getting Started
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-repo/unitree-go1-gesture-control.git
cd unitree-go1-gesture-control
```

### 2️⃣ Run the Gesture Recognition Module
Execute the following command to start the gesture control system:
```bash
python main.py
```

### 3️⃣ Connect to ROS
Ensure that ROS is running before executing the module:
```bash
roscore &
python ros_publisher.py
```

## 🎮 Usage
- 👋 Perform predefined gestures in front of the camera.
- 🤖 The system will recognize gestures and send corresponding movement commands to the **Unitree Go1 EDU**.
- 🖥 Check the ROS topics for real-time updates on gesture recognition.

## 🤝 Contribution
Feel free to contribute by submitting issues or pull requests. 

## 📜 License
This project is licensed under the **MIT License**.

