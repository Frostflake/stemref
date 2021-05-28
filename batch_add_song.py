import json, subprocess

with open("db.json") as db_json:
	database = json.load(db_json)

with open("batch.txt") as in_file:
	for line in in_file:
		if "||" in line:
			new_song = {"key":{}, "content":[]}
			full_string = line.strip().split("||")
			new_song["title"] = full_string[0]
			new_song["artist"] = full_string[1]
			if not "/" in full_string[2]:
				new_song["key"]["primary"] = full_string[2]
			else:
				keys = full_string[2].split("/")
				new_song["key"]["primary"] = keys[0]
				new_song["key"]["secondary"] = keys[1]
			new_song["bpm"] = float(full_string[3])
			new_song["energy"] = int(full_string[4])
			new_song["source"] = full_string[5]
			new_song["content"] = [x.strip() for x in full_string[6].split(",")]

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