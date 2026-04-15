from pathlib import Path
import numpy as np
from pandas import DataFrame

MODEL = None

"""
Erro ao gerar predição: Exception encountered when calling Sequential.call().

[1mInput 0 with name 'None' of layer 'dense_105' is incompatible with the layer: expected axis -1 of input shape to have value 6, but received input with shape (1, 16)[0m

Arguments received by Sequential.call(): • inputs=tf.Tensor(shape=(1, 16), dtype=float32) • training=False • mask=None • kwargs=<class 'inspect._empty'>
"""


def _load_keras_model():
    global MODEL
    if MODEL is not None:
        return MODEL

    try:
        from tensorflow.keras.models import load_model
    except Exception:
        try:
            from keras.models import load_model
        except Exception as exc:
            raise RuntimeError(
                "Keras/TensorFlow is required to load models/best_model.keras. "
                "Install a compatible backend and try again."
            ) from exc

    model_path = Path(__file__).resolve().parents[1] / "models" / "best_model.keras"
    MODEL = load_model(model_path)
    return MODEL


def predict(data: DataFrame) -> tuple[int | float | None, list]:
    model = _load_keras_model()
    res = model.predict(data, verbose=0)
    arr = np.asarray(res)
    if arr.size == 0:
        return None, []

    all_predictions = arr.tolist()

    if arr.ndim == 2 and arr.shape[1] > 1:
        best_prediction = int(arr[0].argmax())
        return best_prediction, all_predictions

    value = float(arr.ravel()[0])
    if 0.0 <= value <= 1.0:
        best_prediction = int(value >= 0.5)
        return best_prediction, all_predictions

    return value, all_predictions
