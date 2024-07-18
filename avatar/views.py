from django.http import JsonResponse

def Avatar(request):
    if request.method == 'GET':
        personagens = [
            'id',
            'naçoes'
        ]
        return personagens(JsonResponse)
    
