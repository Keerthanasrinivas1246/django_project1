from rest_framework.decorators import api_view   # To mention the HTTP methods
from rest_framework.response import Response   #To display the JSON data
from rest_framework import status    # it works similar to message module of CRUD operation
from .models import *
from .serializers import *

@api_view(['GET','POST'])
def couple_create_read(request):
    if request.method == "GET":     #READ OPERATION
        data = couple.objects.all()  #pyhton format data
        serializer = coupleSerializer(data, many=True)      #serialization done
        return Response(serializer.data)     # It displays the serialized data 
    elif request.method =='POST':   #create operation
        serializer= coupleSerializer(data = request.data)   # requested to add the json using serializer
        if serializer.is_valid():     # it checks if it is valid code or not
            serializer.save()         #it saves the data
            return Response(serializer.data, status=status.HTTP_201_CREATED)        # it displays the created record with status
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)      # it displays the invalid data is there


@api_view(['GET','PUT','DELETE'])
def couple_update_delete(request,pk):
    try :
        nibba_nibbi = couple.objects.get(id=pk)
    except couple.DoesNotExist:    #specific
        return Response({'error': 'Couple not found'},
                         status=status.HTTP_404_NOT_FOUND
                        )
    if request.method == 'GET':
        serializer = coupleSerializer(nibba_nibbi)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = coupleSerializer(nibba_nibbi, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        nibba_nibbi.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

