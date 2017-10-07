
import requests
import time
import json
from pprint import pprint

firebase_url = 'https://fir-kings.firebaseio.com/'

labelcounter = 0;
tempInitialValue = 30
movementInitialValue = 0
humidityInitialValue = 0
start = False
startLimit = 0
endLimit = 100

print('Buzzer check')
print('Temperature sensor check')
print('Humidity sensor check')
print('Movement sensor check')
print('Heat lamp check')
print('Fan check')



chartdata =  {
    'labels': [0],
    'datasets': [{
      'label': 'temperature',
      'data': [0],
      'backgroundColor': "rgba(153,255,51,0.4)"
    }, {
      'label': 'humidity',
      'data': [0],
      'backgroundColor': "rgba(255,153,0,0.4)"
    }, {
      'label': 'movement',
      'data': [0],
      'backgroundColor': "rgba(153,255,51,0.4)"
    }
    ]
  }
fixed_interval = 5
counter = 0

while 1:
	try:
		json_str = json.dumps(chartdata)
		json_python = json.loads(json_str);	
		time.sleep(fixed_interval)
		labelcounter = labelcounter + 5
		tempInitialValue = tempInitialValue + 5
		movementInitialValue = movementInitialValue + 1
		humidityInitialValue = humidityInitialValue + 2

		#if temperature goes beyond endLimit turn on fan
		#if temperature goes below startLimit turn on heat lamp
		#if unable to bring back to threshold start beeping and send out email
		#bring temperature down to startLimit and turn off fan
		#move temperature up to endLimit and turn off heat lamp

		json_python['labels'].append(labelcounter)
		json_python['datasets'][0]['data'].append(tempInitialValue)
		if tempInitialValue > 50:
			json_python['datasets'][0]['backgroundColor'] = "rgba(226,33,33,0.4)"
		else:
			json_python['datasets'][0]['backgroundColor'] = "rgba(153,255,51,0.4)"

		json_python['datasets'][1]['data'].append(humidityInitialValue)
		json_python['datasets'][2]['data'].append(movementInitialValue)
		print(json_python) 
		result1 = requests.post(firebase_url + '/' + 'location' + '/temperature.json' , data=json.dumps(chartdata))
		chartdata = json_python

		#if stop value is passed set start to false
		#reset all the sensor values 
		#humidityInitialValue = 0
		#temperatureInitialValue = 0
		#movementInitialValue = 0

		start = True

	except IOError:
		print('Error reading sensor data.')


