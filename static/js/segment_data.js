(function () {
    var myechart = echarts.init(document.getElementById("pie"))
    option = {
        title: {
            text: '客户占比',
        },
        tooltip: {
            trigger: 'item'
        },
        legend: {

        },
        series: [
            {
                name: '客户占比',
                type: 'pie',
                radius: '50%',
                data: segment_Pie_Data,

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

        xAxis: {
            type: 'category',
            data: segment_Bar_Data_01.region
        },
        yAxis: {
            type: 'value'
        },
        series: [
            {
                name:"客户地区分布",
                data: segment_Bar_Data_01.value,
                type: 'bar',
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

          }
        ]
      };
      myechart.setOption(option)
})();