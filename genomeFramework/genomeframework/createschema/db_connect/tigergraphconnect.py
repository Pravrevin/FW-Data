from ..models import TigerGraphConnect
import pyTigerGraph as tg

query_path = "C:/work/YouTube Content/tigergraph/genomeFramework/genomeframework/createschema/query/"


def tigergraph(dbalias,sqlquery):
    print('Creating Tigergraph Schema')
    tgObject = TigerGraphConnect.objects.filter(dbalias=dbalias).values()
    conn = tg.TigerGraphConnection(host=tgObject[0]['host'], graphname=tgObject[0]['graphname'], username=tgObject[0]['username'],
                                   password=tgObject[0]['password'],
                                   restppPort="9000", gsPort=tgObject[0]['port'], gsqlVersion="", version="",
                                   apiToken=tgObject[0]['apitoken'],
                                   useCert=True,
                                   certPath=None,
                                   debug=False, sslPort="443", gcp=False)
    try:
        print(conn.gsUrl)
        gsql_path = query_path + 'gsql/'
        gsql_files= sqlquery.split(',')
        for gsql in gsql_files:
            f = open(gsql_path+gsql,'r')
            try:
                createschema = conn.gsql(query=f.read())
                print('Schema Created', createschema)
                return createschema
            except Exception as e:
                raise
    except Exception as e:
        raise