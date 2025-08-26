# Real-Time Weather Data Dashboard

This project demonstrates the automation of real-time weather data collection, storage, and visualization using Python and Power BI.

## Features
- Fetches current weather data for multiple cities using the OpenWeatherMap API
- Extracts temperature, humidity, and weather descriptions
- Stores weather data in a Microsoft SQL Server database
- Visualizes the collected data with a Power BI dashboard

## Files
- `weather_fetch.py`: Python script to fetch and store weather data
- `WeatherDashboard.pbix`: Power BI dashboard for data visualization
- `TableCreationScript.sql`: SQL script to create the required database table
- `TableCheckQuery.sql`: SQL script to check the contents of the weather data table

## Setup Instructions

### 1. Prerequisites
- Python 3.x
- Required Python packages: `requests`, `pyodbc`
- Microsoft SQL Server (with a database and table created using the provided SQL script)
- Power BI Desktop

### 2. Configure and Run the Python Script
1. Update the `API_KEY`, `SERVER_NAME`, and `DATABASE_NAME` in `weather_fetch.py` as needed.
2. Install required Python packages:
   ```sh
   pip install requests pyodbc
   ```
3. Run the script:
   ```sh
   python weather_fetch.py
   ```

### 3. Power BI Dashboard
- Open `WeatherDashboard.pbix` in Power BI Desktop to view and analyze the weather data.

## Project Highlights
- API integration and data processing with Python
- Automated data storage in SQL Server
- Data visualization with Power BI

## Author
- Maverick Adrian L. Barroso
