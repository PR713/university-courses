def min_sum(rok: int) -> dict:
    for the_smallest_sum in range(1, rok + 1):
        for first_word in range(the_smallest_sum):
            a = first_word # kolejno od 0 do 2023
            b = the_smallest_sum - first_word #od 1 do 2023
            while b < rok: # rok na początku od 1 do 2023
                a,b = b,a+b # czyli dla a przypisujemy kolejny wyraz i dla b kolejny
                #przerwie gdy b czyli wyraz ciągu osiągnie 2023
            if b == rok:
                return{
                    'najmniejsza suma ' : the_smallest_sum,
                    'pierwszy wyraz': first_word,
                    'drugi wyraz' : the_smallest_sum - first_word
                }

print(min_sum(2023))