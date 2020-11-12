from pyecharts import options as opts
from pyecharts.charts import Pie
from pyecharts.faker import Faker
import time

today = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

tittle = '%s\n第x次运行' % today
c = (
    Pie()
    .add(
        "",
        [list(z) for z in zip(Faker.choose(), Faker.values())],
        center=["35%", "50%"],
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title=today,
                                  pos_bottom="-100",pos_left="15%",        # 定义标题位置
                                  title_textstyle_opts=opts.TextStyleOpts(font_size=30,color="#1d953f")),       # 定义标题大小，颜色
        legend_opts=opts.LegendOpts(pos_left="15%")
    )
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    .render("pie_position.html")
)



