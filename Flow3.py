[
    {
        "id": "61c734b3.85f53c",
        "type": "tab",
        "label": "流程3",
        "disabled": false,
        "info": ""
    },
    {
        "id": "f88d8360.bca24",
        "type": "inject",
        "z": "61c734b3.85f53c",
        "name": "",
        "topic": "",
        "payload": "",
        "payloadType": "date",
        "repeat": "5",
        "crontab": "",
        "once": false,
        "onceDelay": 0.1,
        "x": 210,
        "y": 360,
        "wires": [
            [
                "47efe338.be879c"
            ]
        ]
    },
    {
        "id": "47efe338.be879c",
        "type": "function",
        "z": "61c734b3.85f53c",
        "name": "Payload",
        "func": "msg.headers={\n    deviceKey : \"04yn48Zp50wmeXSn\"\n    };\nmsg.payload= \"Temperature,,24.3\";\nreturn msg;",
        "outputs": 1,
        "noerr": 0,
        "x": 450,
        "y": 380,
        "wires": [
            [
                "ec38a01c.3b4d6"
            ]
        ]
    },
    {
        "id": "ec38a01c.3b4d6",
        "type": "http request",
        "z": "61c734b3.85f53c",
        "name": "",
        "method": "POST",
        "ret": "txt",
        "paytoqs": false,
        "url": "https://api.mediatek.com/mcs/v2/devices/Dm4i6hW0/datapoints.csv",
        "tls": "",
        "persist": false,
        "proxy": "",
        "authType": "",
        "x": 640,
        "y": 380,
        "wires": [
            [
                "4800271a.5e4c68",
                "74cfb81d.2b3138"
            ]
        ]
    },
    {
        "id": "4800271a.5e4c68",
        "type": "http response",
        "z": "61c734b3.85f53c",
        "name": "",
        "statusCode": "",
        "headers": {},
        "x": 640,
        "y": 480,
        "wires": []
    },
    {
        "id": "74cfb81d.2b3138",
        "type": "debug",
        "z": "61c734b3.85f53c",
        "name": "",
        "active": true,
        "tosidebar": true,
        "console": false,
        "tostatus": false,
        "complete": "false",
        "x": 640,
        "y": 580,
        "wires": []
    }
]
