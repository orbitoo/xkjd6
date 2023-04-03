# path = "D:/RIMEDATA/opencc/"
# file = "JPVariants.txt"
# output = "JPVariantsRev.txt"
# with open(path+file, 'r') as f:
#     with open(path+output, 'w') as out:
#         for line in f:
#             line = line.strip()
#             a, b = line.split("\t")
#             out.write(b + "\t" + a + "\n")

import opencc
converter = opencc.OpenCC('s2t')
converter.convert("启")
