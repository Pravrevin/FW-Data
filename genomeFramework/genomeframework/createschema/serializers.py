from rest_framework import serializers

dbhub = (
    ('tigergraph','tigergraph'),
    ('Oracle','Oracle'),
)

class DbSelectSerializer(serializers.Serializer):
    dbalias = serializers.CharField(max_length=15)
    dbtype = serializers.ChoiceField(choices = dbhub)
    sqlquery = serializers.CharField(max_length=100,default='')