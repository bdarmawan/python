def longestCommonPrefix(strs):
    if len(strs) == 0:
        return ("")
    if len(strs) == 1:
        return (strs[0])

    pref = strs[0]  # take the 1st str as the preference
    #print(f"PREF: {pref}")
    plen = len(pref)
    #print(f"LENGTH: {plen}")

    for s in strs[1:]:  ## since we take 1st string as pref
        #print(f"\n>>>s: {s}")
        ## then we do the loop from the 2nd str going forward
        while pref != s[0:plen]:
            #print(f"pref: {pref} ---vs--- s: {s}")
            pref = pref[0:(plen - 1)]
            plen -= 1
            #print(f"NEW length={plen}")

            if plen == 0:
                return ("")

    return (pref)


print(longestCommonPrefix(["Horse","Horreay","Horsey"]))

"""
INPUT: ["Horse", "Horray", "Horsey"]
OUTPUT: Hor

Debug Trace:
============
PREF: Horse
LENGTH: 5

>>>s: Horreay
pref: Horse ---vs--- s: Horreay
NEW length=4
pref: Hors ---vs--- s: Horreay
NEW length=3

>>>s: Horsey
Hor


"""