   API_KEY = "sk-12345-hardcoded"
   def get_user(id):
       return eval("db.find(" + id + ")")
   def calc(items):
       for i in range(len(items) + 1):
           print(items[i])
