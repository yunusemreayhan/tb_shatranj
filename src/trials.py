#!/usr/bin/python3

def mirror_square(sq2:int):
    sq2 = ((sq2 & 7) << 3) | (sq2 >> 3);
    return sq2

def test(sq:int):
    print("testing " + str(sq) + " " + str(mirror_square(sq)))

mirror = [[0 for i in range(64)] for j in range(64)]

def isAboveA1H8(sq:int):
    return ((sq >> 3) > (sq & 7))

def isOnA1H8(sq:int):
    return ((sq >> 3) == (sq & 7))

def mirrorTableValue(i, j):
    sq1:int=i
    sq2:int=j
    mirval = 1

    if (sq1 & 0x04):
        sq1 ^= 0x07
        sq2 ^= 0x07
    if (sq1 & 0x20):
        sq1 ^= 0x38
        sq2 ^= 0x38
    print("sq1: " + str(sq1) + " sq2: " + str(sq2))
    mirror[i][j] = 1;
    mirval = 1

    if (isAboveA1H8(sq1)):
        sq1 = mirror_square(sq1)
        sq2 = mirror_square(sq2)
        mirror[i][j] = -1
        mirval = -1
    elif (isOnA1H8(sq1)):
        if (isAboveA1H8(sq2)):
            sq2 = mirror_square(sq2)
            mirror[i][j] = -1
            mirval = -1
        elif (isOnA1H8(sq2)):
            mirror[i][j] = 0
            mirval = 0

    return i,j,sq1, sq2, mirval

"""
      if ((sq1 >> 3) > (sq1 & 7)) // if sq1 is above a1h8
      {
          sq1 = ((sq1 & 7) << 3) | (sq1 >> 3); // mirror according to a1h8
          sq2 = ((sq2 & 7) << 3) | (sq2 >> 3); // mirror according to a1h8
          mirror[i][j] = -1;
      }
      else if ((sq1 >> 3) == (sq1 & 7)) // if sq1 is on a1h8
      {
          if ((sq2 >> 3) > (sq2 & 7)) // if sq2 is above a1h8
          {
              sq2 = ((sq2 & 7) << 3) | (sq2 >> 3); // mirror sq2 according to a1h8
              mirror[i][j] = -1;
          }
          else if ((sq2 >> 3) == (sq2 & 7)) // if sq1 and sq2 are on a1h8
              mirror[i][j] = 0;
      }
      KK_map[i][j] = KK_init[tri0x40_init[sq1]][sq2];
    }
"""

test(1)
test(46)

for i in range(64):
    for j in range(64):
        print(mirrorTableValue(i, j))

for i in range(64):
    calc1 : int = i
    if ( i & 0x04):
        calc1 ^= 0x07
    if (i & 0x20):
        calc1 ^= 0x38

    print("i " + str(i) + " " + bin(i) + " " + str(calc1) + " " + str(mirrorTableValue(i, i)))

def dump_binary(bb:int, period:int):
    print("====================")
    toprint = bin(bb)[2:]
    print(toprint.zfill(64))
    for i in range(int(64/6)):
        temptoprint=bin(bb & 0xff)[2:]
        print(temptoprint.zfill(period))
        bb = bb >> period

mask_a1a8 = mask_a1h1 = 0
for i in range(5):
    mask_a1a8 = (mask_a1a8 << 6) | 0x38
    mask_a1h1 = (mask_a1h1 << 6) | 0x07

dump_binary(0x38, 6)
dump_binary(mask_a1a8, 6)
dump_binary(mask_a1h1, 6)
