import streamlit as st
import pandas as pd
import joblib

st.title("🌱 Dry Bean Classification")

st.image("./img/beans.jpg")

st.header("Enter the Features of the Bean")

Area = st.number_input("Area", min_value=0, step=1, value=31000)

Perimeter = st.number_input("Perimeter", min_value=0.0, step=0.01, value=640.0, format="%.2f")
MajorAxisLength = st.number_input("Major Axis Length", min_value=0.0, step=0.01, value=215.0, format="%.2f")
MinorAxisLength = st.number_input("Minor Axis Length", min_value=0.0, step=0.01, value=185.0, format="%.2f")

AspectRation = st.slider("Aspect Ratio", min_value=0.5, max_value=2.0, step=0.01, value=1.15)
Eccentricity = st.slider("Eccentricity", min_value=0.0, max_value=1.0, step=0.001, value=0.52)

ConvexArea = st.number_input("Convex Area", min_value=0, step=1, value=31500)

EquivDiameter = st.number_input("Equivalent Diameter", min_value=0.0, step=0.01, value=199.0, format="%.2f")

Extent = st.slider("Extent", min_value=0.0, max_value=1.0, step=0.001, value=0.77)
Solidity = st.slider("Solidity", min_value=0.0, max_value=1.0, step=0.001, value=0.99)

roundness = st.slider("Roundness", min_value=0.0, max_value=1.0, step=0.01, value=0.94)
Compactness = st.slider("Compactness", min_value=0.0, max_value=1.0, step=0.01, value=0.93)

ShapeFactor1 = st.number_input("Shape Factor 1", min_value=0.0, max_value=0.02, step=0.0001, value=0.0069, format="%.4f")
ShapeFactor2 = st.number_input(
    "Shape Factor 2", min_value=0.0, max_value=0.02, step=0.0001, value=0.0031, format="%.4f"
)
ShapeFactor3 = st.number_input(
    "Shape Factor 3", min_value=0.0, max_value=1.0, step=0.001, value=0.85, format="%.4f"
)
ShapeFactor4 = st.number_input(
    "Shape Factor 4", min_value=0.0, max_value=1.0, step=0.001, value=0.998, format="%.4f"
)




classes = ['BARBUNYA', 'BOMBAY', 'CALI', 'DERMASON', 'HOROZ', 'SEKER', 'SIRA']

if st.button("Predict"):
    if Area == 0 or Perimeter == 0 or MajorAxisLength == 0:
        st.error("⚠️ Please enter valid values for Area, Perimeter, and Major Axis Length.")
    else:
        input_df = pd.DataFrame([{
            "Area": Area,
            "Perimeter": Perimeter,
            "MajorAxisLength": MajorAxisLength,
            "MinorAxisLength": MinorAxisLength,
            "AspectRation": AspectRation,    # spelling must match model
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
            model = joblib.load('./models/gradient.pkl')
        except Exception as e:
            st.error(f"❌ Error loading model: {e}")
            st.stop()

        try:
            prediction = model.predict(input_df)
            predicted_index = int(prediction[0])
            if 0 <= predicted_index < len(classes):
                predicted_class = classes[predicted_index]
            else:
                predicted_class = "Unknown Class"

            st.subheader("✅ Prediction Result")
            st.success(f"The predicted bean class is: **{predicted_class}**")

            st.write("Possible Classes:")
            for c in classes:
                if c == predicted_class:
                    st.markdown(f"**✔️ {c}**")
                else:
                    st.markdown(c)

        except Exception as e:
            st.error(f"❌ Prediction failed: {e}")
