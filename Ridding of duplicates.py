student_data={'id1':{'name':['Naisa'],'class':['XII'], 'subject_integration':['english, math, science']}, 
              'id2':{'name':['Muhaimin'],'class':['XII'], 'subject_integration':['english, math, science']},
              'id3':{'name':['Nuzhat'],'class':['XII'], 'subject_integration':['english, math, science']},
              'id4':{'name':['Agha'],'class':['XII'], 'subject_integration':['english, math, science']}, 
              
              }
result={}
for key, value in student_data.items():
    if value not in result.values():
        result[key]=value
print(result)