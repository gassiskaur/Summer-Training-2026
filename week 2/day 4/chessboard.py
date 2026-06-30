
wpawn='\u2659'
bpawn='\u265F'

for outer_index in range(8):


    for inner_index in range(8):


        if outer_index== 1 :
            print(wpawn, end=" ")
 
        elif outer_index== 6 :
            print(bpawn, end=" ")
      
        else :
            if (outer_index+ inner_index)% 2 ==0:
                print ("\u25A0", end=" ")
            else :
                print("\u25A1", end=" ")

    
    print()