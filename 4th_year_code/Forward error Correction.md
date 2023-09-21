# Introdcution

  

Welcome to the froward Error  Correction(FEC) of this section

  

FEC is a mechanism to recover lost packets on a link by sending extra “parity” packets for every group (N) of packets. As long as the receiver receives a subset of packets in the group (at-least N-1) and the parity packet, up to a single lost packet in the group can be recovered.

## simple parity

simple parity check implemented in python like the following:

  
  

```

import re

def parity_inject(data,ammount_of_parity_bits):

  modified_string = list(data)

  

  for id in range(amount_of_parity_bits):

      if id ==0:

        modified_string.insert(0,'A')

      random_index = random.randint(0, len(modified_string)-1)

      modified_string.insert(random_index, 'A')

  return ''.join(modified_string)

def cal_P(str_data):

  for j in range(len(str_data)):

    if str_data[j]=='A':

      #even

      if j + 1 < len(str_data) and str_data[j + 1:].count("1") % 2 == 0:

        modified_data = re.sub('A','1',str_data)

      else:

        modified_data = re.sub('A','0',str_data)

  

  return modified_data

cal_P(parity_inject("10011",4))

  

```
## Types