import re

result= dir(re)

#re module

str= "Python Kursu: Python Prpgramlama Rehberiniz | 40 Saat"

# re.finall()

# result = re.findall("Python",str)
# result = len(result)

# re.split()
# result = re.split(" ",str)
# result = re.split("R",str)

# re.sub()
# result = re.sub("\s","-",str)

# re.search()

result= re.search("Python",str) #match ojbesi
# result = result.span() #konumu
# result =result.start()
# result =result.end()

# result =result.group()
# result =result.string


#regular expression
""""
[ ] - Köseli parantezler arasina yazilan bütün karakterler
aranir.
[abc] => a :1 match
         ac:2 match
        Python: No matches

    [a-e] => [abcde]
    [1-5] => [12345]
    [0-39] => [01239]

    [^abc] => abc disindaki karakterler.
    [^0-9] => rakam olmayan karakterler.
"""
result = re.findall("[abc]",str)
result = re.findall("[sat]",str)
result = re.findall("[a-e]",str)
result = re.findall("[a-z]",str)
result = re.findall("[0-5]",str)
result = re.findall("[^abc]",str)
result = re.findall("[^0-9]",str)
"""
    .- Her hangi bir tek karakteri belirtir.

        ..=› a   : No match
            ab   : 1 match
            abc  : 1 match
            abcd : 2 matches

"""
# result = re.findall("...",str)
# result = re.findall("Py..on",str)
"""
        ^ - Belirtilen karakterlerle basliyor mu ?
        ^a =› a:1 match
              abc:1 match
              bac:No match

"""

# result= re.findall("^P",str)
"""
        $ - Belirtilen karakterlerle basliyor mu ?
        ^$ =› a:1 match
              lamba:1 match
              python:No match

"""
# result= re.findall("t$",str)
# result= re.findall("Saat$",str)
# result= re.findall("Saatt$",str)


"""
    * - Bir karakterin sifir ya da daha fazla sayida olmasini kontrol eder.
            ma*n =› mn:1 match
            man:1 match
            maaan:1 match
            main: No match (a' nin arkasindan n gelmiyor.)

"""

result = re.findall("Sa*t",str)

"""
    + - Bir karakterin bir ya da daha fazla sayida olmasini kontrol eder.
            ma*n =› No match
            man:1 match
            maaan:1 match
            main: No match (a' nin arkasindan n gelmiyor.)

"""
result = re.findall("Sa+t",str)

"""
    ? - Bir karakterin sıfır yada bir kez olmasini kontrol eder.
            ma*n =› No match
            man:1 match
            maaan:1 match
            main: No match (a' nin arkasindan n gelmiyor.)

"""
result = re.findall("Sa?t",str)

"""
    {} - Karakter sayisin1 kontrol eder.
            al{2} =› a karakterinin arkasina l karakteri 2 kez tekrarlamali.
            al{2,3} => a karakterinin arkasina l karakteri en az 2 en fazla 3 kez tekrarlamalı
            [0-9]{2,4} => en az 2 en cok 4 basamakli sayilar.
"""
result = re.findall("a{2}",str)
result = re.findall("[0-9]{2}",str)

"""
    -alternatif seçeneklerden birinin gerçeklesmesi gerekir.
         
            a|b => a ya da b

                cde =› no match
                ade =› 1 match
                acdbea => 3 match
"""
"""
        () - gruplamak için kullanilir.
             (a|b|c)xz => a, b, c karakterlerinin arkasina xz gelmelidir.
"""

result = re.findall("\APython",str)
result = re.findall("Saat\Z",str)

"""
        \ - Ozel karakterleri aramamizı saglar.
        \$a => $ karakterinin arkasina a karakterinin arar. Yani
               $ regular exp. engine tarafindan yorumlanmaz.

        \A - Belirtilen karakter string in basinda mi ?
               \the =› the string in basindami

        \z - Belirtilen karakter string in sonunda mi ?
               the\z =› the string in sonunda mi

        \b - Belirtilen karakter kelimenin in basinda ya da sonunda mI
             \bthe => the kelimenin in basinda mI?
             the\b => the kelimenin in sonunda mi?

        \B - Belirtilen karakter kelimenin in basinda ya da sonunda degil mi ?
            \Bthe => the kelimenin in basinda degil mi?
            the\B => the kelimenin in sonunda degil mi?

        \d - [0-9] ile ayna anlama gelir yani rakamlar arar.
              \d => 12abc34

        \D - [^0-9] ile ayni anlama gelir yani rakam olmayanlari arar.
             \D => 1ab44_50

        \s - Bo$luk karakterlerini arar.
        \S - Bosluk karakterleri disindakiler.
        \w - Alfabetik karakterler, rakamlar ve alt cizgi karakteri.
        \W - w nin tam tersi

"""


print(result)