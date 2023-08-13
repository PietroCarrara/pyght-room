import os
import sys
import cv2 as cv
import numpy as np

for filename in sys.argv[1:]:
  def out(technique):
    fname = os.path.basename(filename)
    os.makedirs(technique, exist_ok=True)

    # Recover alpha channel, if any
    out = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
    if in_img.shape[2] == 4:
      out = cv.cvtColor(out, cv.COLOR_BGR2BGRA)
      out[:, :, 3] = in_img[:, :, 3]

    cv.imwrite(f"{technique}/{fname}", out)

  in_img = cv.imread(filename, cv.IMREAD_UNCHANGED)

  # Update saturation
  hsv = cv.cvtColor(in_img, cv.COLOR_BGR2HSV)
  hsv[:, :, 2] = cv.equalizeHist(hsv[:, :, 2])
  out('saturation_equalization')