# from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Robot


@method_decorator(csrf_exempt, name='dispatch')
class AddRobot(View):
    def post(self, request):
        data = json.loads(request.body.decode("utf-8"))
        r_model = data.get('model')
        r_version = data.get('version')
        r_serial = f'{r_model}-{r_version}'
        r_created = data.get('created')

        robot_data = {
            'serial': r_serial,
            'model': r_model,
            'version': r_version,
            'created': r_created
        }

        if len(robot_data['model']) > 2:
            return JsonResponse(data={'message': 'invalid model'}, status=400)

        if len(robot_data['version']) > 2:
            return JsonResponse(data={'message': 'invalid version'}, status=400)

        robot = Robot.objects.create(**robot_data)

        message = {
            'message': f"{robot.serial} has been added to the database"
        }

        return JsonResponse(data=message, status=201)
