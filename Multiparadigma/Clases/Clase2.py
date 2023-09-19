#tupla ordenada e inmutable y permite datos duplicados
#tupla=(1,2,3)
#print(tupla)
#print(type(tupla))
#tupla[0]=5

#tupla=1,2,('a','b'),3
#print(tupla)
#print(tupla[2][0])

#tupla=1,2,3
#lista=list(tupla)
#lista.append(4)
#tupla=tuple(lista)
#print(tupla)
#for t in tupla:
#    print(t)
#x,y,z,a=tupla
#print(x,y,z,a)
#tupla=(2,2,2,1,2,4,6)
#print(tupla)
#print(type(tupla))
#print(tupla.count(2))
#print(tupla.index(1))

#lista ordenada, mutable, permite duplicados
#lista=[1,2,3,4]
#print(lista)
#lista2=list("4567")
#print(lista2)
#lista3=[1,"2",["12",23,2]]
#print(lista3[2][0])

#print(lista3[-1])
#lista3[2]=10
#print(lista3)
#lista4=[1,2,3,4,5,6,7]
#print(lista4[0:2])
#print(lista4[2:6])
#lista4[0:3]=(0,0,0)
#print(lista4)
#lista3+=lista4
#print(lista3)
#for l in lista3:
#    print(l)

#for index,l in enumerate(lista3):
#    print(index,l)

#lista1=(1,2,3)
#lista2=("A","B","C")
#for l1,l2 in zip(lista1,lista2):
#   print(l1,l2)

#for i in range(0,len(lista3)):
#    print(lista3[i])

#lista3.append(4)
#lista3.extend([2,1])
#lista3.insert(1,4)
#lista3.pop(1)
#lista3.reverse()
#lista3.sort()
#lista3.sort(reverse=True)


#Set
#set={1,2,4,3,1,2}
#print(set)
#set.add(9)
#print(set)

#set2 = set([2,3,4,5,2,1])
#print(set)
#lista=("a","b")

#for s in set2:
#    print(s)

#s1={1,3,4}
#s2={3,5,6}
#print(s1 ^ s2)

#s1.add(1)
#s1.remove(4)
#s1.discard(7)
#s1.pop()
#s1.clear()