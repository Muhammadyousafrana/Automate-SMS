# from twilio.rest import Client
#
# account_sid = 'ACe23e05cabcee1ae3885fbe85f855a066'
# auth_token = '[5d92df97826ae5f206515c0fa059f5aa]'
# client = Client(account_sid, auth_token)
#
# message = client.messages.create(
#     messaging_service_sid='MG6c1974a0cf640eea7897309c75012a1b',
#   body='hi wassup bro',
#   to='+923191217498'
# )
#
# print(message.sid)

from twilio.rest import Client

account_sid = 'ACe23e05cabcee1ae3885fbe85f855a066'
auth_token = '5d92df97826ae5f206515c0fa059f5aa'
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='+18159499093',
  body='hello abdulahad',
  to='+923191217498'
)

print(message.sid)
