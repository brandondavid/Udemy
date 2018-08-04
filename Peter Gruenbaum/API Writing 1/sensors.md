# sensors.xml

Represents 

<table>
  <tr>
    <th><b>Element</b></th>
    <th><b>Description</b></th>
    <th><b>Type</b></th>
  </tr>
  <tr>
    <td>dailyData</td>
    <td>temperature and humidty data for single day</td>
    <td>element</td>
  </tr>
</table>


### dailyData
<table>
  <tr>
    <th><b>Element</b></th>
    <th><b>Description</b></th>
    <th><b>Type</b></th>
    <th><b>Notes</b></th>
  </tr>
  <tr>
    <td>date</td>
    <td>date of day represented by dailyData</td>
    <td>string</td>
    <td>format is YYYY-MM-DD</td>
  </tr>
    <tr>
    <td>hourlyData</td>
    <td>tempurature and humidity data for single hour</td>
    <td>element</td>
    <td>can have multiple <code>hourlyData</code> elements</td>
  </tr>
</table>


### hourlyData
<table>
  <tr>
    <th><b>Element</b></th>
    <th><b>Description</b></th>
    <th><b>Type</b></th>
    <th><b>Notes</b></th>
  </tr>
  <tr>
    <td>time</td>
    <td>timestamp of hour represented by hourlyData</td>
    <td>string</td>
    <td>local time, format is HH:MM</td>
  </tr>
    <tr>
    <td>device</td>
    <td>sensor device and its measurements</td>
    <td>element</td>
    <td>can have multiple <code>device</code> elements</td>
  </tr>
</table>

### device
<table>
  <tr>
    <th><b>Element</b></th>
    <th><b>Description</b></th>
    <th><b>Type</b></th>
    <th><b>Notes</b></th>
  </tr>
  <tr>
    <td>id</td>
    <td>identification number of sensor device</td>
    <td>number</td>
    <td></td>
  </tr>
    <tr>
    <td>temperature</td>
    <td>temperature measurement from sensor device</td>
    <td>number</td>
    <td>in degrees Fahrenheit</td>
  </tr>
  </tr>
    <tr>
    <td>humidity</td>
    <td>humidity measurement from sensor device</td>
    <td>number</td>
    <td>as percentage</td>
  </tr>
</table>
