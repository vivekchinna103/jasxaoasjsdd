from unittest import result
import pyodbc
from django.conf import settings
from casestudy.cognitivesearch import runindexer

connection={
    'default': {
        'ENGINE': 'mssql',
        "NAME": "case-study-db",
        "USER": "dbadmin",
        "PASSWORD": "db@admin12345",
        "HOST": 'case-study-poc.database.windows.net',
        'Trusted_Connection': 'yes',
        'OPTIONS': {
          'driver': 'ODBC Driver 17 for SQL Server',}
    }
}

#connection= pyodbc.connect('Server=tcp:case-study-poc.database.windows.net,1433;Initial Catalog=case-study-db;Persist Security Info=False;User ID=dbadmin;Password=db@admin12345;MultipleActiveResultSets=False;Encrypt=True;TrustServerCertificate=False;Connection Timeout=30;')
#Driver={ODBC Driver 17 for SQL Server};Server=tcp:assessmentserverget.database.windows.net,1433;Database=newvivekdb;Uid=dbadmin;Pwd={Admin123};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;
def get_file(id):
    try:
        cursor= connection.cursor()
        result=cursor.execute(f"select FileName from [dbo].[case_studies] where id={id}")
        file_name=cursor.fetchone()
        file_name = result[0] if result else None

        cursor.close()
        connection.close()
        return file_name
    except Exception as e:
        print(f"file name not found:{e}")

def add_data(name,account,vertical,solution,sof,status,dep,remarks,meta,file,rating):
    try:
        cursor=connection.cursor()
        query=f"Insert into [dbo].[case_studies](CaseStudyName,Account,Vertical"\
            f",SolutionName,ServiceOfferingMapping,Status,Dependency,Remarks,MetaData,FileName,Rating) values"\
            f"('{name}','{account}','{vertical}','{solution}','{sof}','{status}','{dep}','{remarks}','{meta}','{file}','{rating}')"
        cursor.execute(query)
        runindexer() 
        connection.commit()
        cursor.close()
        connection.close()
        
    except Exception as e:
        print(f"Error occured:{e}")
def update_data(id, name, account, vertical, solution, sof, status, dep, remarks, meta, file, rating):
    try:
        cursor=connection.cursor()
        query=f"UPDATE [dbo].[case_studies] SET CaseStudyName='{name}', Account='{account}', Vertical='{vertical}', " \
                f"SolutionName='{solution}', ServiceOfferingMapping='{sof}', Status='{status}', Dependency='{dep}', " \
                f"Remarks='{remarks}', MetaData='{meta}', FileName='{file}', Rating='{rating}' WHERE id={id}"
        cursor.execute(query)
        runindexer()
        connection.commit()
        cursor.close()
        print("Updated")
        
    except Exception as e:
        print(f"Error occured: {e}")

def get_row(id):
    try:
        cursor=connection.cursor()
        query=f"select * from [dbo].[case_studies] where id={id}"
        result=cursor.execute(query)
        result=cursor.fetchone()
        result=result[0] if result else None
        connection.commit()
        cursor.close()
        return result
    except Exception as e:
        print(f"error occured:{e}")
def get_all():
    try:
        cursor= connection.cursor()
        result=cursor.execute(f"select * from [dbo].[case_studies]")
        return result
    except Exception as e:
        print(f"error occured:{e}")

def getaiFiltereddata(filename):
    cursor=connection.cursor()
    try:
        result=cursor.execute(f"select * from  [dbo].[case_studies] where FileName={filename}")
        return result
    except Exception as e:
        print(f"error occured at {e}")
