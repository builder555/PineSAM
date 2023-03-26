<script setup>
import { ref } from 'vue';
import { useAppStore } from '../stores/appstore';
import { Chart as ChartJS, CategoryScale, LinearScale, PointElement, LineElement, Title, Tooltip } from 'chart.js';
import { Line } from 'vue-chartjs';

ChartJS.register(CategoryScale, LinearScale, PointElement, LineElement, Title, Tooltip);
const pointsToDisplay = 50;
const chart = ref('chart');
const tempColor = '#f87979';
const powerColor = '#00c4ab';
const refreshRate = 500;
const data = {
  labels: Array(pointsToDisplay+1).fill(''),
  datasets: [
    {
      label: 'Temperature',
      backgroundColor: tempColor,
      borderColor: tempColor,
      data: Array(pointsToDisplay).fill(0),
      yAxisID: 'temperature',
    },
    {
      label: 'Power',
      backgroundColor: powerColor,
      borderColor: powerColor,
      data: Array(pointsToDisplay).fill(0),
      yAxisID: 'power',
    },
  ],
};
const store = useAppStore();
const options = {
  responsive: true,
  maintainAspectRatio: false,
  animation: {
    duration: refreshRate,
    easing: 'linear',
  },
  animations: {
    y: { duration: 0 },
  },
  elements: {
    point: { radius: 0 },
    line: { cubicInterpolationMode: 'monotone' },
  },
  scales: {
    x: {
      min: 1,
      max: pointsToDisplay-1,
      display: false,
      grid: {
        borderDash: [8, 4],
        lineWidth: 2,
      },
    },
    temperature: {
      position: 'left',
      suggestedMin: 0,
      suggestedMax: 450,
      ticks: {
        callback: function (value) {
          const unit = ['C', 'F'][store.settings?.TemperatureUnit?.value ?? 0];
          return `${value} ${unit}`;
        },
        font: { size: '20rem' },
        color: tempColor,
        maxTicksLimit: 12,
      },
      grid: {
        borderDash: [8, 4],
        lineWidth: 2,
      },
    },
    power: {
      position: 'right',
      suggestedMin: 0,
      suggestedMax: 120,
      ticks: {
        callback: function (value) {
          return value + ' W';
        },
        font: { size: '20rem' },
        color: powerColor,
        maxTicksLimit: 8,
      },
      grid: {
        drawOnChartArea: false,
      },
    },
  },
};
const addData = () => {
  const { liveData: { LiveTemp = 0, Watts = 0 } } = store;
  data.datasets[0].data.push(LiveTemp);
  data.datasets[0].data.shift();
  data.datasets[1].data.push(Watts);
  data.datasets[1].data.shift();
  chart.value.chart.update();
};
setInterval(() => {
  addData();
}, refreshRate);
</script>
<template>
  <div class="chart-holder">
    <Line ref="chart" :data="data" :options="options" />
  </div>
</template>
<style scoped>
.chart-holder {
  width: 100%;
  height: 100%;
  min-height:350px;
  position: relative;
}
</style>