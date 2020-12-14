# !/usr/bin/python
# -*- coding:utf-8 -*-
'''
@versoin:V-1.8.0
@author:xiaobao
@file:rtime_demo.py
@time:2020年10月29日
'''
from flask import Flask, render_template
from pyecharts.charts import Line
from pyecharts.charts import Pie
from pyecharts.charts import Bar
from Common.Common_Conf import end_path
from pyecharts import options as opts
import xlrd
from Tool.get_rtime import add_errnum,add_gtime
from gevent import pywsgi
from pyecharts.globals import ThemeType

gtime_list,gtime_num = add_gtime()
errnum,portnum,runnum,errnum_list = add_errnum()                #依次为报错总数，接口总数，运行次数,报错字典数据
data = xlrd.open_workbook(r'%s' % end_path)
table = data.sheets()[0]
port_name = table.row_values(0)[1::]
port_rtime = table.col_values(1)[1::]

app = Flask(__name__, static_folder="templates")

def line_base() -> Line:
    line = (
        Line(init_opts=opts.InitOpts(chart_id=1))
        .add_xaxis(
            table.col_values(0)[1::]
        )
        .add_yaxis(table.row_values(0)[1],
                   table.col_values(1)[1::],
                   markpoint_opts=opts.MarkPointOpts(data=[
                   opts.MarkPointItem(type_="max")])
        )
        .add_yaxis(table.row_values(0)[2],
                   table.col_values(2)[1::],
                   markpoint_opts=opts.MarkPointOpts(data=[
                   opts.MarkPointItem(type_="max")])
        )
        .add_yaxis(table.row_values(0)[3],
                   table.col_values(3)[1::],
                   markpoint_opts=opts.MarkPointOpts(data=[
                   opts.MarkPointItem(type_="max")])
        )
        .add_yaxis(table.row_values(0)[4],
                   table.col_values(4)[1::],
                   markpoint_opts=opts.MarkPointOpts(data=[
                   opts.MarkPointItem(type_="max")])
        )
        .add_yaxis(table.row_values(0)[5],
                   table.col_values(5)[1::],
                   markpoint_opts=opts.MarkPointOpts(data=[
                   opts.MarkPointItem(type_="max")])
        )
        .add_yaxis(table.row_values(0)[6],
                   table.col_values(6)[1::],
                   markpoint_opts=opts.MarkPointOpts(data=[
                   opts.MarkPointItem(type_="max")])
        )
        .add_yaxis(table.row_values(0)[7],
                   table.col_values(7)[1::],
                   markpoint_opts=opts.MarkPointOpts(data=[
                   opts.MarkPointItem(type_="max")])
        )
        .add_yaxis(table.row_values(0)[8],
                   table.col_values(8)[1::],
                   markpoint_opts=opts.MarkPointOpts(data=[
                   opts.MarkPointItem(type_="max")])
        )
        .add_yaxis(table.row_values(0)[9],
                   table.col_values(9)[1::],
                   markpoint_opts=opts.MarkPointOpts(data=[
                   opts.MarkPointItem(type_="max")])
        )
        .add_yaxis(table.row_values(0)[10],
                   table.col_values(10)[1::],
                   markpoint_opts=opts.MarkPointOpts(data=[
                   opts.MarkPointItem(type_="max")])

        )
        .add_yaxis(table.row_values(0)[11],
                   table.col_values(11)[1::],
                   markpoint_opts=opts.MarkPointOpts(data=[
                   opts.MarkPointItem(type_="max")])
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(title=""),
            datazoom_opts=[                                              # 加滚动条，横的是x轴，竖的是y轴
                            opts.DataZoomOpts(xaxis_index=0),
                            opts.DataZoomOpts(type_="inside", xaxis_index=0)
    ],
    )
        )
    return line

def pie_base() -> Pie:
    errlist = ['报错','超时','正常']
    allport = errnum+gtime_num+portnum
    datalist = [('%.2f' % (errnum/allport* 100.0)),
                ('%.2f' % (gtime_num/allport* 100.0)),
                ('%.2f' % (portnum/allport* 100.0))]
    pie = (
        Pie(init_opts=opts.InitOpts(chart_id=2))
        .add(
            "",
            [list(z) for z in zip(errlist, datalist)],
            #center=["35%", "50%"],
        )
        .set_colors(["#FF3F1D", "#FF601D", "#B2E5B2"])
        .set_global_opts(
            title_opts=opts.TitleOpts(title='第%d次运行' % runnum,
                                      pos_bottom="1%", pos_left="33%",  # 定义标题位置
                                      title_textstyle_opts=opts.TextStyleOpts(font_size=30, color="#FF8C52")
    ),
            #legend_opts=opts.LegendOpts(pos_left="15%"),
        )
        .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    )
    return pie

def bar_base() -> Bar:
    port_name = list(errnum_list.keys())
    port_num = list(errnum_list.values())
    bar = (
        Bar(init_opts=opts.InitOpts(theme=ThemeType.MACARONS, chart_id=3))
            .add_xaxis(port_name)
            .add_yaxis("报错排行", port_num)
            #.set_colors(["#FFFF93", "#00FFE0"])
            .set_global_opts(title_opts=opts.TitleOpts(title="", subtitle=""),
                             #xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=-15))          # 标题倾斜展示
                             # legend_opts=opts.LegendOpts(type_="scroll", pos_left="left", orient="vertical")     图表名称位置
                             )
    )
    return bar

def bar_base1() -> Bar:
    port_name = list(gtime_list.keys())
    port_num = list(gtime_list.values())
    bar = (
        Bar(init_opts=opts.InitOpts(theme=ThemeType.MACARONS, chart_id=4))
            .add_xaxis(port_name)
            .add_yaxis("超时排行", port_num)
            .set_colors(["#FFFF93"])
            .set_global_opts(title_opts=opts.TitleOpts(title="", subtitle=""),
                             xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=-30))
                             # legend_opts=opts.LegendOpts(type_="scroll", pos_left="left", orient="vertical")     图表名称位置
                             )
    )
    return bar

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/lineChart")
def get_line_chart():
    c = line_base()
    return c.dump_options_with_quotes()

@app.route("/pieChart")
def get_pie_chart():
    c = pie_base()
    return c.dump_options_with_quotes()

@app.route("/barChart")
def get_bar_chart():
    c = bar_base()
    return c.dump_options_with_quotes()

@app.route("/bar1Chart")
def get_bar_chart1():
    c = bar_base1()
    return c.dump_options_with_quotes()

if __name__ == "__main__":
    server = pywsgi.WSGIServer(('0.0.0.0', 5001), app)
    server.serve_forever()
    #app.run()