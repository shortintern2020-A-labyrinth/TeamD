# このMiddlewareが発動するのはcompanyに対するリクエストだけかもしれない
# TODO: これは要調査
class AuthMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # 前処理
        self.process_request(request)
        # ビューの処理
        response = self.get_response(request)
        # 後処理
        self.process_response(request, response)

        return response

    # ここにloguin確認処理を実装する
    def process_request(self, request):
        if 'Authorization' not in request.headers:
            print("not headers!!! error")

        # tokenを取得
        token = request.headers['Authorization']

        # sessionからvalueを取得
        token_time = request.sessions[token]

        # tokenが失効しているかどうかを確認

        # falseならerrorでレスポンス返却

        pass

    def process_response(self, request, response):
        pass
