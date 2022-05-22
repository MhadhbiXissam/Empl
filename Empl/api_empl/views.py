from django.shortcuts import render
from django.http import JsonResponse as JsonResponse
from .models import Session , Employee
from django.views.decorators.csrf import csrf_exempt
import datetime , json
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework.response import Response 
from django.core.serializers.json import DjangoJSONEncoder
import traceback
import sys



@api_view(['GET', 'POST'])
def get_all_employe(request) : 
	jsondata = list()
	with Session() as session:
		all_employees = session.query(Employee).all()
		jsondata = [r.as_dict_response() for r in all_employees]
	return JsonResponse(jsondata , safe = False )

@api_view(['GET', 'POST'])
@csrf_exempt
def update_employee(request) : 
	if request.method == "POST"  : 
		request_data = request.POST.dict()
		if all (k in request_data for k in ('id', 'Name', 'Birthday', 'HiredOn', 'Position', 'Email', 'PhoneNumber', 'IsManager', 'Team')) : 
			try : 
				with Session() as session:

					selected_employee = session.query(Employee).get(request_data["id"])
					selected_employee.update(request_data)
					session.commit()
				return JsonResponse({"code" : 200 , "message" : "200 OK"})
			except Exception as exc : 
				return JsonResponse({"code" : 422 , "message" : "422 Unprocessable Entity"})
		else : 
			return JsonResponse({"code" : 400 , "message" : "400 Bad Request"}) 
	else  : 
		return JsonResponse({"code" : 405 , "message" : "405 Method Not Allowed"})


@api_view(['GET', 'POST'])
@csrf_exempt
def delete_employees(request) : 
	if request.method == "POST"  : 
		request_data = dict(request.POST.copy())
		print("---------------",request_data)
		if all (k in request_data for k in ('ids',)) : 
			try : 
				with Session() as session:
					if (request_data["ids"]) == ["all"] : 
						session.query(Employee).delete()
					else : 
						session.execute(Employee.__table__.delete().where(Employee.id.in_(request_data["ids"])))
					session.commit()
				return JsonResponse({"code" : 200 , "message" : "200 OK"})
			except Exception as exc : 
				return JsonResponse({"code" : 422 , "message" : "422 Unprocessable Entity"})
		else : 
			return JsonResponse({"code" : 400 , "message" : "400 Bad Request"}) 
	else  : 
		return JsonResponse({"code" : 405 , "message" : "405 Method Not Allowed"})


@csrf_exempt
@api_view(['GET', 'POST'])
def add_new_employees(request) : 
	if request.method == "POST"  :
		request_data = json.loads(*(dict(request.POST)["data"]))
		print("**************************",request_data )

		if all (k in request_data for k in ( 'Name', 'Birthday', 'HiredOn', 'Position', 'Email', 'PhoneNumber', 'IsManager', 'Team') ) : 
			try : 
				with Session() as session:
					e = Employee()
					e.from_json_request(request_data)
					session.add(e)
					session.commit()
				return JsonResponse({"code" : 200 , "message" : "200 OK"})
			except Exception as exc : 
				print(traceback.format_exc())
				return JsonResponse({"code" : 422 , "message" : "422 Unprocessable Entity"})
		else : 
			return JsonResponse({"code" : 400 , "message" : "400 Bad Request"}) 
	else  : 
		return JsonResponse({"code" : 405 , "message" : "405 Method Not Allowed"})


