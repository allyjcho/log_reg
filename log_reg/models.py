from django.db import models
import re

# model Manager
#     validator function
#     if password is not a confirm password
#     if email is not a good email

class UserManager(models.Manager):
    def validator(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(postData['fname']) < 2:
            errors['first_name'] = "First name must be at least 2 characters."
        if len(postData['lname']) < 2:
            errors['last_name'] = "Last name must be at least 2 characters."
        # if '@' not in postData['email']:
        # if '.net' or '.com' or '.org'
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = ("Email must be a valid email.")
        if len(postData['pw']) < 8:
            errors['pw'] = "Password must be at least 8 characters."
        if postData['pw'] != postData['confpw']:
            errors['conf_password'] = "Password & confirm password must match."
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()

class Message(models.Model):
    message = models.CharField(max_length=255)
    poster = models.ForeignKey(User, related_name='messages', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class Comment(models.Model):
    comment = models.CharField(max_length=255)
    poster = models.ForeignKey(User, related_name='comments', on_delete = models.CASCADE)
    message = models.ForeignKey(Message, related_name='comments', on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)