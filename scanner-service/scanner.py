from motor import Motor
from camera import Camera
import time
import json
import paho.mqtt.client as mqtt

MQTT_BROKER = "mqtt"
TOPIC = "scanner/images_ready"


class Scanner:
    def __init__(self, step=30):
        self.motor = Motor()
        self.camera = Camera()
        self.step = step
        self.client = mqtt.Client()
        self.client.connect(MQTT_BROKER, 1883)

    def run_scan(self):
        images = []

        for angle in range(0, 360, self.step):
            self.motor.rotate_to(angle)
            image = self.camera.capture(angle)
            images.append(image)
            time.sleep(0.2)

        payload = json.dumps({"images": images})
        self.client.publish(TOPIC, payload)

        print("[SCANNER] Images published to MQTT")


if __name__ == "__main__":
    scanner = Scanner()
    scanner.run_scan()
