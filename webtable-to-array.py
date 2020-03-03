import lxml.html
markup = lxml.html.fromstring('''<html><body>
<table width="600">
    <tr>
        <td width="50%">0,0,0</td>
        <td width="50%">0,0,1</td>
    </tr>
    <tr>
        <td>0,1,0</td>
        <td>0,1,1</td>
    </tr>
</table>
<table>
    <tr>
        <td>1,0,0</td>
        <td>1,<blink>0,</blink>1</td>
        <td>1,0,2</td>
        <td><bold>1</bold>,0,3</td>
    </tr>
</table>
</body></html>''')

tbl = []
rows = markup.cssselect("tr")
for row in rows:
  tbl.append(list())
  for td in row.cssselect("td"):
    tbl[-1].append(td.text_content())

print(tbl)
#[[u'0,0,0', u'0,0,1'],
# [u'0,1,0', u'0,1,1'],
# [u'1,0,0', u'1,0,1', u'1,0,2', u'1,0,3']]
print('######')
print(tbl[:2])

print('######')
for i in tbl:
    print(*i[-1:])

print('######')
for i in tbl:
    print(*i)

print('######')
print(*tbl, sep='\n')