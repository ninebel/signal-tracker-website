# signal-tracker
An uncomplete website project that tracks stock signals, with user registration, apis, etc.
This website was coded using only Python, HTML and CSS!

## How it works
The complete website is made on 3 major parts:
- alerts: API for tracking signals, alerts' db and some utility functions (backend)
- users: API for the users' db and some utility functions (backend)
- website: serves the visual content, forms, etc. (frontend)
- redis server: execute background tasks and schedules, necessary for alerts in order to work properly (backend) 

Each of these parts are inside its respective app folder, they are meant to be run on a Docker container, separately.
So, for example, users_app has all the necessary files to create a Docker image for the users API. You can create an image with docker build command. After the image is created, it must be run as a standalone container. 
In order to get the website fully worked, it is necessary to run 3 containers:
docker run -d -p 5001:5001 <alerts' image>
docker run -d -p 5000:5000 <users' image>
docker run -d -p 80:80 <website' image>

Each part is already configured for a port, this port must be opened when running a container, in this case alerts uses port 5001, users 5000 and website 80.

Make sure you have a redis server running, it's address and port and configured in alerts_app/alerts/config.py
You can also create a redis server using Docker or simply use another service as Redis Labs (they offer free redis database/server)
This project runs without NGINX, but it is possible to implement it for better performance.
