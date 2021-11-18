'''
predict.py有几个注意点
1、该代码无法直接进行批量预测，如果想要批量预测，可以利用os.listdir()遍历文件夹，利用Image.open打开图片文件进行预测。
具体流程可以参考get_dr_txt.py，在get_dr_txt.py即实现了遍历还实现了目标信息的保存。
2、如果想要进行检测完的图片的保存，利用r_image.save("img.jpg")即可保存，直接在predict.py里进行修改即可。 
3、如果想要获得预测框的坐标，可以进入yolo.detect_image函数，在绘图部分读取top，left，bottom，right这四个值。
4、如果想要利用预测框截取下目标，可以进入yolo.detect_image函数，在绘图部分利用获取到的top，left，bottom，right这四个值
在原图上利用矩阵的方式进行截取。
5、如果想要在预测图上写额外的字，比如检测到的特定目标的数量，可以进入yolo.detect_image函数，在绘图部分对predicted_class进行判断，
比如判断if predicted_class == 'car': 即可判断当前目标是否为车，然后记录数量即可。利用draw.text即可写字。
'''
import cv2
from PIL import Image
import numpy as np

from yolo import YOLO

from IPython import embed

yolo = YOLO()

image = Image.open('./img/view1.jpg')# 返回PIL.img对象
uncroped_image = cv2.imread("./img/view1.jpg")

r_image,boxes = yolo.detect_image(image)

# 进行裁剪并保存到本地
box = boxes

for i in range(boxes.shape[0]):
    # top, left, bottom, right = boxes[i]
    # 或者用下面这句等价
    top = boxes[i][0]
    left = boxes[i][1]
    bottom = boxes[i][2]
    right = boxes[i][3]

    top = top - 5
    left = left - 5
    bottom = bottom + 5
    right = right + 5

    # 左上角点的坐标
    top = int(max(0, np.floor(top + 0.5).astype('int32')))

    left = int(max(0, np.floor(left + 0.5).astype('int32')))
    # 右下角点的坐标
    bottom = int(min(np.shape(image)[0], np.floor(bottom + 0.5).astype('int32')))
    right = int(min(np.shape(image)[1], np.floor(right + 0.5).astype('int32')))

    # embed()

    # 问题出在这里：不能用这个方法，看两个参数是长和宽，是从图像的原点开始裁剪的，这样肯定是不对的
    # 指定裁剪的目标范围
    croped_region = uncroped_image[top:bottom,left:right]# 先高后宽
    # 将裁剪好的目标保存到本地
    cv2.imwrite("./output/croped_view2_img_"+str(i)+".jpg",croped_region)

# embed()
r_image.show()