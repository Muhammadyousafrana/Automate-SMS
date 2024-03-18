# from twilio.rest import Client
#
# account_sid = 'place your twillo account sid'
# auth_token = '[place authentication token]'
# client = Client(account_sid, auth_token)
#
# message = client.messages.create(
#     messaging_service_sid='place message service id',
#   body='hi wassup bro',
#   to='+923191217498'
# )
#
# print(message.sid)

from twilio.rest import Client

account_sid = 'place accont sid'
auth_token = 'authentication token'
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='+18159499093',
  body='hello abdulahad',
  to='+923191217498'
)

print(message.sid)
