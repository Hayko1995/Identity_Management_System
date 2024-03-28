from djoser.serializers import UserSerializer as BaseUserSerializer
from rest_framework import serializers
from accounts.models import User
import json
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
        roles = Roles.objects.create(name=attrs['name'])
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
        projects = Projects.objects.create(name=attrs['name'])
        projects.title = attrs['title']
        projects.description = attrs['description']
        projects.save()
        return attrs


class BlogGetSerializer(serializers.ModelSerializer):
    class Meta:
        fields = []

    def create(self, attrs):
        results = {}

        if 'action' in attrs:
            action = Actions.objects.get(name=attrs['action'])
            role = Roles.objects.get(id=action.id)
            groups = Groups.objects.get(roles=role.id)
            results['action'] = str(action.toDict())
            results['role'] = str(role.toDict())
            results['groups'] = str(groups.toDict())

        if 'role' in attrs:
            role = Roles.objects.get(name=attrs['role'])
            groups = Groups.objects.get(roles=role.id)
            results['role'] = str(role.toDict())
            results['groups'] = str(groups.toDict())

            return results

        if 'group' in attrs:
            groups = Groups.objects.get(name=attrs['group'])
            results['groups'] = str(groups.toDict())

            return results

        if 'project' in attrs:
            project = Projects.objects.get(name=attrs['project'])
            results['project'] = str(project.toDict())

            return results

        return results
