# Handwritten Mathematical Expression Generation and Style Analysis

A compact project wrapper around the official HMEG graph-to-image pipeline for handwritten mathematical expression generation.

The project does four things:

1. Downloads the official HMEG repository and released assets.
2. Runs HMEG inference on CROHME `.lg` symbolic graph files.
3. Filters and curates showable generated outputs.
4. Produces contact sheets and export folders for presentation.

## Quick start

```bash
cd hmeg_project
./scripts/run_inference.sh smoke
```

For a larger result set:

```bash
./scripts/run_inference.sh generate --max-candidates 1500
```

For preparation, inference, generation, and curation:

```bash
./scripts/run_inference.sh all --max-candidates 1500
```

## Outputs

```text
artifacts/smoke/hmeg_test.png
artifacts/generated/hmeg_readable_selected/
artifacts/generated/hmeg_readable_contact_sheet.png
artifacts/final/hmeg_final_best/
artifacts/final/hmeg_final_showable/
artifacts/final/hmeg_not_showable/
```

## Colab

Use:

```text
notebooks/hmeg_colab_reproduction.ipynb
```

The notebook downloads everything, runs HMEG, generates readable candidates, filters showable samples, builds contact sheets, and exports a zip.

## Framing

This is a reproduction and evaluation project for HMEG-style handwritten mathematical expression generation from symbolic graph inputs. It is not a polished arbitrary LaTeX-to-handwriting product.
