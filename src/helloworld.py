# AUTOGENERATED! DO NOT EDIT! File to edit: nbs/helloWorld.ipynb (unless otherwise specified).

__all__ = ['hello1']

# Cell
from awsSchema.apigateway import Event, Response

# Cell
def hello1(event, *args):
  print(Event.parseBody(event))
  return Response.returnSuccess()