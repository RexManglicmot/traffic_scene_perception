from pathlib import Path

# This IS very important, as it will set the root to the directoruy
PROJECT_ROOT = Path(__file__).resolve().parents[1]


INPUT_VIDEO = PROJECT_ROOT / "data" / "sample_videos" / "sample.mp4"

OUTPUT_VIDEO = PROJECT_ROOT / "outputs" / "videos" / "annotated_output.mp4"
TRACKING_CSV = PROJECT_ROOT / "outputs" / "csv" / "tracking_results.csv"

PLOTS_DIR = PROJECT_ROOT / "outputs" / "plots"
METRICS_DIR = PROJECT_ROOT / "outputs" / "metrics"

YOLO_WEIGHTS = "yolov8n.pt"
TRACKER = "bytetrack.yaml"

CONFIDENCE_THRESHOLD = 0.35
IOU_THRESHOLD = 0.5
FRAME_STRIDE = 1

# Classificaiton of the classes in tee videos
# Best to put into a set 
KEEP_CLASSES = {
    "car",
    "truck",
    "bus",
    "motorcycle",
    "bicycle",
    "person",
}