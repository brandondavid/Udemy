# Exercise 2: Using cURL

## Create a User
**Request**  
`curl --request POST --header "accept: application/json" -H "Content-Type: application/json" -d "{ \"id\": 0, \"username\": \"restexpert\", \"firstName\": \"Rachel\", \"lastName\": \"Rest\", \"email\": \"rachel@example.com\", \"password\": \"json\", \"phone\": \"5551212\", \"userStatus\": 0}" http://petstore.swagger.io/v2/user`  

**Response**  
_/USER ENDPOINT CURRENTLY NOT WORKING_  


## Retrieve User Information
**Request**  
`curl --request GET http://petstore.swagger.io/v2/user/restexpert`  

**Response**  
`{"id":0,"username":"restexpert","firstName":"Rachel","lastName":"Rest","email":"rachel@example.com","password":"json","phone":"5551212","userStatus":0}`


## Delete the User
**Request**  
`curl --request DELETE http://petstore.swagger.io/v2/user/restexpert`  

**Response**  
_no response_
