from . import tigergraphconnect as tgconn

def db_conn(dbalias,dbtype,sqlquery):
    print('Making Connection :',dbtype,':',dbalias)
    if dbtype == 'tigergraph':
        createschema = tgconn.tigergraph(dbalias,sqlquery)
        return createschema