def number32np(binary):
    bs=np.array(list(binary[::-1]))
    ns=bs.astype(int)
    dec=1+np.dot( ns[0:23][::-1],np.exp2(-np.arange(1,24)) )
    exp=np.dot( ns[23+0:23+8],np.exp2(np.arange(0,8)) )
    return (-1)**int(ns[-1])*2**(exp-127)*dec