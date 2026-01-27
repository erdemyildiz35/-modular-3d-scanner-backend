from motor import Motor
from camera import Camera
import time


class Scanner:
    def __init__(self, step=30):
        self.motor = Motor()
        self.camera = Camera()
        self.step = step

    def run_scan(self):
        images = []

        for angle in range(0, 360, self.step):
            self.motor.rotate_to(angle)
            image = self.camera.capture(angle)
            images.append(image)

            time.sleep(0.2)

        print("[SCANNER] Scan completed")
        return images


if __name__ == "__main__":
    scanner = Scanner(step=30)
    scanner.run_scan()
