meme_dict = {
            "CRINGE": "Coś wyjątkowo dziwnego lub zawstydzającego",
            "LOL": "Częsta reakcja na coś zabawnego",
            }
for i in range(5):
    word = input("Wpisz słowo, którego nie rozumiesz (używaj wielkich liter!): ")
    if word in meme_dict.keys():
        print(meme_dict[word])
    
else:
    # Co powinniśmy zrobić, jeśli słowo nie zostało znalezione?
    print("słowo nie zostało znalezione")
