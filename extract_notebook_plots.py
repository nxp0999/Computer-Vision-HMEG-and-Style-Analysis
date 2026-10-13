"""Extract all plot images from the style similarity notebook outputs."""
import json
import base64
from pathlib import Path

NOTEBOOK = Path(__file__).parent / "hmeg_authenticity_style_similarity_project (1).ipynb"
OUT_DIR = Path(__file__).parent / "slides_figures"
OUT_DIR.mkdir(exist_ok=True)

with open(NOTEBOOK, "r", encoding="utf-8") as f:
    nb = json.load(f)

# Map execution_count -> human-readable label for the plots we want
CELL_LABELS = {
    16: [
        "16a_sample_image_grid",
        "16b_handcrafted_feature_distributions",
    ],
    18: [
        "18a_tsne_writer_style_embedding",
        "18b_pca_cumulative_variance",
    ],
    19: [
        "19a_kmeans_cluster_scatter",
        "19b_writer_cluster_heatmap",
    ],
    20: [
        "20a_pairwise_similarity_matrix",
        "20b_retrieval_writer_00",
        "20c_retrieval_writer_01",
        "20d_retrieval_writer_02",
        "20e_retrieval_writer_03",
        "20f_retrieval_writer_04",
    ],
    21: [
        "21a_roc_curve",
        "21b_confusion_matrix",
        "21c_authenticity_score_distribution",
    ],
    22: [
        "22a_same_writer_example",
        "22b_different_writer_example",
    ],
    23: [
        "23a_compare_two_images",
    ],
}

saved = []
for cell in nb.get("cells", []):
    if cell.get("cell_type") != "code":
        continue
    ec = cell.get("execution_count")
    if ec not in CELL_LABELS:
        continue
    labels = CELL_LABELS[ec]
    plot_idx = 0
    for output in cell.get("outputs", []):
        data = output.get("data", {})
        img_b64 = data.get("image/png", "")
        if not img_b64:
            continue
        if plot_idx >= len(labels):
            break
        label = labels[plot_idx]
        plot_idx += 1
        # image/png may be a list of strings or a single string
        if isinstance(img_b64, list):
            img_b64 = "".join(img_b64)
        img_bytes = base64.b64decode(img_b64)
        out_path = OUT_DIR / f"{label}.png"
        out_path.write_bytes(img_bytes)
        saved.append(str(out_path))
        print(f"Saved: {out_path.name}")

print(f"\nDone — {len(saved)} images saved to: {OUT_DIR}")
