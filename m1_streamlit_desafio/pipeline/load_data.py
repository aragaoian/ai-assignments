import streamlit as st
import pandas as pd
from typing import Optional

"""
Teste 1: [-0.70315815 -0.30124226  0.98601743  0.79845092  0.59514195  0.46244996] -> 3
Teste 2: [ 3.27109924 -0.30646981  0.99554703  0.59159227  1.24436026  0.69351375] -> 1
Teste 124: [-0.56394453 -0.60279208 -0.39234684  1.0237481   0.79797278  0.88306394] -> 5
"""


def load_data() -> tuple[Optional[pd.DataFrame], bool]:
    """Usar somente os features selecionados na EDA"""
    with st.form("input_form"):
        area = st.number_input("Area", value=-0.70315815)
        eccentricity = st.number_input("Eccentricity", value=-0.30124226)
        extent = st.number_input("Extent", value=0.98601743)
        solidity = st.number_input("Solidity", value=0.79845092)
        roundness = st.number_input("Roundness", value=0.59514195)
        shape_factor4 = st.number_input("ShapeFactor4", value=0.46244996)

        submitted = st.form_submit_button("Gerar predição", type="primary")

    if not submitted:
        return None, submitted

    data = [
        {
            "Area": int(area),
            "Eccentricity": float(eccentricity),
            "Extent": float(extent),
            "Roundness": float(roundness),
            "Solidity": float(solidity),
            "ShapeFactor4": float(shape_factor4),
        }
    ]

    return pd.DataFrame(data), submitted
