try:
    print("hello ji")
except FileNotFoundError as error:
    print("file not found")

else:
    print("all well")

finally:
    print("bhaiya ji hum to chalenge hi chalenge")