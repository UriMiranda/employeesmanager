# Employees Manager  

## System requirements
| Requirement | Version |
|-------------|---------|
| Python      | > 3.*   |
| Django      | 2.*.*   |

## Getting Started

First clone this repository:  
``` bash
    git clone https://github.com/UriMiranda/employeesmanager.git && cd employeesmanger/
```

Then install project requirements:  
``` bash
    pip3 install -r requirements.txt
```

Run migrations:
``` bash
    python3 manage.py migrate
```

Load departament and admin data:
``` bash
    python3 manage.py loaddata departaments admin --database=default
```

## Run project 

Run server:
``` bash
    python3 manage.py runserver
```

Access admin: [http://loacalhost:8000/admin](http://loacalhost:8000/admin)  

| User | Password|
|------|---------|
|admin |  test   |


## API

|Departaments | ID|
|-------------|---|
| T.I.        | 1 |
| Financeiro  | 2 |
| Vandas      | 3 |
| RH          | 4 |

Listing all employees
``` bash
GET http://localhost:8000/employees
```

Create a employee
``` bash
POST http://localhost:8000/employees/store
```
BODY:
``` json
    {
        "name": "Test employee",
        "email": "test@test.com",
        "departament": 1
    }
```

Delete a employee
``` bash
GET http://localhost:8000/employees/delete/<id:int>
```

## Run tests
``` bash
    python3 manage.py test employees
```
