import json
'''
def handler(event, context):
  print('received event:')
  print(event)
  
  return {
      'statusCode': 200,
      'headers': {
          'Access-Control-Allow-Headers': '*',
          'Access-Control-Allow-Origin': '*',
          'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
      },
      'body': json.dumps('Hello Python lambda - Jul 24, 24!')
  }
  
'''  
     
   
def handler(event, context):
  print('received event: ', event)
  get_raw_path    = "/picture/*"
  create_raw_path = "/postP"
  
  time = "Jul 27: 11 am"
  message = {"f_name":"AAAAAAA", "l_name":"BBBBBBBBBB"}
  
  if event['path'] == get_raw_path:
    # call database
    pid = event['queryStringParameters']['p_id']
    print ("Using GEEEEEEEETTTTT")
    print ("received number: ", pid, type(pid), int(pid)+5)
    print ('Hello from your new Amplify Python lambda GET !' + time)
    #return { "aaaaaaaaaaaaaaaaa": "bbbbbbbbb"  }
    #message = {"f_name":"AAAAAAA", "l_name":"BBBBBBBBBB"}
    # not worked:
    #return {"f_name":"AAAAAAA", "l_name":"BBBBBBBBBB"} 
    # worked
    return {
      'statusCode': 200,
      'headers': {
          'Access-Control-Allow-Headers': '*',
          'Access-Control-Allow-Origin': '*',
          'Access-Control-Allow-Methods': 'OPTIONS,POST,GET' }, 'body': json.dumps( message )#'Hello from your new Amplify Python lambda GET !' + time)
          }
    
          
          
  elif  event['path'] == create_raw_path:
    print ("Using POSSSSSSSSSST")
    
    body = json.loads(event['body'])
    f_name = body['f_name']
    l_name = body['l_name']
    print ("received names:  ",  f_name, l_name)
    print ('Hello from your new Amplify Python lambda- POST!'  + time)
    # return {"f_name_received": f_name}
    #worked
    return {
      'statusCode': 200,
      'headers': {
          'Access-Control-Allow-Headers': '*',
          'Access-Control-Allow-Origin': '*',
          'Access-Control-Allow-Methods': 'POST' }, 'body': json.dumps(message)
          }
    
          
  else:
    print ('Hello from your new Amplify Python lambda- POST!'  + time)  
    
    return {
      'statusCode': 200,
      'headers': {
          'Access-Control-Allow-Headers': '*',
          'Access-Control-Allow-Origin': '*',
          'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'  },  'body': json.dumps('Hello from your new Amplify Python lambda-Jul 25, 24 - 6 pm'  + time) }
