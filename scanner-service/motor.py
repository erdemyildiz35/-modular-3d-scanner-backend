import time


class Motor:
    def __init__(self):
        self.current_angle = 0

    def rotate_to(self, angle: int):
        print(f"[MOTOR] Rotating to {angle} degrees")
        time.sleep(0.3)  # simulate rotation delay
        self.current_angle = angle
