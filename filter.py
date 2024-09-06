def my_filter(compare, score_list):
   filtered_score = []
   for score in score_list:
       if compare(score):
           filtered_score.append(score)
   return filtered_score   

score_list = [34,5,6,7,8,10]
filtered_score = my_filter(lambda score: score<=80,score_list)

print(filtered_score)