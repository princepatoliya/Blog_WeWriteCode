# We Write <font color="green"> Code </font>
---

Blog application with fully CURD functionality

Extra features
- register with email verification and Login with OTP
---

## Setup

The first thing to do is to create virtual environment:
- Create a virtual environment to install pakages to using **requirement.txt** file
```
pip install virtualenv
virtualenv MyBlog
cd MyBlog
Scripts\activate
```
- clone repository
```
git clone https://github.com/princepatoliya/Blog_WeWriteCode.git
```

- Then install the dependencies:
```
pip install -r Blog_WeWriteCode/requirement.txt
```

- Inside Blog_WeWriteCode create file '.env' and enter this values
I used sqliteDB (user-admin, pass - admin)
```
EMAIL_PORT = <Value>
EMAIL_USE_TLS = <Value>
EMAIL_HOST_USER = <Value>
EMAIL_HOST_PASSWORD = <Value>
```
- finally run server
```
cd Blog_WeWriteCode
python manage.py runserver
```



