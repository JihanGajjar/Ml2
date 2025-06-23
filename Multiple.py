import pickle
import streamlit as st
from streamlit_option_menu import option_menu

diabetes_model=pickle.load(open("diabetes_model.sav",'rb'))

#heart_model=pickle.load(open('Hear_model','rb'))

#parkinsons_model=pickle.load(open('parkinson_model','rb'))

with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction System',
                           
                           ['Diabetes Prediction',
                            'Heart Diseases Prediction',
                            'Parkinsons Prediction'],
                           icons=['activity','heart','person'],
                           default_index=0)
def diabetes_prediction(input_data):
    #input_data = (5,166,72,19,175,25.8,0.587,51)

    input_data_as_array = np.asarray(input_data)
    input_data_reshaped = input_data_as_array.reshape(1, -1)
    prediction = diabetes_model(input_data_reshaped)
    print(prediction)
    if(prediction[0] == 1):
        return "have diabetes"
    else:
       return "not have diabetes"

    
if selected == 'Diabetes Prediction':

    st.title("daibetes predition")
    Pregnancies = st.text_input('Number of Pregnancies')
    Glucose  = st.text_input('Glucose Level')
    BloodPressure = st.text_input('Blood pressure value')
    SkinThickness = st.text_input('skin thickness')
    Insulin = st.text_input("inslulin value")
    BMI = st.text_input('BMI value')
    DiabetesPedigreeFunction = st.text_input('diabetes pedigree Function value')
    Age = st.text_input('Age of the person')
    diagnosis=''
    if st.button('Diabetes Test Result'):
	
        diagnosis = diabetes_prediction([float(Pregnancies),float(Glucose),float(BloodPressure),float(SkinThickness),float(Insulin),float(BMI),float(DiabetesPedigreeFunction),float(Age)])
    st.success(diagnosis)
