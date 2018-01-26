# -*- coding: utf-8 -*-

from IOTSeedSDK.MqttClient import IOTSeedMqttClient
import json
import time

host = "mqtt.hub.cloudahead.net"


deviceid = 'deviceid'  # 设备ID,通过云平台获得

s_AccessToken = "accessToken"  # 设备accessToken,通过云平台获得

end = False


rootCAPath = r'./mqtt-ca-server.pem'  # 根证书，通过云平台获得
privateKeyPath = r'mqtt-client1-key.pem'  # 设备私钥，通过云平台获得
certificatePath = r'./mqtt-client1.pem'  # 设备证书，通过云平台获得


def customCallback(client, userdata, message):
    print("Received a new message: ")
    print(message.payload)
    print("from topic: ")
    print(message.topic)
    print("--------------\n\n")


if __name__ == '__main__':
    client = IOTSeedMqttClient(deviceid)  # 客户端ID通过IOTSeed平台获取
    client.configureEndpoint(host, 8883)
    client.configureCredentials(rootCAPath, privateKeyPath, certificatePath)

    # AWSIoTMQTTClient connection configuration
    client.configureAutoReconnectBackoffTime(1, 32, 20)
    client.configureOfflinePublishQueueing(-1)  # Infinite offline Publish queueing
    client.configureDrainingFrequency(2)  # Draining: 2 Hz
    client.configureConnectDisconnectTimeout(10)  # 10 sec
    client.configureMQTTOperationTimeout(5)  # 5 sec

    client.configureAccessToken(s_AccessToken)

    # Connect and subscribe to AWS IoT
    client.connect()

    # Publish to the same topic in a loop forever
    loopCount = 0
    while not end:
        message = {}
        message['test_data'] = 150.0
        messageJson = json.dumps(message)
        client.publish("empoweriot/devices/" + deviceid +"/telemetry", messageJson, 1)
        message['test_data'] = 90.0
        messageJson = json.dumps(message)
        client.publish("empoweriot/devices/" + deviceid + "/telemetry", messageJson,1)
        loopCount += 1
        end = True
        # time.sleep(10)
