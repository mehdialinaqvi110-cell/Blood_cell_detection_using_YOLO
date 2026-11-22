# Blood Cell Detection — Streamlit

A simple web app for running your trained YOLO11 blood-cell detector on uploaded microscopy images.

## 1. Add your trained weights

Your notebook's training output reports these files:

- `/content/runs/detect/train/weights/best.pt` — recommended checkpoint
- `/content/runs/detect/train/weights/last.pt` — final epoch checkpoint

In Google Colab, download `best.pt` from the Files panel, or run:

```python
from google.colab import files
files.download("/content/runs/detect/train/weights/best.pt")
```

Copy `best.pt` into this project folder beside `app.py`. The weights file is not included in this starter ZIP because it was not attached with the notebook.

## 2. Run locally on Windows

Open PowerShell in this folder and run:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
streamlit run app.py
```

If PowerShell blocks activation, use:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m streamlit run app.py
```

The browser should open the app, usually at `http://localhost:8501`.

## 3. Deploy to Streamlit Community Cloud

1. Create a GitHub repository for this project.
2. Upload `app.py`, `requirements.txt`, and `best.pt`.
3. Open https://share.streamlit.io/ and create an app from that repository.
4. Choose `app.py` as the main file and deploy.

**Important:** model weights may be several MB and can make a repository large. Do not commit API keys or other secrets. If your weights are too large for GitHub, use an appropriate model-artifact host and download them securely at startup.

## 4. Model improvement plan

The notebook reports validation metrics for YOLO11n after 100 epochs: Precision 0.839, Recall 0.928, mAP50 0.929, and mAP50-95 0.658 on 73 validation images / 967 instances.

Before changing the model, establish a held-out test baseline. Then compare one change at a time:

- Inspect confusion matrix, PR curves, and per-class metrics.
- Try image sizes 640 vs 800/960.
- Compare YOLO11n with YOLO11s if GPU memory allows.
- Test confidence/IoU thresholds on validation data.
- Check annotations and add diverse, correctly labelled training data.
- Keep the test set untouched until final comparison.

Higher image size or a larger model can improve results but may increase latency and memory use. Verify gains empirically.

## Intended use

This app is for education and research demonstrations only. It is not a validated medical device and must not be used to diagnose patients or guide treatment.
