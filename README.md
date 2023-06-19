# HOUSE HUNTING 

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

## Description

[Add project description here]

Basically this website helps people looking for houses to rent , and connects them to people renting their properties by providing them , their contact info

- [Usage](#usage)
This is a website where users go and search for houses , inorder to rent them , the systema facilitates the process of finding houses for rent 
If some one needs to register a house , the person will need to contact the administrator of the site 

Most importantly the site helps someone looking for house , with contact of the house owner once the image is clicked

- [Features](#features)
1. Search for house
2. Browsing for available House
3. Admin is able to Manage all activities go on the site
4. The user has the ability to update his info,delete accout, 
5. Acoount Management /session management of users
- [Screenshots](#screenshots)

## Installation


- [Installation](#installation)
1. Clone the repository:

 ```
	https://github.com/AganzeFelicite/House_hunting.git
```

2. Navigate into the project Directory
```
cd project-name
```
3. Create a virtual environment

```
python3 -m venv env
```
4. Activate the virtual environment
	- for linux
```
source env/bin/activate
	- for windows
```
.\env\Scripts\activate
```

5.Installation of requirements and used Dependencies

```
pip install -r requirements.txt
```
6.Do the DataBase Migrations

```
python manage.py migrate
```

7.Run the server and access it on the port 8080 of the local host
```
python manage.py runserver
```
Note this intall process assumes that u have django intalled and sqlite for database migrations


## Usage

Once You have averything set :
you can create a supperuser in django that will be managing the rest of the user and the site
```
python manage.py createsupper {username}
```
and then afte creating this user u can now access the admin dashbord by login into the sytem ,
Once loged in you will be presented with a friendly interface where u can do the rest of the operation easily 



## Contributing
AganzeFelicite 

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


## Contact
[
	aganzefelicite@gmail.com
]


