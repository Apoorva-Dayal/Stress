"""This modules contains data about prediction page"""

# Import necessary modules
import streamlit as st

# Import necessary functions from web_functions
from web_functions import predict


def app(df, X, y):
    """This function create the prediction page"""

    # Add title to the page
    st.title("Prediction Page")

    # Add a brief description
    st.markdown(
        """
            <p style="font-size:25px">
                This app uses <b style="color:green">Decision Tree Classifier</b> for the Prediction of Stress Level.
            </p>
        """, unsafe_allow_html=True)
    
    # Take feature input from the user
    # Add a subheader
    st.subheader("Select Values:")

    # Take input of features from the user.
    
    # number_input_A = st.number_input("Response value",0,2639,value=10)
    #A = st.slider("Response", int(df["Response"].min()), int(df["Response"].max()),value=number_input_A)

    number_input_sr = st.number_input("Snoring Rate",45,100,value=45)
    sr = st.slider("Snoring Rate", int(df["sr"].min()), int(df["sr"].max()),value=number_input_sr)
    number_input_rr = st.number_input("Respiration Rate",16,30,value=16)
    rr = st.slider("Respiration Rate", int(df["rr"].min()), int(df["rr"].max()),value=number_input_rr)
    number_input_bt = st.number_input("Body Temperature",85,99,value=85)
    bt = st.slider("Body Temperature (in °F)", int(df["bt"].min()), int(df["bt"].max()),value=number_input_bt)
    number_input_lm = st.number_input("Limb Movement",4.00,19.00,value=4.00)
    lm = st.slider("Limb Movement", float(df["lm"].min()), float(df["lm"].max()),value=number_input_lm)
    number_input_bo = st.number_input("Blood Oxygen",82.00,97.00,value=82.00)
    bo = st.slider("Blood Oxygen(%)", float(df["bo"].min()), float(df["bo"].max()),value=number_input_bo)
    number_input_rem = st.number_input("Rapid Eye Movement ",60.00,105.00,value=60.00)
    rem = st.slider("Rapid Eye Movement", float(df["rem"].min()), float(df["rem"].max()),value=number_input_rem)
    number_input_rem = st.number_input("Sleeping Hour",0.00,90.00,value=0.00)
    sh = st.slider("Sleeping Hour", float(df["sh"].min()), float(df["sh"].max()),number_input_rem)
    number_input_hr = st.number_input("Heart Rate",50.0,85.00,value=50.0)
    hr = st.slider("Heart Rate", float(df["hr"].min()), float(df["hr"].max()),value=number_input_hr)
    

    # Create a list to store all the features
    features = [sr,rr,bt,lm,bo,rem,sh,hr]
    
    st.write("SNORING RATE IS ", sr)
    st.write("RESPIRATION RATE IS ", rr)
    st.write("BODY TEMPERATURE IS ", bt)
    st.write("LIMB MOVEMENT IS ",lm)
    st.write("BLOOD OXYGEN IS ", bo)
    st.write("RAPID EYE MOVEMENT IS ",rem)
    st.write("SLEEPING HOUR IS ",sh)
    st.write("HEART RATE IS ",hr)

    # Create a button to predict
    if st.button("Predict"):
        # Get prediction and model score
        prediction, score = predict(X, y, features)
        st.info("Stress level detected...")

        # Print the output according to the prediction
        if (prediction == 1):
            st.success("The person has low stress level 🙂")
            st.write("Stress score =",str(prediction[0]))
        elif (prediction == 2):
            st.warning("The person has medium stress level 😐")
            st.write("Stress score =",str(prediction[0]))
        elif (prediction == 3):
            st.error("The person has high stress level! 😞")
            st.write("Stress score =",str(prediction[0]))
        elif (prediction == 4):
            st.error("The person has very high stress level!! 😫")
            st.write("Stress score =",str(prediction[0]))
        else:
            st.success("The person is stress free and calm 😄")

        # Print teh score of the model 
        st.write("The model used is trusted by doctor and has an accuracy of ", (score*100),"%")
