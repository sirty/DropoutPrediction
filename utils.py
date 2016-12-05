import re
from os import path

class Paths(object):
  data = 'data'
  result = 'result'
  fu_file = path.join(data, 'FU_CSV.csv')
  lack_of_birth = path.join(data, 'LackOfBirthd.csv')
  lack_of_english_grade = path.join(data, 'LackOfEnglishGrade.csv')
  lack_of_village = path.join(data, 'LackOfNativeVillage.csv')
  fu_result_file = path.join(result, 'FU_result.csv')
  eng_result_file = path.join(result, 'vi_result.csv')
  
  fu_v2 = path.join(data, 'fu_v2.csv')
  data_avg = path.join(result, 'data_avg.csv')
  data_linear = path.join(result, 'data_linear.csv')
