# -*- coding: utf-8 -*-

from IOTSeedSDK.MqttClient import IOTSeedMqttClient
import json
import time

host = "mqtt.hub.cloudahead.net"

client_id = 'c8875760-de12-11e7-97a1-71ce277f6bc3'

s_AccessToken = "password"

rootCAPath = r'./root_ca.pem'
privateKeyPath = r'key.pem'
certificatePath = r'./cert.pem'

if __name__ == '__main__':
    client = IOTSeedMqttClient(client_id)  # 客户端ID通过IOTSeed平台获取
    client.configureEndpoint(host, 38883)
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
    while True:
        message = {}
        message['message'] = "xxx"
        message['sequence'] = "bbb"
        messageJson = json.dumps(message)
        client.publishAsync("empoweriot/devices/" + client_id + '/telemetry', messageJson, 1)
        loopCount += 1
        time.sleep(1)
