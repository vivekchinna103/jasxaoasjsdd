from pydoc import Doc
from azure.core.credentials import AzureKeyCredential
from azure.search.documents import SearchClient
import json
from azure.search.documents.indexes.models import  IndexingParameters,SearchIndexer
from azure.core.pipeline.transport import RequestsTransport
from dotenv import load_dotenv
load_dotenv()
endpoint = 'https://case-study-search.search.windows.net'
admin_key="DDghOcnFbOjOb7ipzZZBqa0xAuTkQVGtEWM9BWQZmXAzSeDtdMW7"

index_name = 'azureblob-index1'
credential = AzureKeyCredential(admin_key)
transport=RequestsTransport(connection_verify=False)
search_client = SearchClient(endpoint=endpoint, index_name=index_name, credential=credential,transport=transport)
def aiFilter(tag):
    filter_fields = {
    'tag': tag,
    }

    #if (Vertical!=None):
    #   filter_expression= ("vertical eq '{Vertical}'").format(Vertical=Vertical)
    #result=search_client.search(search_text='',filter=filter_expression)
    #for i in result:
     #   val.append(dict(i))
    #json_data= json.dumps(val)
    val=[]
    filter_expression_list=[]
    tag_value= filter_fields['tag']
    #print(account_value)
    tag_lower_value=tag_value.lower()
    for field, values in filter_fields.items():
       if values is not None:
           if field=='tag' and values!="":
               filter_expression_list.append(f"search.ismatchscoring( '{values}','merged_content')")
    filter_expression= ' and '.join(filter_expression_list)
    results= search_client.search(search_text='',filter=filter_expression,select="metadata_storage_name,merged_content")
    result_data = []
    count=0
    for i in results:
        result_data.append(i['metadata_storage_name'])
        count=count+1
    return result_data
    #json_data= json.dumps(result_data)
    #return json_data
print(aiFilter("UI"))