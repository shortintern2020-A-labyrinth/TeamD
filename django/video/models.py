from company.models import Video


# バリデーション
def video_post_validation(data):
    try:
        video = Video()
        video.name = data['name'],
        video.description = data['description'],
        video.youtube_url = data['youtube_url'],
        video.company_id = data['company_id']

        video.clean_fields()

        return True
    except:
        return False
