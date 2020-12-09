[
    {
        "id": "41ac6729.f0a308",
        "type": "tab",
        "label": "流程1",
        "disabled": false,
        "info": ""
    },
    {
        "id": "dcaa24d2.056368",
        "type": "rpi-gpio out",
        "z": "41ac6729.f0a308",
        "name": "LED",
        "pin": "11",
        "set": true,
        "level": "0",
        "freq": "",
        "out": "out",
        "x": 490,
        "y": 540,
        "wires": []
    },
    {
        "id": "509e9ee0.99143",
        "type": "rpi-gpio in",
        "z": "41ac6729.f0a308",
        "name": "Button",
        "pin": "7",
        "intype": "up",
        "debounce": "25",
        "read": true,
        "x": 180,
        "y": 560,
        "wires": [
            [
                "b3acbf0b.b3525",
                "6c1ddb5e.bb4a74"
            ]
        ]
    },
    {
        "id": "b3acbf0b.b3525",
        "type": "debug",
        "z": "41ac6729.f0a308",
        "name": "",
        "active": true,
        "tosidebar": true,
        "console": false,
        "tostatus": false,
        "complete": "false",
        "x": 500,
        "y": 480,
        "wires": []
    },
    {
        "id": "6c1ddb5e.bb4a74",
        "type": "switch",
        "z": "41ac6729.f0a308",
        "name": "if input is 1",
        "property": "payload",
        "propertyType": "msg",
        "rules": [
            {
                "t": "eq",
                "v": "1",
                "vt": "str"
            },
            {
                "t": "eq",
                "v": "",
                "vt": "str"
            }
        ],
        "checkall": "true",
        "repair": false,
        "outputs": 2,
        "x": 330,
        "y": 620,
        "wires": [
            [
                "3bf86475.c6b84c"
            ],
            [
                "71d1af9d.36df7"
            ]
        ]
    },
    {
        "id": "3bf86475.c6b84c",
        "type": "change",
        "z": "41ac6729.f0a308",
        "name": "Change to 0",
        "rules": [
            {
                "t": "set",
                "p": "payload",
                "pt": "msg",
                "to": "0",
                "tot": "str"
            }
        ],
        "action": "",
        "property": "",
        "from": "",
        "to": "",
        "reg": false,
        "x": 380,
        "y": 320,
        "wires": [
            [
                "dcaa24d2.056368"
            ]
        ]
    },
    {
        "id": "71d1af9d.36df7",
        "type": "change",
        "z": "41ac6729.f0a308",
        "name": "Change to 1",
        "rules": [
            {
                "t": "set",
                "p": "payload",
                "pt": "msg",
                "to": "1",
                "tot": "str"
            }
        ],
        "action": "",
        "property": "",
        "from": "",
        "to": "",
        "reg": false,
        "x": 530,
        "y": 640,
        "wires": [
            [
                "dcaa24d2.056368"
            ]
        ]
    }
]
