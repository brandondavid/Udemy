
# tvrequest2.xml

Represents a request to record a television program.

<table>
  <tr>
    <th colspan="2"><b>Element</b></th>
    <th><b>Attribute</b></th>
    <th><b>Description</b></th>
    <th><b>Type</b></th>
    <th><b>Required<b></th>
    <th><b>Notes</b></th>
  </tr>
  <tr>
    <td colspan="2">recordTV</td>
    <td></td>
    <td>television program to record</td>
    <td>object</td>
    <td>Required</td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td>when</td>
    <td></td>
    <td>start of program broadcast</td>
    <td>object</td>
    <td>Required</td>
    <td></td>
  </tr>
    <tr>
    <td colspan="2"></td>
    <td>date</td>
    <td>date of program</td>
    <td>string</td>
    <td>Optional</td>
    <td>format is YYYY-MM-DD, default is current date</td>
  </tr>
  <tr>
    <td colspan="2"></td>
    <td>time</td>
    <td>start time of program</td>
    <td>string</td>
    <td>Required</td>
    <td>if <code>format</code> attribute is "12" (for 12-hour clock), then format is HH:MM AM or HH:MM PM
    <br>if <code>format</code> attribute is "24" (for 24-hour clock), then format is HH:MM</td></td>
  </tr>
    <tr>
    <td colspan="2"></td>
    <td>format</td>
    <td>time format (12-hour or 24-hour clock)</td>
    <td>number</td>
    <td>Required</td>
    <td>valid values: 12, 24
  </tr>
    <tr>
    <td></td>
    <td>duration</td>
    <td></td>
    <td>length of program</td>
    <td>object</td>
    <td>Required</td>
    <td></td>
  </tr>
    </tr>
    <tr>
    <td colspan="2"></td>
    <td>hours</td>
    <td>duration in hours</td>
    <td>number</td>
    <td>Required</td>
    <td>in hours</td>
  </tr>
  <tr>
    <td></td>
    <td>station</td>
    <td></td>
    <td>station showing program</td>
    <td>object</td>
    <td>Required</td>
    <td></td>
  </tr>
    <tr>
    <td colspan="2"></td>
    <td>channel</td>
    <td>channel of station</td>
    <td>number</td>
    <td>Required</td>
    <td></td>
  </tr>
</table>
