from threading import Thread

import motor_driver

def on_server_loaded(server_context):
    t = Thread(target=motor_driver.update_axis_1, args=())
    t.setDaemon(True)
    t.start()
