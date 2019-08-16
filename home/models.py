import uuid
from django.db import models
from users.models import CustomUser

# Create your models here.

class AjoGroup(models.Model):
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField()
    amount = models.IntegerField()
    capacity = models.IntegerField()
    is_searchable = models.IntegerField(default=1 ,choices=((0, 'No'), (1, 'Yes')))


    def __str__(self):
        return self.name

class AjoMembers(models.Model):
    member = models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name='participant')
    group = models.ForeignKey(AjoGroup,on_delete=models.CASCADE)
    savings = models.IntegerField(default=0)

    def __str__(self):
        return self.member.email
    
class AjoGenerator(models.Model):
    Uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name='guser')
    group = models.ForeignKey(AjoGroup,on_delete=models.CASCADE,related_name='group')\

    def __str__(self):
        return self.user.email
