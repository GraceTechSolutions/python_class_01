str_list = '1 2 3 4 5 6 7 8 9'

def convert(func):
    def main(values:str):
        values = map(lambda num: int(num), values.split(' '))
        # str_value = values.split(' ')
        # ret = []
        # for value in str_value:
        #     val = int(value)
        #     ret.append(val)
        return func(values)
    return main

def print_main():
    print(__name__)

if __name__ == "__main__":
    print('-------------------------------------------')