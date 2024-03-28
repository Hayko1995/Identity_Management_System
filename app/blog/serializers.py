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
        try:
            action = Actions.objects.create(name=attrs['name'])
        except:
            return "item exist"
        action.title = attrs['title']

        action.save()
        return attrs


class CreateRolesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Roles
        fields = ['name']

    def create(self, attrs):

        try:
            roleId = Actions.objects.get(name=attrs['actions']).id
        except:
            return "role is missing"

        try:
            roles = Roles.objects.create(name=attrs['name'], actions_id=roleId)
        except Exception as e:
            print(e)
            return "item exist"

        roles.save()
        return "saved"


class CreateGroupsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Groups
        fields = ['name', 'role', 'parent_group']

    def create(self, attrs):
        try:
            roleId = Roles.objects.get(name=attrs['role']).id
        except:
            return "role is missing"
        try:
            group = Groups.objects.create(name=attrs['name'], roles_id=roleId)
        except:
            return "item exist"

        group.parent_group = attrs['parent_group']
        group.save()
        return attrs


class CreateProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ['name', 'title', 'description']

    def create(self, attrs):
        try:
            projects = Projects.objects.create(name=attrs['name'])
        except:
            return "item exist"
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
