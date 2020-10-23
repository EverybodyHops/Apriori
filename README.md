# Apriori算法

清华大学（THU）2020秋数据挖掘 课程项目  
<br/> 

# 项目说明  

本项目代码由朱子睿（2020310798）完成，代码仅供参考交流，若用于其他用途请与作者沟通。
<br/> 

# 使用说明

项目共有两个`python`文件构成，其中`apriori.py`文件中完成了Apriori算法的实现，`main.py`函数完成命令行参数的解析。

使用如下命令运行算法：
```
python main.py -f groceries.csv -c 0.3 -s 0.02
```

命令中`-f`指定文件位置，`-c`指定置信度， `-s`。
使用以上命令运行输出如下：
```
('citrus fruit',)                        -> ('whole milk',)                Support: 0.030503,   Confidence: 0.368550
('citrus fruit',)                        -> ('other vegetables',)          Support: 0.028876,   Confidence: 0.348894
('margarine',)                           -> ('whole milk',)                Support: 0.024199,   Confidence: 0.413194
('tropical fruit',)                      -> ('whole milk',)                Support: 0.042298,   Confidence: 0.403101
('tropical fruit',)                      -> ('other vegetables',)          Support: 0.035892,   Confidence: 0.342054
('yogurt',)                              -> ('whole milk',)                Support: 0.056024,   Confidence: 0.401603
('yogurt',)                              -> ('other vegetables',)          Support: 0.043416,   Confidence: 0.311224
('pip fruit',)                           -> ('whole milk',)                Support: 0.030097,   Confidence: 0.397849
('other vegetables',)                    -> ('whole milk',)                Support: 0.074835,   Confidence: 0.386758
('butter',)                              -> ('whole milk',)                Support: 0.027555,   Confidence: 0.497248
('rolls/buns',)                          -> ('whole milk',)                Support: 0.056634,   Confidence: 0.307905
('bottled water',)                       -> ('whole milk',)                Support: 0.034367,   Confidence: 0.310948
('curd',)                                -> ('whole milk',)                Support: 0.026131,   Confidence: 0.490458
('beef',)                                -> ('whole milk',)                Support: 0.021251,   Confidence: 0.405039
('frankfurter',)                         -> ('whole milk',)                Support: 0.020539,   Confidence: 0.348276
('fruit/vegetable juice',)               -> ('whole milk',)                Support: 0.026640,   Confidence: 0.368495
('newspapers',)                          -> ('whole milk',)                Support: 0.027351,   Confidence: 0.342675
('pastry',)                              -> ('whole milk',)                Support: 0.033249,   Confidence: 0.373714
('root vegetables',)                     -> ('whole milk',)                Support: 0.048907,   Confidence: 0.448694
('sausage',)                             -> ('whole milk',)                Support: 0.029893,   Confidence: 0.318182
('brown bread',)                         -> ('whole milk',)                Support: 0.025216,   Confidence: 0.388715
('pork',)                                -> ('whole milk',)                Support: 0.022166,   Confidence: 0.384480
('whipped/sour cream',)                  -> ('whole milk',)                Support: 0.032232,   Confidence: 0.449645
('domestic eggs',)                       -> ('whole milk',)                Support: 0.029995,   Confidence: 0.472756
('frozen vegetables',)                   -> ('whole milk',)                Support: 0.020437,   Confidence: 0.424947
('pip fruit',)                           -> ('other vegetables',)          Support: 0.026131,   Confidence: 0.345430
('butter',)                              -> ('other vegetables',)          Support: 0.020031,   Confidence: 0.361468
('root vegetables',)                     -> ('other vegetables',)          Support: 0.047382,   Confidence: 0.434701
('pork',)                                -> ('other vegetables',)          Support: 0.021657,   Confidence: 0.375661
('whipped/sour cream',)                  -> ('other vegetables',)          Support: 0.028876,   Confidence: 0.402837
('domestic eggs',)                       -> ('other vegetables',)          Support: 0.022267,   Confidence: 0.350962
('sausage',)                             -> ('rolls/buns',)                Support: 0.030605,   Confidence: 0.325758
('whole milk', 'yogurt')                 -> ('other vegetables',)          Support: 0.022267,   Confidence: 0.397459
('other vegetables', 'yogurt')           -> ('whole milk',)                Support: 0.022267,   Confidence: 0.512881
('root vegetables', 'whole milk')        -> ('other vegetables',)          Support: 0.023183,   Confidence: 0.474012
('other vegetables', 'whole milk')       -> ('root vegetables',)           Support: 0.023183,   Confidence: 0.309783
('other vegetables', 'root vegetables')  -> ('whole milk',)                Support: 0.023183,   Confidence: 0.489270
```
