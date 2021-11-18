1.文件夹位置
E:\DeepFashion2

2.Dataset数据集
下载DeepFashion2 Dataset(https://github.com/switchablenorms/DeepFashion2)
train解压到train文件夹下
validation解压到validation文件夹下

VOC数据集：
训练集(https://pan.baidu.com/s/16pemiBGd-P9q2j7dZKGDFA 提取码: eiw9) 放在VOCdevkit/VOC2007/Annotation
测试集(https://pan.baidu.com/s/1BnMiFwlNwIWG9gsd4jHLig 提取码: dsda) 放在VOCdevkit/VOC2007/JPEGImages

cd VOCdevkit/VOC2007
python voc2yolov4.py

python voc_annotation.py

3.Train训练
python train.py

4.Predict检测
python predict.py