from xml.etree.ElementTree import tostring

with open('numbers.txt', 'w') as file:
    for i in range(100):
        file.write(str(i)+"\n")

cnt=0
sum=0
with open('numbers.txt', 'r') as file:
    for line in file:
        sum+=int(line.strip())
        cnt+=1

print(sum , sum/cnt)
