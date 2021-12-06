import pyTigerGraph as tg

class TigergraphConect:

    def __init__(self,host,graphname,username,password,apiToken):
        self.host = host
        self.graphname = graphname
        self.username = username
        self.password = password
        self.apiToken = apiToken


    def connect(self):
        conn = tg.TigerGraphConnection(host=self.host, graphname=self.graphname, username=self.username,
                                       password=self.password,
                                       restppPort="9000", gsPort="14240", gsqlVersion="", version="", apiToken=self.apiToken,
                                       useCert=True,
                                       certPath=None,
                                       debug=False, sslPort="443", gcp=False)
        return conn