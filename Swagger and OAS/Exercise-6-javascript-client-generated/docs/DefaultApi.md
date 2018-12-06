# MusicApi.DefaultApi

All URIs are relative to *https://api.muzicplayz.com/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deletePlaylistId**](DefaultApi.md#deletePlaylistId) | **DELETE** /playlist/{playlist-id} | 
[**getImage**](DefaultApi.md#getImage) | **GET** /playlist/{playlist-id}/image | 
[**getPlaylist**](DefaultApi.md#getPlaylist) | **GET** /playlist | 
[**getPlaylistId**](DefaultApi.md#getPlaylistId) | **GET** /playlist/{playlist-id} | 
[**postPlaylist**](DefaultApi.md#postPlaylist) | **POST** /playlist | 


<a name="deletePlaylistId"></a>
# **deletePlaylistId**
> deletePlaylistId(playlistId)



**Remove a playlist.**

### Example
```javascript
var MusicApi = require('music_api');

var apiInstance = new MusicApi.DefaultApi();

var playlistId = "playlistId_example"; // String | ID of the playlist to remove


var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
};
apiInstance.deletePlaylistId(playlistId, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **playlistId** | **String**| ID of the playlist to remove | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="getImage"></a>
# **getImage**
> File getImage(playlistId)



**Returns a generated image for the playlist.**

### Example
```javascript
var MusicApi = require('music_api');

var apiInstance = new MusicApi.DefaultApi();

var playlistId = "playlistId_example"; // String | ID of the playlist for which to generate an image


var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.getImage(playlistId, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **playlistId** | **String**| ID of the playlist for which to generate an image | 

### Return type

**File**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: image/png

<a name="getPlaylist"></a>
# **getPlaylist**
> getPlaylist(opts)



**Return one or more playlists.**

### Example
```javascript
var MusicApi = require('music_api');
var defaultClient = MusicApi.ApiClient.instance;

// Configure HTTP basic authorization: basicAuth
var basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

var apiInstance = new MusicApi.DefaultApi();

var opts = { 
  'limit': 56, // Number | Number of playlists to return
  'offset': 56, // Number | Number of playlists to skip
  'search': "search_example" // String | Search term
};

var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
};
apiInstance.getPlaylist(opts, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **Number**| Number of playlists to return | [optional] 
 **offset** | **Number**| Number of playlists to skip | [optional] 
 **search** | **String**| Search term | [optional] 

### Return type

null (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="getPlaylistId"></a>
# **getPlaylistId**
> PlaylistWithSongs getPlaylistId(playlistId)



**Return a playlist.**

### Example
```javascript
var MusicApi = require('music_api');

var apiInstance = new MusicApi.DefaultApi();

var playlistId = "playlistId_example"; // String | ID of the playlist to return


var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.getPlaylistId(playlistId, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **playlistId** | **String**| ID of the playlist to return | 

### Return type

[**PlaylistWithSongs**](PlaylistWithSongs.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="postPlaylist"></a>
# **postPlaylist**
> postPlaylist(newPlaylist)



**Create a new playlist.**

### Example
```javascript
var MusicApi = require('music_api');

var apiInstance = new MusicApi.DefaultApi();

var newPlaylist = new MusicApi.NewPlaylist(); // NewPlaylist | The playlist to create


var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
};
apiInstance.postPlaylist(newPlaylist, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **newPlaylist** | [**NewPlaylist**](NewPlaylist.md)| The playlist to create | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

