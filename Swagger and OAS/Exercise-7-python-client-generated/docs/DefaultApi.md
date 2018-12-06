# swagger_client.DefaultApi

All URIs are relative to *https://dev.mememeister.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**meme_get**](DefaultApi.md#meme_get) | **GET** /meme | Get meme(s)
[**meme_meme_id_delete**](DefaultApi.md#meme_meme_id_delete) | **DELETE** /meme/{meme-id} | Delete meme by ID
[**meme_meme_id_get**](DefaultApi.md#meme_meme_id_get) | **GET** /meme/{meme-id} | Get meme by ID
[**meme_post**](DefaultApi.md#meme_post) | **POST** /meme | Post meme


# **meme_get**
> list[MemeInfo] meme_get(q=q)

Get meme(s)

Returns one or more memes

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauthFacebook
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
q = 'q_example' # str | Optional URL-encoded search term (optional)

try:
    # Get meme(s)
    api_response = api_instance.meme_get(q=q)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->meme_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| Optional URL-encoded search term | [optional] 

### Return type

[**list[MemeInfo]**](MemeInfo.md)

### Authorization

[oauthFacebook](../README.md#oauthFacebook)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **meme_meme_id_delete**
> meme_meme_id_delete(meme_id)

Delete meme by ID

Remove a meme.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauthFacebook
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
meme_id = 56 # int | ID of meme to remove

try:
    # Delete meme by ID
    api_instance.meme_meme_id_delete(meme_id)
except ApiException as e:
    print("Exception when calling DefaultApi->meme_meme_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **meme_id** | **int**| ID of meme to remove | 

### Return type

void (empty response body)

### Authorization

[oauthFacebook](../README.md#oauthFacebook)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **meme_meme_id_get**
> file meme_meme_id_get(meme_id)

Get meme by ID

Return a meme.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauthFacebook
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
meme_id = 56 # int | ID of meme to return

try:
    # Get meme by ID
    api_response = api_instance.meme_meme_id_get(meme_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->meme_meme_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **meme_id** | **int**| ID of meme to return | 

### Return type

[**file**](file.md)

### Authorization

[oauthFacebook](../README.md#oauthFacebook)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **meme_post**
> file meme_post(topcaption, bottomcaption, image)

Post meme

Create a meme.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauthFacebook
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
topcaption = 'topcaption_example' # str | Top caption for meme (URL-encoded string)
bottomcaption = 'bottomcaption_example' # str | Bottom caption for meme (URL-encoded string)
image = '/path/to/file.txt' # file | Background image for meme

try:
    # Post meme
    api_response = api_instance.meme_post(topcaption, bottomcaption, image)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->meme_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **topcaption** | **str**| Top caption for meme (URL-encoded string) | 
 **bottomcaption** | **str**| Bottom caption for meme (URL-encoded string) | 
 **image** | **file**| Background image for meme | 

### Return type

[**file**](file.md)

### Authorization

[oauthFacebook](../README.md#oauthFacebook)

### HTTP request headers

 - **Content-Type**: image/jpeg, image/gif, image/png, multipart/form-data
 - **Accept**: image/jpeg

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

