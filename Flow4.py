[
    {
        "id": "2003e5ab.f8f26a",
        "type": "tab",
        "label": "流程4",
        "disabled": false,
        "info": ""
    },
    {
        "id": "a4d62822.108098",
        "type": "http in",
        "z": "2003e5ab.f8f26a",
        "name": "",
        "url": "/pin4",
        "method": "get",
        "upload": false,
        "swaggerDoc": "",
        "x": 150,
        "y": 260,
        "wires": [
            [
                "25f8b82f.f9e8e8"
            ]
        ]
    },
    {
        "id": "356db1a8.dffc4e",
        "type": "http response",
        "z": "2003e5ab.f8f26a",
        "name": "",
        "statusCode": "",
        "headers": {},
        "x": 470,
        "y": 260,
        "wires": []
    },
    {
        "id": "64cf256e.ca678c",
        "type": "debug",
        "z": "2003e5ab.f8f26a",
        "name": "",
        "active": true,
        "tosidebar": true,
        "console": false,
        "tostatus": false,
        "complete": "false",
        "x": 490,
        "y": 300,
        "wires": []
    },
    {
        "id": "848fd013.a284a",
        "type": "rpi-gpio in",
        "z": "2003e5ab.f8f26a",
        "name": "GPIO4",
        "pin": "7",
        "intype": "up",
        "debounce": "25",
        "read": true,
        "x": 300,
        "y": 400,
        "wires": [
            [
                "c6806bf2.6fd908"
            ]
        ]
    },
    {
        "id": "c6806bf2.6fd908",
        "type": "function",
        "z": "2003e5ab.f8f26a",
        "name": "Set GPIO",
        "func": "global.set(\"GPIO\",msg.payload)\nreturn msg;",
        "outputs": 1,
        "noerr": 0,
        "x": 460,
        "y": 400,
        "wires": [
            [
                "64cf256e.ca678c"
            ]
        ]
    },
    {
        "id": "25f8b82f.f9e8e8",
        "type": "function",
        "z": "2003e5ab.f8f26a",
        "name": "Set GPIO",
        "func": "msg.payload = global.get(\"GPIO\");\nreturn msg;",
        "outputs": 1,
        "noerr": 0,
        "x": 320,
        "y": 260,
        "wires": [
            [
                "356db1a8.dffc4e",
                "64cf256e.ca678c"
            ]
        ]
    }
]
