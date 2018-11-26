
# tvrequest1.xml

Represents a request to record a television program.

<table>
  <tr>
    <th colspan="2"><b>Element</b></th>
    <th><b>Description</b></th>
    <th><b>Type</b></th>
    <th><b>Required<b></th>
    <th><b>Notes</b></th>
  </tr>
  <tr>
    <td colspan="2">recordTV</td>
    <td></td>
    <td>object</td>
    <td>Required</td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td>date</td>
    <td>date of program</td>
    <td>string</td>
    <td>Optional</td>
    <td>format is YYYY-MM-DD, default is current date</td>
  </tr>
  <tr>
    <td></td>
    <td>time</td>
    <td>start time of program</td>
    <td>string</td>
    <td>Required, has attribute</td>
    <td><code>format</code> attribute:<ul>
    <li>valid values: 12, 24</li>
    <li>if "12" (for 12-hour clock), then format is HH:MM AM or HH:MM PM</li>
    <li>if "24" (for 24-hour clock), then format is HH:MM</li></ul></td>
  </tr>
    <tr>
    <td></td>
    <td>duration</td>
    <td>length of program</td>
    <td>number</td>
    <td>Required</td>
    <td>in hours</td>
  </tr>
  <tr>
    <td></td>
    <td>channel</td>
    <td>television channel showing program</td>
    <td>number</td>
    <td>Required</td>
    <td></td>
  </tr>
</table>
