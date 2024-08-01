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
  get_raw_path    = ""
  create_raw_path = "/postP"
  target_resource = '/picture/{pictureId}'
  
  time = "Jul 30: 11 am"
  message = {"f_name":"AAAAAAA", "l_name":"BBBBBBBBBB"}
  '''
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
   ''' 
          
          
  if event['resource'] == target_resource::

    # Extract the pictureId from the path parameters
    picture_id = event['pathParameters']['pictureId']
    
    # Convert the picture_id to an integer
    picture_id_int = int(picture_id)
    
    # Add 100 to the integer
    result = str(picture_id_int + 100 )
    
  
    print ('Hi from your new Amplify Python lambda: Aug 01: 3:05 pm '  + result)  
    
    return {
      'statusCode': 200,
      'headers': {
          'Access-Control-Allow-Headers': '*',
          'Access-Control-Allow-Origin': '*',
          'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'  },  'body': json.dumps('Hello from your new Amplify Python lambda-Jul 31, 24 - 3:00 pm: '  + result) }
  else: 
    print ("Using POSSSSSSSSSST")
    
    body = json.loads(event['body'])
    f_name = "George"#body['f_name']
    l_name = "Posttter"#body['l_name']
    print ("received names:  ",  f_name, l_name)
    print ('Hello from your new Amplify Python lambda- POST!'  + f_name + l_name)
    # return {"f_name_received": f_name}
    #worked
    return {
      'statusCode': 200,
      'headers': {
          'Access-Control-Allow-Headers': '*',
          'Access-Control-Allow-Origin': '*',
          'Access-Control-Allow-Methods': 'OPTIONS,POST,GET' }, 'body': json.dumps(message)
          }
    
          

          
