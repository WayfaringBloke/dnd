# Deli
## Mission
1. Cowboy explains job in car:
	- Trying to steal a red gem from probably the upstairs apartment.
	- (Cowboy is motivated by jeweller witnessing against one of his friends 7 years ago, and lost stone to him 5 years ago)
2. Casing
 Cohen and Wong
3. Action
	- Storm the back of the resturant, killing goons room by room
	- 6 in the building total + guy out front
4. Streets:
	- Guy pops out with shotgun tries to rob you
	- His buddies pop out to waste you
	- Shotgun, Mac1, Mac2, Long Gun
5. Bar Debrief


# [Map](https://excalidraw.com/#json=xgMIIPRl_JF1cCs1ob_dr,m9zYhlCSyjqThV65g_NFsg)
# Encounter 1

## Dining Area
- A narrow corridor leads up to a cramped dining area, with a bar & stools facing the wall.
- There's a large soda vending machine and a deli counter with a posh brit stood behind it. Called Roger Cohen.
- The resturaunt serves primarily deli food, but also hash browns and a smattering of british dishes (toad in the hole, full breakfast, bangers & mash, fish & chips). 
- In the drinks cabinet there's literally only two things: cans of OrangeLime, a popular soda, and Cold Leprechaun's Brew, a 50/50 mix of whiskey and strong black coffee. Fucking exclusivity deals.
- Gigantic Cash Only Sign
- **SECURITY:** Gun that fires through wall in narrow corridor

## Bathroom
- Occupied by 4th gang member being very sick.
- Sink on one wall, Toilet in the corner

## Pantry
- Heavy bags of flour, cornstarch, and various ingredients.
- A jarring amount of pickles. It smells entirely too much of pickles.
- Just ouside it in the coridoor is the opaque red stone in a display case (with alarmed sticker)

## Closet
- A mix of kitchen wear. 
- A few clean suits. 
- An SMG (d4a). 

## Kitchen
- All stainless steel. 
- Pots dangle from the ceiling above the central table
- In one corner there is 2 giant piles of potatoes, one peeled the other unpeeled
- Along the far wall a deep fat fryer quietly fizzling
- Strong smell of fish & raw beef (blood)
- Two cooks in there, one throws knives at you the other has a d4a pistol in his waistband

## Freezer
- Secured by a thick steel door
- Insulation blocks out noise from the outside
- Has 3 gangsters in there trying to get gems out of the bellies of pigs, cows, and fish.
- Blood spilled everywhere
- All 3 are wearing the white clean suits, bloodied. 
- Carrying a large machete/axe (d8) and pistols (d6)
- Shelves full of almost everything you saw on the menu, nothing is fresh prepared here.
- Central table holds a chopping board and a little tupperware where the bloody gems have been collected.

## Apartment
- Door locked
- Owner hiding upstairs, not going to fight you unless you make a problem of it. Called Wong. **WILL SILENT ALARM FREEZER GUYS TO COME**
- Painting on the wall with jewels in the eyes
- Push them in and under his bed pops open, Uncut Gem is in there

# Encounter 2
- Driving through west side slums to get to industrial where El Torro is.
- Carjacking, guy with a shotgun
- Pistol dude flanks

# Encounter 3
- Walk up see crap game outside played with cops
- Enter busy bar filled with working class looking people all chattering and drinking, bored
- Silence falls as players enter, fear
- Cowboy gives round on house and says mercs are with him
- The bar sells a steriod doped whisky
- Cowboy asks how many people you killed
- Takes gems, pays d2k creds per player
- Oppurtunity for players to ask cowboy about weirdness in setup
- THERE'S A PRICE ON YOUR HEAD, best lay low in the basement for tonight, owner wasn't rich so could only afford to tender your bounty for 48h
;)

# Encounter 4
Selling those jewels

# Assets 
![manager](https://github.com/WayfaringBloke/dnd/blob/main/assets/m1/manager.png?raw=true)![Ronald](https://github.com/WayfaringBloke/dnd/blob/main/assets/rnpc/Ronald.png?raw=true)
# Combat Dumps
```py
cohen_wong = [
    ne(n("l"), h(15), d(12), w(6), a(2), m(9)), # lead
    ne(n("m"), h(12), d(12), w(6), a(1), m(7)), # machete
    ne(n("p"), h(12), d(12), w(6), a(1), m(7)), # pistol
    ne(n("a"), h(8), d(15), w(8, True), a(0), m(6)), # smg (auto)
    ne(n("c"), h(20), d(10), w(8), a(2, False), m(11)), # cohen (revolver)
    ne(n("w"), h(5), d(12), w(2), a(0), m(3)) # wong (long nails)
]

carjack = [
		# far alley, brenm gun
    ne(n("l"), h(25), d(12), w(8, True), a(6, False), m(9)), 
    # mac 10 minion 1
    ne(n("m1"), h(1), d(14), wf(2), a(99), m(4)),
    # mac 10 minion 2
    ne(n("m2"), h(1), d(14), wf(2), a(99), m(4)),
    # pistol (flank)
    ne(n("p"), h(12), d(15), w(6), a(0), m(9)),
    # shotgun (point)
    ne(n("s"), h(15), d(14), w(6), a(2), m(10))
]
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTE3ODM2NzAyOSwxNjIwNTYxMTc0LDIzND
U4MTg5OCw0Njg5ODI2NjMsLTkzMTg3ODk2NCw3NjE3NDI0MCwy
MDE0OTIzNzE3LC0xNzIxMzQxNTA4LC0xMzk3MDMzOTUyLC05ND
M2MDY3OTUsLTExNzA5NzQ1ODAsLTIwNjcxNTA0NTAsNzc4OTYy
ODE4LDE5NTEyODI1MzEsMTI4MzE5MjMzMCwtMTMzMjc1Mzk1NC
wtMTc2MzYxMzYwOCwtMTAzNjU0MTA4NywxOTgxMzk4NTc3LDE0
NzU3MDE2ODhdfQ==
-->