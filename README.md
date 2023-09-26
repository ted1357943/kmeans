## irisdata.py
使用iris_data(鳶尾花資料集)去做kmeans,iris_data包含四維資料:
- sepallength(萼片長度)
- sepalwidth(萼片寬度)
- petallengh(花瓣長度)
- petalwidth(花瓣寬度)  
原資料已事先分為Iris-setosa、Iris-versicolor、Iris-virginica三類  
###作法:
>將事先分好的三類去除掉,只留下剩下四維資料(sepallength、sepalwidth、petallengh、petalwidth)  
將這些資料拿去做kmeans  
最後顯示兩張圖片,左邊是以sepallength與sepalwidth為XY軸作圖,右邊是以petallengh與petalwidth為XY軸作圖
