# Backend API

## Accounts

### Creating a new account

To register a new account, send a plaintext POST request with "username" and "password" parameters to the following URL: <http://host/account/registeruser/>. If successful, you should get an "Success" HTTP text response. Otherwise you will get an error message explaining why the account could not be created.

## Logging in

To log in to an existing account, send a plaintext POST request with "username" and "password" parameters to the following URL: <http://host/account/login/>. If successful, you should get a "Success" HTTP text response. 

## Logging out

To log out of a logged in account, send a GET request to the following URL: <http://host/account/logout/>.

## Sending and receiving day ratings

### Submitting a new rating

You must be logged in to submit a rating. To submit a new rating to the server, send a POST in JSON format as to the following URL: <http://host/data/getratings/>. It should have the following key-value pairs:

``` python
        {
            "description" : "Some string",
            "rating" : (some integer from 0 to 4)
        }
```

You should receive a "Success" HTTP text response if the submission was successful.

### Getting all ratings for the user

You must be logged in to receive ratings. To get all ratings submitted by the logged in users, send a GET request to the following URL: <http://host/data/getratings/>. You should receive a JSON response containing a list of ratings in the following format:

``` python
        {
            "did_submit_today" : (true if user has already submitted a rating today or false if not),
            "ratings" : [ {
                "date" : "Date rating was submitted as a string",
                "rating" : (some integer from 0 to 4),
                "description" : "Some string",
            } 
            ]
        }

```

### Getting good ratings only from the user

You must be logged in to receive ratings. To get all ratings submitted by the logged in users, send a GET request to the following URL: <http://host/data/getgoodtimes/>. You should receive a JSON response containing a list of ratings in the following format:

``` python
        {
            "ratings" : [ {
                "date" : "Date rating was submitted as a string",
                "description" : "Some string",
            } 
            ]
        }

```

