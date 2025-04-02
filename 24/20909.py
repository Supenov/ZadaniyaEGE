s = open('C:/Users/student/Desktop/ZadaniyaEGE/24/24_20909.txt').readline()
l = 0
max_len = -500
c = 0
cur_len = 1


for r in range(1, len(s)):
    if s[r-1] + s[r] == 'AB':
        #c += 1
        cur_len += 1
        
    
    else:
        max_len = max(max_len, cur_len)
        cur_len = 1
    

    # if cur_len == 100:
    #     cur_len = 0

    # while c > 100:
    #     if s[l] + s[l+1] == 'AB':
    #         c -= 1
    #     l += 1
print(max_len)