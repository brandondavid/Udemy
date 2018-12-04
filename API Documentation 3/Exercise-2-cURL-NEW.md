# Exercise 2: Using cURL

## Create a Pet
**Request**  
`curl --request POST --header "Content-Type: application/json" --data "{ \"id\": 5656, \"name\": \"Bela Bardog\", \"status\": \"available\" }" "http://petstore.swagger.io/v2/pet`
**Response**  
`{"id":5656,"name":"Bela Bardog","photoUrls":[],"tags":[],"status":"available"}`

## Retrieve Pet Information
**Request**  
`curl --request GET http://petstore.swagger.io/v2/pet/5656`
**Response**  
`{"id":5656,"name":"Bela Bardog","photoUrls":[],"tags":[],"status":"available"}`

## Delete the Pet
**Request**  
`curl --request DELETE http://petstore.swagger.io/v2/pet/5656`
**Response**  
``
