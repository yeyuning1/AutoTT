class AppSettings(object):
    def __init__(self, platformName=None, platformVersion=None, deviceName=None, appPackage=None,
                 appActivity=None):
        # 前置代码（启动参数）
        self.desired_caps = {
            # 启动的手机平台
            'platformName': platformName,
            # 启动的系统版本
            'platformVersion': platformVersion,
            # 启动的手机 设备名
            'deviceName': deviceName,
            # 启动的包
            'appPackage': appPackage,
            # 启动的页面
            'appActivity': appActivity
        }


app_settings = AppSettings(platformName='Android', platformVersion='8.0', deviceName='android 8')