#Convert Chinese into Hanxiao: a traditional Tianjinren Style
import random

adjective = ['TM','他妈']
shock_list = ['啊-----！', '啊---------------！', '啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊！']
def main():
    origin_text = input('输入你想要柴化的句子')
    shock = input('输入想要的来式震惊程度：1，classic  2, normal, 3 heavy  4 crazy')
    sentence = input('请选择柴化后的句型')
    style = input('请选择柴化的方向: 1,2,3,4')
    print(buhuiyouren_convert(origin_text, int(shock)))



def buhuiyouren_convert(origin_text: str, shock: int) -> str:
    if shock > 1:
        converted_text = origin_text.replace(origin_text[0], shock_list[shock-2] + '不会有人不' + random.choice(adjective))
        converted_text += '吧'
    return converted_text


if __name__ == '__main__':
    main()