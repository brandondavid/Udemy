# Exercise 2: Documenting Method and URL

## Retrieve All Albums
Returns a list of all existing albums, each a collection of images.
> **GET /album**  
> https://phantasticfoto.com/api/v1/album/
<br>

## Retrieve an Album
Returns data about a collection of images, where {albumId} is the ID of the album to retrieve.
> **GET /album/{albumId}**  
> https://phantasticfoto.com/api/v1/album/{albumId}
<br>

## Create an Album
Creates a new collection of images.
> **POST /album**  
> https://phantasticfoto.com/api/v1/album/
<br>

## Print an Album
Prints an existing collection of images, where {albumId} is the ID of the album to print.
> **POST /album/print/{albumId}**  
> https://phantasticfoto.com/api/v1/album/print/{albumId}
<br>

## Update an Album
Updates an existing collection of images, where {albumId} is the ID of the album to update.
> **PUT /album/{albumId}**  
> https://phantasticfoto.com/api/v1/album/{albumId}
<br>

## Remove an Album
Deletes an existing collection of images, where {albumId} is the ID of the album to delete.
> **DELETE /album/{albumId}**  
> https://phantasticfoto.com/api/v1/album/{albumId}
