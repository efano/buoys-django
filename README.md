# Great Lakes Buoys Status Tracker

A web mapping application designed by [Lis Fano](https://efano.github.io/).

### Project Overview

[The National Data Buoy Center (NDBC)](https://www.ndbc.noaa.gov/) is a part of the [National Oceanic and Atmospheric Administration's (NOAA)](https://www.noaa.gov/), [National Weather Service (NWS)](https://www.weather.gov/). NDBC designs, develops, operates, and maintains a network of data collecting buoys and coastal stations. The [United States Coast Guard (USCG)](https://www.uscg.mil/) remains a critically important partner with the NDBC, supplying transportation for buoy deployments, retrievals, and other maintenance services. The premise of this projects is a concept study of how multiple agencies could quickly access realtime data that could indicate instrument sensor issues, as well as a medium of sharing maintenance and transportation scheduling.

The application is designed to provide an interactive web experience that visualizes the current buoy location within the Great Lakes region, realtime sensor data access, and a twitter-like communication interface that would be editable by a logged-in user. The NCDC realtime buoy data is available through the [University Corporation for Atmospheric Research (UCAR)](https://www.ucar.edu/)'s [THREDDS data server](https://unidata.github.io/python-training/workshop/Surface_Data/surface-data-with-siphon-and-metpy).

The technology stack for this application includes Django/Python/HTML/SVG/CSS/JS, Leaflet, and Django's sqlite3 database. The user interface framework includes the use of Bootstrap and JavaScript.