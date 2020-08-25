from company.models import Video
from django.core.files.storage import FileSystemStorage
import os


# 動画情報のバリデーション
def video_post_validation(data):
    try:
        if data['title'] == '' or data['description'] == '' or data['category_id'] == '':
            return False
        if data['title'] == None or data['description'] == None or data['category_id'] == None:
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


# 投稿動画の取得
def get_video_post(company_id):
    videos = Video.objects.filter(company_id=company_id).values()
    list_videos = [video for video in videos]
    return list_videos


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


# パラメータ取得
def get_request_data(request):
    post = request.POST
    data = {}

    data['youtube'] = {}
    data['youtube']['title'] = '' if not 'title' in post else post['title']
    data['youtube']['description'] = '' if not 'description' in post else post['description']
    data['youtube']['category_id'] = '' if not 'category_id' in post else post[
        'category_id']
    data['youtube']['keywords'] = '' if not 'keywords' in post else post['keywords']
    data['youtube']['files'] = []  # [{'name':'', 'path':''}]

    insert_text = [] if 'insert-text' in post else post.getlist('insert-text')
    insert_position = [
    ] if 'insert-position' in post else post.getlist('insert-position')
    videos = request.FILES.getlist('movies')

    data['edit'] = {}
    data['edit']['insert'] = {}
    data['edit']['material'] = {}

    # [{'name':hoge, 'path':'~.mp4'},{},{}]
    data['edit']['material']['files'] = [
        save_video(video) for video in videos]
    data['edit']['insert']['text'] = [
        text for text in insert_text]  # テキスト1, テキスト2, ・・・・
    data['edit']['insert']['position'] = [
        position for position in insert_position]  # 'bottom', 'center', ・・・
    data['edit']['insert']['files'] = []  # [newpath1, newpath2, ・・・]
    data['edit']['combine'] = {}
    # [{'name':'hoge', 'path':'hoge/fuga.mp4'}]
    data['edit']['combine']['files'] = []

    data['paths'] = []  # 削除するファイルのパス配列 [{'name':'', 'path':''}, {}, ・・・・]

    return data
