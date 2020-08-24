from company.models import Category
import json


# カテゴリーの取得
def get_video_category():
    categories = Category.objects.all().values()
    list_categories = [category for category in categories]
    json_categories = json.dumps(list_categories, ensure_ascii=False)
    return json_categories


# カテゴリーをデータベースに新規作成（migrate時に実行）
def create_default_categories(sender, **kwargs):
    Category.objects.get_or_create(id=18, name='ショートムービー')
    Category.objects.get_or_create(id=27, name='教育')
    Category.objects.get_or_create(id=35, name='ドキュメンタリー')
