from asyncio import Transport
from ssl import VerifyMode
from azure.core.credentials import AzureKeyCredential
from azure.search.documents import SearchClient
import json
from azure.search.documents.indexes.models import  IndexingParameters,SearchIndexer
from dotenv import load_dotenv
load_dotenv()
from azure.core.pipeline.transport import RequestsTransport
endpoint = 'https://case-study-search.search.windows.net'
admin_key = 'DDghOcnFbOjOb7ipzZZBqa0xAuTkQVGtEWM9BWQZmXAzSeDtdMW7'
#endpoint="https://dlpractice.search.windows.net"
#admin_key="37jMB2DPlxnGcEbeDnB66vlnXpbOwCFSJVOU7yU8uPAzSeA66uzd"
index_name = 'dlcasestudy'
credential = AzureKeyCredential(admin_key)
transport=RequestsTransport()
search_client = SearchClient(endpoint=endpoint, index_name=index_name, credential=credential)
def oDataFilter(Account,Vertical,ServiceOfferingMapping,MetaData,Rating):
    filter_fields = {
    'Account': Account,
    'Vertical': Vertical,
    'ServiceOfferingMapping':ServiceOfferingMapping,
    'MetaData': MetaData,
    'Rating': Rating
    }

    #if (Vertical!=None):
    #   filter_expression= ("vertical eq '{Vertical}'").format(Vertical=Vertical)
    #result=search_client.search(search_text='',filter=filter_expression)
    #for i in result:
     #   val.append(dict(i))
    #json_data= json.dumps(val)
    val=[]
    filter_expression_list=[]
    account_value= filter_fields['Account']
    if account_value!=None:
        account_lower_value=account_value.lower()
    for field, values in filter_fields.items():
       if values is not None:
           if field=='Vertical' and values!="":
               filter_expression_list.append(f"{field} eq '{values}'")
               print("v")
           elif (field=="Account" and values!="") and (values==account_lower_value or values==account_value):
               filter_expression_list.append(f"{field} eq '{values}'")
               print(values)
           elif field=="ServiceOfferingMapping" and values!="":
               filter_expression_list.append(f"search.ismatchscoring('{values}', '{field}')")
               print("s")
           elif field=="MetaData" and  values!="":
               filter_expression_list.append(f"search.ismatchscoring('{values}', '{field}')")
               print("m")
           elif field=="Rating" and values!="":
               filter_expression_list.append(f"{field} ge '{values}'")
               print("r")
    filter_expression= ' and '.join(filter_expression_list)
    results= search_client.search(search_text='',filter=filter_expression)
    result_data = [dict(result) for result in results]
    json_data= json.dumps(result_data)
    return json_data
print(oDataFilter("Aflac",None,None,None,None))