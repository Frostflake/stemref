import json

with open("db.json") as db_json:
	database = json.load(db_json)

with open("index.html", "w") as file:
	file.write('''<title>Song Stem DB</title>
 
<meta http-equiv="content-type" content="text/html; charset=utf-8" />
<head>
<style>
.header_title {
font-size: 14px;
font-weight: bold;
}

.table_header
{

color: #000000;
border-width: 1px 1px 1px 0px;
border-style: solid;
border-color: #ABABAB;
background-color: #E7F1F7;
padding: 2px;
}
.td1
{

color: #000000;
border-width: 0px 1px 1px 0px;
border-style: solid;
border-color: #ABABAB;
padding: 2px;
background-color: #FFFFFF;
}
.td0
{

color: #000000;
border-width: 0px 1px 1px 0px;
border-style: solid;
border-color: #ABABAB;
padding: 2px;
background-color: #F1F1F1;
}

.td1 small,
.td0 small {
  color: #337396;
}

.header_cw
{

}
</style>

	<br>
	<table border="0" cellpadding="0" cellspacing="0" width="90%" align="center" id="songStems">
	<tr>
	<td class="table_header" width="30" align="center" style="border-width: 1px 1px 1px 1px;">#</td>
	<td class="table_header" align="center">Title</td>
	<td class="table_header" align="center">Artist</td>
	<td class="table_header" align="center">Primary Key</td>
	<td class="table_header" align="center">BPM</td>
	<td class="table_header" align="center">Energy</td>
	<td class="table_header" align="center">Content</td>
	<td class="table_header" align="center">Source</td>
	</tr>''')
	index = 1
	for song in database:
		file.write('<tr><td align="center" width="30" class="td0" style="border-left-width: 1px;">' + str(index) + '</td>')
		file.write('<td class="td0" align="center" width="90">' + song["title"] + '<br></td>')
		file.write('<td class="td0" align="center" width="90">' + song["artist"] + '<br></td>')
		file.write('<td class="td0" align="center" width="30">' + song["key"]["primary"] + '<br></td>')
		file.write('<td class="td0" align="center" width="30">' + str(song["bpm"]) + '<br></td>')
		file.write('<td class="td0" align="center" width="30">' + str(song["energy"]) + '<br></td>')
		file.write('<td class="td0" align="center" width="100"><br></td>')
		file.write('<td class="td0" align="center" width="20">' + song["source"] + '<br></td></tr>')
		index += 1
	file.write("</table>")
		