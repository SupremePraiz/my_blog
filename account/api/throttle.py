from rest_framework.throttling import UserRateThrottle

class CommentListThrottle(UserRateThrottle):
    scope = 'comment-create'

class CommentDetailThrottle(UserRateThrottle):
    scope = 'comment-list'