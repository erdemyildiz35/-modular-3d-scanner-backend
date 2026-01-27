from PIL import Image, ImageDraw
import numpy as np
import uuid


class Camera:
    def capture(self, angle: int):
        img = Image.new("RGB", (300, 300), color="black")
        draw = ImageDraw.Draw(img)

        draw.text((10, 10), f"Angle: {angle}", fill="white")
        draw.rectangle([100, 100, 200, 200], outline="white")

        filename = f"scan_{angle}_{uuid.uuid4().hex}.png"
        img.save(filename)

        print(f"[CAMERA] Captured image at {angle}° → {filename}")

        return filename
