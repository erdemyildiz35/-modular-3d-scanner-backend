import os
import json
import cv2
import paho.mqtt.client as mqtt
from opencv_utils import load_image, preprocess, extract_edges

MQTT_BROKER = "mqtt"
TOPIC = "scanner/images_ready"

OUTPUT_DIR = "./output"
os.makedirs(OUTPUT_DIR, exist_ok=True)


def process_image(image_path: str):
    image = load_image(image_path)
    preprocessed = preprocess(image)
    edges = extract_edges(preprocessed)

    filename = os.path.basename(image_path)
    output_path = os.path.join(OUTPUT_DIR, f"processed_{filename}")

    cv2.imwrite(output_path, edges)
    print(f"[PROCESSOR] Processed {filename}")


def on_message(client, userdata, msg):
    data = json.loads(msg.payload.decode())
    images = data["images"]

    print("[PROCESSOR] Received images via MQTT")

    for image_path in images:
        process_image(image_path)


client = mqtt.Client()
client.connect(MQTT_BROKER, 1883)
client.subscribe(TOPIC)
client.on_message = on_message

print("[PROCESSOR] Waiting for MQTT messages...")
client.loop_forever()
