import json

with open("db.json") as db_json:
	database = json.load(db_json)

new_song = {"key":{}, "content":[]}

new_song["artist"] = input("Artist: ")
new_song["title"] = input("Title: ")
new_song["key"]["primary"] = input("Primary Key: ")
new_song["bpm"] = float(input("BPM: "))
new_song["energy"] = int(input("Energy: "))
new_song["source"] = input("Source: ")
print("inst, diy, vox, multis, stems, project, other\n")
content = [x.strip() for x in input("Content: ").split(",")]
new_song["content"] += content

database.append(new_song)

with open("db.json", "w") as db_json:
	json.dump(database, db_json, indent = 4, sort_keys=True)