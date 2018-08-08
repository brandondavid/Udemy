# Exercise 3: Using Query Parameters

## Step #1
Find the topic ID for "Digital Life" from both the XML and JSON response bodies.

### XML
http://api.npr.org/list?id=3002
```
<list id="3002" typeid="3002">  ...
  <item id="1049" num="19" type="topic">
    <title>Digital Life</title>
    ...
  </item>
  ...
</list>
```

### JSON
http://api.npr.org/list?id=3002&output=JSON
```
{
  ...
  "item": [
    ...
    {
      "id": "1049",
      ...
      "title": {
        "$text": "Digital Life"
      },
      ...
    },
    ...
  ]
}
```
So the topic ID for "Digital Life" is `1049`.  
<br>

## Step #2
Retrieve a story from the list of "Digital Life" stories using the parameter `id=1049`:  
http://api.npr.org/query?id=1049&apiKey=MDE5NDA1NTUzMDE0MzMzNTE4NjhkNzEyMQ001

```
<nprml version="0.94">
<list>
...
<story id="631626802">
<link type="html">
https://www.npr.org/2018/07/23/631626802/encore-many-look-to-buddhism-for-sanctuary-from-an-over-connected-world?ft=nprml&f=1049
</link>
...
</story>
...
</list>
</nprml>
```

So the URL of an example "Digital Life" story is:  
https://www.npr.org/2018/07/23/631626802/encore-many-look-to-buddhism-for-sanctuary-from-an-over-connected-world?ft=nprml&f=1049  
<br>

## Step #3
Using the query parameters `startDate` and `endDate`, return only stories from 2013:  
http://api.npr.org/query?id=1049&startDate=2013-01-01&endDate=2013-12-31&apiKey=MDE5NDA1NTUzMDE0MzMzNTE4NjhkNzEyMQ001  
<br>

## Step #4
Using query parameters above and `sort`, return only stories from 2013 sorted in ascending order:  
http://api.npr.org/query?id=1049&startDate=2013-01-01&endDate=2013-12-31&sort=dateAsc&apiKey=MDE5NDA1NTUzMDE0MzMzNTE4NjhkNzEyMQ001  
<br>

