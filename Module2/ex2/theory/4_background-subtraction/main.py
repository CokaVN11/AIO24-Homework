import numpy as np
import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os

current_path = os.path.dirname(__file__)
images_path = os.path.join(current_path, 'images')
output_path = os.path.join(current_path, 'output')
img_size = (678, 381)


def compute_difference(bg_img, input_img):
    # background subtraction
    difference = np.abs(bg_img.astype(np.int64) - input_img.astype(np.int64))
    difference = np.clip(difference, 0, 255).astype(np.uint8)
    return difference


def compute_binary_mask(difference_single_channel, threshold=50):
    difference_mean = np.mean(difference_single_channel, axis=2)
    mask = np.zeros_like(difference_mean)
    mask[difference_mean > threshold] = 1
    return mask.astype(np.uint8)


def replace_background(bg1_img, bg2_img, ob_img):
    difference_single_channel = compute_difference(bg1_img, ob_img)
    binary_mask = compute_binary_mask(difference_single_channel)

    mask = np.stack([binary_mask] * 3, axis=2)

    output = np.where(mask, ob_img, bg2_img)
    return output


bg1_img = cv2.imread(os.path.join(images_path, 'GreenBackground.png'), 1)
ob_img = cv2.imread(os.path.join(images_path, 'Object.png'), 1)
bg2_img = cv2.imread(os.path.join(images_path, 'NewBackground.jpg'), 1)

bg1_img = cv2.resize(bg1_img, img_size)
ob_img = cv2.resize(ob_img, img_size)
bg2_img = cv2.resize(bg2_img, img_size)

new_img = replace_background(bg1_img, bg2_img, ob_img)
cv2.imwrite(os.path.join(output_path, 'output.png'), new_img)
