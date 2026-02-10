# Modular 3D Scanner Backend

This project simulates the backend architecture of a modular 3D scanning system.
It focuses on system design, microservice communication, and image processing rather than hardware implementation.

The goal of this project is to demonstrate how a real-world 3D scanner backend can be designed in a scalable and modular way.

---

## 🎯 Problem Statement

3D scanning systems involve:
- long-running hardware-dependent tasks,
- coordination between multiple components (camera, motor, processing),
- large amounts of image data,
- and the need for reliable, non-blocking backend communication.

A monolithic backend approach quickly becomes hard to scale and maintain.

---

## 🧩 Solution Overview

To address these challenges, I designed a **microservice-based backend architecture** with clear separation of responsibilities:

- API orchestration is handled independently
- Scanning logic is isolated from image processing
- Services communicate asynchronously using messaging

This approach reflects real-world hardware–software interaction patterns.

---

## 🏗️ System Architecture


---

## 🧠 Services Description

### 🔹 API Gateway
- Exposes REST endpoints to start and monitor scans
- Manages scan lifecycle and status
- Prevents long-running tasks from blocking the API

**Technologies:** FastAPI, Python

---

### 🔹 Scanner Service
- Simulates a motorized turntable
- Simulates camera image capture at different angles
- Publishes scan results asynchronously via MQTT

This service represents the hardware control layer.

**Technologies:** Python, Pillow, MQTT

---

### 🔹 Processing Service
- Listens for scan events via MQTT
- Applies image preprocessing and edge detection
- Converts raw images into structured, processed outputs

This service represents the data processing pipeline.

**Technologies:** Python, OpenCV, MQTT

---

## 📡 Communication Pattern

The system uses **MQTT (publish–subscribe)** for inter-service communication.

**Why MQTT?**
- Lightweight and efficient
- Asynchronous and non-blocking
- Well-suited for hardware-like event-driven systems
- Decouples services and improves scalability

---

## 🐳 Deployment

All services are containerized and orchestrated using Docker Compose.

```bash
docker compose up --build
