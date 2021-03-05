
  ![Incubateur Simplon.co : présentation, liste startups, interview](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSSEcKwborrMn9-Q2kmVlfAFLlq3M5DjW5Hlw&usqp=CAU)

this project is part of my course at simplon school

### Microsoft Cloud Developer

# Scrapping_project:

This project is divided in two parts;  
on the one hand, the scrapper which collects the travel data on the Vintage_ride web site.  
on the other hand, we store this data in a sql table where our users can access it from a front, with the possibility of sending mails

# Features:

-   scrap Vintage_ride web site, find all destinations
-   store this data in mySQL database
-   make a front for users to select and show selected destination
    -   by dates (begin, end or both),
    -   by destinations
-   Add Email sender

## Build with:

-   Python
-   Flask
-   Jinja2
-   Docker

## install and run :

Docker are needed for further steps :  
if needed, for docker install, look at :

```
https://docs.docker.com/get-docker/

```

1.  Clone this repository
    
2.  cd into it
    
3.  launch docker-compose:  
    `docker-compose up`
    
4.  connect to local server:  
    `http://localhost:3002`
    

## Routes:

```
`http://localhost:3002/home`

```

return home for testing connection

```
`http://localhost:3002/api`

```

return json file to check manualy the api

```
`http://localhost:3002/dest`

```

return destination research results

```
`http://localhost:3002/dates`

```

return dates research results

```
`http://localhost:3002/results`

```

return dest + dates research results

## Architecture:

```
|- docker-compose.yml
|- README.md
|- Flask
|	|-templates
|	|- __init__.py
|	|-Dockerfile
|
|- scrapp
|	|- Dockerfile
|	|- LOG_scrapp.py
|	|- __main__.py
|	|- scrapp.py
|	|- sqlconnectors.py
|	|- test-scrapp.py

```
<!--stackedit_data:
eyJoaXN0b3J5IjpbNzE0MTMzODUwXX0=
-->