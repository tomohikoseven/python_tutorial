# words = ["cat", "window", "defenestrate"]
users = {"cat":'inactive', "window":'active', "defenestrate":'inactive'}
for user, status in users.copy().items():
  if status == 'inactive':
    del users[user]

print(users)