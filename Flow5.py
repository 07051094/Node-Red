[
    {
        "id": "49a47fa8.1f58d",
        "type": "tab",
        "label": "流程5",
        "disabled": false,
        "info": ""
    },
    {
        "id": "cf092067.42df5",
        "type": "http in",
        "z": "49a47fa8.1f58d",
        "name": "Set GPIO5",
        "url": "/setgpio5",
        "method": "get",
        "upload": false,
        "swaggerDoc": "",
        "x": 140,
        "y": 280,
        "wires": [
            [
                "9c8b34a.6fc73c8",
                "727e7167.38edc"
            ]
        ]
    },
    {
        "id": "9c8b34a.6fc73c8",
        "type": "function",
        "z": "49a47fa8.1f58d",
        "name": "Set to 1",
        "func": "msg.payload = 1;\nreturn msg;",
        "outputs": 1,
        "noerr": 0,
        "x": 320,
        "y": 280,
        "wires": [
            [
                "46831587.fa0cfc"
            ]
        ]
    },
    {
        "id": "46831587.fa0cfc",
        "type": "rpi-gpio out",
        "z": "49a47fa8.1f58d",
        "name": "",
        "pin": "29",
        "set": "",
        "level": "0",
        "freq": "",
        "out": "out",
        "x": 500,
        "y": 280,
        "wires": []
    },
    {
        "id": "727e7167.38edc",
        "type": "function",
        "z": "49a47fa8.1f58d",
        "name": "Return Status",
        "func": "msg.payload = \"GPIO5 set to HIGH\";\nreturn msg;",
        "outputs": 1,
        "noerr": 0,
        "x": 340,
        "y": 360,
        "wires": [
            [
                "57c2bcf5.b14154",
                "1405e2a1.d60e3d"
            ]
        ]
    },
    {
        "id": "57c2bcf5.b14154",
        "type": "http response",
        "z": "49a47fa8.1f58d",
        "name": "",
        "statusCode": "",
        "headers": {},
        "x": 530,
        "y": 360,
        "wires": []
    },
    {
        "id": "1405e2a1.d60e3d",
        "type": "debug",
        "z": "49a47fa8.1f58d",
        "name": "",
        "active": true,
        "tosidebar": true,
        "console": false,
        "tostatus": false,
        "complete": "false",
        "x": 590,
        "y": 460,
        "wires": []
    },
    {
        "id": "62daa4c0.826dcc",
        "type": "http in",
        "z": "49a47fa8.1f58d",
        "name": "Clear GPIO5",
        "url": "/clear5",
        "method": "get",
        "upload": false,
        "swaggerDoc": "",
        "x": 150,
        "y": 560,
        "wires": [
            [
                "a3bb4edb.6d10e",
                "4a7ebd30.c6d114"
            ]
        ]
    },
    {
        "id": "a3bb4edb.6d10e",
        "type": "function",
        "z": "49a47fa8.1f58d",
        "name": "Clear to 0",
        "func": "msg.payload = 0;\nreturn msg;",
        "outputs": 1,
        "noerr": 0,
        "x": 320,
        "y": 560,
        "wires": [
            [
                "46831587.fa0cfc"
            ]
        ]
    },
    {
        "id": "4a7ebd30.c6d114",
        "type": "function",
        "z": "49a47fa8.1f58d",
        "name": "Return Status",
        "func": "msg.payload = \"GPIO5 set to LOW\";\nreturn msg;",
        "outputs": 1,
        "noerr": 0,
        "x": 340,
        "y": 620,
        "wires": [
            [
                "57c2bcf5.b14154",
                "1405e2a1.d60e3d"
            ]
        ]
    }
]
