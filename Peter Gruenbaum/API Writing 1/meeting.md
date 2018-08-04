# meeting.json

Represents a meeting request in a calendar.

<table>
  <tr>
    <th colspan="2"><b>Element</b></th>
    <th><b>Description</b></th>
    <th><b>Type</b></th>
    <th><b>Required<b></th>
    <th><b>Notes</b></th>
  </tr>
  <tr>
    <td colspan="2">meeting</td>
    <td></td>
    <td>object</td>
    <td>Required</td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td>time</td>
    <td>date and time when meeting begins</td>
    <td>string</td>
    <td>Required</td>
    <td>timezone is GMT, format is YYYY-MM-DD HH:MM</td>
  </tr>
  <tr>
    <td></td>
    <td>duration</td>
    <td>duration of meeting</td>
    <td>number</td>
    <td>Required</td>
    <td>in minutes</td>
  </tr>
    <tr>
    <td></td>
    <td>description</td>
    <td>description of meeting</td>
    <td>string</td>
    <td>Required</td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td>location</td>
    <td>location of meeting</td>
    <td>string</td>
    <td>Optional</td>
    <td>default is empty string</td>
  </tr>
    <tr>
    <td></td>
    <td>reminder</td>
    <td>interval between reminder and meeting</td>
    <td>number</td>
    <td>Optional</td>
    <td>in minutes, default value is 10</td>
  </tr>
  <tr>
    <td></td>
    <td>invitees</td>
    <td>email addresses of invitees</td>
    <td>array of string</td>
    <td>Optional</td>
    <td>format is array of valid email addresses, default is empty array</td>
  </tr>
</table>
