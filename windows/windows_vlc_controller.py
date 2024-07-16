'''
windows环境下控制vlc播放器进行各种操作的类
pip install python-vlc
'''

import os
import vlc
import logging

# 配置日志
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class win_vlc_controller:
    def __init__(self):
        self.vlc_instance = vlc.Instance('--no-xlib')
        self.vlc_player = self.vlc_instance.media_player_new()
        self.mlp = self.vlc_instance.media_list_player_new()
        self.media_list = self.vlc_instance.media_list_new()

    def _check_path(self, path):
        if not isinstance(path, str) or not os.path.exists(path):
            raise ValueError(f"The path '{path}' does not exist.")

    # 循环播放单个媒体文件
    def loop_play_single(self, file_path):
        try:
            self._check_path(file_path)
            self.vlc_player.set_fullscreen(True)
            media = self.vlc_instance.media_new(file_path)
            # 设置媒体循环播放
            media.parse()
            # 解析媒体资源定位符
            media.get_mrl()
            # 设置循环播放
            media.add_option('input-repeat-1')
            self.vlc_player.set_media(media)
            self.vlc_player.play()
        except Exception as e:
            logger.error(f"Failed to play file: {file_path}. Error: {e}")

    # 循环播放文件夹中的所有媒体文件
    def loop_play_folder(self, file_folder):
        try:
            if not all(isinstance(p, str) and os.path.exists(p) for p in file_folder):
                raise ValueError("One or more paths in the list do not exist.")
            self.vlc_player.set_fullscreen(True)
            for path in file_folder:
                self.media_list.add_media(self.vlc_instance.media_new(path))
            self.mlp.set_media_list(self.media_list)
            self.mlp.set_media_player(self.vlc_player)
            self.mlp.set_playback_mode(vlc.PlaybackMode.loop)
            self.mlp.play()
        except Exception as e:
            logger.error(f"Failed to play folder: {file_folder}. Error: {e}")

    # 暂停播放
    def single_pause(self):
        try:
            self.vlc_player.pause()
        except Exception as e:
            print(f'暂停失败：{e}')

    def folder_pause(self):
        try:
            self.mlp.pause()
        except Exception as e:
            print(f'暂停失败：{e}')

    # 继续播放
    def single_resume(self):
        try:
            self.vlc_player.play()
        except Exception as e:
            print(f'继续播放失败：{e}')

    def folder_resume(self):
        try:
            self.mlp.play()
        except Exception as e:
            print(f'继续播放失败：{e}')

    # 停止播放
    def single_stop(self):
        try:
            self.vlc_player.stop()
        except Exception as e:
            print(f'停止播放失败：{e}')

    def folder_stop(self):
        try:
            self.mlp.stop()
        except Exception as e:
            print(f'停止播放失败：{e}')

    # 播放上一视频
    def play_previous(self):
        try:
            self.mlp.previous()
        except Exception as e:
            print(f"播放上一视频失败：{e}")

    # 播放下一视频
    def play_next(self):
        try:
            self.mlp.next()
        except Exception as e:
            print(f"播放下一视频失败：{e}")