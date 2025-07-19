async function loadForecast() {
    const latitude = 38.9;  // Washington DC
    const longitude = -77.04;
    const response = await fetch(`https://api.open-meteo.com/v1/forecast?latitude=${latitude}&longitude=${longitude}&hourly=temperature_2m&daily=temperature_2m_max,temperature_2m_min&timezone=auto`);
    const data = await response.json();

    const container = document.getElementById('forecast');
    container.innerHTML = '';

    const hourlyTimes = data.hourly.time;
    const hourlyTemps = data.hourly.temperature_2m;

    const dailyTimes = data.daily.time;
    const dailyMax = data.daily.temperature_2m_max;
    const dailyMin = data.daily.temperature_2m_min;

    for (let d = 0; d < dailyTimes.length; d++) {
        const dayDiv = document.createElement('div');
        dayDiv.className = 'day';

        const header = document.createElement('div');
        header.className = 'day-header';
        header.textContent = `${dailyTimes[d]}  High: ${dailyMax[d]}°C  Low: ${dailyMin[d]}°C`;
        dayDiv.appendChild(header);

        const hourlyDiv = document.createElement('div');
        hourlyDiv.className = 'hourly';

        for (let h = 0; h < hourlyTimes.length; h++) {
            if (hourlyTimes[h].startsWith(dailyTimes[d])) {
                const hourDate = new Date(hourlyTimes[h]);
                const hour = hourDate.getHours();
                if (hour >= 21 || hour < 5) continue; // skip overnight

                const temp = hourlyTemps[h];
                const hourSpan = document.createElement('div');
                hourSpan.className = 'hour';
                const color = tempColor(temp);
                hourSpan.style.backgroundColor = color;
                hourSpan.textContent = `${hourlyTimes[h].replace('T', ' ')}\n${temp}°C`;
                hourlyDiv.appendChild(hourSpan);
            }
        }

        dayDiv.appendChild(hourlyDiv);
        container.appendChild(dayDiv);
    }
}

function tempColor(temp) {
    // Map -10C (blue) to 35C (red)
    const min = -10;
    const max = 35;
    const ratio = Math.min(1, Math.max(0, (temp - min) / (max - min)));
    const r = Math.round(255 * ratio);
    const b = Math.round(255 * (1 - ratio));
    return `rgb(${r},0,${b})`;
}

loadForecast();
