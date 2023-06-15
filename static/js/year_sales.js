(function () {
  var tableData = document.getElementById("tobody")
  for (i = 0; i < 4 ; i++) {
    var tatr = document.createElement('tr')
    var tatd1 = document.createElement('td')
    tatd1.innerHTML = year_Sales_table_data.year[i]
    var tatd2 = document.createElement('td')
    tatd2.innerHTML = year_Sales_table_data.sale[i]
    var tatd3 = document.createElement('td')
    tatd3.innerHTML = year_Sales_table_data.profit[i]
    var tatd4 = document.createElement('td')
    tatd4.innerHTML = year_Sales_table_data.profitrate[i] + "%"
    var tatd5 = document.createElement('td')
    tatd5.innerHTML = year_Sales_table_data.count[i]
    var tatd6 = document.createElement('td')
    tatd6.innerHTML = year_Sales_table_data.numberOrder[i]
    var tatd7 = document.createElement('td')
    tatd7.innerHTML = year_Sales_table_data.averageDiscount[i] + "%"
    var tatd8 = document.createElement('td')
    tatd8.innerHTML = year_Sales_table_data.guestListPrice[i]

    tatr.appendChild(tatd1)
    tatr.appendChild(tatd2)
    tatr.appendChild(tatd3)
    tatr.appendChild(tatd4)
    tatr.appendChild(tatd5)
    tatr.appendChild(tatd6)
    tatr.appendChild(tatd7)
    tatr.appendChild(tatd8)
    tableData.appendChild(tatr)
  }
})();

(function () {
  var myecharts = echarts.init(document.getElementById("col_02_01"))
  option = {
    legend: {},
    title: {
      text: "年销售累计"
    },
    tooltip: {
      trigger: 'item',
      axisPointer: {
        type: 'shadow'
      }
    },
    xAxis: {
      type: 'category',
      name: "年",
      nameLocation: "middle",
      nameGap: 40,
      data: year_Sales_table_data.year
    },
    yAxis: [{
      name: '销售额',
      type: 'value',
      axisLine: {
        show: true,
      },
    }, {
      name: '数量',
      type: 'value',
      axisLine: {
        show: true,
      },
    }, {
      name: '利润',
      type: 'value',
      offset: 40,
      axisLine: {
        show: true,
      },
    }],
    series: [
      {
        name: "销售额",
        data: year_Sales_table_data.sale,
        type: 'bar',
        showBackground: true,
        backgroundStyle: {
          color: 'rgba(180, 180, 180, 0.2)'
        },
        yAxisIndex: 0,

      }, {
        name: "数量",
        data: year_Sales_table_data.count,
        type: 'bar',
        showBackground: true,
        backgroundStyle: {
          color: 'rgba(180, 180, 180, 0.2)'
        },
        yAxisIndex: 1,

      }, {
        name: "利润",
        data: year_Sales_table_data.profit,
        type: 'bar',
        showBackground: true,
        backgroundStyle: {
          color: 'rgba(180, 180, 180, 0.2)'
        },
        yAxisIndex: 2,

      }
    ]
  };
  myecharts.setOption(option)
})();
(function () {
  var myecharts = echarts.init(document.getElementById("col_02_02"))
  // Generate data.
  option = {
    title: {
      text: '月销售',
      left: 'left'
    },
    legend: {
      top: '10%'
    },
    tooltip: {
      trigger: 'item',
      axisPointer: {
        type: 'shadow'
      }
    },
    grid: {
      left: '10%',
      top: '20%',
      right: '10%',
      bottom: '15%'
    },
    dataset: [
      {
        source: year_month_data.sale
      },
      {
        source: year_month_data.count
      },
      {
        source: year_month_data.profit
      },
      {
        fromDatasetIndex: 0,
        transform: {
          type: 'boxplot',
          config: {
            itemNameFormatter: function (params) {
              switch (params.value) {
                case 0: return '2015'
                  break;
                case 1: return '2016'
                  break;
                case 2: return '2017'
                  break;
                case 3: return '2018'
                  break;
                // code
              }
            }
          }
        }
      },
      {
        fromDatasetIndex: 1,
        transform: {
          type: 'boxplot',
          config: {
            itemNameFormatter: function (params) {
              switch (params.value) {
                case 0: return '2015'
                  break;
                case 1: return '2016'
                  break;
                case 2: return '2017'
                  break;
                case 3: return '2018'
                  break;
                // code
              }
            }
          }
        }
      },
      {
        fromDatasetIndex: 2,
        transform: {
          type: 'boxplot',
          config: {
            itemNameFormatter: function (params) {
              switch (params.value) {
                case 0: return '2015'
                  break;
                case 1: return '2016'
                  break;
                case 2: return '2017'
                  break;
                case 3: return '2018'
                  break;
                // code
              }
            }
          }
        }
      },
    ],
    xAxis: {
      type: 'category',
      boundaryGap: true,
      nameGap: 30,
      splitArea: {
        show: true
      },
      splitLine: {
        show: false
      }
    },
    yAxis: [{
      type: 'value',
      name: '销售额',
      splitArea: {
        show: false
      },
      axisLine: {
        show: true,
      },
    }, {
      type: 'value',
      name: '数量',
      splitArea: {
        show: false
      },
      axisLine: {
        show: true,
      },
    }, {
      type: 'value',
      name: '利润',
      splitArea: {
        show: false
      },
      axisLine: {
        show: true,
      },
      offset: 40
    }],
    series: [
      {
        name: '销售额',
        type: 'boxplot',
        datasetIndex: 3,
        yAxisIndex: 0,
        itemStyle: {
          color: '#b8c5f2'
        },
      },
      {
        name: '数量',
        type: 'boxplot',
        datasetIndex: 4,
        yAxisIndex: 1,
        itemStyle: {
          color: '#65B581'
        },
      },
      {
        name: '利润',
        type: 'boxplot',
        datasetIndex: 5,
        yAxisIndex: 2,
        itemStyle: {
          color: '#FFCE34'
        },
      }
    ]
  };
  myecharts.setOption(option)
})();

(function () {
  year_div = ["col_03_01", "col_03_02", "col_03_03", "col_03_04"]
  month_x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
  for (i = 0; i < 4; i++) {
    var myecharts = echarts.init(document.getElementById(year_div[i]))
    option = {
      legend: {
        right: 0
      },
       tooltip: {
      trigger: 'item',
      axisPointer: {
        type: 'shadow'
      }
    },
      title: {
        text: "201" + (i + 5) + "年月销售"
      },
      xAxis: {
        type: 'category',
        data: month_x
      },
      yAxis: [{
        name: '销售额',
        type: 'value',

      },
        {
        name: '数量',
        type: 'value',
      },
        {
        name: '利润',
        type: 'value',
        offset: 25,

      }],
      series: [
        {
          name: "销售额",
          data: year_month_data.sale[i],
          type: 'line',
          smooth: false,
          yAxisIndex: 0,
        },
        {
          name: "数量",
          data: year_month_data.count[i],
          type: 'line',
          smooth: false,
          yAxisIndex: 1,
        },
        {
          name: "利润",
          data: year_month_data.profit[i],
          type: 'line',
          smooth: false,
          yAxisIndex: 2,
        }
      ]
    };
    myecharts.setOption(option)
  }
})();