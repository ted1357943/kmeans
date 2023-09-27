## kmeans_irisdata.py
使用iris_data(鳶尾花資料集)去做kmeans,iris_data包含四維資料:
- sepallength(萼片長度)
- sepalwidth(萼片寬度)
- petallengh(花瓣長度)
- petalwidth(花瓣寬度)  
原資料已事先分為Iris-setosa、Iris-versicolor、Iris-virginica三類  
### 作法:
>將事先分好的三類去除掉,只留下四維資料(sepallength、sepalwidth、petallengh、petalwidth)  
將這些資料拿去做kmeans  
程式開始時會要求輸入群心數,並透過手動輸入的群心數來進行k-means分群  
最後顯示一張圖片  
>>左上是以sepallength與sepalwidth為XY軸並透過原資料分為三類作圖,右上是以petallengh與petalwidth為XY軸並透過原資料分為三類作圖  
左下是以sepallength與sepalwidth為XY軸並透過k-means分為k群作圖,右下是以petallengh與petalwidth為XY軸並透過k-means分為k群作圖  
---
## kmems_picture.py
透過opencv套件,將圖片進行kmeans分群  
### 作法:
>程式開始時會要求輸入群心數,並透過手動輸入的群心數來進行k-means分群  
先讀取圖片,並記錄圖片每個像素點的RGB值  
程式預設讀取圖片大小為480x360,因此共有480*360筆資料,每筆資料有R、G、B三個維度去進行k-means分群  
最後將分為同一群的像素的RGB值都設為群心的RGB值,達到顏色分群的效果
