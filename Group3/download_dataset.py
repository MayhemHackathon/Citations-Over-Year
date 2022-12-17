from __future__ import print_function
import os

PYOACORE_KEY = "RDGVzeO2d6jgNHFyaoXfupK9WSI5Bh4k"
os.environ["CORE_API_KEY"] = PYOACORE_KEY
import time
import swagger_client
import pyoacore
from pyoacore.rest import ApiException
from pprint import pprint
# create an instance of the API class
api_instance = pyoacore.ArticlesApi()
core_id = '42' # str | The id of the article

try:
    # Get articles by ID
    api_instance.articles_get_core_id_get(core_id)
except ApiException as e:
    print("Exception when calling ArticlesApi->articles_get_core_id_get: %s\n" % e)
