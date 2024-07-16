'''
windows环境下控制各项系统操作
'''

import os
import comtypes.client
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

class win_sys_controller:

    #关机命令
    def close_windows(self):
        try:
            os.system('shutdown /s /t 0')
        except Exception as e:
            print(f"关机失败:{e}")

    # 调整windows音量
    def adjust_windows_volume(self, is_reduce, vp):
        comtypes.CoInitialize()
        sessions = AudioUtilities.GetSpeakers()
        interface = sessions.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = interface.QueryInterface(IAudioEndpointVolume)
        current_volume_db = volume.GetMasterVolumeLevel()
        if is_reduce:
            new_volume = current_volume_db - vp
        else:
            new_volume = current_volume_db + vp
        volume.SetMasterVolumeLevel(new_volume, None)

    # def search_web(self, key):
        # str_key = command.replace("搜索_", "")
        # url = f"https://www.baidu.com/s?wd={str_key}"
        # response = requests.get(url)
        # if response.status_code == 200:
        #     soup = BeautifulSoup(response.text, 'html.parser')
        #     results = soup.find_all('div', {'class': 'result c-container'})
        #     for i, result in enumerate(results[:5], start=1):
        #         print(f"123->Result {i}:")
        #         print(f"123->{result.get_next()}")