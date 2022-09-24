def lab11task13():

    def findAncestors(name, people):
        def loop(name, pairs, relatives):
            for pair in pairs:
                if name == pair[0]:
                    relatives.append(pair[1])
                    return loop(pair[1], pairs, relatives)
            return relatives
        rels = [name]
        return loop(name, people, rels)

    n = int(input())
    childToAncestorList = [input().split() for i in range(n - 1)]
    names = input().split()

    firstNameAnc = findAncestors(names[0], childToAncestorList)
    secondNameAnc = findAncestors(names[1], childToAncestorList)
    commonAncs = set(firstNameAnc) & set(secondNameAnc)

    print(firstNameAnc)
    print(secondNameAnc)
    if len(commonAncs) == 0:
        print('No such a Lowest Common Ancestor')
    else:
        print('Lowest Common Ancestor –', firstNameAnc[len(firstNameAnc) - 1])

"""
Входные данные

9
Alexei Peter_I
Anna Peter_I
Elizabeth Peter_I
Peter_II Alexei
Peter_III Anna
Paul_I Peter_III
Alexander_I Paul_I
Nicholaus_I Paul_I


Alexander_I Nicholaus_I
Peter_II Paul_I
Alexander_I Anna
"""
# demo
if __name__ == "__main__":
    lab11task13()
