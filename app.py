import io
from pathlib import Path

import streamlit as st
from PIL import Image
from ultralytics import YOLO

st.set_page_config(
    page_title="Blood Cell Detection",
    page_icon="🔬",
    layout="wide",
)

st.title("🔬 Blood Cell Detection")
st.write(
    "Upload a microscopy image to detect Platelets, red blood cells (RBC), "
    "and white blood cells (WBC) using your trained YOLO model."
)
st.warning(
    "Research/educational use only. This tool is not a medical diagnostic system "
    "and must not be used to make clinical decisions."
)

MODEL_PATH = Path("best (1).pt")  # Update this to your trained model weights file name


@st.cache_resource
def load_model(model_path: str):
    return YOLO(model_path)


if not MODEL_PATH.exists():
    st.error(
        "Model weights not found. Place your trained best.pt file in the same "
        "folder as app.py, then restart the app."
    )
    st.code("blood_cell_streamlit_app/\n├── app.py\n├── best.pt  # copy this from your training output\n└── requirements.txt")
    st.stop()

model = load_model(str(MODEL_PATH))

with st.sidebar:
    st.header("Detection settings")
    confidence = st.slider(
        "Confidence threshold",
        min_value=0.05,
        max_value=0.95,
        value=0.25,
        step=0.05,
        help="Higher values reduce weaker detections but may miss some cells.",
    )
    iou = st.slider(
        "NMS IoU threshold",
        min_value=0.10,
        max_value=0.90,
        value=0.45,
        step=0.05,
        help="Controls how overlapping boxes are filtered.",
    )
    image_size = st.selectbox("Inference image size", [640, 800, 960], index=0)
    show_labels = st.checkbox("Show class labels", value=True)
    show_confidence = st.checkbox("Show confidence scores", value=True)

uploaded_file = st.file_uploader(
    "Upload a blood-cell image",
    type=["png", "jpg", "jpeg", "bmp", "webp"],
)

if uploaded_file is not None:
    try:
        image = Image.open(uploaded_file).convert("RGB")
    except Exception:
        st.error("Could not read this image. Please upload a valid image file.")
        st.stop()

    left, right = st.columns(2)
    with left:
        st.subheader("Original image")
        st.image(image, use_container_width=True)

    if st.button("Detect blood cells", type="primary", use_container_width=True):
        with st.spinner("Running YOLO detection..."):
            results = model.predict(
                source=image,
                conf=confidence,
                iou=iou,
                imgsz=image_size,
                verbose=False,
            )
            result = results[0]
            annotated_bgr = result.plot(
                labels=show_labels,
                conf=show_confidence,
            )
            # Ultralytics plot() returns a BGR NumPy array.
            import cv2
            annotated_rgb = cv2.cvtColor(annotated_bgr, cv2.COLOR_BGR2RGB)
            annotated_image = Image.fromarray(annotated_rgb)

        with right:
            st.subheader("Detection result")
            st.image(annotated_image, use_container_width=True)

        boxes = result.boxes
        names = result.names
        counts = {}
        rows = []

        if boxes is not None and len(boxes) > 0:
            cls_ids = boxes.cls.cpu().numpy().astype(int)
            confs = boxes.conf.cpu().numpy()
            xyxy = boxes.xyxy.cpu().numpy()

            for cls_id, score, coords in zip(cls_ids, confs, xyxy):
                label = names.get(int(cls_id), str(cls_id))
                counts[label] = counts.get(label, 0) + 1
                rows.append({
                    "Cell class": label,
                    "Confidence": round(float(score), 4),
                    "X1": round(float(coords[0]), 1),
                    "Y1": round(float(coords[1]), 1),
                    "X2": round(float(coords[2]), 1),
                    "Y2": round(float(coords[3]), 1),
                })

        st.subheader("Detection summary")
        total = sum(counts.values())
        metric_cols = st.columns(4)
        metric_cols[0].metric("Total detections", total)
        for idx, label in enumerate(["Platelets", "RBC", "WBC"], start=1):
            metric_cols[idx].metric(label, counts.get(label, 0))

        if rows:
            import pandas as pd
            st.dataframe(pd.DataFrame(rows), use_container_width=True, hide_index=True)
        else:
            st.info("No cells were detected at this confidence threshold. Try lowering it.")

        output = io.BytesIO()
        annotated_image.save(output, format="PNG")
        st.download_button(
            "Download annotated image",
            data=output.getvalue(),
            file_name="blood_cell_detections.png",
            mime="image/png",
            use_container_width=True,
        )
else:
    st.info("Choose an image above to get started.")
