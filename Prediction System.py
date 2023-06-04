import pickle
import streamlit as st
import numpy as np


# Load the saved model
prediction_model = pickle.load(open('C:/Users/Lenovo/Desktop/Mental Health Prediction System/prediction_model.pkl','rb'))


def treatment_prediction(input_data):
    

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = prediction_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
      return 'The person do not need Treatment'
    else:
      return 'The person need Treatment'   
  
st.set_page_config(page_title="Mental Health Prediction System", page_icon=":brain:", layout="centered")

# Set up the app
with st.sidebar:
    st.title("Mental Health Prediction System")
    st.subheader("Check if you need Mental Treatment or not:")
    
st.title("Treatment Prediction")
st.write("Enter the following details to check the need for treatment:")




  
def main():
    
    Age = st.slider("Age of the Person:", 18, 100,20, 1)
    Gender = st.selectbox("Gender of the person",["1","0"])
    self_employed = st.selectbox("Are you currently employed?",["1","0"])
    family_history = st.selectbox("Any history of mental illness in your family:", ["1", "0"])
    work_interfere = st.selectbox("Do you feel that your mental condition interferes with your work?", ["0", "2", "3", "1"])
    remote_work = st.selectbox("Do you occasionally work from home?", ["0", "1"])
    tech_company = st.selectbox("Do you work in a tech company?", ["0", "1"])
    benefits = st.selectbox("Do you ever think about mental health benefits?", ["0", "1", "2"])
    care_options = st.selectbox("Do you suspect any options for mental health care?", ["0", "1", "2"])
    wellness_program = st.selectbox("Have you recently brought up mental health as an aspect of a wellness plan?", ["0", "1", "2"])
    seek_help = st.selectbox("Do you ever ask for guidance with your mental health?",["0", "1", "2"])
    leave = st.selectbox("How easy is it for you to take time off work for mental health reasons?", ["1", "3", "2", "4", "0"])
    mental_health_consequence = st.selectbox("Do you believe talking about a mental health condition would be destructive?", ["0", "1", "2"])
    phys_health_consequence = st.selectbox("Do you believe talking about a physical health condition would be destructive?", ["0", "1", "2"])
    supervisor = st.selectbox("Have you ever thought about the need for a mental health supervisor?", ["0", "1", "2"])
    mental_health_interview = st.selectbox("Have you ever felt anxious or stressed in an interview?", ["0", "1", "2"])
    phys_health_interview = st.selectbox("Would you bring up a physical health issue in an interview?", ["0", "1", "2"])
    mental_vs_physical = st.selectbox("Do you consider mental health to be just as important as physical health?", ["0", "1", "2"])
    obs_consequence = st.selectbox("Have you seen any negative effects that mental illness has on you?", ["0", "1"])


    mental_health = ''
    
    # creating a button for Prediction
    
    if st.button('Test Result'):
        mental_health = treatment_prediction([Age,Gender,self_employed,family_history,work_interfere,remote_work,tech_company,benefits,care_options,wellness_program,seek_help,leave,mental_health_consequence,phys_health_consequence,supervisor,mental_health_interview,phys_health_interview,mental_vs_physical,obs_consequence])
        
        
    st.success(mental_health)
    
    
    
    
    
if __name__ == '__main__':
    main()


# Define the input fields


