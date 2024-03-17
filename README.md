# Smoking Detector

This is a simple application that uses a pre-trained model to classify images as either "Smoking" or "Not Smoking". The application provides a graphical user interface (GUI) that allows users to select an image and scan it for smoking detection.

## Prerequisites

- Python 3.x
- tkinter
- PIL
- numpy
- tensorflow
- tensorflow_hub

## Usage

1. Clone the repository or download the code files.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Run the application using `python smoking_detector.py`.
4. The application window will open with a title, image label, select image button, scan button, and result label.
5. Click the **Select Image** button to choose an image file (supports PNG, JPG, JPEG, and GIF formats).
6. After selecting an image, it will be displayed in the image label.
7. Click the **SCAN** button to initiate the smoking detection process.
8. The result label will display the prediction result, indicating whether the image contains smoking or not.

## Code Explanation

- The code uses the `tkinter` library to create the GUI elements.
- The `PIL` library is used for image processing and displaying images in the GUI.
- The `numpy` library is used for array manipulation.
- The `tensorflow` and `tensorflow_hub` libraries are used for loading the pre-trained smoking detection model.
- The application is implemented as a class called `SmokingDetector`.
- The class constructor sets up the GUI elements and loads the pre-trained model.
- The `select_image` method is responsible for opening a file dialog to select an image file and displaying the selected image in the GUI.
- The `predict_image` method processes the selected image and performs smoking detection using the pre-trained model. The result is displayed in the GUI.
- The `run` method starts the main event loop of the GUI.
- The `__main__` block creates an instance of the `SmokingDetector` class and runs the application.

## License

This project is licensed under the [MIT License](LICENSE).
