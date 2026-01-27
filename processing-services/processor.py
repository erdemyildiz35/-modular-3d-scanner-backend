import os
import cv2
from opencv_utils import load_image, preprocess, extract_edges


INPUT_DIR = "./input"
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

    return output_path


def process_all():
    for file in os.listdir(INPUT_DIR):
        if file.endswith(".png"):
            process_image(os.path.join(INPUT_DIR, file))


if __name__ == "__main__":
    print("[PROCESSOR] Starting image processing service...")
    process_all()
