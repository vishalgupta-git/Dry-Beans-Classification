import streamlit as st
import pandas as pd
import joblib

st.title("Shape Feature Prediction")

st.header("Enter Feature Values")

# Input fields
Area = st.number_input("Area", step=1.0)
Perimeter = st.number_input("Perimeter")
MajorAxisLength = st.number_input("Major Axis Length")
MinorAxisLength = st.number_input("Minor Axis Length")
AspectRation = st.number_input("Aspect Ratio")
Eccentricity = st.number_input("Eccentricity")
ConvexArea = st.number_input("Convex Area", step=1.0)
EquivDiameter = st.number_input("Equivalent Diameter")
Extent = st.number_input("Extent")
Solidity = st.number_input("Solidity")
roundness = st.number_input("Roundness")
Compactness = st.number_input("Compactness")
ShapeFactor1 = st.number_input("Shape Factor 1")
ShapeFactor2 = st.number_input("Shape Factor 2")
ShapeFactor3 = st.number_input("Shape Factor 3")
ShapeFactor4 = st.number_input("Shape Factor 4")

# Submit button
if st.button("Predict"):
    input_df = pd.DataFrame([{
        "Area": Area,
        "Perimeter": Perimeter,
        "MajorAxisLength": MajorAxisLength,
        "MinorAxisLength": MinorAxisLength,
        "AspectRation": AspectRation,
        "Eccentricity": Eccentricity,
        "ConvexArea": ConvexArea,
        "EquivDiameter": EquivDiameter,
        "Extent": Extent,
        "Solidity": Solidity,
        "roundness": roundness,
        "Compactness": Compactness,
        "ShapeFactor1": ShapeFactor1,
        "ShapeFactor2": ShapeFactor2,
        "ShapeFactor3": ShapeFactor3,
        "ShapeFactor4": ShapeFactor4,
    }])

    try:
        model = joblib.load("model.pkl")
    except Exception as e:
        st.error(f"Error loading model: {e}")
        st.stop()

    try:
        prediction = model.predict(input_df)
        st.subheader("Prediction Result")
        st.success(f"Predicted Class: {prediction[0]}")
    except Exception as e:
        st.error(f"Prediction failed: {e}")
