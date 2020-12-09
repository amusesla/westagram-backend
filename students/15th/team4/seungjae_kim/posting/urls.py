#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.urls   import path
from posting.views import PostsView, CommentsView, LikesView

urlpatterns =                  [
    path('',PostsView.as_view()),
    path('/<int:posting_pk>/comments',CommentsView.as_view()),
    path('/<int:posting_pk>/likes', LikesView.as_view()),
]