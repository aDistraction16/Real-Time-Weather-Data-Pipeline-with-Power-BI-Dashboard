import requests
import datetime
import pyodbc

#-----Configuration-----
API_KEY = '45521171f0746b72492b29d8599ea86e'  # Replace with your actual API key
CITIES = ['Davao City', 'Manila', 'New York', 'San Francisco', 'Japan', 'Seoul']
weather_data_list = []

#-----SQL Server Configuration-----
SERVER_NAME='LAPTOP-LDBL784J'
DATABASE_NAME='WeatherDB'

#Connection String
CONNECTION_STRING = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={SERVER_NAME};DATABASE={DATABASE_NAME};Trusted_Connection=yes;'

#-----Fetch Data from API -----
for city in CITIES:
    #Construct API URL
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'

    #Make the API Call
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()

        #Extract relevant information
        temp = data['main']['temp']
        humidity = data['main']['humidity']
        weather_description = data['weather'][0]['description']
        timestamp = datetime.datetime.now()

        #Store Data
        weather_data_list.append({
            'CityName': city,
            'Temperature': temp,
            'Humidity': humidity,
            'WeatherDescription': weather_description,
            'Timestamp': timestamp
        })
        print(f"Weather data for {city} fetched successfully.")
    else:
        print(f"Failed to fetch weather data for {city}. Status code: {response.status_code}")

#----- Insert Data into SQL Server-----
if weather_data_list:
    print('\nInserting data into the database...')
    try:
        with pyodbc.connect(CONNECTION_STRING) as conn:
            with conn.cursor() as cursor:
                for item in weather_data_list:
                    sql_insert = """
                        INSERT INTO WeatherData (CityName, Temperature, Humidity, WeatherDescription, Timestamp)
                        VALUES (?, ?, ?, ?, ?)
                    """
                    cursor.execute(sql_insert, (
                        item['CityName'],
                        item['Temperature'],
                        item['Humidity'],
                        item['WeatherDescription'],
                        item['Timestamp']
                    ))
                conn.commit()
                print("Data inserted successfully.")
    except pyodbc.Error as ex:
        sqlstate = ex.args[0]
        print(f"Database error: {sqlstate}")
        print(f"Error message: {ex}")
        print("Failed to insert data into the database.")

#-----Print Statements for Successful Data fetching-----
print("-" * 40)
print("Data fetched:")
for item in weather_data_list:
    print(f"City: {item['CityName']}, Temperature: {item['Temperature']}°C, Humidity: {item['Humidity']}%, Weather: {item['WeatherDescription']}, Timestamp: {item['Timestamp']}")
