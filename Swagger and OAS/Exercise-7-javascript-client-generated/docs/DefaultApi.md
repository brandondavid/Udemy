# MemeMeister.DefaultApi

All URIs are relative to *https://dev.mememeister.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**memeGet**](DefaultApi.md#memeGet) | **GET** /meme | Get meme(s)
[**memeMemeIdDelete**](DefaultApi.md#memeMemeIdDelete) | **DELETE** /meme/{meme-id} | Delete meme by ID
[**memeMemeIdGet**](DefaultApi.md#memeMemeIdGet) | **GET** /meme/{meme-id} | Get meme by ID
[**memePost**](DefaultApi.md#memePost) | **POST** /meme | Post meme


<a name="memeGet"></a>
# **memeGet**
> [MemeInfo] memeGet(opts)

Get meme(s)

Returns one or more memes

### Example
```javascript
var MemeMeister = require('meme_meister');
var defaultClient = MemeMeister.ApiClient.instance;

// Configure OAuth2 access token for authorization: oauthFacebook
var oauthFacebook = defaultClient.authentications['oauthFacebook'];
oauthFacebook.accessToken = 'YOUR ACCESS TOKEN';

var apiInstance = new MemeMeister.DefaultApi();

var opts = { 
  'q': "q_example" // String | Optional URL-encoded search term
};

var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.memeGet(opts, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **String**| Optional URL-encoded search term | [optional] 

### Return type

[**[MemeInfo]**](MemeInfo.md)

### Authorization

[oauthFacebook](../README.md#oauthFacebook)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="memeMemeIdDelete"></a>
# **memeMemeIdDelete**
> memeMemeIdDelete(memeId)

Delete meme by ID

Remove a meme.

### Example
```javascript
var MemeMeister = require('meme_meister');
var defaultClient = MemeMeister.ApiClient.instance;

// Configure OAuth2 access token for authorization: oauthFacebook
var oauthFacebook = defaultClient.authentications['oauthFacebook'];
oauthFacebook.accessToken = 'YOUR ACCESS TOKEN';

var apiInstance = new MemeMeister.DefaultApi();

var memeId = 56; // Number | ID of meme to remove


var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
};
apiInstance.memeMemeIdDelete(memeId, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **memeId** | **Number**| ID of meme to remove | 

### Return type

null (empty response body)

### Authorization

[oauthFacebook](../README.md#oauthFacebook)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="memeMemeIdGet"></a>
# **memeMemeIdGet**
> File memeMemeIdGet(memeId)

Get meme by ID

Return a meme.

### Example
```javascript
var MemeMeister = require('meme_meister');
var defaultClient = MemeMeister.ApiClient.instance;

// Configure OAuth2 access token for authorization: oauthFacebook
var oauthFacebook = defaultClient.authentications['oauthFacebook'];
oauthFacebook.accessToken = 'YOUR ACCESS TOKEN';

var apiInstance = new MemeMeister.DefaultApi();

var memeId = 56; // Number | ID of meme to return


var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.memeMemeIdGet(memeId, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **memeId** | **Number**| ID of meme to return | 

### Return type

**File**

### Authorization

[oauthFacebook](../README.md#oauthFacebook)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="memePost"></a>
# **memePost**
> File memePost(topcaption, bottomcaption, image)

Post meme

Create a meme.

### Example
```javascript
var MemeMeister = require('meme_meister');
var defaultClient = MemeMeister.ApiClient.instance;

// Configure OAuth2 access token for authorization: oauthFacebook
var oauthFacebook = defaultClient.authentications['oauthFacebook'];
oauthFacebook.accessToken = 'YOUR ACCESS TOKEN';

var apiInstance = new MemeMeister.DefaultApi();

var topcaption = "topcaption_example"; // String | Top caption for meme (URL-encoded string)

var bottomcaption = "bottomcaption_example"; // String | Bottom caption for meme (URL-encoded string)

var image = "/path/to/file.txt"; // File | Background image for meme


var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.memePost(topcaption, bottomcaption, image, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **topcaption** | **String**| Top caption for meme (URL-encoded string) | 
 **bottomcaption** | **String**| Bottom caption for meme (URL-encoded string) | 
 **image** | **File**| Background image for meme | 

### Return type

**File**

### Authorization

[oauthFacebook](../README.md#oauthFacebook)

### HTTP request headers

 - **Content-Type**: image/jpeg, image/gif, image/png, multipart/form-data
 - **Accept**: image/jpeg

