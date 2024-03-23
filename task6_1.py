from random import randint


print(randint(1,100))
with open('scripts/file2.sh', 'w', encoding='utf-8') as f:
      print(randint(1,100), file=f)