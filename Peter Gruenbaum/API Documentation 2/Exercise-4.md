# Exercise 4: Documenting Query Parameters

## Query Parameters
**Parameter** | **Description** | **Type** | **Required** | **Notes**
---: | --- | --- | --- | --- 
startDate | Earliest date of bugs to return | string  | Optional | Format is `YYYY-MM-DD`.  Default is date of earliest record.
endDate | Latest date of bugs to return | string | Optional | Format is `YYYY-MM-DD`.  Default is current date.
priority | Importance of the bug | integer | Optional | Valid values: `1` (highest priority), `2`, `3`, `4` (lowest priority).  Default is all priorities.
severity | Impact of the bug | integer | Optional | Valid values: `1` (most severe), `2`, `3`, `4` (least severe).  Default is all severities.
status | Status of the bug | string | Optional | Valid values: `open`, `closed`, `duplicate`, `notabug`. Default is all statuses.
start | Starting index of bugs to return | integer | Optional | First bug is at the 0th index.  Default is zero.
total | Total number of bugs to return | integer | Optional | Default is all bugs past the starting index given by `start`
<br>

## Sample Request
**GET** https://api.bugsquisher.com/bug?startDate=2018-01-01&priority=1&severity=1&status=open&total=10  

Returns the first ten worst bugs so far this year (2018), where "worst" is defined as highest priority, most severe, and still open.
