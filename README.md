# Personal Financial Management App

## Documentation

Context: We are building a Personal Financial Management App. We want our system to
propose a Financial Plan to the user, based on their Historical Transactions. We acquire this
data when the user connects their bank account to our app using Dapi.co. Based on the
historical transactions, we want to identify the monthly recurrent expenses.


#### Project Setup

Create a directory for the clone.
Take clone of this repository from the git, using following command 


#### Installation

First You will need to install python version 3.6 or latest version.


#### Setup Virtual Environment

Create Virtual using python3 or follow below command

```
python3 -m venv <your-environment-name>
```

#### Install Requirements

For install requirements.txt use following command.

```
pip install -r requirements.txt
```

#### Setup Environment Variables

Create a .env file inside the root directory
and will need to add the following env variables inside the .env file-

```
SECRET_KEY='!60xzi363941!_^f=748oa)lg0did^pm9hl9o-yx3k-3pmt%%v'
DEBUG=True
ALLOWED_HOSTS=*
```

after it run following command

```
set -a; . .env; set +a
```

#### Run Project

Follow below commands to run the project.

```
python3 manage.py runserver
```

#### Call API

Find below api and past it in postman or browser 
and send a "POST" request and enter historical transactions as input in the following format,
or copy transactions from dapi.co

API to get monthly recurrent expenses:

```
POST http://localhost:8000/api/transactions
```

Dummy historical transactions:

```
{
  "transactions": [
    {
      "afterAmount": null,
      "beforeAmount": null,
      "amount": 44.1,
      "currency": {
          "code": "AED",
          "name": "UNITED ARAB EMIRATES DIRHAM"
      },
      "date": "2020-03-12T19:04:11.000Z",
      "description": "POTATO STATION",
      "details": "Food",
      "type": "debit"
    },
    {
      "afterAmount": null,
      "beforeAmount": null,
      "amount": 67.2,
      "currency": {
          "code": "AED",
          "name": "UNITED ARAB EMIRATES DIRHAM"
      },
      "date": "2020-03-12T19:02:47.000Z",
      "description": "POTATO STATION",
      "details": "drink",
      "type": "debit"
    },
    {
      "afterAmount": null,
      "beforeAmount": null,
      "amount": 44.1,
      "currency": {
          "code": "AED",
          "name": "UNITED ARAB EMIRATES DIRHAM"
      },
      "date": "2020-03-12T19:04:11.000Z",
      "description": "POTATO STATION",
      "details": "Food",
      "type": "debit"
    }
  ]
}

``` 

#### RESPONSE/OUTPUT:

The final response you'll get:

```
{
  "Monthly Recurrent Transactions": [
    {
      "afterAmount": null,
      "beforeAmount": null,
      "amount": 44.1,
      "currency": {
          "code": "AED",
          "name": "UNITED ARAB EMIRATES DIRHAM"
      },
      "description": "POTATO STATION",
      "details": "Food",
      "type": "debit",
      "recurrent_count": 2,
      "recurrent_amount": 88.2
    }
  ],
  "Monthly Fixed Recurrent Expenses": 88.2
}
```
