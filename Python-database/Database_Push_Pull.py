from Database_Classes import *
from bottle import route, run, request
from datetime import datetime, timedelta
import json 

def serialize_list(l):

    return [m.to_dict() for m in l]

@route('/')
def endpoint():
    current_date = datetime.now()

    end_date_str = request.query.end_date or current_date.strftime('%Y-%m-%d %H:%M:%S')
    start_date_str = request.query.start_date or current_date.strftime('%Y-%m-%d 00:00:00')

    try:
        end_date = datetime.strptime(end_date_str, '%Y-%m-%d %H:%M:%S')
        start_date = datetime.strptime(start_date_str, '%Y-%m-%d %H:%M:%S')
    except ValueError as e:
        return 'Invalid date format'

    serialized_body_temp = serialize_list(session.query(Body_temperature).filter(Body_temperature.TimeStamp >= start_date, Body_temperature.TimeStamp <= end_date).all())
    serialized_heart_rate = serialize_list(session.query(Heart_Rate).filter(Heart_Rate.TimeStamp >= start_date, Heart_Rate.TimeStamp <= end_date).all())
    serialized_blood_pressure = serialize_list(session.query(Blood_Pressure).filter(Blood_Pressure.TimeStamp >= start_date, Blood_Pressure.TimeStamp <= end_date).all())
    serialized_blood_oxygen = serialize_list(session.query(Blood_Oxygen).filter(Blood_Oxygen.TimeStamp >= start_date, Blood_Oxygen.TimeStamp <= end_date).all())
    serialized_respiratory_rate = serialize_list(session.query(Respiratory_Rate).filter(Respiratory_Rate.TimeStamp >= start_date, Respiratory_Rate.TimeStamp <= end_date).all())
    serialized_sweat = serialize_list(session.query(sweat).filter(sweat.TimeStamp >= start_date, sweat.TimeStamp <= end_date).all())
    serialized_sugar = serialize_list(session.query(sugar).filter(sugar.TimeStamp >= start_date, sugar.TimeStamp <= end_date).all())
    
    serialized_steps = serialize_list(session.query(Steps).filter(Steps.TimeStamp >= start_date, Steps.TimeStamp <= end_date).all())
    
    serialized_emotion = serialize_list(session.query(Emotion).filter(Emotion.TimeStamp >= start_date, Emotion.TimeStamp <= end_date).all())
    serialized_stress = serialize_list(session.query(Stress).filter(Stress.TimeStamp >= start_date, Stress.TimeStamp <= end_date).all())
    
    serialized_data = {
        'Body_Temperature': serialized_body_temp,
        'Heart_Rate': serialized_heart_rate,
        'Blood_Pressure': serialized_blood_pressure,
        'Blood_Oxygen': serialized_blood_oxygen,
        'Respiratory_Rate': serialized_respiratory_rate,
        'sweat': serialized_sweat,
        'sugar': serialized_sugar,
        'steps': serialized_steps,
        'emotion': serialized_emotion,
        'stress': serialized_stress
    }
    return json.dumps(serialized_data)
    


run(host='localhost', port=8080)


# z = session.query(Body_temperature).all()
# print(z[0].temperature)