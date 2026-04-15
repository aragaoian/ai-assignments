from __future__ import annotations

import numpy as np
import matplotlib.pyplot as plt

from utils.formatting import CLASS_MAP


def _to_percentages(all_predictions: list) -> tuple[list[str], np.ndarray]:
    values = np.asarray(all_predictions, dtype=float)

    if values.size == 0:
        return [], np.asarray([])

    if values.ndim > 1:
        values = values[0]

    if values.size == 1 and len(CLASS_MAP) == 2:
        values = np.asarray([1.0 - values.item(), values.item()], dtype=float)

    class_indices = list(CLASS_MAP.keys())
    class_names = [CLASS_MAP[index] for index in class_indices[: values.size]]
    values = values[: len(class_names)]

    total = float(values.sum())
    if total > 0:
        values = values / total * 100.0

    return class_names, values


def plot_classes(all_predictions: list) -> plt.Figure:
    class_names, percentages = _to_percentages(all_predictions)

    figure, axis = plt.subplots(figsize=(10, 5))

    if len(class_names) == 0:
        axis.text(0.5, 0.5, "Sem dados para plotar", ha="center", va="center")
        axis.axis("off")
        return figure

    bars = axis.bar(class_names, percentages, color="#3B82F6")
    axis.set_title("Percentual por classe predita")
    axis.set_ylabel("Percentual (%)")
    axis.set_ylim(0, max(100.0, float(percentages.max()) * 1.15))
    axis.tick_params(axis="x", rotation=30)

    for bar, percentage in zip(bars, percentages):
        axis.annotate(
            f"{percentage:.1f}%",
            xy=(bar.get_x() + bar.get_width() / 2, bar.get_height()),
            xytext=(0, 3),
            textcoords="offset points",
            ha="center",
            va="bottom",
        )

    figure.tight_layout()
    return figure
