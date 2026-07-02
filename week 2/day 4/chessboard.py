wpawn = '\u2659'
bpawn = '\u265F'

wpieces = ['\u2656', '\u2658', '\u2657', '\u2655', '\u2654', '\u2657', '\u2658', '\u2656']
bpieces = ['\u265C', '\u265E', '\u265D', '\u265B', '\u265A', '\u265D', '\u265E', '\u265C']

for outer_index in range(8):

    for inner_index in range(8):

        if outer_index == 0:
            print(wpieces[inner_index], end=" ")

        elif outer_index == 1:
            print(wpawn, end=" ")

        elif outer_index == 6:
            print(bpawn, end=" ")

        elif outer_index == 7:
            print(bpieces[inner_index], end=" ")

        else:
            if (outer_index + inner_index) % 2 == 0:
                print("\u25A0", end=" ")
            else:
                print("\u25A1", end=" ")

    print()