import re

message = "my email is krzysztof.kruszynski@gmail.com"

pattern = "[a-z.0-9]+@[a-z\.]+\.[a-z]{1,3}$" # \d is a digit

m = re.search("[a-z.0-9]+@[a-z\.]+\.[a-z]{1,3}", message)

if m: # would be None if no match is found
    print(m.group())