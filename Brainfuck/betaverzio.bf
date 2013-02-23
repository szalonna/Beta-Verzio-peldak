"Beta Verzio" szöveget akarjuk kiíratni

ASCII értékek:
66 101 116 97 32 86 101 114 122 105 111

Optimális cella kezdőértékek:
32 64 84 100 116 120

Mind néggyel osztható ezért lesz egy külső ciklusunk ami
négyszer fut le majd a megfelelő értékekkel növelünk cellákat
úgy hogy ezeket a kezdőértékeket kapjuk
Később ezeket a cellákat felhasználva egyszerűbben tudjuk 
előállítani a szükséges ASCII kódokat

###############################################################

++++  cella(0) = 4 ez lesz a külső ciklusváltozónk
[
  >   Következő cellára lépünk

  ++++  cella(1) = 4 ez lesz a belső ciklusaink változója
  [
    > ++    cella(2) nő kettővel
    > ++++  cella(3) nő néggyel
    << -    cella(1) csökken az értéke eggyel
  ]

  +++++ cella(1) = 5
  [
    >>> +++++   cella(4) nő öttel
    >   +++++ + cella(5) nő hattal
    <<<< -      cella(1) csökken eggyel
  ]

  +++ cella(1) = 3
  [
    >>>>> +++++ ++   cella(6) nő héttel
    >     +++++ ++++ cella(7) nő kilenccel
    <<<<<< -         cella(1) csökken eggyel
  ]

  >>>>>> ++ cella(7) nő kettővel
  <<<<<<< - cella(0) csökken eggyel
]

A cella(2:7) megfelelő kezdőértékekkel rendelkezik ahhoz hogy
kevés lépéssel ki tudjuk írni a "Beta Verzio" feliratot

>> átlépünk a cella(2)re

###############################################################

Innentől ugrálunk az előállított cellák között módosítjuk
értéküket majd kiírju a kimenetre

Kezdeti cellaértékek:

cella:  2 |  3 |  4  |  5  |  6 |  7
érték: 32 | 64 | 100 | 120 | 84 | 116

       Cella | régi :  új | Karakter
> ++ .     3 |   64 :  66 | B
> + .      4 |  100 : 101 | e
>>>  .     7 |  116       | t
<<< ---- . 4 |  101 :  97 | a
<< .       2 |   32       | ' '
>>>> ++ .  6 |   84 :  86 | V
<< ++++ .  4 |   97 : 101 | e
>>> -- .   7 |  116 : 114 | r
<< ++ .    5 |  120 : 122 | z
< ++++ .   4 |  101 : 105 | i
>>> --- .  7 |  114 : 111 | o