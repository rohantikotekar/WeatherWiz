# WeatherWiz

## Features

- Fetches current weather information for any city.
- Displays temperature, humidity, wind speed, pressure, and weather conditions.
- Shows the time of sunrise and sunset for the specified location.
- User-friendly GUI built with Tkinter.
- Background image for a visually appealing interface.

## Installation

### Prerequisites

- Python 3.x installed on your system.
- `requests` and `Pillow` libraries for handling HTTP requests and image processing.

### Installation Steps

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/rohantikotekar/weather-app-python.git
    cd weather-app-python
    ```

2. **Install Required Packages:**

    Use `pip` to install the necessary libraries:

    ```bash
    pip install requests Pillow
    ```

3. **API Key Setup:**

    This application uses the OpenWeatherMap API. You need to sign up on [OpenWeatherMap](https://openweathermap.org/) and get an API key. Replace the API key in the code with your own:

    ```python
    api = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=YOUR_API_KEY"
    ```

4. **Run the Application:**

    Execute the Python script to start the weather application:

    ```bash
    python weather_app.py
    ```

## Usage

1. Launch the application by running the Python script.
2. Enter the name of the city for which you want to know the weather.
3. Press Enter or click anywhere to see the weather information displayed on the screen.

