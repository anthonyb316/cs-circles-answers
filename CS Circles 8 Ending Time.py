starting_time = input()   # Starting time
D = int(input())   # Duration
H = int(starting_time[0:2])   # Final time: hours
M = int(starting_time[3:5])   # Final time: minutes

if D + M > 59:   # If the final minutes exceed 59
    H = H + (D + M) // 60   # Final hours
    M = (D + M) % 60   # Final minutes
    if len(str(M)) == 1:   # When the final minutes become one figure
        M = '0' + str(M)   # Put 0 before the actual minute
    if H > 23:   # When the final time exceeds 00:00
        H = H % 24
        if len(str(H)) == 1:   # When the final hours become one figure
           H = '0' + str(H)   # Put 0 before the actual hours
print(str(H) + ':' + str(M))
