import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Person, Motorbike, Ride
from django.shortcuts import redirect

def get_json_data(request):
    return json.loads(request.body.decode("utf-8"))

@csrf_exempt
def person_view(request, person_id=None):
    """
    Handles GET (list all), POST (add new), PUT (update), and DELETE (remove) 
    operations for the Person model.
    """
    # List all persons or create a new person
    if request.method == "GET" and person_id is None:
        persons = list(Person.objects.values())
        return JsonResponse(persons, safe=False)
    
    elif request.method == "POST" and person_id is None:
        data = get_json_data(request)
        person = Person.objects.create(
            name=data["name"],
            date_of_birth=data["date_of_birth"]
        )
        return JsonResponse({
            "id": person.id,
            "name": person.name,
            "date_of_birth": person.date_of_birth
        }, status=201)

    # Handle update and delete for a specific person
    if person_id:
        try:
            person = Person.objects.get(id=person_id)
        except Person.DoesNotExist:
            return JsonResponse({"error": "Person not found"}, status=404)

        if request.method == "PUT":
            data = get_json_data(request)
            person.name = data["name"]
            person.date_of_birth = data["date_of_birth"]
            person.save()
            return JsonResponse({
                "id": person.id,
                "name": person.name,
                "date_of_birth": person.date_of_birth
            })
        
        elif request.method == "DELETE":
            person.delete()
            return JsonResponse({"message": "Person deleted successfully"}, status=204)

    return JsonResponse({"error": "Invalid request method or parameters"}, status=400)

@csrf_exempt
def motorbike_view(request, motorbike_id=None):
    """
    Handles all CRUD operations for Motorbike.
    - GET (without motorbike_id): Returns a list of all motorbikes.
    - GET (with motorbike_id): Returns details of a single motorbike.
    - POST: Creates a new motorbike.
    - PUT: Updates an existing motorbike.
    - DELETE: Deletes a motorbike.
    """
    # GET request for listing or retrieving a motorbike
    if request.method == "GET":
        if motorbike_id is None:
            # Return list of motorbikes
            motorbikes = list(Motorbike.objects.values())
            return JsonResponse(motorbikes, safe=False)
        else:
            # Return details of a specific motorbike
            try:
                motorbike = Motorbike.objects.get(id=motorbike_id)
                return JsonResponse({
                    "id": motorbike.id,
                    "name": motorbike.name,
                    "engine_capacity": motorbike.engine_capacity,
                    "description": motorbike.description,
                    "is_automatic": motorbike.is_automatic
                })
            except Motorbike.DoesNotExist:
                return JsonResponse({"error": "Motorbike not found"}, status=404)

    # POST request to create a new motorbike
    elif request.method == "POST":
        data = get_json_data(request)
        motorbike = Motorbike.objects.create(
            name=data["name"],
            engine_capacity=data["engine_capacity"],
            description=data["description"],
            is_automatic=data["is_automatic"]
        )
        return JsonResponse({
            "id": motorbike.id,
            "name": motorbike.name,
            "engine_capacity": motorbike.engine_capacity,
            "description": motorbike.description,
            "is_automatic": motorbike.is_automatic
        }, status=201)

    # PUT request to update an existing motorbike
    elif request.method == "PUT" and motorbike_id is not None:
        try:
            motorbike = Motorbike.objects.get(id=motorbike_id)
            data = get_json_data(request)
            motorbike.name = data["name"]
            motorbike.engine_capacity = data["engine_capacity"]
            motorbike.description = data["description"]
            motorbike.is_automatic = data["is_automatic"]
            motorbike.save()
            return JsonResponse({
                "id": motorbike.id,
                "name": motorbike.name,
                "engine_capacity": motorbike.engine_capacity,
                "description": motorbike.description,
                "is_automatic": motorbike.is_automatic
            })
        except Motorbike.DoesNotExist:
            return JsonResponse({"error": "Motorbike not found"}, status=404)

    # DELETE request to remove a motorbike
    elif request.method == "DELETE" and motorbike_id is not None:
        try:
            motorbike = Motorbike.objects.get(id=motorbike_id)
            motorbike.delete()
            return JsonResponse({"message": "Motorbike deleted successfully"}, status=204)
        except Motorbike.DoesNotExist:
            return JsonResponse({"error": "Motorbike not found"}, status=404)

    # If the request method is not supported, return a 405 Method Not Allowed
    return JsonResponse({"error": "Method not allowed"}, status=405)

@csrf_exempt
def ride_view(request, ride_id=None):
    """
    Handles all CRUD operations for Ride.
    - GET (without ride_id): Returns a list of all rides.
    - GET (with ride_id): Returns details of a single ride.
    - POST: Creates a new ride.
    - PUT: Updates an existing ride.
    - DELETE: Deletes a ride.
    """
    if request.method == "GET":
        if ride_id is None:
            # Return list of rides
            rides = list(Ride.objects.select_related('person', 'motorbike').values(
                "id",
                "person_id",
                "person__name",
                "motorbike_id",
                "motorbike__name",
                "is_favourite"
            ))
            return JsonResponse(rides, safe=False)
        else:
            # Return details of a specific ride
            try:
                ride = Ride.objects.select_related('person', 'motorbike').get(id=ride_id)
                return JsonResponse({
                    "id": ride.id,
                    "person_id": ride.person_id,
                    "motorbike_id": ride.motorbike_id,
                    "is_favourite": ride.is_favourite
                })
            except Ride.DoesNotExist:
                return JsonResponse({"error": "Ride not found"}, status=404)

    elif request.method == "POST":
        data = json.loads(request.body.decode("utf-8"))
        ride = Ride.objects.create(
            person_id=data["person_id"],
            motorbike_id=data["motorbike_id"],
            is_favourite=data["is_favourite"]
        )
        return JsonResponse({
            "id": ride.id,
            "person_name": ride.person.name,
            "motorbike_name": ride.motorbike.name,
            "is_favourite": ride.is_favourite
        }, status=201)

    elif request.method == "PUT" and ride_id is not None:
        try:
            ride = Ride.objects.get(id=ride_id)
            data = json.loads(request.body.decode("utf-8"))
            ride.person_id = data["person_id"]
            ride.motorbike_id = data["motorbike_id"]
            ride.is_favourite = data["is_favourite"]
            ride.save()
            return JsonResponse({
                "id": ride.id,
                "person_id": ride.person_id,
                "motorbike_id": ride.motorbike_id,
                "is_favourite": ride.is_favourite
            })
        except Ride.DoesNotExist:
            return JsonResponse({"error": "Ride not found"}, status=404)


    elif request.method == "DELETE" and ride_id is not None:
        try:
            ride = Ride.objects.get(id=ride_id)
            ride.delete()
            return JsonResponse({"message": "Ride deleted successfully"}, status=204)
        except Ride.DoesNotExist:
            return JsonResponse({"error": "Ride not found"}, status=404)

    # If the request method is not supported, return a 405 Method Not Allowed
    return JsonResponse({"error": "Method not allowed"}, status=405)

def index_view(request):
    return redirect('motorbike_list')