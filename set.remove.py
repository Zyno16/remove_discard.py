myset = set()
myset.add("ahmed")
myset.add("amr")
myset.add("ehab")
myset.add(123)
myset.add(True)
myset.add("asad")
print(myset)
myset.remove(True)
myset.remove(123)
myset.remove("ehab")
print(myset) #if you try to remove value not exicte the code will blow up
myset.discard(33) #this discard is remove the value but if i snot exicte the code not blow up
           
