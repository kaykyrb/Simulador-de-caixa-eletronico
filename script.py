print('-=' *15);
print('{:^30}'.format('BANCO PRIME'));
print('-=' *15);

money = int(input('Que valor você deseja sacar? R$ '));

total = money;
ballot = 100;
total_ballot = 0;

while True:
  if total >= ballot:
    total -= ballot;
    total_ballot += 1;
  else:
    if total_ballot > 0:
      print(f'Total de {total_ballot} de R$ {ballot}.');

    if ballot == 100:
      ballot = 50;
    elif ballot == 50:
      ballot = 20;
    elif ballot == 20:
      ballot = 10;
    elif ballot == 10:
      ballot = 5.
    elif ballot == 5:
      ballot = 2;
    elif ballot == 2:
      ballot = 1;
    total_ballot = 0;

    if total == 0:
      break;

print('=' *30);
print('Operção finalizada!\nVolte sempre ao BANCO PRIME!');
print('=' *30);

  





  
  

