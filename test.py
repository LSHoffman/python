def most_classes(dict):
  max_count = 0
  teacher_with_most_classes = ''
  for teacher in dict:
    if len(dict[teacher]) > max_count:
      max_count = len(dict[teacher])
      teacher_with_most_classes = teacher
  return teacher_with_most_classes

def num_teachers(dict):
  teacher_count = 0
  for teacher in dict:
    teacher_count += 1
  return teacher_count

def stats(dict):
  new_list = []
  for teacher in dict.keys():
    teach_list = []
    teach_list.append(teacher)
    value_list = list(dict[teacher])
    teach_list.append(len(value_list))
    new_list.append(teach_list)
  return new_list
  
def courses(dict):
  new_list = []
  for values in dict.values():
    new_list.extend(values)
  return new_list