# Exercise 1: Making REST Requests

## Create Pet

**POST /pet**  
https://petstore.swagger.io/v2/pet

**Request body**
```
{
  "id": 2018,
  "name": "Brandon David",
  "status": "available"
}
```

**Response body**
```
{
  "id": 2018,
  "name": "Brandon David",
  "photoUrls": [],
  "tags": [],
  "status": "available"
}
```

## Retrieve Pet

**GET /pet/{petId}**  
https://petstore.swagger.io/v2/pet/2018

**Response body:**
```
{
  "id": 2018,
  "name": "Brandon David",
  "photoUrls": [],
  "tags": [],
  "status": "available"
}
```

## Update Pet

**PUT /pet**
https://petstore.swagger.io/v2/pet/2018

**Request body**
```
{
  "name": "Brandon David",
  "status": "sold"
}
```

## Delete Pet

**DELETE /pet**
https://petstore.swagger.io/v2/pet/2018


