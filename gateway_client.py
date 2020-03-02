import json
import time

import psutil
import wiotp.sdk.gateway

ANDROID_DEVICE_TYPE = "Android"

def eventPublishCallback():
    print("Device Publish Event done!!!")


def myEventCallback(event):
    str = "%s event '%s' received from device [%s]: %s"
    print(str % (event.format, event.eventId, event.device, json.dumps(event.data)))


def myCommandCallback(cmd):
    print("Command received for %s:%s: %s" % (cmd.typeId, cmd.deviceId, cmd.data))


def myStatusCallback(status):
    if status.action == "Disconnect":
        str = "%s - device %s - %s (%s)"
        print(str % (status.time.isoformat(), status.device, status.action, status.reason))
    else:
        print("%s - %s - %s" % (status.time.isoformat(), status.device, status.action))


def get_gateway_cilent(config_file_path):
    config = wiotp.sdk.gateway.parseConfigFile(config_file_path)
    client = wiotp.sdk.gateway.GatewayClient(config=config, logHandlers=None)
    return client


def send_status_event(client):
    payload = {
        "cpu": psutil.cpu_percent(),
        "memory": psutil.virtual_memory().percent
    }
    client.publishEvent(eventId="status", msgFormat="json", data=payload, qos=1)


def send_regular_status(client, interval):
    while True:
        send_status_event(client)
        time.sleep(interval)


def send_android_device_event(client, device_id, eventId, data, callback=None):
    client.publishDeviceEvent(ANDROID_DEVICE_TYPE, device_id, eventId, msgFormat="json", data=data, qos=0, onPublish=callback)
