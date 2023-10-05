import json

#question 1 loading the json file
with open('results.json', 'r') as file:
    data = json.load(file)

#question2 encoding the data
json_data = json.dumps(data, indent=4)
print("Encoded JSON")
print(json_data)

#uestion 2 decoding the data
decoded_data = json.loads(json_data)
print("\n Decoded Python data:")
print(decoded_data)

#question 3 total number of videos
total_videos = len(data)
print(f"\nTotal number of videos{total_videos}")


