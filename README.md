# Face Reconstructor 👤🔍💻 <br>

## Description
Welcome to the Face Reconstructor project! 🌟 This advanced application utilizes the cutting-edge capabilities of the Mediapipe library Holistic tool
to accurately identify and analyze a comprehensive set of 468 facial landmarks. Leveraging the power of OpenCV (cv2), this system employs sophisticated 
algorithms to generate a meticulously crafted triangulation mesh, wherein each polygon is expertly filled with a seamless patch of skin derived from 
the original frame. 📸💡 <br><br>


## Features
🔍✨ Facial Landmark Detection: Utilizing Mediapipe Holistic, this system accurately detects key facial landmarks, revealing detailed structural insights. 🎯💡

🔳✨ Triangulated Mesh Generation: With OpenCV (cv2), this application creates a precise triangulation mesh, enabling advanced analysis and visualizations 
of facial geometry. 📏🔲

🎨✨ Patch-based Skin Reconstruction: This system achieves lifelike face reconstruction by filling triangulation mesh polygons with carefully selected skin 
patches, maintaining a natural appearance. 🖌️🧑‍🎨<br><br>


## Installation and Usage
1. :fork_and_knife:  Fork the repository to your GitHub account.
2. :arrow_down: Clone the forked repository to your local machine.
3. :cd: Navigate to the local repository using the command line.
4. :computer: Run the script using the following command: <br><kbd style="background-color: black; color: white; padding: 50px 75px; border-radius: 10px;">python reconstructor.py --input_image assets/example_video.mp4 --output_path results/processed_example_video.mp4</kbd>, <br>where <kbd style="background-color: black; color: white; padding: 50px 75px; border-radius: 10px;">assets/example_video.mp4</kbd>is the path to the input video you want to extract the face from.
8. :envelope: The generated stickers will be saved in the "results" folder for further usage.<br><br>

## Usage Preview
### Input Video - - Output Video: 

<br>![Example 1](gif/example_video.gif)![Processed Example 1](gif/processed_example_video.gif)
<br><br>![Example 2](gif/example_video_2.gif)![Processed Example 2](gif/processed_example_video_2.gif)
<br><br>![Example Test](gif/test.gif)![Processed Example Test](gif/processed_test.gif)<br><br>

## Requirements
The following dependencies are required to run the Face Reconstructor:

1. Python 3.x
2. Mediapipe
3. OpenCV Python
4. Numpy

You can install these dependencies manually using the package manager of your choice.
