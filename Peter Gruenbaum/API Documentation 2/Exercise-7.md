# Exercise 7: Reference Documentation

## 1. Uploading a Sound File to the Current User’s Profile

### Method & Resource
> **POST /profile/sound**  
> https://api.sounddate.com/profile/sound

### Headers
**Name** | **Description** | **Required** | **Values**
--- | --- | --- | ---
Bearer | access token | Required | 
Content-Type | sound file format | Optional | Valid values: `audio/mpeg` for MP3, `audio/x-wav` for WAV.  Default is `audio/mpeg`
Accept | response format | Optional | Valid values: `application/json` for JSON, `application/xml` for XML.  Default is `application/json`

### Request Body
POST body is the sound file, must be 5min or shorter.

### Sample Request
This request uploads a song in WAV format and returns data in XML format:
```
PUT https://api.sounddate.com/profile/sound

Bearer: {ACCESS TOKEN}
Content-Type: audio/x-wav
Accept: application/xml

{SOUND FILE}
```

### Response Body
**Element** | **Description** | **Type** | **Notes**
--- | --- | --- | ---
id | identification number of sound file | integer | 
length | length of sound file | float | in seconds

### Sample Response
**JSON**
```
{
  "id": 12345,
   "length": 67.89
}
```

**XML**
```
<id>123435</id>
<length>67.89</length>
```


## 2. Retrieving Sound File Information for a User

### Method & Resource
> **GET /user/{userId}/profile/sound**  
> https://api.sounddate.com/user/{userId}/profile/sound

### Query Parameter
**Parameter** | **Description** | **Type** | **Required** | **Notes**
--- | --- | --- | --- | ---
sortOrder | order that the sound files are returned | string | Optional | Valid values: `mostRecent`, `earliest`, `shortest`, `longest`.  Default is `mostRecent` (sorted from latest to earliest).

### Headers
**Name** | **Description** | **Required** | **Values**
--- | --- | --- | ---
Bearer | access token | Required | 
Accept | response format | Optional | Valid values: `application/json` for JSON, `application/xml` for XML.  Default is `application/json`

### Sample Request
This request returns a list of song data in XML format for user #2018:
```
GET https://api.sounddate.com/user/2018/profile/sound?sortOrder=earliest

Bearer: {ACCESS TOKEN}
Accept: application/xml
```

### Response Body
<table>
  <tr>
    <th colspan="2"><b>Element</b></th>
    <th><b>Description</b></th>
    <th><b>Type</b></th>
    <th><b>Notes</b></th>
  </tr>
  <tr>
    <td colspan="2">soundFiles</td>
    <td>list of song data</td>
    <td>array</td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td>id</td>
    <td>identification number of sound file</td>
    <td>integer</td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td>url</td>
    <td>link to sound file</td>
    <td>string</td>
    <td>format is valid URL</td>
  </tr>
  <tr>
    <td></td>
    <td>length</td>
    <td>length of sound file</td>
    <td>float</td>
    <td>in seconds</td>
  </tr>  
</table>

### Sample Response
**JSON**
```
{
  "soundFiles": [
    {
      "id": 23456,
      "url": "https://api.sounddate.com/profile/sound/23456.mp3",
      "length": 11.2
    },
    {
      "id": 24559,
      "url": "https://api.sounddate.com/profile/sound/24559.mp3",
      "length": 19.8
    }
  ]
}
```

**XML**
```
<soundFiles>
  <soundFile id="23456" url="https://api.sounddate.com/profile/sound/23456.mp3" length="11.2" />
  <soundFile id="24559" url="https://api.sounddate.com/profile/sound/24559.mp3" length="19.8" />
</soundFiles>
```

## 3. Status Codes & Errors
**Code** | **Description** | **Notes**
--- | --- | ---
200 | OK | Sound file was successfully added.
401 | Unauthorized | The access token is not valid for this resource.
413 |  Payload Too Large | Sound file is too long to upload.
