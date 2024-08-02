from django.db import models
import uuid
from django.core.exceptions import ValidationError

class Tag(models.Model):

    class TagType(models.TextChoices):
        TECHNOLOGY = 'TECH', 'Technology'
        EDUCATION = 'EDU', 'Education'
        ENTERTAINMENT = 'ENT', 'Entertainment'
        HEALTH = 'HEA', 'Health'
        LIFESTYLE = 'LIFE', 'Lifestyle'

    tag_id = models.UUIDField(primary_key=True, default=uuid.uuid4)

    name = models.CharField(
        max_length=50,
        choices=TagType.choices,
        default=TagType.LIFESTYLE,
        unique=True
    )

    def __str__(self):
        return self.get_name_display()
 

class Post(models.Model):
    post_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    author = models.UUIDField(default=uuid.uuid4)
    content = models.CharField(max_length=10000)
    title = models.CharField(max_length=300)

    POST_TYPE = (
        ('t', 'Thread'), 
        ('p', 'Post'), 
        ('c', 'Comment')
    )
    post_type = models.CharField(max_length=1, choices=POST_TYPE, blank=False)
    parent_type = models.CharField(max_length=1, choices=POST_TYPE, blank=True, null=True)
    
    parent_post = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='child_posts')
    
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    tag = models.ManyToManyField(Tag, blank=True)

    def clean(self):
        super().clean()

        # Custom validation
        # if self.post_type != 't' and self.tag.exists():
        #     self.tag.clear()
        #     raise ValidationError("Tags are only allowed for posts of type 'Thread'.")

        
        # Validate parent post
        if self.post_type == 't' and self.parent_post is not None:
            raise ValidationError("Posts of type 'Thread' cannot have a parent post.")
        
        # Validate parent type
        if self.post_type == 't' and self.parent_type is not None:
            raise ValidationError("Posts of type 'Thread' cannot have a parent type.")