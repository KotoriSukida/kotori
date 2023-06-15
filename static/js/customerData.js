

(function () {
  var tableData = document.getElementById("tobody")
  for (i = 0; i < rfmData.customer_id.length; i++) {

    var tatr = document.createElement('tr')

    var tatd1 = document.createElement('th')
    tatd1.innerHTML = i
    var tatd2 = document.createElement('td')
    tatd2.innerHTML = rfmData.customer_id[i]
    var tatd3 = document.createElement('td')
    tatd3.innerHTML = rfmData.R[i]
    var tatd4 = document.createElement('td')
    tatd4.innerHTML = rfmData.F[i]
    var tatd5 = document.createElement('td')
    tatd5.innerHTML = rfmData.M[i]

    tatr.appendChild(tatd1)
    tatr.appendChild(tatd2)
    tatr.appendChild(tatd3)
    tatr.appendChild(tatd4)
    tatr.appendChild(tatd5)
    tableData.appendChild(tatr)
  }
})();

(function () {
  var myecharts = echarts.init(document.getElementById('rfmsum'))
  var idsum = 0
  var moneysum = 0
  for (i = 0; i < rfmSumData.RFM客户数.length; i++) {
    idsum = rfmSumData.RFM客户数[i] + idsum
    moneysum = rfmSumData.RFM销售额[i] + moneysum
  }
  option = {
    legend: {},
    title: {
      text: "RFM分级分析"
    },
    xAxis: {
      type: 'category',
      data: rfmSumData.客户类型
    },
    yAxis: [
      {
        name: "客户id计数",
        nameLocation: "middle",
        type: 'value',
        nameGap: 40
      },
      {
        name: "销售额",
        type: 'value',
        nameLocation: "middle",
        axisLabel: {
          formatter: '{value} k'
        },
        nameGap: 60
      }
    ],
    series: [
      {
        name: "RFM客户数",
        data: rfmSumData.RFM客户数,
        type: 'bar',
        yAxisIndex: 0,
        showBackground: true,
        backgroundStyle: {
          color: 'rgba(180, 180, 180, 0.2)'
        },
        label: {
          show: true,
          position: 'top',
          formatter: '{c}\n'
        }
      }, {
        name: "RFM销售额",
        data: rfmSumData.RFM销售额,
        type: 'bar',
        yAxisIndex: 1,
        showBackground: true,
        backgroundStyle: {
          color: 'rgba(180, 180, 180, 0.2)'
        },
        label: {
          show: true,
          position: 'top'
        }
      }
    ]
  };
  myecharts.setOption(option)
})();
(function () {
  var myecharts = echarts.init(document.getElementById('rfm_r'))
  option = {
    title: {
      text: "R值分布情况(RFM)"
    },
    visualMap: {
      orient: 'vertical',
      right: 0,
      top: 'center',
      calculable: true,
      min: 0,
      max: 150,
      // Map the score column to color
      // dimension: 0,
      inRange: {
        color: ['#65B581', '#FFCE34', '#FD665F']
      }
    },
    xAxis: {
      type: 'category',
      name: "天",
      data: rfmRData.R值
    },
    yAxis: {
      name: "客户id计数",
      nameLocation: "middle",
      type: 'value',
      nameGap: 40
    },
    series: [
      {
        name: "RFM客户数",
        data: rfmRData.count,
        type: 'bar',
        yAxisIndex: 0,
        showBackground: true,
        backgroundStyle: {
          color: 'rgba(180, 180, 180, 0.2)'
        },
        label: {
          show: true,
          position: 'top',
          formatter: '{c}\n'
        }
      }
    ]
  };
  myecharts.setOption(option)
})();
(function () {
  var myecharts = echarts.init(document.getElementById('rfm_f'))
  option = {
    title: {
      text: "F值分布情况(RFM)"
    },
    visualMap: {
      orient: 'vertical',
      right: 0,
      top: 'center',
      calculable: true,
      min: 0,
      max: 120,
      // Map the score column to color
      // dimension: 0,
      inRange: {
        color: ['#65B581', '#FFCE34', '#FD665F']
      }
    },
    xAxis: {
      type: 'category',
      name: "次",
      data: fSetData.F值
    },
    yAxis: {
      name: "客户id计数",
      nameLocation: "middle",
      type: 'value',
      nameGap: 40
    },
    series: [
      {
        name: "RFM客户数",
        data: fSetData.count,
        type: 'bar',
        yAxisIndex: 0,
        showBackground: true,
        backgroundStyle: {
          color: 'rgba(180, 180, 180, 0.2)'
        },
        label: {
          show: true,
          position: 'top',
          formatter: '{c}\n'
        }
      }
    ]
  };
  myecharts.setOption(option)
})();
(function () {
  var myecharts = echarts.init(document.getElementById('rfm_m'))
  option = {
    title: {
      text: "M值分布情况(RFM)"
    },
    visualMap: {
      orient: 'vertical',
      right: 0,
      top: 'center',
      calculable: true,
      min: 0,
      max: 150,
      // Map the score column to color
      // dimension: 0,
      inRange: {
        color: ['#65B581', '#FFCE34', '#FD665F']
      }
    },
    xAxis: {
      type: 'category',
      name: "元",
      data: mSetData.m值
    },
    yAxis: {
      name: "客户id计数",
      nameLocation: "middle",
      type: 'value',
      nameGap: 40
    },
    series: [
      {
        name: "RFM客户数",
        data: mSetData.count,
        type: 'bar',
        yAxisIndex: 0,
        showBackground: true,
        backgroundStyle: {
          color: 'rgba(180, 180, 180, 0.2)'
        },
        label: {
          show: true,
          position: 'top',
          formatter: '{c}\n'
        }
      }
    ]
  };
  myecharts.setOption(option)
})();