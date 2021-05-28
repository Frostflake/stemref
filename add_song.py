import json, subprocess

with open("db.json") as db_json:
	database = json.load(db_json)

new_song = {"key":{}, "content":[]}

new_song["artist"] = input("Artist: ")
if "||" in new_song["artist"]:
	full_string = new_song["artist"].split("||")
	new_song["title"] = full_string[0]
	new_song["artist"] = full_string[1]
	new_song["key"]["primary"] = full_string[2]
	new_song["bpm"] = float(full_string[3])
	new_song["energy"] = int(full_string[4])
	new_song["source"] = full_string[5]
	new_song["content"] = [x.strip() for x in full_string[6].split(",")]
else:
	new_song["title"] = input("Title: ")
	new_song["key"]["primary"] = input("Primary Key: ")
	new_song["bpm"] = float(input("BPM: "))
	new_song["energy"] = int(input("Energy: "))
	new_song["source"] = input("Source: ")

	print("inst, diy, vox, multi, stems, project, other\n")
	content = [x.strip() for x in input("Content: ").split(",")]
	new_song["content"] += content

# Handle shorthand
if new_song["source"] == "rg":
	new_song["source"] = "Rhythm Game"
elif new_song["source"] == "rc":
	new_song["source"] = "Remix Contest"
elif new_song["source"] == "d":
	new_song["source"] = "Direct From Artist"

database.append(new_song)

with open("db.json", "w") as db_json:
	json.dump(database, db_json, indent = 4, sort_keys=True)

subprocess.run(['python3', 'generate.py'])
subprocess.run(['git', 'commit', '--message', 'Add ' + new_song["title"] + ' by ' + new_song["artist"], 'db.json', 'index.html'])
subprocess.run(['git', 'push'])