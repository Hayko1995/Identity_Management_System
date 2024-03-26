from djoser.serializers import UserSerializer as BaseUserSerializer
from rest_framework import serializers
from accounts.models import User
from blog.models import Actions, Projects, Groups, Roles


class CreateActionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Actions
        fields = ['name', 'title']

    def create(self, attrs):
        action = Actions.objects.create()
        action.name = attrs['name']
        action.title = attrs['title']

        action.save()
        return attrs


class CreateRolesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Roles
        fields = ['name']

    def create(self, attrs):
        roles = Roles.objects.create()
        roles.name = attrs['name']
        actions = Actions.objects.all()
        roles.actions_id = Actions.objects.get(name=attrs['actions']).id

        roles.save()
        return attrs


class CreateGroupsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Groups
        fields = ['name', 'role', 'parent_group']

    def create(self, attrs):
        group = Groups.objects.create(name=attrs['name'])
        group.roles_id = Roles.objects.get(name=attrs['role']).id
        group.parent_group = attrs['parent_group']
        group.save()
        return attrs


class CreateProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ['name', 'title', 'description']

    def create(self, attrs):
        projects = Projects.objects.create()
        projects.name = attrs['name']
        projects.title = attrs['title']
        projects.description = attrs['description']
        projects.save()
        return attrs


class BlogGetSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['action',]

    def create(self, attrs):
        if ('action' in attrs):
            action = Actions.objects.get(name=attrs['action'])
            print(action.name)

        return 'results'
