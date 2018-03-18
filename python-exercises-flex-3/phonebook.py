 import pickle

phonebook_dict = {
   'alice': '703-493-1834',
   'bob': '857-384-1234',
   'elizabeth': '484-584-2923',
   'sarrah': '832-671-8977',
   'albert': '832-256-1800'
 }

book = phonebook_dict

def save_entries():
    file = open('phonebook.pickle', 'wb')
    pickle.dump(book, file)
    file.close()
    return

def load_entries():
    with open('phonebook.pickle', 'rb') as file:
        book = pickle.load(file)
    return
   
def intro():
   while True:
       print ("""Electronic Phone Book)
   =====================
   1. Look up an entry
   2. Set an entry
   3. Delete an entry
   4. List all entries
   5. Quit""")
       ans = int(input("Please select a menu option 1-5: "))
       if ans == 1:
           ent = input("Please enter an entry to lookup: ")
           ent = ent.lower()
          #  load_entries()
           if ent in book:
               print (book[ent])
           else:
               print ("Unfortunately, there is no listing for that person.")
       elif ans == 2:
           name = input("Please enter full name: ")
           name = name.lower()
           num = input("Phone number: ")
           book[name] = num
          #  save_entries()
           print ('An entry for ' + name.capitalize() + " was saved.")
           
       elif ans == 3:
           name = input("Which entry would you like to delete? ")
           name = name.lower()
          #  load_entries()
           del book[name]
           print("The entry for", name.capitalize(), "was deleted as requested.")
          #  save_entries()
       elif ans == 4:
          #  load_entries()
           for key, value in book.items():
               print ('{}: {}'.format(key, value))
       elif ans == 5:
           print ("Thanks, come again soon!")
           break
       else:
           print ("Please enter a number 1-5.")

load_entries()
intro()
save_entries() 