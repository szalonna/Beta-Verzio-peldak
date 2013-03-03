#!/usr/bin/env python
# -*- coding: utf-8 -*-

# A fenti két sor meghatározza, hogy milyen környezetben fusson
# Linux alatt, illetve hogy a fájl UTF-8-as kódolásban van.

# A kód két prím kereső osztályt tartalmaz és egy metódust,
# amellyel 

# Külső modul betöltése
import math
from datetime import datetime

# Globális változók deklarálása
hatar    = 1000		# A határ alatti prímszámokat keresi meg
listazza = False	# Listázza-e ki a talált prímeket

# Ősosztályunk
class Alaposztaly():

	# Alaposztály kontruktora
	# Minden egyed szintű metódusnak tartalmaznia kell
	# a példányt, mint első paraméter
	def __init__(self, felsohatar):
		self.felsohatar = felsohatar
		self.primek     = []

	def countprimes(self):
		return len(self.primek)

	def getname(self):
		return "Alaposztaly"

# Eratoszthenészi szita osztály
# Az Alaposztályból származtatjuk
class Eratosthenes(Alaposztaly):

	def getname(self):
		return "Eratosthenes"

	def execute(self):

		# A for ciklus nem a klasszikus for ciklus, talán a 
		# foreach-hoz hasoníltható leginkább, mivel egy listán
		# fut végig a ciklus változónk. A range() egy számlistát
		# állít elő a 0 - megadott érték között.
		for i in range(self.felsohatar - 1):
			# A tömbök használhatóak, mint stack-ek.
			# Itt feltöltjük a tömböt a 2 - felső határ
			# közötti értékekkel
			self.primek.append(i + 2)

		# Aktuális prím szám indexe, amelynek a többszöröseit
		# fogjuk eltávolítani
		p = 0

		# Amíg a tömbnek van nem vizsgált eleme
		while p < len(self.primek) - 1:

			# A maradék tömbön akarunk végigmenni, így vesszük a
			# prím utáni elem indexét
			t = p + 1
			# Végig futunk a maradék tömbön
			while t < len(self.primek):
				# Ha az aktuális elemünk osztható a prímünkkel,
				# eltávolítjuk a listából
				if self.primek[t] % self.primek[p] == 0:
					self.primek.pop(t)
				t = t + 1
			p = p + 1

class Speedy(Alaposztaly):

	def getname(self):
		return "Speedy"

	def execute(self):
		# A kettes mindenképpen prím
		self.primek.append(2)

		# Az aktuálisan vizsgálandó értéket fogjuk ebben tárolni
		curr = 3
		while(curr <= self.felsohatar):
			# Tételezzük fel, hogy alapvetően a vizsgált számunk
			# prím
			prim  = True
			# A szám négyzetgyökénél nagyobb prímekre nem végzünk
			# vizsgálatot
			lim = math.sqrt(curr)

			# Végigfutunk az eddig megtalált prímeken
			for p in self.primek:

				# Ha a vizsgált szám osztható az aktuális prímmel,
				# akkor az nem prím
				if curr % p == 0:
					prim = False
					break

				# Ha az akutális prím már nagyobb, mint a négyzetgyöke
				# a vizsgált elemnek, értelmetlen a további keresés
				if p > lim:
					break

			# Ha prím, akkor hozzáadjuk a prímek listájához
			if prim:
				self.primek.append(curr)

			# Megnöveljük a vizsgálandó számot
			curr += 1

#######################################################

# Globális függvény az osztályok használatához
# Paraméterként nem az osztály egyik példányát adjuk át,
# hanem az osztályt magát, amit példányosítunk majd.
def searchPrimes(className):

	# Példányosítás paraméterrel
	pf = className(hatar)

	# Időmérés
	startTime = datetime.now()

	# Prímkeresés
	pf.execute()

	# Időmérés befejezése
	endTime = datetime.now()

	# Ha listázni kívánjuk a talált prímeket, akkor
	# egyesével kiírjuk
	if listazza:
		for i in pf.primek:
			print i

	# Kis összefoglaló szöveg
	print "Talált prímek száma a " \
			+ pf.getname() \
			+ " osztállyal " \
			+ str(hatar) + "-ig: " \
			+ str(pf.countprimes())

	print "Mindezt " \
		  + str(endTime - startTime) \
		  + " idő alatt."

#######################################################

searchPrimes(Eratosthenes)

print "------"

searchPrimes(Speedy)