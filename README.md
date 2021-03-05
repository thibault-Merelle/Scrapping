
  ![Incubateur Simplon.co : présentation, liste startups, interview](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSSEcKwborrMn9-Q2kmVlfAFLlq3M5DjW5Hlw&usqp=CAU)

this project is part of my course at simplon school

### Microsoft Cloud Developer

# groupes repartition:

The goal of this project is to build a simple front page, making groupes randomly from a list of names.

# Features:

-   make a simple interface user friendly
-   store inputs data in cache
-   use the data to create groupes.

## Build with:

-   HTML
-   CSS
-   Vanilla JS

## install and run :

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
eyJoaXN0b3J5IjpbLTMwMDM4NzU5OSw3MTQxMzM4NTBdfQ==
-->