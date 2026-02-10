import cv2  # OpenCV for image processing
import numpy as np # NumPy for numerical operations

def undistort(image, camera_matrix, dist_coeffs):
    return cv2.undistort(image, camera_matrix, dist_coeffs)
# purpose : camera calibration and undistortion to correct lens distortion in the captured images, ensuring accurate measurements and improved image quality for subsequent processing steps.


def reduce_noise(image):
    return cv2.bilateralFilter(image, 9, 75, 75)
# purpose : noise reduction to enhance the quality of the captured images, making it easier to extract meaningful features and details during the 3D reconstruction process. The bilateral filter is particularly effective at reducing noise while preserving edges, which is crucial for maintaining the integrity of the features in the images.

def normalize_exposure(image):
    lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
    l, a, b = cv2.split(lab)
    clache= cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    cl = clache.apply(l)
    limg = cv2.merge((cl, a, b))
    return cv2.cvtColor(limg, cv2.COLOR_LAB2BGR)
# purpose : exposure normalization to improve the visibility of details in the captured images, especially in cases where lighting conditions may be uneven or suboptimal. By applying CLAHE (Contrast Limited Adaptive Histogram Equalization), we can enhance the contrast of the images while preventing over-amplification of noise, resulting in clearer and more detailed images for the 3D reconstruction process.

def enhance_features(image):
    kernel = np.array([[0, -1, 0], [-1, 5,-1], [0, -1, 0]])
    return cv2.filter2D(image, -1, kernel)
# purpose : feature enhancement to improve the visibility of important details and edges in the captured images, which is crucial for accurate 3D reconstruction. By applying a sharpening filter, we can enhance the contrast of edges and fine details, making it easier to extract meaningful features during the subsequent processing steps.
def preprocess_image(image, camera_matrix, dist_coeffs):
    undistorted = undistort(image, camera_matrix, dist_coeffs)
    denoised = reduce_noise(undistorted)
    normalized = normalize_exposure(denoised)
    enhanced = enhance_features(normalized)
    return enhanced
    # purpose : This function serves as the main preprocessing pipeline for the captured images. It sequentially applies camera calibration and undistortion, noise reduction, exposure normalization, and feature enhancement to prepare the images for accurate 3D reconstruction. By combining these steps, we can ensure that the images are of high quality and contain the necessary details for successful 3D scanning.





    # piplene.py= core image processing (geometry correction, noise reduction, feature enhancement) for the captured images, ensuring that they are optimized for accurate 3D reconstruction. This modular approach allows for easy maintenance and scalability of the preprocessing steps as needed.