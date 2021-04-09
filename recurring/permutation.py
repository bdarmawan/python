class PermutationClass:
    def permutation(self, input):
        if len(input) == 1:
            return input if isinstance(input, list) else [input]

        result = []
        for i in range(len(input)):
            first = input[i]
            rest = input[:i] + input[i + 1:]
            #print(f"first: {first} --- rest: {rest}")
            rest_permutation = self.permutation(rest)
            #print(f"first: {first} --- rest: {rest} --- rest_permutation:  {str(rest_permutation)}")
            for p in rest_permutation:
                result.append(first + p)
                #print(f"    {first} : {first + p}")
        return result

if __name__ == '__main__':
    pc = PermutationClass()
    #print(pc.permutation("ab"))
    print(pc.permutation("abc"))
    #print(pc.permutation(['a', 'b', 'c', 'd']))


"""
RESULT:

first: a --- rest: bc
first: b --- rest: c
first: b --- rest: c --- rest_permutation:  ['c']
    b : bc
first: c --- rest: b
first: c --- rest: b --- rest_permutation:  ['b']
    c : cb
first: a --- rest: bc --- rest_permutation:  ['bc', 'cb']
    a : abc
    a : acb
    
first: b --- rest: ac
first: a --- rest: c
first: a --- rest: c --- rest_permutation:  ['c']
    a : ac
first: c --- rest: a
first: c --- rest: a --- rest_permutation:  ['a']
    c : ca
first: b --- rest: ac --- rest_permutation:  ['ac', 'ca']
    b : bac
    b : bca

first: c --- rest: ab
first: a --- rest: b
first: a --- rest: b --- rest_permutation:  ['b']
    a : ab
first: b --- rest: a
first: b --- rest: a --- rest_permutation:  ['a']
    b : ba
first: c --- rest: ab --- rest_permutation:  ['ab', 'ba']
    c : cab
    c : cba


['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
"""