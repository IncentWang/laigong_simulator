
def convert(input: str) -> str:
    if input.startswith('我'):
        input = input[1:]
    input = delete_le(input)
    return '不会有人不' + input + '吧？'

def delete_le(input: str) -> str:
    if input.endswith('了'):
        input = input[:-1]
    else:
        pass
    return input

if __name__ == '__main__':
    print(convert(input()))