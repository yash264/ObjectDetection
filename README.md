# 🧠 Object Detection Model

A **real-time object detection system** built using **OpenCV’s DNN module** and a **pre-trained SSD MobileNet model**.  
This project detects and labels multiple objects in live video streams or images with high accuracy and low latency.

---

## 🚀 Overview

This project demonstrates how deep learning models can be deployed efficiently on local systems using OpenCV’s **Deep Neural Network (DNN)** module.  
The system identifies objects, draws bounding boxes, and displays class names with confidence scores in real time.

---

## 🖥️ Features

- Real-time detection from webcam or video input.  
- Displays bounding boxes, confidence scores, and class labels.  
- Adjustable confidence threshold for fine-tuning detection accuracy.  
- Lightweight and fast — runs efficiently on CPU.  
- Can be extended to process images or recorded videos.

---


## 🚀 Video Tutorial

 [Watch It](https://youtu.be/Rk5TgP_4Bhw)

---

## 🧩 Model Used

### 🔸 SSD (Single Shot MultiBox Detector)
- A deep learning–based object detection framework.  
- Detects objects in a **single forward pass**, making it extremely fast for real-time use.  
- Predicts bounding boxes and class probabilities directly from feature maps at multiple scales.

### 🔸 MobileNet
- A lightweight, efficient CNN architecture optimized for **mobile and edge devices**.  
- Designed for speed and low computational cost while maintaining good accuracy.

### 🔸 SSD MobileNet
- Combines SSD’s fast detection with MobileNet’s compact architecture, ideal for real-time object detection on CPU or GPU.

---

## ⚙️ Detection Algorithm

1. **Input Frame Capture:**  
   Captures each frame from a webcam or video source using OpenCV.

2. **Preprocessing:**  
   Resizes the image and normalizes pixel values to prepare it for the neural network.

3. **Forward Pass:**  
   Sends the frame through the SSD MobileNet network via OpenCV’s DNN module.

4. **Post-processing:**  
   Extracts class IDs, confidence scores, and bounding box coordinates.

5. **Display:**  
   Draws bounding boxes and class labels for all detected objects in real time.

---

## 🧰 Tech Stack

- **Language:** Python  
- **Libraries:** OpenCV, NumPy  
- **Model:** SSD MobileNet (pre-trained on COCO dataset)  
- **Dataset:** COCO (Common Objects in Context)
