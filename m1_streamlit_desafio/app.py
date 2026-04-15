import streamlit as st

from pipeline.load_data import load_data
from pipeline.pre_processing import pre_processing
from pipeline.prediction import predict

from utils.formatting import select_class_name
from utils.plot_classes import plot_classes


def main():
    st.title("M1 - Inteligência Artifical I")

    if "prediction" not in st.session_state:
        st.session_state.prediction = None

    if st.session_state.prediction is not None:
        best_prediction, all_predictions = st.session_state.prediction
        st.subheader("Predição")
        st.success(f"Melhor predição: {select_class_name(pred_index=best_prediction)}")
        st.write("Array completo de predições:")
        st.json(all_predictions)
        st.pyplot(plot_classes(all_predictions), clear_figure=True)

        if st.button("Nova predição"):
            st.session_state.prediction = None
            st.rerun()
        return

    df, submitted = load_data()
    if df is None:
        st.info("Preencha as informações para gerar as predições!")
        return

    if submitted:
        pre_processed_df = pre_processing(df)
        try:
            prediction = predict(pre_processed_df)
        except Exception as exc:
            st.error(f"Erro ao gerar predição: {exc}")
            return
        st.session_state.prediction = prediction
        st.rerun()


if __name__ == "__main__":
    main()
