// get json from views.py
const jsonData = JSON.parse(document.getElementById('data').textContent)

// convert to geojson
let jsonFeatures = []

jsonData.forEach((point) => {
  let lat = point.latitude
  let lon = point.longitude

  let feature = {
    type: 'Feature',
    properties: point,
    geometry: {
      type: 'Point',
      coordinates: [lon, lat]
    }
  }
  jsonFeatures.push(feature)
})

const geojson = {
  type: 'FeatureGroup',
  features: jsonFeatures
}

const svgTemplate = `
  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32" class="buoy-marker" id="buoy-marker">
    <path d="m 2,19 c -0.49,0.417 -0.99,0.7925 -2,0.9375 v 2 C 1.01,21.7925 1.51,21.417 2,21 c 0.887,0.754 2.167,1 3,1 0.833,0 2.113,-0.246 3,-1 0.887,0.754 2.167,1 3,1 0.833,0 2.113,-0.246 3,-1 0.887,0.754 2.167,1 3,1 0.833,0 2.113,-0.246 3,-1 0.579,0.492 1.32,0.743 2,0.875 v -2 C 21.32,19.743 20.579,19.492 20,19 c -0.887,0.754 -2.167,1 -3,1 -0.833,0 -2.113,-0.246 -3,-1 -0.887,0.754 -2.167,1 -3,1 C 10.167,20 8.887,19.754 8,19 7.113,19.754 5.833,20 5,20 4.167,20 2.887,19.754 2,19 Z" id="path8565" style="fill:#52b8e4;fill-opacity:1" />
    <path d="M 11,0 C 9.35503,0 8,1.3550302 8,3 V 4 H 7 V 6 L 5.21875,14 H 3 c 0,2.314 0.685,3.92925 1.25,4.90625 C 4.525,18.95625 4.776,19 5,19 5.672,19 6.68275,18.813 7.34375,18.25 L 8,17.6875 8.65625,18.25 C 9.31725,18.813 10.328,19 11,19 c 0.672,0 1.68275,-0.187 2.34375,-0.75 L 14,17.6875 14.65625,18.25 C 15.31725,18.813 16.328,19 17,19 17.224,19 17.475,18.95625 17.75,18.90625 18.315,17.92925 19,16.314 19,14 H 16.78125 L 15,6 V 4 H 14 V 3 C 14,1.3550302 12.64497,0 11,0 Z m 0,2 c 0.56503,0 1,0.4349698 1,1 V 4 H 10 V 3 C 10,2.4349698 10.43497,2 11,2 Z M 8.78125,7 h 4.4375 l 1.5625,7 h -7.5625 z" id="path94" style="fill:#d8534e;fill-opacity:1" />
  </svg`

const options = {
  center: [45.3, -85],
  zoom: 4,
  zoomSnap: 0,
  zoomControl: false
}

const map = L.map('map', options)

L.tileLayer('https://{s}.basemaps.cartocdn.com/rastertiles/voyager/{z}/{x}/{y}{r}.png', {
  attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors &copy; <a href="https://carto.com/attributions">CARTO</a>',
  subdomains: 'abcd',
  maxZoom: 19
}).addTo(map)

map.addControl(L.control.zoom({
  position: 'bottomright'
}))

drawFeatures()

function drawFeatures() {

  const dataLayer = L.geoJson(geojson, {
    pointToLayer: function (feature, latlng) {
      return L.marker(latlng, {
        icon: L.divIcon({
          className: feature.properties.station,
          html: svgTemplate,
          iconSize: [30, 30],
          iconAnchor: [10, 10],
          tooltipAnchor: [10, 0]
        })
      })
    },
    onEachFeature: function (feature, layer) {

      const station = feature.properties.station
      const unixTimestamp = feature.properties.time
      const dateObject = new Date(unixTimestamp)
      const obTime = dateObject.toLocaleString("en-US", {
        timeZoneName: "short"
      })
      let windDirection = layer.feature.properties.wind_direction
      windDirection = (windDirection != null) ? windDirection + '\xB0' : 'no data'
      let windSpeed = layer.feature.properties.wind_speed
      windSpeed = (windSpeed != null) ? windSpeed + ' kts' : 'no data'
      let pressure = layer.feature.properties.pressure
      pressure = (pressure != null) ? pressure + ' in' : 'no data'
      let pressureT = layer.feature.properties.pressure_tendency_3hr
      pressureT = (pressureT != null) ? pressureT + ' in' : 'no data'
      const airTempC = layer.feature.properties.air_temperature
      let airTempCDeg = (airTempC != null) ? airTempC + '\xB0C' : ''
      const airTempFDeg = (airTempC != null) ? (+airTempC * 9 / 5 + 32).toFixed(1) + '\xB0F /' : 'no data'
      const dewpointC = layer.feature.properties.dewpoint
      let dewpointCDeg = (dewpointC != null) ? dewpointC + '\xB0C' : ''
      const dewpointFDeg = (dewpointC != null) ? (+dewpointC * 9 / 5 + 32).toFixed(1) + '\xB0F /' : 'no data'
      const waterTempC = layer.feature.properties.water_temperature
      let waterTempCDeg = (waterTempC != null) ? waterTempC + '\xB0C' : ''
      const waterTempFDeg = (waterTempC != null) ? (+waterTempC * 9 / 5 + 32).toFixed(1) + '\xB0F /' : 'no data'
      let waveHeight = layer.feature.properties.wave_height
      waveHeight = (waveHeight != null) ? waveHeight + ' m' : 'no data'
      const sidebarList = document.querySelector('#sidebar-list')
      //const commentsHeader = document.querySelector('.comments-header').innerHTML

      sidebarList.innerHTML += `
          <div class="accordion-item acc-${station}" id="acc-${station}">
          
            <h2 class="accordion-header" >
              <button id="station-${station}" class="accordion-button collapsed ${station}" type="button" data-bs-toggle="collapse" data-bs-target="#collapse${station}" aria-expanded="false" aria-controls="collapse${station}">
                Buoy ID: &nbsp;<span class="buoy-name" id="${station}"> ${station}</span>
              </button>
            </h2>

            <div id="collapse${station}" class="accordion-collapse collapse" aria-labelledby="heading${station}">
              <div class="accordion-body">
                <div>Latest Observation:</div>
                <div class="table-timestamp">${obTime}</div>
                <table class="table table-borderless table-sm">
                  <tbody>
                    <tr>
                      <td>Wind Direction:</td>
                      <td class="table-data">${windDirection}</td>
                    </tr>
                    <tr>
                      <td>Wind Speed:</td>
                      <td  class="table-data">${windSpeed}</td>
                    </tr>
                    <tr>
                      <td>Pressure:</td>
                      <td  class="table-data">${pressure}</td>
                    </tr>
                    <tr>
                      <td>3-Hr Pressure Tendency:</td>
                      <td  class="table-data">${pressureT}</td>
                    </tr>
                    <tr>
                      <td>Air Temperature: </td>
                      <td  class="table-data">${(airTempFDeg)} ${(airTempCDeg)}</td>
                    </tr>
                    <tr>
                      <td>Dewpoint: </td>
                      <td  class="table-data">${(dewpointFDeg)} ${(dewpointCDeg)}</td>
                    </tr
                    <tr>
                      <td>Water Temperature: </td>
                      <td  class="table-data">${(waterTempFDeg)} ${(waterTempCDeg)}</td>
                    </tr
                    <tr>
                      <td>Wave Height: </td>
                      <td  class="table-data">${(waveHeight)}</td>
                    </tr>
                  </tbody>
               </table>
               <hr>      
              </div>
            </div>
          </div>
        `

      let tooltip = ('<div class=tooltip-buoy-text>' + 'Buoy ID: ' +
        '<span class=tooltip-id>' + feature.properties.station + '</span></div>')
      layer.bindTooltip(tooltip, {
        className: 'tooltip'
      })
      layer.on('mouseover', function () {
        document.getElementById(station).classList.add('highlight')
      }).openTooltip()

      layer.on('click', function () {
        //map.flyTo(e.latlng, 10)
        scrollAccordion(station)
      })

      layer.on('mouseout', function () {
        document.getElementById(station).classList.remove('highlight')
      }).closeTooltip()
    }
  }).addTo(map)

  map.fitBounds(dataLayer.getBounds(), {
    padding: [20, 20]
  })

  const accItem = document.querySelectorAll('.accordion-item')
  const leafletMarker = document.querySelectorAll('.leaflet-marker-icon')

  accItem.forEach((btn) => {
    btn.addEventListener('mouseover', (e) => {
      let sidebarID = e.currentTarget.id.replace('acc-', '')
      highlightBuoyIcon(sidebarID)
    })

    btn.addEventListener('mouseout', (e) => {
      e.currentTarget.classList.remove('buoy-highlight')

      leafletMarker.forEach((item) => {
        item.classList.remove('buoy-highlight')
      })

      $('.leaflet-tooltip').css('visibility', 'hidden')
    })
  })

  function highlightBuoyIcon(sidebarID) {
    dataLayer.eachLayer(function (layer) {
      const stationID = layer.feature.properties.station
      if (stationID === sidebarID) {
        $(`.${sidebarID}`).addClass('buoy-highlight')
        let tooltip = ('<div class=tooltip-buoy-text>' + 'Buoy ID: ' +
          '<span class=tooltip-id>' + layer.feature.properties.station + '</span></div>')
        layer.bindTooltip(tooltip, {
          className: 'tooltip'
        }).openTooltip()
      }
    })
  }

  function scrollAccordion(station) {
    const accBtnName = document.querySelectorAll('.buoy-name')

    for (item of accBtnName) {
      if (station === item.id) {

        const accItem = document.getElementById(`${station}`)
        accItem.classList.add('acc-item')
        accItem.scrollIntoView({
          behavior: 'smooth',
          block: 'start'
        })

        let collapseElementList = [].slice.call(document.querySelectorAll(`#collapse${station}`))
        let collapseList = collapseElementList.map(function (collapseEl) {
          return new bootstrap.Collapse(collapseEl)
        })
      }
    }
  }



}