file = open('youtube.txt', 'w')

try:
    file.write("Hello Hruthik I Love You")
finally:
    file.close()

with open('youtube.txt', 'w') as file:
    file.write("Hello fuck u")
