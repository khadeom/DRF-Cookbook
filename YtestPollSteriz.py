from polls.serializers import PollSerializer
from django.contrib.auth.models import User
from polls.models import Poll

from django.contrib.auth.models import User

# user = User.objects.get(username="foo")
# print(user.username)
poll_serializer = PollSerializer(data={"question": "Mojito or Caipirinha?", "created_by": 1})

print(poll_serializer.is_valid())
# True

poll = poll_serializer.save()
for i in range(1000):print("?nsdjhjhdhuwu") 
print(poll)

