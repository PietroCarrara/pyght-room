import os
import sys
import cv2 as cv
import numpy as np

for filename in sys.argv[1:]:

    def out(technique, out):
        fname = os.path.basename(filename)
        os.makedirs(technique, exist_ok=True)

        # Recover alpha channel, if any
        out = cv.cvtColor(out, cv.COLOR_HSV2BGR)
        if in_img.shape[2] == 4:
            out = cv.cvtColor(out, cv.COLOR_BGR2BGRA)
            out[:, :, 3] = in_img[:, :, 3]

        cv.imwrite(f"{technique}/{fname}", out)

    in_img = cv.imread(filename, cv.IMREAD_UNCHANGED)

    # Equalize brightness
    hsv = cv.cvtColor(in_img, cv.COLOR_BGR2HSV)
    hsv[:, :, 2] = cv.equalizeHist(hsv[:, :, 2])
    out("brightness_equalization", hsv)

    # Move up the brightness while preserving relative distances
    PERCENTAGE = 1 - 1 / 10
    hsv = cv.cvtColor(in_img, cv.COLOR_BGR2HSV)
    hsv[:, :, 2] = hsv[:, :, 2] * PERCENTAGE + ((1 - PERCENTAGE) * 255)
    out("uplift_brightness", hsv)

    # Move up the saturation (20%) while preserving relative distances
    PERCENTAGE = 1 - 2 / 10
    hsv = cv.cvtColor(in_img, cv.COLOR_BGR2HSV)
    hsv[:, :, 1] = hsv[:, :, 1] * PERCENTAGE + ((1 - PERCENTAGE) * 255)
    out("uplift_saturation_20", hsv)

    # Move up the saturation (30%) while preserving relative distances
    PERCENTAGE = 1 - 3 / 10
    hsv = cv.cvtColor(in_img, cv.COLOR_BGR2HSV)
    hsv[:, :, 1] = hsv[:, :, 1] * PERCENTAGE + ((1 - PERCENTAGE) * 255)
    out("uplift_saturation_30", hsv)

    # Gamma correction (gamma = 0.67)
    GAMMA = 0.67
    hsv = cv.cvtColor(in_img, cv.COLOR_BGR2HSV)
    lookUpTable = np.array([pow(i / 255.0, GAMMA) for i in range(256)]) * 255
    hsv[:, :, 2] = cv.LUT(hsv[:, :, 2], lookUpTable)
    out("gamma_correction_0.67", hsv)

    # Gamma correction (gamma = 0.5)
    GAMMA = 0.5
    hsv = cv.cvtColor(in_img, cv.COLOR_BGR2HSV)
    lookUpTable = np.array([pow(i / 255.0, GAMMA) for i in range(256)]) * 255
    hsv[:, :, 2] = cv.LUT(hsv[:, :, 2], lookUpTable)
    out("gamma_correction_0.5", hsv)
