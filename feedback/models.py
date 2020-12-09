from django.db import models


class Feedback(models.Model):
    FEEDBACK_CATEGORIES = [
        ('Report an issue', 'Report an issue'),
        ('Feature Request', 'Feature Request'),
        ('Improvement', 'Improvement'),
        ('General Comments', 'General Comments'),
    ]
    category = models.CharField(
        max_length=100,
        choices=FEEDBACK_CATEGORIES,
        verbose_name='Feedback Category',
    )
    comments = models.CharField(max_length=300)
    