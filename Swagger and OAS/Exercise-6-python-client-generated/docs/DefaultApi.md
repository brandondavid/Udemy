# swagger_client.DefaultApi

All URIs are relative to *https://api.muzicplayz.com/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_playlist_id**](DefaultApi.md#delete_playlist_id) | **DELETE** /playlist/{playlist-id} | 
[**get_image**](DefaultApi.md#get_image) | **GET** /playlist/{playlist-id}/image | 
[**get_playlist**](DefaultApi.md#get_playlist) | **GET** /playlist | 
[**get_playlist_id**](DefaultApi.md#get_playlist_id) | **GET** /playlist/{playlist-id} | 
[**post_playlist**](DefaultApi.md#post_playlist) | **POST** /playlist | 


# **delete_playlist_id**
> delete_playlist_id(playlist_id)



**Remove a playlist.**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
playlist_id = 'playlist_id_example' # str | ID of the playlist to remove

try:
    api_instance.delete_playlist_id(playlist_id)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_playlist_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **playlist_id** | **str**| ID of the playlist to remove | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_image**
> file get_image(playlist_id)



**Returns a generated image for the playlist.**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
playlist_id = 'playlist_id_example' # str | ID of the playlist for which to generate an image

try:
    api_response = api_instance.get_image(playlist_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **playlist_id** | **str**| ID of the playlist for which to generate an image | 

### Return type

[**file**](file.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: image/png

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_playlist**
> get_playlist(limit=limit, offset=offset, search=search)



**Return one or more playlists.**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
limit = 56 # int | Number of playlists to return (optional)
offset = 56 # int | Number of playlists to skip (optional)
search = 'search_example' # str | Search term (optional)

try:
    api_instance.get_playlist(limit=limit, offset=offset, search=search)
except ApiException as e:
    print("Exception when calling DefaultApi->get_playlist: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of playlists to return | [optional] 
 **offset** | **int**| Number of playlists to skip | [optional] 
 **search** | **str**| Search term | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_playlist_id**
> PlaylistWithSongs get_playlist_id(playlist_id)



**Return a playlist.**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
playlist_id = 'playlist_id_example' # str | ID of the playlist to return

try:
    api_response = api_instance.get_playlist_id(playlist_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_playlist_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **playlist_id** | **str**| ID of the playlist to return | 

### Return type

[**PlaylistWithSongs**](PlaylistWithSongs.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_playlist**
> post_playlist(new_playlist)



**Create a new playlist.**

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
new_playlist = swagger_client.NewPlaylist() # NewPlaylist | The playlist to create

try:
    api_instance.post_playlist(new_playlist)
except ApiException as e:
    print("Exception when calling DefaultApi->post_playlist: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **new_playlist** | [**NewPlaylist**](NewPlaylist.md)| The playlist to create | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

