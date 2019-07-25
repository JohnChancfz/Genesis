# -*- coding: utf-8 -*-
import paho.mqtt.client as mqtt
import json
import os

mqttClient = mqtt.Client()


def g_value():
    try:
        r = os.popen('uci get cloud.cloud.type')
        type = str(r.read()).strip()
        print(type)
        if type != 'mqtt':
            return False, "", "", ""
        r = os.popen('uci get cloud.cloud.name')
        APPID = str(r.read()).strip()
        print(APPID)
        r = os.popen('uci get cloud.cloud.ipaddr')
        MQTTHOST = str(r.read()).strip()
        print(MQTTHOST)
        r = os.popen('uci get cloud.cloud.port')
        MQTTPORT = int(r.read())
        print(MQTTPORT)
        return True, APPID, MQTTHOST, MQTTPORT
    except:
        print("no cloud")


# 连接MQTT服务器
def on_mqtt_connect(host, port):
    print("connect start")
    # client_id = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
    # client = mqtt.Client(client_id)  # ClientId不能重复，所以使用当前时间
    # client.username_pw_set("admin", "admin")  # 必须设置，否则会返回「Connected with result code 4」
    mqttClient.on_connect = on_connect
    mqttClient.on_message = on_message_come
    mqttClient.connect(host, port, 60)
    mqttClient.loop_forever()
    print("connect end")


def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe("client")


# publish 消息
def on_publish(topic, payload, qos):
    mqttClient.publish(topic, payload, qos)


# 消息处理函数
def on_message_come(lient, userdata, msg):
    print(msg.topic + " " + ":" + str(msg.payload))
    op(msg.payload)


# subscribe 消息
def on_subscribe():
    print("subscribe start")
    mqttClient.subscribe("client", 1)
    mqttClient.on_message = on_message_come  # 消息到来处理函数
    print("subscribe end")


def op(ss):
    print("op start")
    print(ss)
    payload = json.loads(ss)
    print(payload)
    aid = payload['appid']
    r = os.popen('uci get cloud.cloud.name')
    APPID = str(r.read()).strip()
    print(aid)
    print(APPID)
    print(aid == APPID)
    if aid != APPID:
        return
    version = payload['version']
    if version == 1:
        # 下载
        download_file(payload)
    elif version == 3:
        running(payload)
    else:
        print("f")


def running(payload):
    file_name = payload['fileName']
    path = '~/zip/' + file_name + '/main.py'
    if os.path.exists(path):
        try:
            r = os.popen('python3 ' + path + '&')
            print(r.read())
            payload['version'] = 4
            payload['log'] = 'running'
            on_publish('gateway', payload, 1)
        except:
            payload['version'] = 6
            payload['log'] = 'failure'
            on_publish('gateway', payload, 1)
    else:
        payload['version'] = 6
        payload['log'] = 'failure'
        on_publish('gateway', payload, 1)


def download_file(payload):
    download_url = payload['path']
    file_name = payload['fileName']

    os.system('mkdir -p ~/dl')
    os.system('mkdir -p ~/zip')
    path = 'cd ~/dl && { curl -O ' + download_url + '; }'

    download = os.popen(path)
    print(download.read())

    if file_name != "":
        del_file = os.popen("rm -rf ~/zip/" + file_name)
        print(del_file.read())

    upzip_file = os.popen('unzip -o ~/dl/' + file_name + '.zip -d ~/zip')
    print(upzip_file.read())

    payload['version'] = 2
    payload['log'] = 'finnish'
    on_publish('gateway', str(payload), 1)
    print('download', file_name, 'finnish!')


def action():
    a, b, c, d = g_value()
    if a:
        on_mqtt_connect(c, d)


if __name__ == '__main__':
    action()
