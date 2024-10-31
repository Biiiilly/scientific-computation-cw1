""" 
    Your college id here: 02046683
    Template code for project 1, contains 7 functions:
    func2A, func2B, func2C, method1, method2: complete functions for part 1
    part1_test: function to be completed for part 1
    part2: function to be completed for question 2
"""


#----------------- Code for Part 1 -----------------#
def func2A(L,R):
    """
    Called by func2B
    """
    M = [] 
    indL,indR = 0,0
    nL,nR = len(L),len(R)

    for i in range(nL+nR):
        if L[indL][1]<R[indR][1]:
            M.append(L[indL])
            indL = indL + 1
            if indL>=nL:
                M.extend(R[indR:])
                break
        else:
            M.append(R[indR])
            indR = indR + 1
            if indR>=nR:
                M.extend(L[indL:])
                break
    return M

def func2B(X):
    """
    Called by method2
    """
    n = len(X)
    if n==1:
        return X
    else:
        L = func2B(X[:n//2])
        R = func2B(X[n//2:])
        return func2A(L,R)
    

def func2C(L,x):
    """
    Called by method2
    """
    istart = 0
    iend = len(L)-1

    while istart<=iend:
        imid = int(0.5*(istart+iend))
        if x==L[imid][1]:
            return L[imid][0]
        elif x < L[imid][1]:
            iend = imid-1
        else:
            istart = imid+1

    return -1000 


def method1(L,x):
    for ind,l in enumerate(L):
        if x==l:
            return ind        
    return -1000


def method2(L,x,flag=True):
    if flag:
        L2 = list(enumerate(L))
        Lnew = func2B(L2)
        return func2C(Lnew,x),Lnew
    else:
        return func2C(L,x)


def part1_test():
    """Part 1, question 2: investigate trends in wall times of methods 1 and 2.
    Use the variables inputs and outputs if/as needed.
    You may import modules within this function as needed, please do not import
    modules elsewhere without permission.
    """
    import random
    import time
    from matplotlib import pyplot as plt

    # Firstly, we fix the length of the list (i.e. the value of n).
    ns = [100, 10000]
    ms = list(range(10, 1000, 50))

    method1_times_n = []
    method2_times_n = []

    # Run over the loop
    for n in ns:
    
        # Initialize the list L and and stored data sets
        L = random.sample(range(1000000), n)
        method1_times = []
        method2_times = []

        for m in ms:

            sequence = random.sample(range(1000000), m)

            # Method1
            start_time = time.time()
            for x in sequence:
                method1(L, x)
            method1_times.append(time.time() - start_time)

            # Method2
            start_time = time.time()
            _, sorted_L = method2(L, sequence[0])
            for x in sequence:
                method2(sorted_L, x, flag=False)
            method2_times.append(time.time() - start_time)

        method1_times_n.append(method1_times)
        method2_times_n.append(method2_times)

    # Now, we fix the length of the sequence (i.e. the value of m).
    # We consider two cases: m=1 and m is large enough.
    ns1 = list(range(100, 1000, 50))
    ms1 = [10, 1000]

    method1_times_m = []
    method2_times_m = []

    # Run over the loop
    for m in ms1:

        sequence = random.sample(range(1000000), m)
    
        method1_times1 = []
        method2_times1 = []

        for n in ns1:

            # Initialize the list L and and stored data sets
            L = random.sample(range(1000000), n)

            # Method1
            start_time = time.time()
            for x in sequence:
                method1(L, x)
            method1_times1.append(time.time() - start_time)

            # Method2
            start_time = time.time()
            _, sorted_L = method2(L, sequence[0])
            for x in sequence:
                method2(sorted_L, x, flag=False)
            method2_times1.append(time.time() - start_time)

        method1_times_m.append(method1_times1)
        method2_times_m.append(method2_times1)

    fig, axs = plt.subplots(2, 2, figsize=(15, 12))

    axs[0, 0].plot(ms, method1_times_n[0], label='Method 1', marker='o')
    axs[0, 0].plot(ms, method2_times_n[0], label='Method 2', marker='o')
    axs[0, 0].set_title('Figure 1: Comparison for n=100')
    axs[0, 0].set_xlabel('the size of m')
    axs[0, 0].set_ylabel('Time (units)')
    axs[0, 0].legend()
    axs[0, 0].grid(True)

    axs[0, 1].plot(ms, method1_times_n[1], label='Method 1', marker='o')
    axs[0, 1].plot(ms, method2_times_n[1], label='Method 2', marker='o')
    axs[0, 1].set_title('Figure 2: Comparison for n=10000')
    axs[0, 1].set_xlabel('the size of m')
    axs[0, 1].set_ylabel('Time (units)')
    axs[0, 1].legend()
    axs[0, 1].grid(True)

    axs[1, 0].plot(ns1, method1_times_m[0], label='Method 1', marker='o')
    axs[1, 0].plot(ns1, method2_times_m[0], label='Method 2', marker='o')
    axs[1, 0].set_title('Figure 3: Comparison for m=10')
    axs[1, 0].set_xlabel('the size of n')
    axs[1, 0].set_ylabel('Time (units)')
    axs[1, 0].legend()
    axs[1, 0].grid(True)

    axs[1, 1].plot(ns1, method1_times_m[1], label='Method 1', marker='o')
    axs[1, 1].plot(ns1, method2_times_m[1], label='Method 2', marker='o')
    axs[1, 1].set_title('Figure 4: Comparison for m=1000')
    axs[1, 1].set_xlabel('the size of n')
    axs[1, 1].set_ylabel('Time (units)')
    axs[1, 1].legend()
    axs[1, 1].grid(True)

    plt.subplots_adjust(hspace=0.4)
    plt.show()

    outputs = None
    return outputs


#----------------- End code for Part 1 -----------------#


#----------------- Code for Part 2 -----------------#

def part2(A1,A2,L):
    """Part 2: Complete function to find amino acid patterns in
    amino acid sequences, A1 and A2
    Input:
        A1,A2: Length-n strings corresponding to amino acid sequences
        L: List of l sub-lists. Each sub-list contains 2 length-m strings. Each string corresponds to an amino acid sequence
        sequence
    Output:
        F: List of lists containing locations of amino-acid sequence pairs in A1 and A2.
        F[i] should be a list of integers containing all locations in A1 and A2 at
        which the amino acid sequence pair stored in L[i] occur in the same place.
    """

    #use/modify the code below as needed
    n = len(A1) #A2 should be same length
    l = len(L)
    m = len(L[0][0])
    F = [[] for i in range(l)]

    def base9(S):
        """
        Convert string to list of ints
        This is similar to the function used in lecture notes.
        """
        c2b = {}
        c2b['a']=0
        c2b['b']=1
        c2b['c']=2
        c2b['d']=3
        c2b['e']=4
        c2b['f']=5
        c2b['g']=6
        c2b['h']=7
        c2b['i']=8
        L=[]
        for s in S:
            L.append(c2b[s])
        return L
   
    def heval(L,Base,Prime):
        """
        Convert list L to base-10 number mod Prime
        where Base specifies the base of L.
        This is the function used in lecture notes.
        """
        f = 0
        for l in L[:-1]:
            f = Base*(l+f)
            h = (f + (L[-1])) % Prime
        return h

    def match(X, Y):
        """
        Compare two lists element by element.
        Returns True if they are identical, False otherwise.
        """
        for x, y in zip(X, Y):
            if x != y:
                return False
        
        return True

    A1_val = base9(A1)
    L_val = [] # L_val should returns the first value for each pair in L
    Base = 9
    Prime = 10000000
    for i in range(l):
        val = heval(base9(L[i][0]), Base, Prime)
        L_val.append(val)

    # The first pattern in A1
    ind = 0
    hi_A1 = heval(A1_val[:m], Base, Prime)
    if hi_A1 in L_val:
        position = L_val.index(hi_A1)
        if match(A1[:m], L[position][0]) and match(A2[:m], L[position][1]):
            F[position].append(ind)

    bm = (Base**m) % Prime

    for ind in range(1,n-m+1):
        #Update rolling hash
        hi_A1 = (Base*hi_A1 - int(A1_val[ind-1])*bm + int(A1_val[ind-1+m])) % Prime
        if hi_A1 in L_val:
            position = L_val.index(hi_A1)
            if match(A1[ind:ind+m], L[position][0]) and match(A2[ind:ind+m], L[position][1]):
                F[position].append(ind)

    return F

#----------------- End code for Part 2 -----------------#



if __name__=='__main__':
    x=0 #please do not remove
    part1_test()
    #Add code here to call part1_test and generate the figures included in your report.
