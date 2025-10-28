from rest_framework.throttling import UserRateThrottle

class reviewListThrottle(UserRateThrottle):
    scope = "review-list"

class reviewCreateThrottle(UserRateThrottle):
    scope = "review-create"