import cv2
import numpy as np
import mediapipe as mp
from scipy.spatial import Delaunay

class facial_landmarker():
    
    def __init__(self, video_feed = False, smooth_landmarks = True):
        
        self.static_image_mode = not(video_feed)
        self.smooth_landmarks = smooth_landmarks
        mp_holistic = mp.solutions.holistic
        self.face_detector = mp_holistic.Holistic(static_image_mode = self.static_image_mode, smooth_landmarks = self.smooth_landmarks)
        
        
    def get_landmarks(self, image, dimensions = 3):
        
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        self.dimension = dimensions
        self.result = self.face_detector.process(image_rgb)
        self.faces = self.result.face_landmarks.landmark
        self.left_hand = self.result.left_hand_landmarks
        self.right_hand = self.result.right_hand_landmarks
        
        landmarks = []
        lm = []
        
        if self.faces:
            landmarks.extend([(landmark.x, landmark.y, landmark.z) for landmark in self.faces])
        if self.left_hand:
            landmarks.extend([(landmark.x, landmark.y, landmark.z) for landmark in self.left_hand.landmark])
        if self.right_hand:
            landmarks.extend([(landmark.x, landmark.y, landmark.z) for landmark in self.right_hand.landmark])
            
        if self.dimension == 3:
            for landmark in landmarks:
                x, y, z = landmark
                lm.append((int(x*image.shape[1]), int(y*image.shape[0]), int(z*(np.minimum(image.shape[0], image.shape[1])))))
        else:
            for landmark in landmarks:
                x, y, _ = landmark
                lm.append((int(x*image.shape[1]), int(y*image.shape[0])))
            
        return lm
        
        
    def show_landmarks(self, img, landmarks, font = cv2.FONT_HERSHEY_SIMPLEX, font_scale = 0.4, color = (150, 255, 120), thickness = 2):

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        self.landmarks = landmarks
        self.font = font
        self.font_scale = font_scale
        self.color = color
        self.thickness = thickness
        
        for i in range(len(self.landmarks)):
            x = self.landmarks[i][0]
            y = self.landmarks[i][1]
            cv2.putText(img, str(i), (int(x), int(y)), self.font, self.font_scale, self.color, self.thickness)
        
        cv2.imshow('Facial Landmarks', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
    
    def facial_segmentation(self, image, landmarks):
        
        self.landmarks = landmarks
        
        vertices = np.array(self.landmarks, dtype=np.float32)
        triangulation = Delaunay(vertices)
        faces = triangulation.simplices
        image_width = image.shape[1]
        image_height = image.shape[0]
        filled_image = np.zeros_like(image)
        
        for face in faces:
            pt1, pt2, pt3 = tuple(vertices[face[0]].astype(int)), tuple(vertices[face[1]].astype(int)), tuple(vertices[face[2]].astype(int))
            roi_corners = np.array([pt1, pt2, pt3], dtype = np.int32)
            
            mask = np.zeros((image_height, image_width), dtype = np.uint8)
            cv2.fillPoly(mask, [roi_corners], 255)
            patch = cv2.bitwise_and(image, image, mask = mask)
            filled_image = cv2.bitwise_or(filled_image, patch)
            
        return filled_image