# このMiddlewareが発動するのはcompanyに対するリクエストだけかもしれない
from django.http import JsonResponse
from rest_framework import status
import time, datetime
from session.redis import SessionRedis

# 鎌塚直己
class AuthMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # ビューの処理
        response = self.get_response(request)
        return response

    # ここにlogin確認処理を実装する
    def process_view(self, request, view_func, view_args, view_kwargs):
        #ログインと会員申請、承認、ログアウトのAPIはログイン状態の確認取らない
        if request.path == "/api/company/login/" or request.path == "/api/company/register/" or request.path == "/api/company/logout/" or request.path == "/api/admin/accept/company/":
            return None
        else:
            return None
            if 'Authorization' not in request.headers:
                return JsonResponse(
                    {
                        'message': 'not headers!!! error'
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )

            # tokenを取得
            token = request.headers['Authorization']

            # sessionからvalueを取得
            sessionRedis = SessionRedis()
            str_time, company_id = sessionRedis.get(token)
            token_time = float(str_time)

            # tokenが失効しているかどうかを確認(1時間でタイムアウト)
            current_time = time.time()
            time_difference = current_time - token_time
            if time_difference > 3600:
                #セッション破棄
                sessionRedis.delete(token)
                return JsonResponse(
                    {
                        'message': 'session timeout!'
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )
            else:
                #セッション更新
                request.session[token] = time.time()

            return None
