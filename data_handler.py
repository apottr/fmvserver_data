import re,json

def convert_json_to_stanag(j):
    kmap = ["Checksum",
    "UNIX Time Stamp",
    "Mission ID",
    "Platform Tail Number",
    "Platform Heading Angle",
    "Platform Pitch Angle",
    "Platform Roll Angle",
    "Platform True Airspeed",
    "Platform Indicated Airspeed",
    "Platform Designation",
    "Image Source Sensor",
    "Image Coordinate System",
    "Sensor Latitude",
    "Sensor Longitude",
    "Sensor True Altitude",
    "Sensor Horizontal Field of View",
    "Sensor Vertical Field of View",
    "Sensor Relative Azimuth Angle",
    "Sensor Relative Elevation Angle",
    "Sensor Relative Roll Angle",
    "Slant Range",
    "Target Width",
    "Frame Center Latitude",
    "Frame Center Longitude",
    "Frame Center Elevation",
    "Offset Corner Latitude Point 1",
    "Offset Corner Longitude Point 1",
    "Offset Corner Latitude Point 2",
    "Offset Corner Longitude Point 2",
    "Offset Corner Latitude Point 3",
    "Offset Corner Longitude Point 3",
    "Offset Corner Latitude Point 4",
    "Offset Corner Longitude Point 4",
    "Icing Detected",
    "Wind Direction",
    "Wind Speed",
    "Static Pressure",
    "Density Altitude",
    "Outside Air Temperature",
    "Target Location Latitude",
    "Target Location Longitude",
    "Target Location Elevation",
    "Target Track Gate Width",
    "Target Track Gate Height",
    "Target Error Estimate - CE90",
    "Target Error Estimate - LE90",
    "Generic Flag Data 01",
    "Security Local Metadata Set",
    "Differential Pressure",
    "Platform Angle of Attack",
    "Platform Vertical Speed",
    "Platform Sideslip Angle",
    "Airfield Barometric Pressure",
    "Airfield Elevation",
    "Relative Humidity",
    "Platform Ground Speed",
    "Ground Range",
    "Platform Fuel Remaining",
    "Platform Call Sign",
    "Weapon Load",
    "Weapon Fired",
    "Laser PRF Code",
    "Sensor Field of View Name",
    "Platform Magnetic Heading",
    "UAS LDS Version Number",
    "Target Location Covariance Matrix",
    "Alternate Platform Latitude",
    "Alternate Platform Longitude",
    "Alternate Platform Altitude",
    "Alternate Platform Name",
    "Alternate Platform Heading",
    "Event Start Time - UTC",
    "Remote Video Terminal LDS Conversion"]
    stanag = {}
    for i in range(len(kmap)):
        if i != 47:
            stanag[kmap[i]] = j[str(i+1)] if str(i+1) in j else ""
        else:
            stanag[kmap[i]] = sec_meta_decode(j["48"])
    return stanag

def sec_meta_decode(s):
    keys = [
        "Security Classification",
        "Classifying Country and Releasing Instructions Country Method",
        "Classifying Country",
        "SCI/SHI information",
        "Caveats",
        "Releasing Instructions",
        "Classified By",
        "Derived From",
        "Classification Reason",
        "Declassification Date",
        "Classification and Marking System",
        "Object Country Coding Method",
        "Object Country Codes",
        "Classification Comments",
        "UMID Video",
        "UMID Audio",
        "UMID Data",
        "UMID System",
        "Stream ID",
        "Transport Stream ID",
        "Item Designator ID",
        "Version"
    ]
    d = s.split("\r\n")
    b = {}
    for x in d:
        try:
            k = re.search(r"(\d+)\.(.+)",x)
            b[keys[int(k.group(1))-1]] = k.group(2)
        except Exception as e:
            pass
    return b

def ret_tel():
    return {
            "1": -15945,
            "2": 1348087245386309,
            "3": "ESRI_Metadata_Collect",
            "4": "N97826",
            "5": 199.0258640421149,
            "6": 5.093539231543931,
            "7": -6.694235053559984,
            "10": "C208B",
            "13": 41.14318403468616,
            "14": -104.805938901755,
            "15": 2936.371404592965,
            "16": 18.652323186083773,
            "17": 10.49210345616846,
            "18": 266.07031264949364,
            "19": -23.65625002591696,
            "20": 0,
            "21": 2099.412959557821,
            "22": 0,
            "23": 41.1382525838624,
            "24": -104.785526872047,
            "25": 1855.3612573434038,
            "26": 0.002302621539963988,
            "27": 0.00641117587817011,
            "28": -0.004685354167302469,
            "29": 0.0034539323099459823,
            "30": -0.0016983550523392437,
            "31": -0.004728843043305765,
            "32": 0.0034585100863673817,
            "33": -0.0025475325785088657,
            "47": 0,
            "48": "1. Unclassified\r\n2. ISO-3166 Two Letter\r\n3. //CA\r\n4. \r\n5. \r\n6. CA\r\n12. ISO-3166 Two Letter\t\r\n21. \r\n22. 5\r\n",
            "56": 0,
            "59": "Firebird",
            "65": 1,
            "72": "1970-01-01 00:00:00.0"
        }

def ret_seg():
    seg = {
    "sensor": {
        "name": "EO"
    },
    "name": "Cheyenne",
    "imageSourceSensors": [],
    "platforms": [
        "C208B"
    ],
    "_id": "589370b0d874730ab8587725",
    "missionId": "589370a5d874730ab8587722",
    "media": [
        {
            "streamInfo": {
                "GeneralInfo": {
                    "Format": "MPEG-4",
                    "Bitrate": 1632643,
                    "Size": 0,
                    "Duration": "00:01:25.1630000"
                },
                "VideoInfo": [
                    {
                        "Height": 720,
                        "Width": 1280,
                        "GOP": "",
                        "Standard": "Advanced Video Codec",
                        "ScanType": "Progressive",
                        "Profile": None,
                        "BitRate": 1500000,
                        "BitRateMode": "",
                        "Format": "High@L3.1",
                        "Pid": 1
                    }
                ],
                "AudioInfo": [],
                "MetadataInfo": []
            },
            "url": "file:///C:/ImpleoTV/StServer/videos/589370a5d874730ab8587722/Cheyenne.mp4",
            "relativeUrl": "589370a5d874730ab8587722\\Cheyenne.mp4",
            "master": False
        }
    ],
    "__v": 1,
    "startTime": "2012-09-19T20:40:44.105Z",
    "endTime": "2012-09-19T20:42:08.999Z"
    }

    return {
        "mission": seg["missionId"],
        "start": seg["startTime"],
        "end": seg["endTime"],
        "video": "https://vod.impleotv.com/videos/"+(seg["media"][0]["relativeUrl"]).replace("\\","/")
    }

if __name__ == "__main__":
    j = ret_tel()
    print(json.dumps(convert_json_to_stanag(j)))
    print(ret_seg())