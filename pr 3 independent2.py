def season_events(n):
    if n==1:
        return ('Your were born in January.White snow fell outside the window')
    elif n==2:
        return('Your were born in Februry.White snow fell outside the window')
    elif n==3:
        return('Your were born in March.Birds sang beautiful songs')
    elif n==4:
        return('Your were born in April.Birds sang beautiful songs')
    elif n==5:
        return('Your were born in May.Birds sang beautiful songs')
    elif n==6:
        return('Your were born in June.The sun shone brighter than ever')
    elif n==7:
        return('Your were born in July.The sun shone brighter than ever')
    elif n==8:
        return('Your were born in August.The sun shone brighter than ever')
    elif n==9:
        return('Your were born in September.The harvest was incredible')
    elif n==10:
        return('Your were born in October.The harvest was incredible')
    elif n==11:
        return('Your were born in November.The harvest was incredible')
    elif n==12:
        return('Your were born in December.White snow fell outside the window')
    else:
        return('такого месяца не существует вы чего')
    
        

a=int(input())
print(season_events(a))
