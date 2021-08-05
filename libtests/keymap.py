"""
    按键映射
"""
import platform
import threading
import time

# import commons
import hmi_driver

# 全功能键1
M1 = "M1"
# 全功能键2
M2 = "M2"
# 上
UP = "UP"
# 下
DOWN = "DOWN"
# 左
LEFT = "LEFT"
# 右
RIGHT = "RIGHT"
# OK
OK = "OK"
# power
POWER = "POWER"
# ALL
ALL = "ALL"
# 关机
SHUTDOWN = "SHUTDOWN"
# 开机完成（用于更新后自动开机）
APO = "APO"


class KeyEvent:
    HMI_MAP = {
        "UP": UP,
        "DOWN": DOWN,
        "RIGHT": RIGHT,
        "LEFT": LEFT,
        "OK": OK,
        "M1": M1,
        "M2": M2,
        "PWR": POWER,
        "ALL": ALL,
        "STDN": SHUTDOWN,
        "APO": APO,
    }

    HOST_MAP = {
        59:  M1,    # ,
        60:  M2,    # .
        111: UP,    # arrow up
        116: DOWN,  # arrow down
        113: LEFT,  # arrow left
        114: RIGHT, # arrow right
        36:  OK,    # Enter
        108: POWER, # Right_Alt
        105: ALL    # Right_Ctrl
    }

    def __init__(self):
        self._target = None
        self._lock = threading.RLock()

    def _compat(self, event):
        """
            兼容性适配,根据当前的环境返回键码
        :param event:
        :return:
        """
        if platform.processor() != 'armv7l' and not isinstance(event, str):
            key_code = event.keycode
            if key_code in self.HOST_MAP:
                return self.HOST_MAP[key_code]
        else:
            if event in self.HMI_MAP:
                return self.HMI_MAP[event]
        print("没有被处理的按键事件: ", event)
        return event

    @staticmethod
    def _run_shutdown():
        # 屏幕转交回32
        hmi_driver.stopscreen()
        hmi_driver.shutdowning()  # 请求32关机
        hmi_driver.stophmi()
        # commons.startPlatformCMD("sudo shutdown -t 0")  # 请求全志关机

    def onKey(self, event):
        """
            在有按键时间发生时回调
        :param event:
        :return:
        """
        with self._lock:
            if self._target is None or not callable(self._target):
                print("没有按键事件处理目标")
                return

            # 开始处理按键的兼容性传递
            event = self._compat(event)

            if event == SHUTDOWN:
                print("在keymap.py中拦截到关机事件，将会直接进行软件关闭与关机")

                threading.Thread(target=self._run_shutdown).start()
                return

            self._target(event)  # 调用按键事件处理目标处理事件

    def bind(self, target):
        """
            绑定一个函数到本地接收按键事件
        :param target: 事件分发的目标
        :return:
        """
        with self._lock:
            self._target = target

    def unbind(self):
        """
            解绑事件回调到函数的映射
        :return:
        """
        with self._lock:
            self._target = None


key = KeyEvent()  # 单例模式
