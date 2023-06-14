from django.shortcuts import render, HttpResponse

# Create your views here.

from echart.models import ParetoRate, rfm, visualizationdata01, visualizationdata01_month, segment_datatable, \
    category_saleDataTable, shipData
from django.db.models import Count, Sum, F
import json
import numpy as np
import pandas as pd


def index(request):
    return render(request, "echart/index.html")


def customer_data(request):
    # 3.帕累托法则
    paretoData = {"customer_id": [], "Pareto_rate": [], "customer_count": []}
    paretoSet = ParetoRate.objects.all().values()
    for i in paretoSet:
        paretoData["customer_id"].append(i["customer_id"])
        paretoData["Pareto_rate"].append(round(i["Pareto_rate"] * 100, 2))
        paretoData["customer_count"].append(round(i["customer_count"] * 100, 2))
    paretoJson = json.dumps(paretoData, ensure_ascii=False)

    # 2.RFM模型
    ## 1右侧表格
    rfmtable = {"customer_id": [], "R": [], "F": [], "M": [], "customer_type": []}
    rfmSet = rfm.objects.filter(customer_type="高价值客户").order_by("-m_data").values()
    for i in rfmSet:
        rfmtable["customer_id"].append(i["customer_id"])
        rfmtable["R"].append(i["r_data"])
        rfmtable["F"].append(i["f_data"])
        rfmtable["M"].append(round(i["m_data"], 0))
        rfmtable["customer_type"].append(i["customer_type"])
    rfmJson = json.dumps(rfmtable, ensure_ascii=False)

    ## 2rfm图
    rfmSumSet = rfm.objects.values("customer_type").annotate(customer_count=Count("customer_id"),
                                                             customerMoneySum=Sum('m_data'))
    rfmSumData = {"客户类型": [], "RFM客户数": [], "RFM销售额": []}

    for i in rfmSumSet:
        rfmSumData["客户类型"].append(i['customer_type'])
        rfmSumData["RFM客户数"].append(round(i['customer_count'], 2))
        rfmSumData["RFM销售额"].append(round(i['customerMoneySum'] / 1000, 2))
    rfmSumJson = json.dumps(rfmSumData, ensure_ascii=False)

    ##2 r图
    rfm_rSet = rfm.objects.values("r_data")
    rList = []
    for i in rfm_rSet:
        rList.append(i['r_data'])
    rSetData_bins = [i for i in range(0, 571, 30)]
    rSetData_bins.append(100000)
    rSetData_labels = [i for i in range(30, 600 + 1, 30)]
    rSetData = pd.value_counts(pd.cut(rList, bins=rSetData_bins, labels=rSetData_labels, right=False), sort=False)
    rSetJson = {"R值": rSetData_labels, "count": list(rSetData)}

    ##2 f图
    rfm_fSet = rfm.objects.values("f_data")
    fList = []
    for i in rfm_fSet:
        fList.append(i['f_data'])
    fSetData_bins = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 15, 17, 20, 23, 26, 30, 35, 40, 50, 100]
    fSetData_labels = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 15, 17, 20, 23, 26, 30, 35, 40, 50, 100]
    fSetData = pd.value_counts(pd.cut(fList, bins=fSetData_bins, labels=fSetData_labels, right=False), sort=False)
    fSetJson = {"f值": fSetData_labels, "count": list(fSetData)}

    ##2 m图
    rfm_mSet = rfm.objects.values("m_data")
    mList = []
    for i in rfm_mSet:
        mList.append(i['m_data'])
    mSetData_bins = [0, 5000, 10000, 15000, 20000, 25000, 30000, 35000, 40000, 45000, 50000, 60000, 70000, 80000, 90000,
                     100000, 200000]
    mSetData_labels = [5000, 10000, 15000, 20000, 25000, 30000, 35000, 40000, 45000, 50000, 60000, 70000, 80000, 90000,
                       100000, 200000]
    mSetData = pd.value_counts(pd.cut(mList, bins=mSetData_bins, labels=mSetData_labels, right=False), sort=False)
    mSetJson = {"m值": mSetData_labels, "count": list(mSetData)}

    return render(request, "echart/customer_data.html",
                  {"pareto_data": paretoJson, "rfm_data": rfmJson, "rfmSumJson": rfmSumJson, "rfmRJson": rSetJson,
                   "fSetJson": fSetJson, "mSetJson": mSetJson})


def year_sales(request):
    # 可视化01
    year_sales_Data = {"year": [], "sale": [], "profit": [], "profitrate": [], "count": [], "numberOrder": [],
                       "averageDiscount": [], "guestListPrice": []}
    year_sales_Set = visualizationdata01.objects.all().values()
    for i in year_sales_Set:
        year_sales_Data["year"].append(i["year"])
        year_sales_Data["sale"].append(round(i["sales"] / 10000, 2))
        year_sales_Data["profit"].append(round(i["profit"] / 10000, 2))
        year_sales_Data["profitrate"].append(round(i["profitrate"] * 100, 2))
        year_sales_Data["count"].append(i["count"])
        year_sales_Data["numberOrder"].append(i["numberOrder"])
        year_sales_Data["averageDiscount"].append(round(i["averageDiscount"] * 100, 2))
        year_sales_Data["guestListPrice"].append(i["guestListPrice"])
    year_sales_Json = json.dumps(year_sales_Data, ensure_ascii=False)
    # 可视化02
    year_month_Data = {"year": [], "sale": [[], [], [], []]
        , "count": [[], [], [], []]
        , "profit": [[], [], [], []]
                       }
    year_sales_Set = visualizationdata01_month.objects.all().order_by('year', 'month').values()
    for i in year_sales_Set:
        year_month_Data["year"].append(i["year"])
        year_month_Data["sale"][int(i["year"]) % 2015].append(round(i["sales"] / 10000, 2))
        year_month_Data["count"][int(i["year"]) % 2015].append(i["count"])
        year_month_Data["profit"][int(i["year"]) % 2015].append(round(i["profit"] / 10000, 2))
    year_month_Json = json.dumps(year_month_Data, ensure_ascii=False)

    return render(request, "echart/year_data.html", {"year_sales_Json": year_sales_Json, "year_month_Json": year_month_Json})


def category_sale(request):
    category_Pie_data = {}
    category_pie_subdata = {}
    category_pie_subdata_list = []

    subcategory_tar_data = {}
    category_tar_subdata = {
        "subcategory": [],
        "sale": [],
        "profit": []
    }

    category_sale_Pie__set = category_saleDataTable.objects.all().values("year", "category").annotate(
        saleSum=Sum("sale"))
    subcategory_sale__tar_set = category_saleDataTable.objects.all().order_by('year', 'profit').values()
    temp = category_sale_Pie__set[0]["year"]

    for i in subcategory_sale__tar_set:
        if (temp != i["year"]):
            subcategory_tar_data["y" + temp] = {}
            subcategory_tar_data["y" + temp].update(category_tar_subdata.copy())

            category_tar_subdata = {"subcategory": [], "sale": [], "profit": []}
            temp = i["year"]

        category_tar_subdata["subcategory"].append(i["subCategory"])
        category_tar_subdata["sale"].append(round(i["sale"] / 10000))
        category_tar_subdata["profit"].append(round(i["profit"] / 10000, 2))

    subcategory_tar_data["y" + temp] = {}
    subcategory_tar_data["y" + temp].update(category_tar_subdata.copy())
    category_tar_subdata = {"subcategory": [], "sale": [], "profit": []}
    for i in category_sale_Pie__set:

        if (temp != i["year"]):
            category_Pie_data["y" + temp] = category_pie_subdata_list
            category_pie_subdata_list = []
            temp = i["year"]
        # if(i["id"]==category_sale_set_last.id):
        #     category_Pie_data["y"+temp]=category_pie_subdata_list
        #     category_pie_subdata_list=[]
        #     temp=i["year"]
        category_pie_subdata["name"] = i["category"]
        category_pie_subdata["value"] = round(i["saleSum"])
        category_pie_subdata_list.append(category_pie_subdata.copy())

    category_Pie_data["y" + temp] = category_pie_subdata_list
    category_pie_subdata_list = []

    # print(category_Pie_data)
    category_Pie_Json = json.dumps(category_Pie_data, ensure_ascii=False)
    subcategory_tar_Json = json.dumps(subcategory_tar_data, ensure_ascii=False)

    return render(request, "echart/category_sale.html",
                  {"category_tar_data": subcategory_tar_Json, "category_Pie_data": category_Pie_Json})


def segment_data(request):
    segment_Pie_Data = []
    segment_Pie_subData = {}
    segment_Pie_Set = segment_datatable.objects.all().values("cutomer_type").annotate(countSum=Sum("count"))
    for i in segment_Pie_Set:
        segment_Pie_subData["name"] = i["cutomer_type"]
        segment_Pie_subData["value"] = i["countSum"]
        segment_Pie_Data.append(segment_Pie_subData)
        segment_Pie_subData = {}
    segment_Pie_Json = json.dumps(segment_Pie_Data, ensure_ascii=False)

    segment_tar_Data_01 = {
        "region": [],
        "value": []
    }
    segment_Bar_Set_01 = segment_datatable.objects.all().values("region").annotate(countSum=Sum("count")).order_by(
        "countSum")

    for i in segment_Bar_Set_01:
        segment_tar_Data_01["region"].append(i["region"])
        segment_tar_Data_01["value"].append(i["countSum"])
    segment_Bar_Json_01 = json.dumps(segment_tar_Data_01, ensure_ascii=False)

    segment_bar_Data_02 = {
        "province": [],
        "value": []
    }
    segment_Bar_Set_02 = segment_datatable.objects.all().values("province").annotate(countSum=Sum("count")).order_by(
        "countSum")
    print(segment_Bar_Set_02)
    for i in segment_Bar_Set_02:
        segment_bar_Data_02["province"].append(i["province"])
        segment_bar_Data_02["value"].append(i["countSum"])
    segment_Bar_Json_02 = json.dumps(segment_bar_Data_02, ensure_ascii=False)

    return render(request, "echart/segment_data.html", {"segment_Pie_Json": segment_Pie_Json,
                                                 "segment_Bar_Json_01": segment_Bar_Json_01,
                                                 "segment_Bar_Json_02": segment_Bar_Json_02})


def loadParetoData(request):
    import pandas as pd
    df = pd.read_csv('E:\code\shixun\导入订单utf8.csv', index_col=0)
    # 2. RFM模型: 衡量客户价值和客户创造利益能力，并可视化
    ##2.1计算用户最后一次消费
    ### 根据客户id分类
    data_r = df[['客户 ID', '订单日期']]

    ## r 用户最后一次购买时间距离统计结束的时间
    data_r['订单日期'] = pd.to_datetime(data_r['订单日期'])
    data_r = data_r.groupby("客户 ID")['订单日期'].max().reset_index()
    data_r['R'] = (data_r['订单日期'].max() - data_r['订单日期']).dt.days + 1
    r = data_r.drop(['订单日期'], axis=1)

    ## f 用户购买频次
    f = df.groupby(['客户 ID', '订单日期']).size().reset_index(name="trade_num")
    ### 总共交易频次
    f = f.groupby('客户 ID')['trade_num'].sum().reset_index()
    f = f.rename(columns={'trade_num': 'F'})

    ## m 用户的消费总额
    ### m=消费总额
    m = df.groupby('客户 ID')['销售额'].sum().reset_index(name="M")
    m.head()
    ## rfm 三表联合
    rfm_data = pd.merge(r, f, on='客户 ID')
    rfm_data = pd.merge(rfm_data, m, on='客户 ID')
    ### 各值评分
    #### R-score
    r_bins = [0, 130, 200, 300, 400, 10000]
    r_labels = [5, 4, 3, 2, 1]
    rfm_data['R-score'] = pd.cut(rfm_data['R'], bins=r_bins, labels=r_labels, right=False)

    #### F-score
    f_bins = [1, 3, 5, 7, 13, 10000]
    f_labels = [1, 2, 3, 4, 5]
    rfm_data['F-score'] = pd.cut(rfm_data['F'], bins=f_bins, labels=f_labels, right=False)

    #### M-score
    m_bins = [0, 5000, 10000, 30000, 40000, 1000000]
    m_labels = [1, 2, 3, 4, 5]
    rfm_data['M-score'] = pd.cut(rfm_data['M'], bins=m_bins, labels=m_labels, right=False)
    ### 用户分类
    #### 将三个评分字段设置成float类型
    rfm_data['R-score'] = rfm_data['R-score'].astype(float)
    rfm_data['F-score'] = rfm_data['F-score'].astype(float)
    rfm_data['M-score'] = rfm_data['M-score'].astype(float)
    #### 计算每一个用户的评分是否大于均值
    rfm_data['r_above_mean'] = (rfm_data['R-score'] > rfm_data['R-score'].mean()) * 1
    rfm_data['f_above_mean'] = (rfm_data['F-score'] > rfm_data['F-score'].mean()) * 1
    rfm_data['m_above_mean'] = (rfm_data['M-score'] > rfm_data['M-score'].mean()) * 1
    #### total_score
    #### RFM总分值：RFM = R_score∗100 + F_score∗10 + M_score∗1
    rfm_data['total_score'] = rfm_data['r_above_mean'] * 1 + rfm_data['f_above_mean'] * 10 + rfm_data[
        'm_above_mean'] * 100
    rfm_data = rfm_data.sort_values(by=['total_score'], ascending=True)
    ### 客户分层
    customer_type_label = {111: '高价值客户', 110: '一般价值客户', 101: '重点发展客户', 100: '一般发展客户',
                           11: '重点保持客户', 10: '一般保持客户', 1: '重点挽留客户', 0: '潜在客户'}
    rfm_data['客户类型'] = rfm_data['total_score'].map(customer_type_label)
    for index, row in rfm_data.iterrows():
        rfm.objects.create(customer_id=row['客户 ID'], r_data=row['R'], f_data=row['F'], m_data=row['M'],
                           customer_type=row['客户类型'])

    # 3帕累托法则

    # Pareto_data = df.groupby('客户 ID')['销售额'].sum().reset_index(name="销售总额").sort_values(by=['销售总额'],ascending=False)
    # # #计算累计营收占比
    # Pareto_rate=Pareto_data[['客户 ID']]
    # Pareto_data["count"]=1
    # Pareto_rate['rate']=Pareto_data['销售总额'].cumsum()/Pareto_data['销售总额'].sum()
    # Pareto_rate["客户数"]=Pareto_data['count'].cumsum()/Pareto_data['count'].sum()

    # for index, row in Pareto_rate.iterrows():
    #     ParetoRate.objects.create(customer_id=row['客户 ID'],Pareto_rate=row['rate'],customer_count=row["客户数"])

    return HttpResponse("完成")


def visualization01(request):
    # 01
    import pandas as pd
    df = pd.read_csv('E:\code\shixun\导入订单utf8.csv', index_col=0)
    df['年'] = df['订单日期'].str.slice(0, 4)
    df['月'] = df['订单日期'].str.slice(5, 7)
    groupYear = (df.groupby('年'))['销售额'].sum().reset_index()
    groupYear['利润'] = ((df.groupby('年'))['利润'].sum()).reset_index()['利润']
    groupYear['利润率'] = groupYear['利润'] / (groupYear['销售额'] - groupYear['利润'])
    groupYear['卖出商品数'] = df.groupby(['年'])['数量'].sum().reset_index()['数量']
    groupYear['订单数'] = \
    df.groupby(['年', '订单 ID', '客户 ID']).count().reset_index()['年'].value_counts().reset_index()['count']
    groupYear['平均折扣'] = 1 - df.groupby(['年'])['折扣'].mean().reset_index()['折扣']
    groupYear['客单价'] = 1

    for index, row in groupYear.iterrows():
        visualizationdata01.objects.create(year=row['年'], sales=row['销售额'], profit=row['利润'],
                                           profitrate=row['利润率'], count=row['卖出商品数'], numberOrder=row['订单数'],
                                           averageDiscount=row['平均折扣'], guestListPrice=row['客单价'])

    groupmonth = df.groupby(['年', '月'])['销售额'].sum().reset_index()
    groupmonth['数量'] = df.groupby(['年', '月'])['数量'].sum().reset_index()['数量']
    groupmonth['利润'] = df.groupby(['年', '月'])['利润'].sum().reset_index()['利润']

    for index, row in groupmonth.iterrows():
        visualizationdata01_month.objects.create(year=row['年'], month=row['月'], sales=row['销售额'],
                                                 count=row['数量'], profit=row['利润'])
    return HttpResponse("okk")

def load_segment_data(request):
    import pandas as pd
    df = pd.read_csv('E:\code\shixun\导入订单utf8.csv', index_col=0)
    df = df.drop_duplicates(["客户 ID"])
    df["客户类型"] = df["细分"].replace([1, 2, 3], ["公司", "小型企业", "消费者"])

    segment_Data = df.groupby(["客户类型", '省/自治区', '地区', '城市'])["细分"].count().reset_index()
    for index, row in segment_Data.iterrows():
        segment_datatable.objects.create(cutomer_type=row["客户类型"], city=row["城市"], province=row['省/自治区'],
                                         region=row['地区'], count=row["细分"])

    return HttpResponse("okk")


def load_category_sale_data(request):
    import pandas as pd
    df = pd.read_csv('E:\code\shixun\导入订单utf8.csv', index_col=0)
    df['年'] = df['订单日期'].str.slice(0, 4)
    category_sale = df[["年", "类别", "子类别", "销售额", "利润"]].groupby(["年", "类别", "子类别"]).sum().reset_index()
    for index, row in category_sale.iterrows():
        category_saleDataTable.objects.create(year=row["年"], category=row['类别'], subCategory=row["子类别"],
                                              sale=row["销售额"], profit=row["利润"])
    return HttpResponse("okk")


def load_shipData(request):
    # if(shipData.objects.all().values())
    import pandas as pd
    df = pd.read_csv('E:\code\shixun\导入订单utf8.csv', index_col=0)
    df['年'] = df['订单日期'].str.slice(0, 4)
    df["订单日期"] = pd.to_datetime(df['订单日期'])
    df["发货日期"] = pd.to_datetime(df['发货日期'])
    df['天'] = (df["发货日期"] - df["订单日期"]).dt.days
    ship_Data = df.groupby(["年", "省/自治区", "邮寄方式"])["天"].mean().reset_index()
    ship_Data["邮寄方式"] = ship_Data["邮寄方式"].replace([1, 2, 3, 4], ["标准级", "当日", "一级", "二级"])
    for index, row in ship_Data.iterrows():
        shipData.objects.create(shiplevel=row["邮寄方式"], shipregion=row["省/自治区"], shipDay=row["天"],
                                shipYear=row["年"])

    return HttpResponse("okk")
