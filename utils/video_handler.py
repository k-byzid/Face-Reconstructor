import cv2
import numpy as np

class video_processor():
    
    def __init__(self):
        pass
        
        
    def preprocess_video(self, input_path):
        
        video = cv2.VideoCapture(input_path)
        fps = video.get(cv2.CAP_PROP_FPS)
        frame_count = 1
        
        image_list = []
        
        while video.isOpened():
            ret, frame = video.read()
            if not ret:
                break
                
            frame_interval = frame_count

            if frame_count % frame_interval == 0:
                image_list.append(frame)

            frame_count += 1
         
        return image_list
    
    
    def video_stitch(self, image_list, output_path, fps):
        
        height, width, _ = image_list[0].shape
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        video_writer = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

        for image_file in image_list:
            video_writer.write(image_file)
        video_writer.release()
        
        
    def view_videos(self, path_1, path_2):
        
        video1 = cv2.VideoCapture(path_1)
        video2 = cv2.VideoCapture(path_2)
        
        while True:
            ret1, frame1 = video1.read()
            ret2, frame2 = video2.read()
            if not ret1 or not ret2:
                break
                
            combined_frame = np.hstack((frame1, frame2))

            cv2.imshow('Videos', combined_frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break