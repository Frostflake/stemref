import json

with open("db.json") as db_json:
	database_raw = json.load(db_json)

database = {}
for song in database_raw:
	database[song["artist"] + " - " + song["title"]] = song

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
	for song in sorted(database.keys()):
		file.write('<tr><td align="center" width="30" class="td0" style="border-left-width: 1px;">' + str(index) + '</td>')
		file.write('<td class="td0" align="center" width="90">' + database[song]["title"] + '<br></td>')
		file.write('<td class="td0" align="center" width="90">' + database[song]["artist"] + '<br></td>')
		file.write('<td class="td0" align="center" width="30">' + database[song]["key"]["primary"] + '<br></td>')
		file.write('<td class="td0" align="center" width="30">' + str(database[song]["bpm"]) + '<br></td>')
		file.write('<td class="td0" align="center" width="30">' + str(database[song]["energy"]) + '<br></td>')
		file.write('<td class="td0" align="center" width="100">')
		if 'inst' in database[song]["content"]:
			file.write('<img src="img/instrumental.png" alt="Instrumental" title="The instrumental is archived!">')
		else:
			file.write('<img src="img/noinstrumental.png" alt="No Instrumental" title="The instrumental is not yet archived.">')
		if 'vox' in database[song]["content"]:
			file.write('<img src="img/vox.png" alt="Vox" title="The studio vocals are archived!">')
		elif 'diy' in database[song]["content"]:
			file.write('<img src="img/diy.png" alt="DIY Vox" title="DIY vocals are archived!">')
		else:
			file.write('<img src="img/novox.png" alt="No Vox" title="The vocals are not yet archived.">')
		if 'multis' in database[song]["content"]:
			file.write('<img src="img/multis.png" alt="Multitracks" title="The multitracks are archived!">')
		else:
			file.write('<img src="img/nomultis.png" alt="No Multitracks" title="The multitracks are not yet archived.">')
		if 'stems' in database[song]["content"]:
			file.write('<img src="img/stems.png" alt="Stems" title="The stems are archived!">')
		else:
			file.write('<img src="img/nostems.png" alt="No Stems" title="The stems are not yet archived.">')
		if 'project' in database[song]["content"]:
			file.write('<img src="img/project.png" alt="Project" title="The project is archived!">')
		else:
			file.write('<img src="img/noproject.png" alt="No Project" title="The project is not yet archived.">')
		if 'other' in database[song]["content"]:
			file.write('<img src="img/other.png" alt="Other" title="Something else is archived!">')
		else:
			file.write('<img src="img/noother.png" alt="No Other" title="Nothing else is archived.">')
		file.write('<br></td>')
		file.write('<td class="td0" align="center" width="20">' + database[song]["source"] + '<br></td></tr>')
		index += 1
	file.write("</table>")
		