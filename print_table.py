"""
to use the function print_table(data), only you have to pass a dictionary as parameter

for example:
    data = {'nombre':['hernan','robert'],'apellido':['La Paz','Escobar'],'edad':[15,12]}

make example in the __main__
"""
def separator(data,list_high):
    print()
    for i in data:
        print("-"*(list_high[i]+2),end="")
    print()

def print_table(data):
    list_high = {}
    number_row = 0
    for i in data:
        size_data = len(data[i])
        if number_row < size_data:
            number_row = size_data
        high = len(i) 
        for j in data[i]:
            size_element = len(str(j))
            if high < size_element:
                high = size_element
        list_high[i] = high
    
    for i in data:#print title
        print(i.title(),end=" "*(list_high[i]-len(i)+1)+"|")
    
    separator(data,list_high)

    index = 0
    while index < number_row:
        for i in data:
            if index >= len(data[i]):
                data[i].append("")
            element = data[i][index]
            print(element,end = " "*(list_high[i]-len(str(element))+1)+'|')
        separator(data,list_high)
        index += 1

if __name__ == "__main__":
    datos = {'nombre':['hernan','robert','ana','alejandra'],'apellido':['La Paz','Escobar','Castilla','Espinoza'],'edad':[15,12,13,16]}

    print_table(datos)