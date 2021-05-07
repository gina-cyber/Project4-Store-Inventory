#I still need to fix indentation issues. Also, it doesn't look like you are using SQLAlchemy to create your model and you're not importing anything. 
#I have Fields, which SQLAlchemy does not, so this may not run.


Project 4 Idea:
db = SqliteDatabase (inventory.db’)
Class Item(Model):
item_name = IntegerField(Unique = True)
item_price = IntegerField()
item_weight = IntegerField(Unique = True)
class Meta:
    database = db

def delete_item_weight (weight): weight.delete_instance()

items = {‘item-name’: Tea
               ‘item_price’: $2.99}
              {‘item_date’ = ‘12/2/2021’}

def add_items():
     for item in items:
         try:
             item.create (item_name = item[‘Tea’]
                                  item_price = item[‘price’]
                                  item_date = item (‘dates’))
          except Integrity Error: # if it does not fail,        save it
               inventory.save()
          else: # if it fails
               pass

def main_menu():
     print (‘Welcome’)
     program_run = input (press “R” to run program:’)
#i should probably say ‘s’ for start though 
    while True:
     Print(‘welcome’)

def search_items(item_name, item_price):
    return item.select().where(item.content.contains(name),
item.price == price
#maybe using if search_query is better?

for items in all_items:
print (Item name:, item_name)
print (‘Item name:’, item_price)
print (‘\n’)

                
Sent from my iPhone
