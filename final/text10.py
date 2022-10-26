import pyecharts.options as opts
from pyecharts.charts import Line
import pandas as pd
import numpy as np

df = pd.read_excel("D:\\全国总人口10年数据.xls")
df = pd.DataFrame(df[1:7][:])
array = np.array(df)
list1 = array.tolist()
x = list1[0][1:11]
x.reverse()
y1 = list1[1][1:11]
y1.reverse()
y2 = list1[2][1:11]
y2.reverse()
y3 = list1[3][1:11]
y3.reverse()
y4 = list1[4][1:11]
y4.reverse()
y5 = list1[5][1:11]
y5.reverse()
l=(
    Line()
    .add_xaxis(x)
    .add_yaxis(series_name="年末总人口(万人)",y_axis=y1)
    .add_yaxis(series_name="男性人口(万人)",y_axis=y2)
    .add_yaxis(series_name="女性人口(万人)",y_axis=y3)
    .add_yaxis(series_name="城镇人口(万人)",y_axis=y4)
    .add_yaxis(series_name="乡村人口(万人)",y_axis=y5)
    .set_global_opts(title_opts=opts.TitleOpts(title="人口变化情况"))
)
l.render('mycharts-10.html')
