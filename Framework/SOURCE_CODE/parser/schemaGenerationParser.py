import Framework.SOURCE_CODE.db_connect.tigergraph as tc
import sys
import yaml

gsql_path = "C:/work/YouTube Content/tigergraph/Framework/USER_CODE/gsql/"
yml_path = "C:/work/YouTube Content/tigergraph/Framework/USER_CODE/Workflow/"

def create_schema(gsqlQuery):
    print('Creating Schema')
    try:
        hostname = data['host']
        username = data['username']
        password = data['password']
        graphname = data['graphname']
        apiToken = data['apiToken']
        connObject = tc.TigergraphConect(host=hostname,graphname=graphname,
                                     username=username,
                                     password=password,apiToken=apiToken)
        tgConn = connObject.connect()
        print('Creating Connection URl :',tgConn.gsUrl)
        createschema = tgConn.gsql(query=gsqlQuery)
        print('Schema Created',createschema)

    except Exception as e:
        raise

try :
    yaml_file = yml_path + sys.argv[1] +'.yml'
    f = open(yaml_file,'r')
    data = yaml.safe_load(f)
    print(data,type(data))
    gsqlObject = data['gsql']

    for gsql in gsqlObject:
        gsqlFile = gsql_path + gsql
        gsqlFileOpen = open(gsqlFile,'r')
        gsqlQuery = gsqlFileOpen.read()
        #print(gsqlQuery)
        create_schema(gsqlQuery)

except Exception as e:
    raise
