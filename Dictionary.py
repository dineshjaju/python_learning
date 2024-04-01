dummy_dict = dict()
dummy_dict = {"Dinesh":36 , "Poojitha" : 36 , "Advaith" : 6 , "Mihira" : 4}

print(dummy_dict)
print(dummy_dict.get("Dinesh"))


phone_book = {"Batman": 468426,
              "Cersei": 237734,
              "Ghostbusters": 44678}
print(phone_book["Cersei"])
print(phone_book.get("Ghostbusters"))


# Removing item

phone_book = {"Batman": 468426,
              "Cersei": 237734,
              "Ghostbusters": 44678}
print(phone_book)

del phone_book["Batman"]
print(phone_book)