def pozdrav():
    print('Hello')
def obal(fce):
    return fce()


obal(pozdrav)