def max_split(s):
    w_count = l_count = r_count = 0
    balance_st = []    
    for ch in s:
        if ch == "L":
            l_count += 1
        else:
            r_count += 1
        if l_count == r_count:
            w_count += 1
            balance_st.append(s[:l_count+r_count])
            s = s[l_count+r_count:]
            l_count = r_count = 0
            
    print(w_count)
    for st in balance_st:
        print(st)
        
        
s = input()
max_split(s)
