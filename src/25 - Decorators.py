def cough_dec(func):
    def func_wrap():
        # before func
        print("cough")
        func()
        # after func
        print("cough")

    return func_wrap


@cough_dec
def question():
    print("Am i rich?")

# question()

@cough_dec
def answer():
    print("maybe someday")

answer()
