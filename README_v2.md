# Dataset: BDD100K

This project uses (or is intended to use) sample driving footage from **BDD100K**
(Berkeley DeepDrive 100K), a large-scale, diverse driving video dataset released by
UC Berkeley's DeepDrive research group. It's a common source for traffic scene
perception tasks like object detection, tracking, lane detection, and drivable-area
segmentation.

## Key facts

- **Videos:** 100,000 driving clips, ~40 seconds each, 720p at 30fps
- **Diversity:** collected across multiple US cities, times of day, and weather
  conditions (clear, overcast, rainy, snowy, foggy), covering both highway and
  city street driving
- **Annotations available:** image tagging, bounding-box object detection,
  instance segmentation, lane markings, drivable area, multi-object tracking,
  multi-object tracking & segmentation, and pose estimation
- **Detection classes** (relevant to this repo's `KEEP_CLASSES` in `src/config.py`):
  car, bus, truck, person, rider, bike, motor, train, traffic light, traffic sign
  - Note: BDD100K uses `bike`/`motor`, while this repo's config uses
    `bicycle`/`motorcycle` — worth reconciling class names if you map BDD100K
    labels directly into this pipeline.

## Links

- Official site / download portal: https://www.bdd100k.com/
- GitHub toolkit (devkit, label format, evaluation scripts): https://github.com/bdd100k/bdd100k
- Paper: *BDD100K: A Diverse Driving Dataset for Heterogeneous Multitask Learning* (CVPR 2020)
  https://arxiv.org/abs/1805.04687

## Usage notes for this repo

- Sample clips for local testing should go in `data/sample_videos/` (currently empty).
- BDD100K is released for **non-commercial research and educational use only** —
  check the license terms on the official site before any other use.
- When citing BDD100K in reports or papers, cite the CVPR 2020 paper above.

## Citation

```bibtex
@InProceedings{bdd100k,
    author = {Yu, Fisher and Chen, Haofeng and Wang, Xin and Xian, Wenqi and Chen, Yingying and Liu, Fangchen and Madhavan, Vashisht and Darrell, Trevor},
    title = {BDD100K: A Diverse Driving Dataset for Heterogeneous Multitask Learning},
    booktitle = {Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},
    year = {2020}
}
```
