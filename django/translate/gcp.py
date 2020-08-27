# export GOOGLE_APPLICATION_CREDENTIALS=/~/credential.json
# でcredの設定が必要
from google.cloud import translate_v2 as translate
translate_client = translate.Client()

""" 利用例
    c = Translate()
    text = '今日も1日頑張ります！！！'
    print(c.translate(text))

    output: I&#39;ll do my best today as well! !! !!


    TODO: ' ←これが&#39;になってしまう
"""

class Translate():
    def __init__(self):
        self.client = translate.Client()
        # 英語に翻訳
        self.language = 'en'

    def translate(self, text):
        res = translate_client.translate(text, target_language=self.language)
        print(res)
        return res['translatedText']

c = Translate()
text = '今日も1日頑張ります！！！'
print(c.translate(text))
