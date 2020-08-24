# このMiddlewareが発動するのはcompanyに対するリクエストだけかもしれない
from django.http import JsonResponse
from rest_framework import status

# TODO: これは要調査
class AuthMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # ビューの処理
        response = self.get_response(request)
        return response

    # ここにlogin確認処理を実装する
    def process_view(self, request, view_func, view_args, view_kwargs):
        #ログインと会員申請のAPIはログイン状態の確認取らない
        if request.path == "/api/company/login/" or request.path == "/api/company/register/" or request.path == "/api/company/logout/":
            return None
        else:
            if 'Authorization' not in request.headers:
                return JsonResponse(
                    {
                        'message': 'not headers!!! error'
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )

            # tokenを取得
            print(request.path)
            token = request.headers['Authorization']

            # sessionからvalueを取得
            token_time = request.sessions[token]

            # tokenが失効しているかどうかを確認(1時間でタイムアウト)
            current_time = time.time()
            time_difference = current_time - token_time
            if time_difference > 3600:
                #セッション破棄
                request.session.clear()
                return JsonResponse(
                    {
                        'message': 'session timeout!'
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )
            else:
                #セッション更新
                request.sessions[token] = time.time()
            
            return None
