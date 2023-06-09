import cv2
import numpy as np
import mediapipe as mp
from scipy.spatial import Delaunay
import argparse

from utils.landmarker import facial_landmarker
from utils.video_handler import video_processor


def reconstructor(input_path, output_path):

    vp = video_processor()
    fl = facial_landmarker()
    image_list = vp.preprocess_video(input_path)
    processed_image_list = []

    for i in range(len(image_list)):
        processed_landmarks = fl.get_landmarks(image_list[i], 2)
        processed_image = fl.facial_segmentation(image_list[i], processed_landmarks)
        processed_image_list.append(processed_image)

    vp.video_stitch(processed_image_list, output_path, fps = 25)


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        "Face Reconstruction Demo", add_help=True
    )
    parser.add_argument(
        "--input_path", type=str, default='assets/example_video.mp4', required=False, help="path to input video file"
    )
    parser.add_argument(
        "--output_path", type=str, default='results/processed_example_video.mp4', required=False, help="path to output video file"
    )
    
    args = parser.parse_args()

    input_path = args.input_path
    output_path = args.output_path

    reconstructor(input_path, output_path)