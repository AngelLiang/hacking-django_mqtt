from django.dispatch import Signal

# mqtt 连接信号
mqtt_connect = Signal(providing_args=["client"])
# mqtt 预发布信号
mqtt_pre_publish = Signal(providing_args=["client", "topic", "payload", "qos", "retain"])
# mqtt 发布信号
mqtt_publish = Signal(providing_args=["client", "userdata", "mid"])
# mqtt 断开连接信号
mqtt_disconnect = Signal(providing_args=["client", "userdata", "rc"])
