# We Write <font color="green"> Code </font>
---

Blog application with fully CURD functionality

Extra features
- register with email verification and Login
---

## Setup

The first thing to do is to clone the repository:
- create folder and inside folder run this command
```
git clone https://github.com/princepatoliya/Blog_WeWriteCode.git
```

- Create a virtual environment to install pakages to using **requirement.txt** file
```
pip install virtualenv
virtualenv MyBlog
```
- Then install the dependencies:
```
pip install -r requirements.txt
```
- create file '.env' and enter you passwords and apis(razorpay => KEY_ID, KEY_SECRET),
I used sqliteDB
```
EMAIL_PORT = <Value>
EMAIL_USE_TLS = <Value>
EMAIL_HOST_USER = <Value>
EMAIL_HOST_PASSWORD = <Value>
```
- finally run server
```
python manage.py runserver
```



