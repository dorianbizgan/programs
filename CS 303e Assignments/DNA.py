#  File: DNA.py

#  Description: Find the longest sub_string that's shared
#               between two different strands of DNA

#  Student Name: Dorian Bizgan

#  Student UT EID: dab4567

#  Course Name: CS 303E

#  Unique Number: 51345

#  Date Created: 10/25/17

#  Date Last Modified: 10/25/17

def main ():
  # open file for reading
  in_file = open ("./dna.txt", "r")

  print("Longest Common Sequences")
  print()

  # read the number of pairs
  num_pairs = in_file.readline ()
  num_pairs = num_pairs.strip()
  num_pairs = int (num_pairs)

  mach = []

  # read each pair of dna strands
  for i in range (num_pairs):
    st1 = in_file.readline()
    st2 = in_file.readline()

    st1 = st1.strip()
    st2 = st2.strip()

    st1 = st1.upper ()
    st2 = st2.upper ()

    # order the strands by size
    if (len(st1) > len (st2)):
      dna1 = st1
      dna2 = st2
    else:
      dna1 = st2
      dna2 = st1

#    print(dna1, dna2)

    # get all substrands of dna2
    wnd = len (dna2)
    while (wnd > 1):
      start_idx = 0
      while ((start_idx + wnd) <= len(dna2)):
        sub_strand = dna2[start_idx: start_idx + wnd]
#        print (sub_strand,"here")
        # move the window by one
        start_idx += 1
        start_point = 0

        while start_point + len(sub_strand) <= len(dna1):
          if sub_strand == dna1[start_point:len(sub_strand)]:
              mach.append(sub_strand)
#          print(dna1[start_point:len(sub_strand)])
          start_point += 1
        last = len(dna1)

        while last - len(sub_strand) > 0:
          if sub_strand == dna1[last - len(sub_strand):last]:
              mach.append(sub_strand)
          last -= 1
      # decrease the window size
      wnd = wnd - 1
     #  print(mach)
    lng_mach = []
    for j in range(len(mach)):
        if len(mach[j]) == len(mach[0]) and mach[j] not in lng_mach:
            lng_mach.append(mach[j])

    if len(mach) == 0:
      print("Pair",i + 1,":","No Common Sequence Found")
      print()
    else:
  #formatting print statements for strings of same lengths
      print("Pair",i+1,": ", end="")
      for k in range(0,len(lng_mach)):
        print(lng_mach[k], end="\n         ")
      print()
  #reset the elements in the list
    del mach[:]

  # close the file
  in_file.close()

main()
