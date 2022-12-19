# Twitter-fast-api
## This project is focused on a Twitter api done with Fast-api

This project is a Twitter API done with FastAPI, PostgreSQL and Docker
The project is based in a CRUD project done for the user `jrpinzong` specifically from the next repository https://github.com/jrpinzong/CRUD-Rest-Docker-Fastapi-ProgreSQL where he used PostgreSQL as Database

## Version: 1.0
## Features and Tools
- Windows x64
- FastApi
- PostgreSQL
- Docker and docker-compose

## Steps
### FIrst Step: Install Docker
> Go to the next link: https://docs.docker.com/desktop/install/windows-install/ and install Docker for windows

![image](https://user-images.githubusercontent.com/86843637/208322964-ba2a4134-e02a-462c-be26-5408523e8b54.png)

> Open Docker Desktop

### Second Step: Copy the repository and install the requirements.txt
- `git clone https://github.com/MauricioAliendre182/Twitter-fast-api.git`
- `cd Twitter-fast-api`
- `pip install venv` (if you don't already have virtualenv installed)
- `pip -m venv venv` to create your new environment (called 'venv' here)
- `source venv/Script/activate` to enter the virtual environment
- `pip install -r requirements.txt` to install the requirements in the current environment

### Third Step: Execute docker-compose up
> Firstly you have to check the docker compose version that you have

![image](https://user-images.githubusercontent.com/86843637/208323872-d7946d27-9505-4603-94cd-983c1c66b44a.png)

> Secondly go to the `docker-compose.yml` file and verify if the version matches, If that is not the case change the version to the docker-compose version

![image](https://user-images.githubusercontent.com/86843637/208324014-22ee7792-0c02-4099-8149-8c50c112e0ab.png)

> Lastly execute the command `docker-compose up` on your terminal, the corresponding images will be dowonload and the containers will be active

### Fourth Step: Create the Tables in pgAdmin
> Go to the link: http://localhost/, once there in pgAdmin introduce `admin@admin.com` as Email and `admin` as password

> Register a new server and put the next configurations:

![image](https://user-images.githubusercontent.com/86843637/208324315-b9069136-bfc4-45cb-a371-7edb76bc5628.png)

![image](https://user-images.githubusercontent.com/86843637/208324323-9f26eec0-4052-41ad-b2c7-d03e87368a00.png)

> **The password is `R2D2-333`**

> In DataBase go directly to Schemas > Tables and in the Query Tool introduce the commands stated in `create_tables.sql`

> This will create three tables Users, Password and Tweets

![image](https://user-images.githubusercontent.com/86843637/208324554-5a221b3d-ddd7-4ec9-becc-32199d5cbcb9.png)

### Fifth Step: Start with FastAPI
> Go to the link: http://localhost:8000/docs, now you can create, read, update and delete a User or a Tweet

### Extra Step: Stop the containers
> Simply execute `docker-compose stop` to stop the containers