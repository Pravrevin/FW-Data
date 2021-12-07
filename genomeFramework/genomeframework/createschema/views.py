from .serializers import DbSelectSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .db_connect.db_connection import db_conn


class CreateSchema(APIView):

    def post(self,request):
        serializer = DbSelectSerializer(data=request.data)
        if serializer.is_valid():
            dbalias = serializer.data['dbalias']
            dbtype = serializer.data['dbtype']
            sqlquery = serializer.data['sqlquery']
            result = db_conn(dbalias, dbtype,sqlquery)
            print(result)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



