import cv2


def load_image(path: str):
    return cv2.imread(path)


def preprocess(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    return blurred


def extract_edges(image):
    edges = cv2.Canny(image, 50, 150)
    return edges
