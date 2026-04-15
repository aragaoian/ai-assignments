import streamlit as st
import pandas as pd
from typing import Optional


def load_data() -> tuple[Optional[pd.DataFrame], bool]:
    with st.form("input_form"):
        area = st.number_input("Area", min_value=0, step=1, value=0)
        perimeter = st.number_input("Perimeter", value=0.0)
        major_axis_length = st.number_input("MajorAxisLength", value=0.0)
        minor_axis_length = st.number_input("MinorAxisLength", value=0.0)
        aspect_ratio = st.number_input("AspectRatio", value=0.0)
        eccentricity = st.number_input("Eccentricity", value=0.0)
        convex_area = st.number_input("ConvexArea", min_value=0, value=0)
        equiv_diameter = st.number_input("EquivDiameter", value=0.0)
        extent = st.number_input("Extent", value=0.0)
        solidity = st.number_input("Solidity", value=0.0)
        roundness = st.number_input("Roundness", value=0.0)
        compactness = st.number_input("Compactness", value=0.0)
        shape_factor1 = st.number_input("ShapeFactor1", value=0.0)
        shape_factor2 = st.number_input("ShapeFactor2", value=0.0)
        shape_factor3 = st.number_input("ShapeFactor3", value=0.0)
        shape_factor4 = st.number_input("ShapeFactor4", value=0.0)

        submitted = st.form_submit_button("Gerar predição", type="primary")

    if not submitted:
        return None, submitted

    data = [
        {
            "Area": int(area),
            "Perimeter": float(perimeter),
            "MajorAxisLength": float(major_axis_length),
            "MinorAxisLength": float(minor_axis_length),
            "AspectRatio": float(aspect_ratio),
            "Eccentricity": float(eccentricity),
            "ConvexArea": int(convex_area),
            "EquivDiameter": float(equiv_diameter),
            "Extent": float(extent),
            "Solidity": float(solidity),
            "Roundness": float(roundness),
            "Compactness": float(compactness),
            "ShapeFactor1": float(shape_factor1),
            "ShapeFactor2": float(shape_factor2),
            "ShapeFactor3": float(shape_factor3),
            "ShapeFactor4": float(shape_factor4),
        }
    ]

    return pd.DataFrame(data), submitted
