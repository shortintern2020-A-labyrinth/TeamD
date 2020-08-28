from company.models import Video, Urls, Company
from django.core.files.storage import FileSystemStorage
import os
from company.util.models import get_company_id
from translate.gtrans import Translate


# 中原航大
# 動画情報のバリデーション
def video_post_validation(data):
    try:
        # 投稿する上で必要な情報に対してバリデーション
        if data['title'] == '' or data['description'] == '' or data['category_id'] == '' or data['token'] == '':
            return False
        if data['title'] == None or data['description'] == None or data['category_id'] == None or data['token'] == '':
            return False
        return True
    except:
        return False


# 中原航大
# 素材動画のバリデーション
def material_video_validation(data):
    try:
        videos = data.getlist('movies')
        # 動画の有無でバリデーションをかける
        if len(videos) == 0:
            return False
        if videos == None:
            return False
        return True
    except:
        return False


# 中原航大
# 投稿動画の取得
def get_video_post(company_id):
    videos = Video.objects.filter(company_id=company_id).values()
    list_videos = [video for video in videos]
    return list_videos


# 中原航大
# 動画の保存
def save_video(video):
    fs = FileSystemStorage()
    file_name = fs.save(video.name, video)
    file_path = 'tmp/{}'.format(file_name)  # fs.url(file_name)だと文字コードが変わってしまう
    return file_path


# 中原航大
# 動画の削除
def remove_video(file_path):
    fs = FileSystemStorage()
    file_name = file_path[4:] # パスからファイル名だけ取り出す tmp/hoge.mp4 → hoge.mp4
    fs.delete(file_name)


# 中原航大
# 詳細を英語翻訳する
def create_english_description(data):
    c = Translate()
    description = '------ english ------ '
    split_text = data['youtube']['description'].split('\n')
    # 1文ずつ翻訳する
    for text in split_text:
        if text != '':
            description += '{}'.format(c.translate(text))
        else:
            description += ''
    return description


# 中原航大
# パラメータ取得
def get_request_data(request):
    post = request.POST # postリクエストの中身
    data = {} 
    company = {}
    c = Translate() # 翻訳するためのクラス

    data['token'] = '' if not 'token' in post else post['token'] # トークン取得

    # YouTube投稿に関する部分
    data['youtube'] = {}
    data['youtube']['title'] = '' if not 'title' in post else post['title']
    if data['youtube']['title'] != '' and len(data['youtube']['title']+"/{}".format(c.translate(data['youtube']['title']))) <= 80:
        data['youtube']['title'] += ' - {}'.format(c.translate(data['youtube']['title']))

    '''
    花火職人の技術/Fireworks craftsmanship
    '''

    _, company_id = get_company_id(data['token'])
    company_id = None if company_id is None else int(company_id)
    company = Company.objects.get(id=company_id)
    urls = [url for url in Urls.objects.filter(company_id=company_id).values()]
    data['youtube']['description'] = ''
    data['youtube']['description'] += '{}'.format(company.name)
    data['youtube']['description'] += '{}'.format(company.description)
    for url in urls:
        if url['type'] == 1:
            data['youtube']['description'] += 'ホームページ：{}'.format(url['value'])
        elif url['type'] == 2:
            data['youtube']['description'] += '商品購入はこちら：{}'.format(url['value'])
        elif url['type'] == 3:
            data['youtube']['description'] += '体験応募はこちら：{}'.format(url['value'])
    data['youtube']['description'] += '' if not 'description' in post else '{}'.format(post['description'])
    english_description = create_english_description(data)
    data['youtube']['description'] = english_description

    '''
    ほげほげ
    私達の企業は主にものづくりをしています

    ホームページ：hoge_company_url
    商品購入はこちら：fuga_ec_url

    花火は難しいです------ english ------
    Hogehoge
    Our company is mainly manufacturing

    Home page: hoge_company_url
    Click here to purchase the product: fuga_ec_url

    Fireworks is difficult
    '''
    data['youtube']['category_id'] = '' if not 'category_id' in post else post['category_id']
    data['youtube']['keywords'] = '' if not 'keywords' in post else post['keywords']
    data['youtube']['paths'] = []  # [path1, path2,,,,] # 加工後の動画のパスが入る

    insert_text = [] if not 'insert_text' in post else post.getlist('insert_text')
    insert_position = [] if not 'insert_position' in post else post.getlist('insert_position')
    videos = [] if not 'movies' in request.FILES else request.FILES.getlist('movies')

    # 動画加工に関する部分
    data['edit'] = {}
    data['edit']['insert'] = {}
    data['edit']['material'] = {}
    data['edit']['material']['paths'] = [save_video(video) for video in videos]  # [path1, path2,,,]
    data['edit']['insert']['text'] = [text if text == '' else '{} -- {}'.format(c.translate(text),text) for text in insert_text]
    data['edit']['insert']['position'] = [position for position in insert_position]  # 'bottom', 'center', ・・・
    data['edit']['insert']['paths'] = []  # [newpath1, newpath2, ・・・]
    data['edit']['combine'] = {}
    data['edit']['combine']['paths'] = []

    # 削除するファイルのパス配列 [path1, path2 ,,,,]
    data['delete'] = data['edit']['material']['paths']

    return data


# 中原航大
# 投稿したビデオをデータベースに追加
def set_video_post(data):
    _, company_id = get_company_id(data['token'])
    company_id = None if company_id is None else int(company_id)
    if company_id != None:
        video = Video(name=data['youtube']['title'], description=data['youtube']
                      ['description'], youtube_url='hoge/fuga.com', company_id=company_id,category_id=int(data['youtube']['category_id']))
        video.save()
