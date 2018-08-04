# threeday.json

Represents a multi-day weather forecast.

<table>
  <tr>
    <th colspan="2"><b>Element</b></th>
    <th><b>Description</b></th>
    <th><b>Type</b></th>
    <th><b>Notes</b></th>
  </tr>
  <tr>
    <td colspan="2">longitude</td>
    <td>longitude of forecast area</td>
    <td>number</td>
    <td>center of area</td>
  </tr>
    <tr>
    <td colspan="2">latitude</td>
    <td>latitude of forecast area</td>
    <td>number</td>
    <td>center of area</td>
  </tr>
    <tr>
    <td colspan="2">forecasts</td>
    <td>daily forecasts</td>
    <td>array</td>
    <td>of forecast objects</td>
  </tr>
  <tr>
    <td></td>
    <td>date</td>
    <td>date of forecast</td>
    <td>string</td>
    <td>format is YYYY-MM-DD</td>
  </tr>
  <tr>
    <td></td>
    <td>description</td>
    <td>description of weather</td>
    <td>string</td>
    <td>valid values: sunny, overcast, partly cloudy, raining, snowing</td>
  </tr>
    <tr>
    <td></td>
    <td>maxTemp</td>
    <td>high temperature</td>
    <td>number</td>
    <td>in degrees Celsius</td>
  </tr>
  <tr>
    <td></td>
    <td>minTemp</td>
    <td>low temperature</td>
    <td>number</td>
    <td>in degrees Celsius</td>
  </tr>
    <tr>
    <td></td>
    <td>windSpeed</td>
    <td>average windspeed</td>
    <td>number</td>
    <td>in kilometers per hour</td>
  </tr>
  <tr>
    <td></td>
    <td>danger</td>
    <td>true if conditions are dangerous; otherwise, false</td>
    <td>Boolean</td>
    <td></td>
  </tr>
</table>
