from company.models import Video


# バリデーション
def video_post_validation(data):
    print(data)
    if data['title'] == '' or data['description'] == '' or data['category_id'] == '' or data['company_id'] == '' or len(data['movies']) == 0:
        return False
    if data['title'] == None or data['description'] == None or data['category_id'] == None or data['company_id'] == None or len(data['movies']) == 0:
        return False
    return True
