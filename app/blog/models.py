from django.db import models

# Create your models here.


class Actions(models.Model):
    name = models.CharField(max_length=100, blank=False, unique=True)
    title = models.CharField(max_length=255, blank=False)
    REQUIRED_FIELDS = ['name', "title"]

    def str(self) -> str:
        return self.name


class Roles(models.Model):
    name = models.CharField(max_length=100, blank=False, unique=True)
    actions = models.ForeignKey(
        Actions, on_delete=models.DO_NOTHING, related_name='actions', null=True, blank=True)
    REQUIRED_FIELDS = ['name']

    def str(self) -> str:
        return self.name


class Groups(models.Model):
    name = models.CharField(max_length=100, blank=False, unique=True)
    roles = models.ForeignKey(
        Roles, on_delete=models.DO_NOTHING, related_name='roles', null=True, blank=True)
    parent_group = models.CharField(max_length=100, blank=True)

    def str(self) -> str:
        return self.name


class Projects(models.Model):
    name = models.CharField(max_length=100, blank=False, unique=True)
    title = models.CharField(max_length=255, blank=False,
                             verbose_name='Display Name')
    description = models.CharField(max_length=255, blank=True)
    REQUIRED_FIELDS = ['name', 'title']

    def str(self) -> str:
        return self.name
