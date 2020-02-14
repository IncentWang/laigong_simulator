#Convert Chinese into Hanxiao: a traditional Tianjinren Style
adjective = ['特别','TM','他妈']
def main():
    chn = input('输入你想要柴化的句子')
    shock = input('输入想要的来式震惊程度：1，classic  2, normal, 3 heavy  4 crazy')
    sentence = input('请选择柴化后的句型')
    style = input('请选择柴化的方向: 1,2,3,4')
    buhuiyouren_convert(chn)
    print(buhuiyouren_convert(chn))



def buhuiyouren_convert(chn):
    x = chn.replace(chn[0],'不会有人不')
    x = x + '吧'
    return x





main()