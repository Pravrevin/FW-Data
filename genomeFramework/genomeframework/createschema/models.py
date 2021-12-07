from django.db import models

class TigerGraphConnect(models.Model):
    dbalias = models.CharField(max_length=15,primary_key=True)
    dbtype = models.CharField(max_length=15,default='tigergraph')
    host = models.CharField(max_length=100,null=False)
    port = models.CharField(max_length=10,null=False)
    graphname = models.CharField(max_length=100,null=True,default='',blank=True)
    username = models.CharField(max_length=100,null=False)
    password = models.CharField(max_length=100,null=False)
    apitoken = models.CharField(max_length=100,default='',null=True,blank=True)

    def __str__(self):
        data = self.host + '_' + self.dbalias
        return data

