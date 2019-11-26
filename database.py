mport boto3


db_name = 'database-4'
db_storage = '20'
instanceclass = 'db.m5.xlarge'

def db_instance(db_name,db_storage,instanceclass):
int_data = int(db_storage)
client = boto3.client('rds')
response = client.create_db_instance(
DBInstanceIdentifier=db_name,
AllocatedStorage=int_data,
DBInstanceClass= instanceclass,#'db.m5.xlarge',
Engine='oracle-ee',
MasterUsername='datadata',
MasterUserPassword='admin1234',
prot = ''

)
response = client.describe_db_instances()
for data in response['DBInstances']:
db_instance_name = data['DBInstanceIdentifier'],
db_type = data['DBInstanceClass'],
db_storage = data['AllocatedStorage'],
db_engine = data['Engine'],
db_version = data['EngineVersion']
db_Status  = data['DBInstanceStatus']
db_mas = data['MasterUsername']
db_time = data['InstanceCreateTime']
db_n = data['DBName']
print ("DBInstanceIdentifier :",db_instance_name,'\n',
"Db_class type :",db_type,'\n',"AllocatedStorage :",db_storage,'\n',
"Engine_name :",db_engine,'\n',"Db_version:",db_version,'\n',"Db_Status :",db_Status,'\n',
"MasterUsername :",db_mas,'\n',"InstanceCreateTime :",db_time,'\n',
"DBName :",db_n)

return client

db_instance(db_name,db_storage,instanceclass)
