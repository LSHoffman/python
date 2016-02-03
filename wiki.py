import datetime

answer_format = '%m/%d'
link_format = '%b_%d'
link = 'https://en.wikipedia.org/wiki/{}'
output_list = []
i = 0

while True:
    print("What date(s) would you like? Please use the MM/DD format. Enter QUIT to quit. ")
    answer = input(">")
    if answer.upper() == "QUIT":
        break
    
    date_list = answer.split(",")
    
    if len(date_list) == 1:
        try:
            date = datetime.datetime.strptime(date_list[0].strip(), answer_format)
            output = link.format(date.strftime(link_format))
            output_list.append(output)
        except ValueError:
            output_list.append("Invalid Date")
    else:
        try:
            for term in date_list:
                date = datetime.datetime.strptime(date_list[i].strip(), answer_format)
                output = link.format(date.strftime(link_format))
                output_list.append(output)
                i += 1
        except: 
            output_list.append("Invalid Date")
            i += 1
            
    print("\n".join(output_list))