// paso 1: Obtener referencias a los elementos del DOM necesarios y definir la clave API
let cityInput = document.getElementById('city_input'),
    busquedaBtn = document.getElementById('busquedaBtn'),
    api_key = '1fbb81deb89df45c5990d2d2fc8eb5b8'; // Asegúrate de que esta clave API sea válida

// paso 5: Obtener la referencia a la primera carta en la sección de clima actual
currentweathercard = document.querySelectorAll('.weather-izquierda .carta')[0];

// paso 8: Obtener la referencia a la primera carta en la sección de pronóstico de cinco días
fiveDaysForecastcard = document.querySelectorAll('.dias-pronostico')[0];

// paso 9: Obtener la referencia a la primera carta en la sección de destacados (calidad del aire)
aquicard = document.querySelectorAll('.destacados .carta')[0];
aquilist = ['bueno', 'medio', 'moderado', 'pobre', 'muy pobre'];

// paso 11: Obtener la referencia a la segunda carta en la sección de destacados (amanecer y anochecer)
sunrisecard = document.querySelectorAll('.destacados .carta')[1];

// paso 13: Obtener referencias a los elementos de detalles del clima (humedad, presión, etc.)
humidity = document.getElementById('humedadVal'),
pression = document.getElementById('pressionVal'),
visibilidaad = document.getElementById('viisibilidadVal'),
velocidaad_viento = document.getElementById('velociidad_vientoVal'),
termicaa = document.getElementById('teermicaVal');

// paso 14: Obtener la referencia a la sección de pronóstico por hora
hourforecastcard = document.querySelector('.hora-pronostico')

// paso 3: Función para obtener los detalles del clima utilizando la latitud y longitud
function getweatherdetails(name, lat, lon, country, state) {
    let WEATHER_API_URL = `https://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lon}&appid=${api_key}`,
        Forecast_API_URL = `https://api.openweathermap.org/data/2.5/forecast?lat=${lat}&lon=${lon}&appid=${api_key}`,
        AQI_API_URL = `https://api.openweathermap.org/data/2.5/air_pollution?lat=${lat}&lon=${lon}&appid=${api_key}`,
        // paso 6: Definir arrays para los días de la semana y meses del año
        days = [
            'sunday',
            'monday',
            'tuesday',
            'wednesday',
            'thursday',
            'friday',
            'saturday'
        ],
        months = [
            'jan',
            'feb',
            'mar',
            'apr',
            'may',
            'jun',
            'jul',
            'aug',
            'sep',
            'oct',
            'nov',
            'dec'
        ];

    // paso 10: Fetch para obtener la calidad del aire
    fetch(AQI_API_URL).then(res => res.json()).then(data => {
        //console.log(data);
        let { co, no, no2, o3, so2, pm2_5, pm10, nh3 } = data.list[0].components;
        aquicard.innerHTML = `
            <div class="carta-cabeza">
                <p>Calidad del aire</p>
                <p class="calidad-aire aire-${data.list[0].main.aqui}">${aquilist[data.list[0].main.aqui - 1]}</p>
            </div> 
            <div class="indices-aire">
                <i class="fa-regular fa-wind fa-3x"></i>
                <div class="item">
                    <p>PM2.5</p>
                    <h2>${pm2_5}</h2>
                </div>
                <div class="item">
                    <p>PM10</p>
                    <h2>${pm10}</h2>
                </div>
                <div class="item">
                    <p>SO2</p>
                    <h2>${so2}</h2>
                </div>
                <div class="item">
                    <p>CO</p>
                    <h2>${co}</h2>
                </div>
                <div class="item">
                    <p>No</p>
                    <h2>${no}</h2>
                </div>
                <div class="item">
                    <p>NH3</p>
                    <h2>${nh3}</h2>
                </div>
                <div class="item">          
                    <p>O3</p>
                    <h2>${o3}</h2>
                </div>          
            </div>
        `;
    }).catch(() => {                                
        alert('failed to fetch air quality ');
    });

    // paso 4: Fetch para obtener el clima actual
    fetch(WEATHER_API_URL).then(res => res.json()).then(data => {
        let date = new Date();
        currentweathercard.innerHTML = `
            <div class="actual-weather">
                <div class="detalles">
                    <p>Ahora</p>
                    <h2>${(data.main.temp - 273.15).toFixed(2)}&deg;C</h2>
                    <p>${data.weather[0].description}</p>
                </div>
                <div class="weather-iconos">
                    <img src="https://openweathermap.org/img/wn/${data.weather[0].icon}@2x.png" alt="">
                </div>
            </div>
            <hr>
            <div class="carta-pie">
                <p><i class="fa-light fa-calendar"></i>${days[date.getDay()]}, ${date.getDate()}, ${months[date.getMonth()]} ${date.getFullYear()}</p>
                <p><i class="fa-light fa-location-dot"></i>${name}, ${country}</p>
            </div>    
        `;

        // paso 12 y 13: Obtener detalles adicionales del clima (amanecer, anochecer, humedad, etc.)
        let { sunrise, sunset } = data.sys,
            { timezone, visibility } = data,
            { humidity, pressure, temp } = data.main,
            { speed } = data.wind,
            sRiseTime = moment.utc(sunrise, 'X').add(timezone, 'seconds').format('hh:mm A'),
            sSetTime = moment.utc(sunset, 'X').add(timezone, 'seconds').format('hh:mm A');
        sunrisecard.innerHTML = `
            <div class="carta-cabeza">
                <p>Amanecer y anochecer</p>
            </div>
            <div class="amanecer-anoche">
                <div class="item">
                    <div class="icon">
                        <i class="fa-light fa-sunrise fa-4x"></i>
                    </div>
                    <div>
                        <p>Amanecer</p>
                        <h2>${sRiseTime}</h2>
                    </div>
                </div>
                <div class="item">
                    <div class="icon">
                        <i class="fa-light fa-sunset fa-4x"></i>
                    </div>
                    <div>
                        <p>Anochecer</p>
                        <h2>${sSetTime}</h2>
                    </div>
                </div>
            </div>        
        `;
        humedadVal.innerHTML = `${humidity}%`;
        pressionVal.innerHTML = `${pressure} hPa`;
        viisibilidadVal.innerHTML = `${visibility / 1000} km`;
        velociidad_vientoVal.innerHTML = `${speed} m/s`;
        teermicaVal.innerHTML = `${(temp - 273.15).toFixed(2)}&deg;C`;
    }).catch(() => {
        alert('Failed to retrieve current weather');
    });

    // paso 7 y 15: Fetch para obtener el pronóstico del clima
    fetch(Forecast_API_URL).then(res => res.json()).then(data => {
        // paso 15: Mostrar el pronóstico por hora
        let hourforecast = data.list;
        hourforecastcard.innerHTML = '';
        for (i = 0; i <= 7; i++) {
            let hourforecastdate = new Date(hourforecast[i].dt_txt);
            let hr = hourforecastdate.getHours();
            let a = 'PM';
            if (hr < 12) a = 'AM';
            if (hr == 0) hr = 12;
            if (hr > 12) hr = hr - 12;
            hourforecastcard.innerHTML += `
                <div class="carta">
                    <p>${hr} ${a}</p>
                    <img src="https://openweathermap.org/img/wn/${hourforecast[i].weather[0].icon}.png" alt="">
                    <p>${(hourforecast[i].main.temp - 273.15).toFixed(2)}&deg;C</p>
                </div>
            `;
        }

        // paso 7: Filtrar y mostrar el pronóstico de cinco días
        let uniqueForecastDays = [];
        let fiveDaysForecast = data.list.filter((forecast, index) => {
            let forecastDate = new Date(forecast.dt * 1000).getDate();
            if (!uniqueForecastDays.includes(forecastDate)) {
                uniqueForecastDays.push(forecastDate);
                return true;
            }
            return false;
        });
        //console.log(fiveDaysForecast);
        fiveDaysForecastcard.innerHTML = '';
        for (i = 1; i < fiveDaysForecast.length; i++) {
            let date = new Date(fiveDaysForecast[i].dt_txt);
            fiveDaysForecastcard.innerHTML += `
                <div class="pronostico-item">
                    <div class="icon-wrapper">
                        <img src="https://openweathermap.org/img/wn/${fiveDaysForecast[i].weather[0].icon}.png" alt="">
                        <span>${(fiveDaysForecast[i].main.temp - 273.15).toFixed(2)}&deg;C</span>
                    </div>
                    <P>${date.getDate()} ${months[date.getMonth()]}</P>
                    <P>${days[date.getDay()]}</P>
                </div>
            `;
            console.log(fiveDaysForecast)
        }
    }).catch(() => {
        alert('Failed to retrieve forecast');
    });
}

// paso 3: Función para obtener las coordenadas de la ciudad ingresada
function getcityCoordinates() {
    let cityName = cityInput.value.trim();
    cityInput.value = '';
    if (!cityName) return;
    console.log(cityName);
    let GEOCODING_API_URL = `https://api.openweathermap.org/geo/1.0/direct?q=${cityName}&limit=1&appid=${api_key}`;
    fetch(GEOCODING_API_URL).then(res => res.json()).then(data => {
        if (data.length === 0) {
            alert(`City not found: ${cityName}`);
            return;
        }
        let { name, lat, lon, country, state } = data[0];
        getweatherdetails(name, lat, lon, country, state);
    }).catch(() => {
        alert(`City not found: ${cityName}`);
    });
}

// paso 2: Añadir un evento al botón de búsqueda para obtener las coordenadas de la ciudad
busquedaBtn.addEventListener('click', getcityCoordinates);
