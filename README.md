# 🩸 Blood Cell Detection Using YOLO

A computer vision project that detects and identifies **Red Blood Cells (RBCs), White Blood Cells (WBCs), and Platelets** in microscopy images using a trained YOLO object detection model. The project uses Roboflow for dataset preparation and Streamlit to provide an interactive web application for image-based detection.

## 📌 Project Overview

Blood cell detection is an object detection task in which a computer vision model identifies blood cells and locates them using bounding boxes.

In this project, I trained a YOLO model using a dataset of **364 images prepared using Roboflow** and developed a Streamlit application to make predictions on uploaded microscopy images.

### Key Features

- Detects RBCs, WBCs, and Platelets.
- Uses a custom-trained YOLO object detection model.
- Uses Roboflow for dataset preparation and annotation workflow.
- Provides an interactive Streamlit web interface.
- Allows users to upload microscopy images.
- Displays annotated images with predicted bounding boxes and confidence scores.
- Provides configurable confidence and IoU thresholds.
- Displays detected cell counts and allows users to download annotated results.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| YOLO (Ultralytics) | Object detection |
| Roboflow | Dataset preparation and annotation |
| Streamlit | Web application |
| OpenCV | Image processing |
| Pillow | Image handling |
| Pandas | Tabular results and detection counts |

## 📂 Dataset

- **Dataset size:** 364 images
- **Dataset preparation:** Roboflow
- **Task:** Object detection in blood microscopy images
- **Target classes:** RBC, WBC, and Platelets

The images and annotations were prepared for training an object detection model. The model learns to locate blood cells and classify them into the corresponding categories.

*Note: The dataset size refers to the images used for training as reported for this project. The exact train, validation, and test split should be documented separately if applicable.*

## 🧠 Model Training

The project uses a YOLO object detection model trained on the prepared blood cell dataset.

The training workflow includes:

1. Preparing and annotating microscopy images using Roboflow.
2. Exporting the dataset in a YOLO-compatible format.
3. Training the YOLO model on the dataset.
4. Evaluating model performance using object detection metrics.
5. Saving the trained weights as `best.pt`.
6. Loading the trained model into the Streamlit application for inference.

### Evaluation Metrics

The following validation results were reported for the trained model:

| Metric | Score |
|---|---:|
| Precision | 83.9% |
| Recall | 92.8% |
| mAP@50 | 92.9% |
| mAP@50–95 | 65.8% |

These results indicate the model's reported performance on its validation dataset. Performance may vary on images from different microscopes, laboratories, or imaging conditions.

## 🖥️ Application Preview

The Streamlit application allows users to upload a microscopy image and view the model's predictions.

The application provides:

- Image upload
- Detection confidence configuration
- IoU threshold configuration
- Annotated image output
- Detected cell counts
- Downloadable annotated images

## 📁 Project Structure

```text
blood_cell_streamlit_app/
│
├── app.py
├── requirements.txt
├── README.md
└── best.pt
```

**Important:** The trained model weights file is required to run the application. It is not included automatically when you install the Python dependencies.

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/blood-cell-detection.git
```

Navigate into the project directory:

```bash
cd blood-cell-detection
```

Replace `YOUR_USERNAME` and the repository name with your actual GitHub details.

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### 4. Add the trained model

Copy your trained model weights into the project directory.

The application must reference the exact model filename. For example, if your file is named `best (1).pt`, update the model path in `app.py` accordingly.

```python
from pathlib import Path

MODEL_PATH = Path("best (1).pt")
```

Alternatively, rename the file to `best.pt` and set the model path to `Path("best.pt")`.

### 5. Run the Streamlit application

```bash
python -m streamlit run app.py
```

Open the local URL displayed in the terminal, usually:

```text
http://localhost:8501
```

Upload a microscopy image to view the model's predictions.

## 📊 Applications

Potential applications of blood cell object detection include:

- Educational demonstrations of computer vision.
- Research experiments involving microscopy images.
- Automated image analysis prototypes.
- Exploring object detection in biomedical image datasets.

## ⚠️ Limitations and Disclaimer

- The model was trained using a limited dataset of 364 images, so its ability to generalize to unseen data may be limited.
- Detection accuracy depends on image quality, cell appearance, annotation quality, and the distribution of the training data.
- The reported metrics are validation results and do not establish clinical reliability.
- This project is intended for educational and research purposes only. It is **not a medical diagnostic system** and must not be used to make clinical decisions.

## 🚀 Future Improvements

- Expand the dataset with more diverse and accurately annotated images.
- Compare different YOLO model sizes and training configurations.
- Evaluate performance separately for each blood cell class.
- Analyze false positives and false negatives using a confusion matrix.
- Test generalization on an independent dataset.
- Deploy the application using a suitable cloud hosting platform.

## 👨‍💻 Author

**Mehdi Ali**

Developed as a computer vision project exploring YOLO-based object detection and interactive deployment with Streamlit.

## ⭐ Acknowledgements

- [Ultralytics YOLO](https://docs.ultralytics.com/)
- [Roboflow](https://roboflow.com/)
- [Streamlit](https://streamlit.io/)

---

If you find this project useful, consider giving the repository a ⭐ on GitHub.
