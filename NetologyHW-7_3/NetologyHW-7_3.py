from pprint import pprint

with open('1.txt', 'r', encoding='utf-8') as file1:
    file1_data = file1.readlines()
with open('2.txt', 'r', encoding='utf-8') as file2:
    file2_data = file2.readlines()
with open('3.txt', 'r', encoding='utf-8') as file3:
    file3_data = file3.readlines()

files = [[len(file1_data), file1_data, file1.name], [len(file2_data), file2_data, file2.name], [len(file3_data), file3_data, file3.name]]

sorted_files = sorted(files, key=lambda x: x[0])

with open('result.txt', 'w', encoding='utf-8') as result_file:
    result = ''
    for el in sorted_files:
        result += f'\n{el[2]}\n{str(el[0])}\n{" ".join(el[1])}'
    result_file.write(result[1:])

file1.close()
file2.close()
file3.close()
result_file.close()

