def add():
    a = 15

    def modify():
        global a
        a = 20

    print("Перед изменением:", a)
    print("Внесение изменений")
    modify()
    print("После изменения:", a)


add()
print("Значение a:", a)