alfa_ge = 'აბგდევზთიკლმნოპჟრსტუფქღყშჩცძწჭხჯჰაბგდევზთიკლმნოპჟრსტუფქღყშჩცძწჭხჯჰ'
#alfa_en = 'abcdefghiklmnopqrstvxyzabcdefghiklmnopqrstvxyz'#

while True:
    ch = int(input("""\n
[ 1 ] დაშიფვრა
[ 2 ] დეშიფრაცია
[ 3 ] პროგრამიდან გამოსვლა\n
რომელი ოპერაცია გსურთ შეასრულოთ?""")) # მისი მეშვეობით ვირჩევთ თუ რომელი ოპერაცია უნდა შევასრულოთ

    if ch == 1: # თუ 1 აირჩევთ შესრულდება დაშიფვრის პროცესი
        value = input('\n[ შეიყვანე დასაშიფრი ტექსტი ] ') # ტექსტის ველი
        key = int(input('\n[ შეიყავენ გასაღები ] ')) # გასაღების ველი
        value_low = value.lower() # შეყვანილი ტექსტი გადაგვყავს დავალ რეგისტრში ეს მუშაობს მხოლოდ ინგლისურ ასოებზე
        v = '' # ცარიელი სტრიქონი

        for letter in value_low: # ტექსტს ვშლით სიმბოლოებად
            position = alfa_ge.find(letter) # ვეძებთ მათ ინდექსებს ანბანში
            new_posution = position + key # ვანიჭებთ ახალ პოზიციას მათ პოზიციას + გასაღები
            if letter in alfa_ge: # ვშლით ანბანს სიმბოლოებად
                v = v + alfa_ge[new_posution] # ცარიელ სტრიქონს ვამატებთ მიღებულ სიმბოლოებს  და ვიღებთ დაშიფრულ ტექსტს
            else:
                v = v + letter
        print(v)

    if ch == 2: # დეშიფრაცია აქაც სწორედ იამვეს ვაკეთებთ მხოლოდ პოზიის ინდექს ვაკლებთ შეყვანილ გასაღებს
        value = input('\n[ შეიყვანე დეშიფრაციისთვის ტექსტი ] ')
        key = int(input('\n[ შეიყავენ გასაღები ] '))
        value_low = value.lower()
        v = ''

        for letter in value_low:
            position = alfa_ge.find(letter)
            new_posution = position + (-key)
            if letter in alfa_ge:
                v = v + alfa_ge[new_posution]
            else:
                v = v + letter
        print(v)
    if ch == 3: # 3 იანის შეყვანის შემთხვევაშ გაითშება პროგრამა
        exit()
