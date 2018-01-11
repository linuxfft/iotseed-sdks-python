# -*- coding: utf-8 -*-

from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient

from AWSIoTPythonSDK.core.protocol.paho.client import MQTTv311

from AWSIoTPythonSDK.core.protocol.mqtt_core import MqttCore


class IOTSeedMqttClient(AWSIoTMQTTClient):
    def __init__(self, clientID, protocolType=MQTTv311, useWebsocket=False, cleanSession=True):
        self._mqtt_core = IOTSeedMqttcore(clientID, cleanSession, protocolType, useWebsocket)


class IOTSeedMqttcore(MqttCore):
    def _load_username_password(self):
        username_candidate = self._username
        self._internal_async_client.set_username_password(username_candidate, self._password)
