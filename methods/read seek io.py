# with open('sample.txt.txt', 'r')as f:
#     f.seek(9)                  # !seeking the characters
#     print(f.tell())           #/ telling the seek range
#     data = f.read(9)          #? reading after the seeking the characters
# print(data)
with open('sample.txt.txt', 'w')as f:
    f.write("hello abhijeet")
    f.truncate(11)
