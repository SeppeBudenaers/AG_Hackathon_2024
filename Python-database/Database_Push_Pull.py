from Database_Classes import *
from Anomaly_Algorithm import *
from bottle import route, run, request, post
from datetime import datetime, timedelta
import json 

def serialize_list(l):
    return [m.to_dict() for m in l]

@route('/', method='POST')
def push():
    json_data = request.query.data or None
    if json_data is None:
        return 'No data provided'
    print(json_data)
    #parse json data here and push to database
    json_data = json.loads(json_data)
    Data_points = list(json_data.keys())
    for data_point in Data_points:
        #parsing json datapoints 
        entry  = json_data[data_point]
        if data_point == 'Body_Temperature':
            new_entry = Body_temperature(TimeStamp=datetime.strptime(entry['TimeStamp'], '%Y-%m-%dT%H:%M:%S'), Temperature=entry['Temperature'])
        elif data_point == 'Heart_Rate':
            new_entry = Heart_Rate(TimeStamp=datetime.strptime(entry['TimeStamp'], '%Y-%m-%dT%H:%M:%S'), HeartRate=entry['HeartRate'])
        elif data_point == 'Blood_Pressure':
            new_entry = Blood_Pressure(TimeStamp=datetime.strptime(entry['TimeStamp'], '%Y-%m-%dT%H:%M:%S'), Systolic=entry['Systolic'], Diastolic=entry['Diastolic'])
        elif data_point == 'Blood_Oxygen':
            new_entry = Blood_Oxygen(TimeStamp=datetime.strptime(entry['TimeStamp'], '%Y-%m-%dT%H:%M:%S'), Oxygen=entry['Oxygen'])
        elif data_point == 'Respiratory_Rate':
            new_entry = Respiratory_Rate(TimeStamp=datetime.strptime(entry['TimeStamp'], '%Y-%m-%dT%H:%M:%S'), RespiratoryRate=entry['RespiratoryRate'])
        elif data_point == 'Sweat':
            new_entry = sweat(TimeStamp=datetime.strptime(entry['TimeStamp'], '%Y-%m-%dT%H:%M:%S'), Sweat=entry['Sweat'])
        elif data_point == 'Sugar':
            new_entry = sugar(TimeStamp=datetime.strptime(entry['TimeStamp'], '%Y-%m-%dT%H:%M:%S'), Sugar=entry['Sugar'])
        elif data_point == 'Steps':
            new_entry = Steps(TimeStamp=datetime.strptime(entry['TimeStamp'], '%Y-%m-%dT%H:%M:%S'), Steps=entry['Steps'])
        elif data_point == 'Emotion':
            new_entry = Emotion(TimeStamp=datetime.strptime(entry['TimeStamp'], '%Y-%m-%dT%H:%M:%S'), Emotion=entry['Emotion'])
        elif data_point == 'Stress':
            new_entry = Stress(TimeStamp=datetime.strptime(entry['TimeStamp'], '%Y-%m-%dT%H:%M:%S'), Stress=entry['Stress'])
        else:
            return 'Invalid data point'
        session.add(new_entry)
        session.commit()
    return 'Data successfully pushed to database'

@route('/', method='GET')

def get():
    
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
        'Sweat': serialized_sweat,
        'Sugar': serialized_sugar,
        'Steps': serialized_steps,
        'Emotion': serialized_emotion,
        'Stress': serialized_stress
    }
    
    return json.dumps(serialized_data)
    

@route("/anomaly")
def detect_anomalies():
    print('Detecting anomalies')
    return json.dumps(Anomaly())

@post("/chat")
def Chat():
    messages = request.json
    print("1",messages)
    return json.dumps(chat(messages))

run(host='localhost', port=8080)
