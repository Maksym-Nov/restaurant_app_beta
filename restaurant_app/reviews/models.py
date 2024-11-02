from django.db import models
from accounts.models import UserProfile
from menu.models import Dish

class Review(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE, related_name="reviews")
    rating = models.PositiveIntegerField(default=5)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.user.username} for {self.dish.name}"
