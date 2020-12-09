import json

from django.http      import JsonResponse
from django.views     import View

from post.models  import Post
from user.utils   import login_required


class LikeView(View):
    # 1. 인증
    @login_required
    def get(self, request, post_id):
        print("================= 좋아요 등록 절차 기동 =================")

        # 2. post 존재 확인, 사용자가 현재 post 에 이미 좋아요를 눌렀는지 확인
        try:
            post = Post.objects.get(id=post_id)
        except Post.DoesNotExist as e:
            print(f'Exception: {e}')
            return JsonResponse({"MESSAGE": "POST_DOES_NOT_EXIST"}, status=400)

        liker = request.user
        if post.liker.filter(id=liker.id).exists():
            return JsonResponse({'MESSAGE': 'LIKE_DUPLICATION'}, status=401)

        # 3. DB에 데이터 작성
        try:
            post.liker.add(liker)  # 이렇게만 해도 중복을 거를 수 있음, try 통과해도 중간테이블에 중복데이터가 애초에 안들어감
        except Exception as e:
            print(f'Exception: {e}')
            return JsonResponse({"MESSAGE": "INVALID_PAYLOAD"}, status=400)

        # 4. 모든 과정 통과 -> 201 리턴
        print("================= 좋아요 등록 정상 종료 =================")
        return JsonResponse({'MESSAGE': 'SUCCESS'}, status=201)
