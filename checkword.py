def intersect(seq1, seq2):
      res = [] # Start empty
      for x in seq1:
            if x in seq2:
                  res.append(x) # Add to end
      return res

intersect('eat','cat')
