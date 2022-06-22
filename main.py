from pathlib import Path

# Standard method (without pathlib)
p1='files/abc.txt'
with open(p1,'r') as file:
  print(p1,file.read(),'\n')

# With Pathlib:
p2=Path('files/ghi.txt')
print(type(p1))
print(p2.name)
print(p2.stem)
print(p2.suffix)


if p2.exists():
  with open(p2,'r') as file:
    print(file.read(),'\n')
else:
  with open(p2,'w') as file:
    file.write('Content 3')

p3=Path('files')
print(p3.iterdir())
for item in p3.iterdir():
  print(item, type(item))

print(list(p3.iterdir()))
