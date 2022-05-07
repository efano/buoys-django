# Great Lakes Buoys

A web mapping application designed by [Lis Fano](https://efano.github.io/) as a capstone project for [PDX Code Guild](https://pdxcodeguild.com/).

### Project Overview

[The National Data Buoy Center (NDBC)](https://www.ndbc.noaa.gov/) is a part of the [National Oceanic and Atmospheric Administration's (NOAA)](https://www.noaa.gov/), [National Weather Service (NWS)](https://www.weather.gov/). NDBC designs, develops, operates, and maintains a network of data collecting buoys and coastal stations. The [United States Coast Guard (USCG)](https://www.uscg.mil/) remains a critically important partner with the NDBC, supplying transportation for buoy deployments, retrievals, and other maintenance services. The premise of this projects is a concept study of how multiple agencies could quickly access realtime data that could indicate instrument sensor issues, as well as a medium of sharing maintenance and transportation scheduling.

The application is designed to provide an interactive web experience that visualizes the current buoy location within the Great Lakes region, realtime sensor data access, and a twitter-like communication interface that would be editable by a logged-in user. The NCDC realtime buoy data is available through the [University Corporation for Atmospheric Research (UCAR)](https://www.ucar.edu/)'s [THREDDS data server](https://unidata.github.io/python-training/workshop/Surface_Data/surface-data-with-siphon-and-metpy/#timeseries).

The technology stack for this application includes Django/Python/HTML/SVG/CSS/JS, Leaflet, and Django's sqlite3 database. The user interface framework includes the use of Bootstrap and vanilla JavaScript.

### Functionality

At full-size, the layout of the application comprises of a navigational bar at the top of the application, a sidebar, and an interactive slippy map taking up the rest of the display.  All elements are developed following the responsive web design (RWD) approach to render well on a variety of devices and window or screen sizes. Modals will be used for user login and blog editing.

### Data Model

Stored data will include user login credentials, and a messages model, as taught in the class in early April that mimicked a Twitter-type application. Data fields are still pending.

### Schedule

#### Week 1

- [ ] create a basic Django project and application
- [ ] because the Leaflet map is the canvas for the displaying the initial data, designing a responsive user interface is required
- [ ] get the Leaflet map running
- [ ] configure access to the THREDDS data server
- [ ] convert json data to geojson and project the buoy locations on the map
- [ ] display realtime buoy observation data in the sidebar

#### Week 2

- [ ] continue with building frontend user affordance between the map and sidebar
- [ ] build login models (backend)
- [ ] build login forms and modals (frontend)

#### Week 3

- [ ] build twitter-like models (backend)
- [ ] build twitter-like forms and modals (frontend)
- [ ] finalize styling
- [ ] hosting and deployment (?)

### Minimum Viable Product

A successful minimum viable product would be all listed items completed within weeks one and two. The items in week3 are still vague at this time and additional studying is required.
