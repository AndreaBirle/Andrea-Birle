phrase= '''Buzăul este cel mai cald oraș din țară, arată un studiu la nivel european.
Autoritățile locale încearcă să facă temperaturile ridicate mai suportabile cu ajutorul copacilor.
Corespondenta RRA Cristina Moise transmite.'''
print(phrase[:len(phrase)//2]. translate(str.maketrans(" "," ")).upper().strip() + phrase[len(phrase)//2::-1].capitalize().translate(str.maketrans("","",',''')))

