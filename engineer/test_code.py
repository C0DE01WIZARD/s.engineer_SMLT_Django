try:
    a=2/1
    print(a)

except ZeroDivisionError:
    print("на ноль делить нельзя")
finally:
    print("Финал")