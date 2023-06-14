(function () {
    var myechart = echarts.init(document.getElementById("pie"))
    option = {
        title: {
            text: '客户占比',
            left: 'center'
        },
        tooltip: {
            trigger: 'item'
        },
        legend: {
            orient: 'vertical',
            left: 'left'
        },
        series: [
            {
                name: 'Access From',
                type: 'pie',
                radius: '50%',
                data: segment_Pie_Data,
                label: {
                    normal: {
                        show: true,
                        position: 'inner',
                        formatter: '{b}\n{c}\n{d}%',
                    },
                },
            }
        ]
    };
    myechart.setOption(option)
})();
(function () {
    var myechart = echarts.init(document.getElementById("bar_01"))
    option = {
        title:{
            text:"客户地区分布"
        },
        tooltip: {
          trigger: 'item'
      },
        legend:{},
        xAxis: {
            type: 'category',
            data: segment_Bar_Data_01.region
        },
        yAxis: {
            type: 'value'
        },
        series: [
            {
                name:"客户",
                data: segment_Bar_Data_01.value,
                type: 'bar',
                showBackground: true,
                backgroundStyle: {
                    color: 'rgba(180, 180, 180, 0.2)'
                }
            }
        ]
    };
    myechart.setOption(option)
})();
(function(){
    var myechart=echarts.init(document.getElementById("bar_02"))
    option = {
        title: {
          text: "客户省份分析"
        },
        tooltip: {
          trigger: 'item'
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
          data: segment_bar_Data_02.province
        },
        yAxis: {
          type: 'value',
          nameGap: 40
        },
        series: [
          {
            name: "RFM客户数",
            data: segment_bar_Data_02.value,
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
      myechart.setOption(option)
})();