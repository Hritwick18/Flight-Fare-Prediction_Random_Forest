import streamlit as st 
from PIL import Image
import pickle
import numpy as np
import pandas as pd
import time
st.set_option('deprecation.showfileUploaderEncoding', False)
# Load the pickled model
model = pickle.load(open('flight.pkl'))

def predict_price(Total_Stops, Jounary_day, Jounary_Month, Deep_hour, Deep_min,
       Arival_hour, Arival_min,Duration_hour, Duration_min,
       Airline_AirIndia, Airline_GoAir, Airline_IndiGo,
       Airline_JetAirways, Airline_JetAirwaysBusiness,
       Airline_Multiplecarriers,
       Airline_MultiplecarriersPremiumeconomy, Airline_SpiceJet,
       Airline_Trujet, Airline_Vistara, Airline_VistaraPremiumeconomy,
       Destination_Cochin, Destination_Delhi, Destination_Hyderabad,
       Destination_Kolkata, Destination_NewDelhi, Source_Chennai,
       Source_Delhi, Source_Kolkata, Source_Mumbai):
  input = np.array([[Total_Stops, Jounary_day, Jounary_Month, Deep_hour, Deep_min,
       Arival_hour, Arival_min,Duration_hour, Duration_min,
       Airline_AirIndia, Airline_GoAir, Airline_IndiGo,
       Airline_JetAirways, Airline_JetAirwaysBusiness,
       Airline_Multiplecarriers,
       Airline_MultiplecarriersPremiumeconomy, Airline_SpiceJet,
       Airline_Trujet, Airline_Vistara, Airline_VistaraPremiumeconomy,
       Destination_Cochin, Destination_Delhi, Destination_Hyderabad,
       Destination_Kolkata, Destination_NewDelhi, Source_Chennai,
       Source_Delhi, Source_Kolkata, Source_Mumbai]]).astype(np.float64)
  prediction = model.predict(input)
  return float(prediction)

def main():
  st.title("50_Startups")
  html_temp ="""
  <div style="background-color:black; padding:10px">
  <h2 style="color:white;text-align:center;">50_Startups</h2>
  </div>
  """
  st.markdown(html_temp,unsafe_allow_html=True)
  Total_Stops = st.text_input("Total Stops")

  Jounary_Day = st.date_input('Jounary_Day')
  Jounary_day = pd.to_datetime(Jounary_Day,format="%Y-%m-%d").day
  Jounary_Month = pd.to_datetime(Jounary_Day,format="%Y-%m-%d").month

  Depature = st.time_input('Depature Time')
  Deep_hour = int(pd.to_datetime(Depature, format ="%H:%M:%S").hour)
  Deep_min = int(pd.to_datetime(Depature, format ="%H:%M:%S").minute)

  Arival = st.time_input('Arival Time')
  Arival_hour = int(pd.to_datetime(Arival, format ="%H:%M:%S").hour)
  Arival_min = int(pd.to_datetime(Arival, format ="%H:%M:%S").minute)

  Duration_hour = abs(Arival_hour-Deep_hour)
  Duration_min = abs(Arival_min-Deep_min)


  airline = st.selectbox('Select Airlines name:',('IndiGo', 'Air India', 'Jet Airways', 'SpiceJet','Multiple carriers', 'GoAir', 'Vistara', 'Air Asia','Vistara Premium economy', 'Jet Airways Business', 'Multiple carriers Premium economy', 'Trujet'))
 
  if (airline=='Jet Airways'):
     Airline_AirIndia = 0
     Airline_GoAir = 0
     Airline_IndiGo = 0
     Airline_JetAirways = 1
     Airline_JetAirwaysBusiness = 0
     Airline_Multiplecarriers = 0
     Airline_MultiplecarriersPremiumeconomy = 0
     Airline_SpiceJet = 0
     Airline_Trujet = 0
     Airline_Vistara = 0
     Airline_VistaraPremiumeconomy = 0
            

  elif (airline=='IndiGo'):
    Airline_AirIndia = 0
    Airline_GoAir = 0
    Airline_IndiGo = 1
    Airline_JetAirways = 0
    Airline_JetAirwaysBusiness = 0
    Airline_Multiplecarriers = 0
    Airline_MultiplecarriersPremiumeconomy = 0
    Airline_SpiceJet = 0
    Airline_Trujet = 0
    Airline_Vistara = 0
    Airline_VistaraPremiumeconomy = 0

            
  elif (airline=='Air India'):
   Airline_AirIndia = 1
   Airline_GoAir = 0
   Airline_IndiGo = 0
   Airline_JetAirways = 0
   Airline_JetAirwaysBusiness = 0
   Airline_Multiplecarriers = 0
   Airline_MultiplecarriersPremiumeconomy = 0
   Airline_SpiceJet = 0
   Airline_Trujet = 0
   Airline_Vistara = 0
   Airline_VistaraPremiumeconomy = 0
            

  elif (airline=='Multiple carriers'):
    Airline_AirIndia = 0
    Airline_GoAir = 0
    Airline_IndiGo = 0
    Airline_JetAirways = 0
    Airline_JetAirwaysBusiness = 0
    Airline_Multiplecarriers = 1
    Airline_MultiplecarriersPremiumeconomy = 0
    Airline_SpiceJet = 0
    Airline_Trujet = 0
    Airline_Vistara = 0
    Airline_VistaraPremiumeconomy = 0
            

  elif (airline=='SpiceJet'):
    Airline_AirIndia = 0
    Airline_GoAir = 0
    Airline_IndiGo = 0
    Airline_JetAirways = 0
    Airline_JetAirwaysBusiness = 0
    Airline_Multiplecarriers = 0
    Airline_MultiplecarriersPremiumeconomy = 0
    Airline_SpiceJet = 1
    Airline_Trujet = 0
    Airline_Vistara = 0
    Airline_VistaraPremiumeconomy = 0
                        
  elif (airline=='Vistara'):
    Airline_AirIndia = 0
    Airline_GoAir = 0
    Airline_IndiGo = 0
    Airline_JetAirways = 0
    Airline_JetAirwaysBusiness = 0
    Airline_Multiplecarriers = 0
    Airline_MultiplecarriersPremiumeconomy = 0
    Airline_SpiceJet = 0
    Airline_Trujet = 0
    Airline_Vistara = 1
    Airline_VistaraPremiumeconomy = 0

  elif (airline=='GoAir'):
    Airline_AirIndia = 0
    Airline_GoAir = 1
    Airline_IndiGo = 0
    Airline_JetAirways = 0
    Airline_JetAirwaysBusiness = 0
    Airline_Multiplecarriers = 0
    Airline_MultiplecarriersPremiumeconomy = 0
    Airline_SpiceJet = 0
    Airline_Trujet = 0
    Airline_Vistara = 0
    Airline_VistaraPremiumeconomy = 0

  elif (airline=='Multiple carriers Premium economy'):
    Airline_AirIndia = 0
    Airline_GoAir = 0
    Airline_IndiGo = 0
    Airline_JetAirways = 0
    Airline_JetAirwaysBusiness = 0
    Airline_Multiplecarriers = 0
    Airline_MultiplecarriersPremiumeconomy = 1
    Airline_SpiceJet = 0
    Airline_Trujet = 0
    Airline_Vistara = 0
    Airline_VistaraPremiumeconomy = 0

  elif (airline=='Jet Airways Business'):
    Airline_AirIndia = 0
    Airline_GoAir = 0
    Airline_IndiGo = 0
    Airline_JetAirways = 0
    Airline_JetAirwaysBusiness = 1
    Airline_Multiplecarriers = 0
    Airline_MultiplecarriersPremiumeconomy = 0
    Airline_SpiceJet = 0
    Airline_Trujet = 0
    Airline_Vistara = 0
    Airline_VistaraPremiumeconomy = 0

  elif (airline=='Vistara Premium economy'):
    Airline_AirIndia = 0
    Airline_GoAir = 0
    Airline_IndiGo = 0
    Airline_JetAirways = 0
    Airline_JetAirwaysBusiness = 0
    Airline_Multiplecarriers = 0
    Airline_MultiplecarriersPremiumeconomy = 0
    Airline_SpiceJet = 0
    Airline_Trujet = 0
    Airline_Vistara = 0
    Airline_VistaraPremiumeconomy = 1

  elif (airline=='Trujet'):
    Airline_AirIndia = 0
    Airline_GoAir = 0
    Airline_IndiGo = 0
    Airline_JetAirways = 0
    Airline_JetAirwaysBusiness = 0
    Airline_Multiplecarriers = 0
    Airline_MultiplecarriersPremiumeconomy = 0
    Airline_SpiceJet = 0
    Airline_Trujet = 1
    Airline_Vistara = 0
    Airline_VistaraPremiumeconomy = 0

  else:
    Airline_AirIndia = 0
    Airline_GoAir = 0
    Airline_IndiGo = 0
    Airline_JetAirways = 0
    Airline_JetAirwaysBusiness = 0
    Airline_Multiplecarriers = 0
    Airline_MultiplecarriersPremiumeconomy = 0
    Airline_SpiceJet = 0
    Airline_Trujet = 0
    Airline_Vistara = 0
    Airline_VistaraPremiumeconomy = 0

  Destination = st.selectbox('Select Destination name:',('New Delhi', 'Banglore', 'Cochin', 'Kolkata', 'Delhi', 'Hyderabad'))
  if (Destination == 'Cochin'):
    Destination_Cochin = 1
    Destination_Delhi = 0
    Destination_NewDelhi = 0
    Destination_Hyderabad = 0
    Destination_Kolkata = 0
            
        
  elif (Destination == 'Delhi'):
    Destination_Cochin = 0
    Destination_Delhi = 1
    Destination_NewDelhi = 0
    Destination_Hyderabad = 0
    Destination_Kolkata = 0

  elif (Destination == 'New_Delhi'):
    Destination_Cochin = 0
    Destination_Delhi = 0
    Destination_NewDelhi = 1
    Destination_Hyderabad = 0
    Destination_Kolkata = 0

  elif (Destination == 'Hyderabad'):
    Destination_Cochin = 0
    Destination_Delhi = 0
    Destination_NewDelhi = 0
    Destination_Hyderabad = 1
    Destination_Kolkata = 0

  elif (Destination == 'Kolkata'):
    Destination_Cochin = 0
    Destination_Delhi = 0
    Destination_NewDelhi = 0
    Destination_Hyderabad = 0
    Destination_Kolkata = 1

  else:
    Destination_Cochin = 0
    Destination_Delhi = 0
    Destination_NewDelhi = 0
    Destination_Hyderabad = 0
    Destination_Kolkata = 0  
  Source = st.selectbox('Select Source name:',('Banglore', 'Kolkata', 'Delhi', 'Chennai', 'Mumbai'))  
  if Source == 'Delhi':
    Source_Delhi = 1
    Source_Kolkata = 0
    Source_Mumbai = 0
    Source_Chennai = 0

  elif Source == 'Kolkata':
    Source_Delhi = 0
    Source_Kolkata = 1
    Source_Mumbai = 0
    Source_Chennai = 0

  elif Source == 'Mumbai':
    Source_Delhi = 0
    Source_Kolkata = 0
    Source_Mumbai = 1
    Source_Chennai = 0

  elif Source == 'Chennai':
    Source_Delhi = 0
    SourceKolkata = 0
    Source_Mumbai = 0
    Source_Chennai = 1

  else:
    Source_Delhi = 0
    Source_Kolkata = 0
    Source_Mumbai = 0
    Source_Chennai = 0    

  
  if st.button("Predict"):
    output = predict_price(Total_Stops, Jounary_day, Jounary_Month, Deep_hour, Deep_min,
       Arival_hour, Arival_min, Duration_hour, Duration_min,
       Airline_AirIndia,Airline_GoAir, Airline_IndiGo,
       Airline_JetAirways, Airline_JetAirwaysBusiness,
       Airline_Multiplecarriers, Airline_MultiplecarriersPremiumeconomy,
       Airline_SpiceJet, Airline_Trujet, Airline_Vistara,
       Airline_VistaraPremiumeconomy, Destination_Cochin,
       Destination_Delhi, Destination_Hyderabad, Destination_Kolkata,
       Destination_NewDelhi, Source_Chennai, Source_Delhi,
       Source_Kolkata, Source_Mumbai)
    st.success(round(output))

  if st.button("About"):
    st.header("By Hritwick Goyal")
    st.subheader("Intern")
  
if __name__=='__main__':
  main()
