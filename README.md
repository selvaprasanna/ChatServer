# ChatServer

Instructions to Run Chat Server: 
1. Install MySQL Server. Ensure the Server is running in localhost
2. The settings can be changed in ChatServer/config.py
3. Run Chat Server via command line:
    >> python ChatServer.py

Requirements: 
1. Run ChatServer
2. Go to http://localhost:8081

Samples APIs: 
1. curl -H "Content-Type: application/json" http://localhost:8081/messages
2. curl -X POST -H "Content-Type: application/json" --data '{"user":"superman", "text":"hello"}' http://localhost:8081/message
3. curl -H "Content-Type: application/json" http://localhost:8081/users
    
Metrics to Monitor:
1. Average Response Time
2. Error Count - How many errors do users get? 
3. Count of client connected to the Chat Server at the same time
4. Request Rate - How many client requests come in at a time? 
5. Server CPU usage
6. Server Availability
7. User Satisfaction

Potential Improvements:
1. What will happen when we access the MySQL when someone is updating it? Do we get the latest data? Not sure. Something to look into.
2. More specific Error Responses. Currently we have only one error response. {"error": True}

Implementation Details:
1. Used Flask and Flask_Restful Packages to run the Chat Server
    a. 404 are automatically handled. 
2. The messages are stored in MYSQL Database
    a. MySQL query handles getting the unique users and latest 100 messages
    
Test Cases:
1. Bad API Requests that is not supported. For e.g., http://localhost:8081/userssssss
    => Return 404. Verified. 
2. API for http://localhost:8081/message:
    a. Send empty text: Verified. 
        => No Error. This is valid. 
    b. No "text" attribute: Verified. Get Error 
        => Response: {"error": True}
    c. Lot of text: mySQL TEXT can take 65,535 characters. If the message value exceeds this, we get error response.
        => Response: {"error": True}
    d. XSS Attack from the messages:
        => The strings need to be encoded before the server can consume them. Fortunately, Flask_Restful already handles this intrinsically. 
    e. No MySQL DB created. Verified. 
        => New DB is created
    f. MySQL Server Not Running. Did not check this. 
3. API for http://localhost:8081/users
    a. No DB Created. Verified. 
        => Send Error Response: {"error": True}
4. API for http://localhost:8081/messages:
    a. What is there are no message in the database
        => Didn't try. My code would not run into such scenario. But Ideally would return a empty dict.  
    b. What if there are less than 100 messages. But we requested the latest 100. Verified.  
        => All the messaged would be returned in a dict. 
4. Too many clients connecting at the same time.
    => Have not tried
5. Accessing the DB while client is updating new messages. Do we get the latest data?
    => Have not tried. 