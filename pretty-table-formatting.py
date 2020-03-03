from prettytable import PrettyTable

d1 = {
  "key1":["val1_1", "val1_2"],
  "key2":["val2_1", "val2_2"],
  "key3":["val3_1", "val3_2"],
  "key4":["val4_1", "val4_2"],
}

table = PrettyTable()

for key,val in d1.items():
  table.add_column(key, val)

print (table)
print (table.get_html_string(attributes={"size":"100%", "class":"MyTable"}))
