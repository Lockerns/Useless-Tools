import re
import pyperclip

string = "  * it     is blank    space     test *  "
str1 = 'dfadf   d\n \n\n \nfa  ds '


str_new = re.sub('[\n]+', '\n', str1)
# str_new4 = re.sub(r"\s+", " ", string)  # 多个连续空格合并成一个空格

text = pyperclip.paste()

space_d = re.compile(r'\s+')
str_new4 = space_d.sub(' ', text)
pyperclip.copy(str_new4)
# print(str_new4)
