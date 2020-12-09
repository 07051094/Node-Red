[
    {
        "id": "64a8e4f8.71263c",
        "type": "tab",
        "label": "流程2",
        "disabled": false,
        "info": ""
    },
    {
        "id": "fc363f2b.7313e",
        "type": "inject",
        "z": "64a8e4f8.71263c",
        "name": "",
        "topic": "",
        "payload": "",
        "payloadType": "date",
        "repeat": "5",
        "crontab": "",
        "once": false,
        "onceDelay": 0.1,
        "x": 170,
        "y": 260,
        "wires": [
            [
                "b953e8ce.5dde78"
            ]
        ]
    },
    {
        "id": "b953e8ce.5dde78",
        "type": "function",
        "z": "64a8e4f8.71263c",
        "name": "Payload",
        "func": "msg.headers={\n    deviceKey: \"04yn48Zp50wmeXSn\"\n}\nreturn msg;",
        "outputs": 1,
        "noerr": 0,
        "x": 380,
        "y": 260,
        "wires": [
            [
                "506ce267.b9706c"
            ]
        ]
    },
    {
        "id": "506ce267.b9706c",
        "type": "http request",
        "z": "64a8e4f8.71263c",
        "name": "",
        "method": "GET",
        "ret": "txt",
        "paytoqs": false,
        "url": "http://api.mediatek.com/mcs/v2/devices/Dm4i6hW0/datachannels/LEDControl/datapoints.csv",
        "tls": "",
        "persist": false,
        "proxy": "",
        "authType": "",
        "x": 580,
        "y": 260,
        "wires": [
            [
                "43f1ec6f.5cd744",
                "5711070f.630a48"
            ]
        ]
    },
    {
        "id": "43f1ec6f.5cd744",
        "type": "http response",
        "z": "64a8e4f8.71263c",
        "name": "",
        "statusCode": "",
        "headers": {},
        "x": 670,
        "y": 380,
        "wires": []
    },
    {
        "id": "5711070f.630a48",
        "type": "debug",
        "z": "64a8e4f8.71263c",
        "name": "",
        "active": true,
        "tosidebar": true,
        "console": false,
        "tostatus": false,
        "complete": "false",
        "x": 600,
        "y": 500,
        "wires": []
    }
]
