import windows_sys_controller
import windows_vlc_controller
from flask import Flask

app = Flask(__name__)
vlc_controller = windows_vlc_controller()
sys_controller = windows_sys_controller()

# 解析get请求
@app.route('/<command>', methods=['GET'])
def handle_command_request(command):
    print(f"从请求中收到的字符串:{command}")
    if '关机' in command:
        sys_controller.close_windows()
        return '执行关机操作', 200
    elif '降低音量' in command:
        sys_controller.adjust_windows_volume(True, 5)
        return '降低音量', 200
    elif '增加音量' in command:
        sys_controller.adjust_windows_volume(False, 5)
        return '增加音量', 200
    elif '单播' in command:
        # 案例播放地址
        vlc_controller.loop_play_single('D:/videos/Gamet2k.mp4')
        return '单播视频', 200
    elif '播放文件夹' in command:
        folder = ['D:/videos/Gamet2k.mp4',
                  'D:/videos/电脑端连接配置.mp4',
                  'D:/videos/格姆特网站加载速度.mp4',
                  'D:/videos/手机端连接配置.mp4']
        vlc_controller.loop_play_folder(folder)
        return '播放文件夹', 200
    elif '暂停' in command:
        # vlc_controller.single_pause() # 单视频播放暂停
        vlc_controller.folder_pause() # 视频文件夹暂停播放
        return '暂停播放', 200
    elif '续播' in command:
        # vlc_controller.single_resume() # 单视频继续播放
        vlc_controller.folder_resume()  # 视频文件夹继续播放
        return '继续播放', 200
    elif '停止' in command:
        # vlc_controller.single_stop() # 单视频继停止播放
        vlc_controller.folder_stop()  # 视频文件夹停止播放
        return '停止播放', 200
    elif '上个视频' in command:
        vlc_controller.play_previous()
        return '播放上个视频', 200
    elif '下个视频' in command:
        vlc_controller.play_next()
        return '播放下个视频', 200
    else:
        return f"收到的请求字符串:{command}", 200

if __name__ == '__main__':
    # 开启服务器, 服务器ip自设
    app.run(host='192.168.3.186', port=4406, debug=True)