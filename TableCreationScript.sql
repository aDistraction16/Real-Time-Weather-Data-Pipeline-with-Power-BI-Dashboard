CREATE TABLE WeatherData (
    RecordID INT PRIMARY KEY IDENTITY(1,1), -- Auto-incrementing primary key
    CityName VARCHAR(50),
    Temperature DECIMAL(5, 2), -- e.g., 25.50
    Humidity INT,
    WeatherDescription VARCHAR(100),
    Timestamp DATETIME
);