<!-- This is for the top 5 words -->
<template>
  <Bar
    :chart-options="chartOptions"
    :chart-data="chartData"
    :chart-id="chartId"
    :dataset-id-key="datasetIdKey"
    :plugins="plugins"
    :css-classes="cssClasses"
    :styles="styles"
    :width="width"
    :height="height"
  />
</template>

<script>
import { Bar } from 'vue-chartjs'
import { Chart as ChartJS, Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale } from 'chart.js'

ChartJS.register(Title, BarElement, CategoryScale, LinearScale)

export default {
  name: 'BarChart',
  components: { Bar },
  props: {
    chartId: {
      type: String,
      default: 'bar-chart'
    },
    datasetIdKey: {
      type: String,
      default: 'label'
    },
    width: {
      type: Number,
      default: 50
    },
    height: {
      type: Number,
      default: 35
    },
    cssClasses: {
      default: '',
      type: String
    },
    styles: {
      type: Object,
      default: () => {}
    },
    plugins: {
      type: Object,
      default: () => {}
    },

    
  },
  data() {
    return {
      chartData: {
        labels: [ 'January', 'February', 'March' ],
        datasets: [ { data: [40, 20, 12] , backgroundColor: ['#1c1e21', '#373b41', '#525861', '#525861'] } ],
      },
      chartOptions: {
        responsive: true,
       
    //     scales: {
    //     yAxes: [{
    //     ticks: {
    //       min: 0,
    //       max: 300,
    //       stepSize: 100,
    //       reverse: false,
    //       beginAtZero: true
    //     }
    //   }]
    // }

        scales: {
            y: {
                type: 'linear',
                min: 0,
                ticks: { 
                    stepSize: 1
                }
            }
        
        }
  

        
        
        
        
      }
    }
  }
}
</script>