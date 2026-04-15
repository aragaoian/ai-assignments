import joblib
from pandas import DataFrame

LABEL_ENCODER = joblib.load("models\label_encoder.joblib")
STD_SCALER = joblib.load("models\std_scaler.joblib")


def pre_processing(data: DataFrame) -> DataFrame:
    df = data.copy()

    if "Class" in df.columns:
        df["Class"] = LABEL_ENCODER.transform(df["Class"])

    numeric_cols = df.select_dtypes(include=["number"]).columns.tolist()
    if "Class" in numeric_cols:
        numeric_cols.remove("Class")

    df[numeric_cols] = STD_SCALER.transform(df[numeric_cols])

    return df
