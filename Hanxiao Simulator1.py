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

class buhuiyouren_sentence(str):
    def __init__(self,text: str):
        self.text = text
    def bu_hui_you_ren_convert(self, text: str):
        text = '不会有人不' + text + '吧？'
        return  text
    def bu_hui_you_ren_bu_convert(self, text: str):
        text = '不会有人' + text + '吧？'
        return  text
    def total_convert(self):
        if self.text.startswith('不会有人不'):
            self.text = self.text[5:]
            return self.bu_hui_you_ren_bu_convert(self.text)
        elif self.text.startswith('不会有人'):
            self.text = self.text[4:]
            return self.bu_hui_you_ren_convert(self.text)

def buhuiyouren_convert(origin_text: str, shock: int) -> str:
    if shock > 1:
        converted_text = origin_text.replace(origin_text[0], shock_list[shock-2] + '不会有人不' + random.choice(adjective))
        converted_text += '吧'
    else:
        converted_text = origin_text
    return converted_text


if __name__ == '__main__':
    main()
