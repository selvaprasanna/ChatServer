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
