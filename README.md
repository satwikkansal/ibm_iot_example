# IoT Door monitoring system

This repository contains code for the [Build your IoT skills by developing a door monitoring system](https://developer.ibm.com/technologies/iot/tutorials/iot-lp201-build-door-monitoring-system) tutorial published on IBM Developer blog. It is highly recommended to read the tutorial first before using this project.



## Project files

- `application.py`: Contains code for the application.
- `gateway_client.py`: Contains code for the gateway client.
- `udp_listener.py`: The code for receiving and parsing [SensorUDP](https://play.google.com/store/apps/details?id=com.ubccapstone.sensorUDP&hl=en_IN) data sent by the Android device over sockets.
- `main.py`: The script that is supposed to run on raspberry pi as per the tutorial. It uses` gateway_client` and `udp_listener` internally.

Install the requirements using pip,

```sh
$ pip install -r requirements.txt
```



