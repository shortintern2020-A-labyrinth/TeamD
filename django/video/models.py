from company.models import Video
from django.core.files.storage import FileSystemStorage
import os


# 動画情報のバリデーション
def video_post_validation(data):
    try:
        if data['title'] == '' or data['description'] == '' or data['category_id'] == '' or data['company_id'] == '':
            return False
        if data['title'] == None or data['description'] == None or data['category_id'] == None or data['company_id'] == None:
            return False
        return True
    except:
        return False


# 素材動画のバリデーション
def material_video_validation(data):
    try:
        videos = data.getlist('movies')
        if len(videos) == 0:
            return False
        if videos == None:
            return False
        return True
    except:
        return False


# 動画の保存
def save_video(video):
    file_info = {}
    fs = FileSystemStorage()
    file_name = fs.save(video.name, video)
    file_path = fs.url(file_name)
    file_info['name'] = file_name
    file_info['path'] = file_path
    return file_info


# 動画の削除
def remove_video(file_name):
    fs = FileSystemStorage()
    fs.delete(file_name)
