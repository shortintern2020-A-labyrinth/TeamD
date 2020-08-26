from googletrans import Translator

class Translate():
    def __init__(self):
        self.client = Translator()
        # 英語に翻訳
        self.from_language = 'ja'
        self.target_language = 'en'

    def translate(self, text):
        res = self.client.translate(text, src=self.from_language, dest=self.target_language)
        return res.text

c = Translate()
text = '今日も頑張ります'
print(c.translate(text))
