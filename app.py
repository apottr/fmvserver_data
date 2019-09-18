import requests,json,arrow
from pathlib import Path

directory = Path(__file__).parent.resolve()

cheyenne = "https://guest:guest@vod.impleotv.com/missions/589370a5d874730ab8587722"

aa = "https://guest:guest@vod.impleotv.com/segments/589370b0d874730ab8587725"

cheyenne_data = {"url": "https://vod.impleotv.com/telemetrypackets/",
                "missionId":"589370a5d874730ab8587722",
                "time_start":"2012-09-19T20:40:44.105Z",
                "time_end":"2012-09-19T20:40:50.105Z",
                "_":"1568831299184"}

cheyenne_data_2 = {"url":"https://vod.impleotv.com/telemetrypackets/",
"missionId":"589370a5d874730ab8587722",
"time_start":"2012-09-19T20:40:50.997Z",
"time_end":"2012-09-19T20:40:56.997Z",
"_":"1568831299187"}

def process_missions_file():
    with open("missions","r") as f:
        x = json.loads("".join(f.readlines()))
        for each in x[:1]:
            meta = {
                "mission": each["_id"],
                "name": each["name"]
            }
            pull_whole_mission(meta)

def pull_mission_data(id):
    r = requests.get(f"https://guest:guest@vod.impleotv.com/missions/{id}",verify=False)
    j = json.loads(r.text)
    return j["segments"]

def pull_segment(id):
    url = f"https://guest:guest@vod.impleotv.com/segments/{id}"
    r = requests.get(url,verify=False)
    seg = json.loads(r.text)
    return {
        "mission": seg["missionId"],
        "start": seg["startTime"],
        "end": seg["endTime"],
        "video": "https://vod.impleotv.com/videos/"+(seg["media"][0]["relativeUrl"]).replace("\\","/")
    }

def pull_telemetry(mission,start,end):
    r = requests.get("https://vod.impleotv.com/telemetrypackets/",params={
        "missionId": mission,
        "time_start": start,
        "time_end": end
    },verify=False)
    return r.text

def pull_whole_mission(obj):
    id = obj["mission"]
    name = obj["name"]
    for seg in pull_mission_data(id):
        d = pull_segment(seg)
        r = requests.get(d["video"],verify=False)
        tel = pull_telemetry(d["mission"],d["start"],d["end"])
        ext = d["video"][-3:]
        with open(f"{directory}/videos/{name}.{ext}","w+b") as f:
            f.write(r.content)
        with open(f"{directory}/telemetry/{name}","w+") as t:
            t.write(tel)

def test_pull():
    a = cheyenne_data
    b = a["url"]
    c = dict((k, a[k]) for k in ('missionId', 'time_start', 'time_end'))
    pull_telemetry(b,c)

if __name__ == "__main__":
    process_missions_file()