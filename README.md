# Bible Search Engine

> It is a search engine that efficiently queries over the 2001 Translation of Bible and returns the best matching chapter that matches with the user queried verse.  
  
<div align="center"><strong>Video:</strong><a href="https://www.youtube.com/watch?v=OjqZtkpyjlg">Click here to watch the full walkthrough of the application</a></div>  
<br/>
  
[![Click me to watch the application video!](https://github.com/Georgey764/Bible-Search-Engine/assets/127057827/40d84c66-3047-48f5-920b-21987083b7f1)](https://www.youtube.com/watch?v=OjqZtkpyjlg)

  
_**Interested in how I made this?**_ Check out the [blog](https://medium.com/@georgesamuel764/how-to-create-a-simple-and-efficient-search-engine-in-python-bd1196ac4c1c). I went over all the steps that I took to make this application in this [blog](https://medium.com/@georgesamuel764/how-to-create-a-simple-and-efficient-search-engine-in-python-bd1196ac4c1c).

**Keep in mind that this engine is based on 2001 Translation of Bible and other popular translation will not work.** _2001 Translation Bible can be found [here](https://2001translation.org/)._  

## Overview
1. <a href="#how-to-CLI">How to run the app from CLI (Easiest)
2. <a href="#how-to-frontend">How to run the app's frontend</a> 
3. <a href="#how-to-backend">How to start the backend server</a>
4. <a href="#how-to-backend-api">Backend API Documentation</a>

<br/>

## <p id="how-to-CLI">How to Run the APP in CLI</p>

#### Prerequisites
* latest version of python3

#### Steps
1. In CLI, upon cloning the repository change your directory to the directory where you cloned this repository then change directory to Bible Search Engine and then to my-app-frontend.

    ``` >>> cd ./path-to-cloned-repository/Bible-Search-Engine/ ```

2. Create a virtual env in python

    ``` >>> python3 -m venv ./.venv ```

3. Activate the virtual environment

    ``` >>> source ./.venv/bin/activate ```

5. Install the required packages

    ``` >>> pip3 install -r requirements.txt ```
   
7. Start the backend server

    ``` >>> python3 run query_chapter.py "Your query goes here inside double quotes" y(optional) #y=the maximum number of results to be returned```

In Summary, enter the following commands:

```
>>> cd ./path-to-cloned-repository/Bible-Search-Engine/
>>> python3 -m venv ./.venv
>>> pip3 install -r requirements.txt
>>> python3 query_chapter.py "Your query goes here inside double quotes" y(optional) #y=the maximum number of results to be returned
```

<br/>

## <p id="how-to-frontend">How to Run the APP's Frontend</p>

#### Prerequisites
* latest version of npm

#### Steps

1. In CLI, upon cloning the repository change your directory to the directory where you cloned this repository then change directory to Bible Search Engine and then to my-app-frontend.

    ``` >>> cd ./path-to-cloned-repository/Bible-Search-Engine/my-app-frontend/ ```

2. Then you have to initialize the package.json by hitting:

    ``` >>> npm init ```

3. Install the required packagages:

    ``` >>> npm install ```

4. Run the frontend

    ``` >>> npm run dev ```

5. Access the frontend on http://localhost:3000/

In Summary, enter the following commands:

```
>>> cd ./path-to-cloned-repository/Bible-Search-Engine/my-app-frontend/
>>> npm init
>>> npm install
>>> npm run dev
```

<br/>

## <p id="how-to-backend">How to Start the Backend Server</p>

#### Prerequisites
* latest version of python3

#### Steps
1. In CLI, upon cloning the repository change your directory to the directory where you cloned this repository then change directory to Bible Search Engine and then to my-app-frontend.

    ``` >>> cd ./path-to-cloned-repository/Bible-Search-Engine/ ```

2. Create a virtual env in python

    ``` >>> python3 -m venv ./.venv ```

3. Activate the virtual environment

    ``` >>> source ./.venv/bin/activate ```

5. Install the required packages

    ``` >>> pip3 install -r requirements.txt ```

6. Start the backend server

    ``` >>> python3 main.py ```
   
8. Access the backend on http://localhost:8080/

In Summary, enter the following commands:

```
>>> cd ./path-to-cloned-repository/Bible-Search-Engine/
>>> python3 -m venv ./.venv
>>> pip3 install -r requirements.txt
>>> python3 main.py
```
        
<br/>

## <p id="how-to-backend-api">Backend API Documentation</p>

**Name**: Read Query <br/>  
  
**Method**: GET  
  
**Endpoint**: http://localhost:8080/read/<query>  
  
**Request Parameters**:  
* query (path parameter) : URL Safe query string for which BM25 scores need to be retrieved. You can encode your query [here](https://www.urlencoder.org/)  
  
**Description**: This endpoint allows the client to retrieve BM25 scores for a given query.  
  
**Response**  
* Status Code: 200 OK if the request is successful.  
* Content-Type: application/json  
* Response Body:  
   
    ```
    [
        [
            Document_name(string),
            bm25_scores(int)
        ],
        [
            Document_name_2(string),
            bm25_scores(int)
        ],
        ...
    ]
    ```
