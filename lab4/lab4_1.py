from PIL import Image

#构造节点的类
class node:
    def __init__(self, right=None, left=None, parent=None, weight=0, code=None):
        self.left = left
        self.right = right
        self.parent = parent
        self.weight = weight
        self.code = code

#将文件转换为灰色图并保存
def picture_convert(filename,newfilename):
    picture = Image.open(filename)
    picture = picture.convert('L')
    picture.save(newfilename)
    return picture #返回转换后的图片对象

#统计像素数量
def pixel_number_calculate(list):
    pixel_number = {}
    #遍历list中所有像素
    for i in list:
        #如果该像素值不在数组的key中，创建相应数值的key
        if i not in pixel_number.keys():
            pixel_number[i]=1
        #否则，在对应的key上加1
        else:
            pixel_number[i] += 1
    return pixel_number

#构造节点
def node_constructor(pixel_number):
    node_list = []
    for i in range(len(pixel_number)):
        node_list.append(node(weight=pixel_number[i][1], code=str(pixel_number[i][0])))
    return node_list

#构造霍夫曼树
def tree_construct(listnode):
    listnode = sorted(listnode, key=lambda node:node.weight)
    while len(listnode) != 1:
        low_node0, low_node1 = listnode[0], listnode[1]
        new_change_node = node()
        new_change_node.weight = low_node0.weight + low_node1.weight
        new_change_node.left = low_node0
        new_change_node.right = low_node1
        low_node0.parent = new_change_node
        low_node1.parent = new_change_node
        listnode.remove(low_node0)
        listnode.remove(low_node1)
        listnode.append(new_change_node)
        listnode = sorted(listnode, key=lambda node:node.weight)
        print("Weight:", low_node0.weight, low_node1.weight)
        print("Code:", low_node0.code, low_node1.code)
    return listnode

def Huffman_Coding(picture):
    width = picture.size[0]
    height = picture.size[1]
    im = picture.load()
    print("width:"+str(width)+"pixel")
    print("height:"+str(height)+"pixel")

    list = []
    for i in range(width):
        for j in range(height):
            list.append(im[i,j])

    pixel_number = pixel_number_calculate(list)
    p_num = pixel_number
    pixel_number = sorted(pixel_number.items(),key=lambda item:item[1])

    node_list = node_constructor(pixel_number)

    head = tree_construct(node_list)[0]

    coding_table = {}
    for e in node_list:
        new_change_node = e
        coding_table.setdefault(e.code,"")
        while new_change_node != head:
            if new_change_node.parent.left == new_change_node:
                coding_table[e.code] = "1" + coding_table[e.code]
            else:
                coding_table[e.code] = "0" + coding_table[e.code]
            new_change_node = new_change_node.parent

    total_bits = 0  # 用于累计码字长度的变量
    total_pixels = width * height  # 图像总像素数量

    for key in coding_table.keys():
        print("信源像素点" + key + "霍夫曼编码后的码字为：" + coding_table[key])
        total_bits += len(coding_table[key]) * p_num[int(key)]  # 累计码字长度

    average_code_length = total_bits / total_pixels
    print("平均码字长度：", average_code_length)

    print("编码表为:",coding_table)

    coding_result = ''
    for i in range(width):
        for j in range(height):
            for key, values in coding_table.items():
                if str(im[i,j]) == key:
                    coding_result = coding_result+values
    file = open('./data/coding_result.txt','w')
    file.write(coding_result)

    return width, height, coding_table, coding_result

def Decoding(width,height,coding_table,coding_result):
    code_read_now = ''
    new_pixel = []
    i = 0
    while(i!= coding_result.__len__()):
        code_read_now += coding_result[i]
        for key in coding_table.keys():
            if code_read_now == coding_table[key]:
                new_pixel.append(key)
                code_read_now = ''
                break
        i+=1
    
    decode_image = Image.new('L',(width,height))
    k = 0
    for i in range(width):
        for j in range(height):
            decode_image.putpixel((i,j),(int(new_pixel[k])))
            k+=1
    decode_image.save('./data/decode.bmp')
    print("decode已完成。")

if __name__ == '__main__':
    picture = picture_convert('./data/sample.bmp','./data/huff_gray.bmp')
    width, height, coding_table, coding_result =Huffman_Coding(picture)
    Decoding(width, height, coding_table, coding_result)