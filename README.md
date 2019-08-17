Setup steps

#Prerequisites
1. Linux/windows server
2. Visual studio code
3. Web browser
4. Docker setup on server (optional)


#Getting Started
Via Cloning Repository
Git clone https://github.com/olufekosamuel/Ajo.git
cd Ajo
pip install -r requirements.txt


# Database local
update settings.py file with your database credentials
DB_CONNECTION=mysql
DB_HOST=127.0.0.1
DB_DATABASE=ajo
DB_USERNAME=root
DB_PASSWORD=root

# Database on server
You will need to deploy mysql db into a docker container
then start the container and create a db for the application

Below is the crendentials for your settings.py if connecting to a db in anothe container using mysql connector with django
DB_CONNECTION=mysql.connector.django
DB_HOST=db_container_name
DB_PORT=3306
DB_DATABASE=ajo
DB_USERNAME=root
DB_PASSWORD=root

After installing the above, you can start your server by simply running python manage.py runserver 

