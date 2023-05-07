<script setup>
import { ref, computed } from 'vue';
import { useAppStore } from '../stores/appstore';
import { Chart as ChartJS, CategoryScale, LinearScale, PointElement, LineElement, Title, Tooltip } from 'chart.js';
import { Line } from 'vue-chartjs';
const store = useAppStore();
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
    // horizontal line to display the set temperature
    {
      label: 'Set Temperature',
      backgroundColor: 'rgb(160,23,165)',
      borderColor: 'rgb(160,23,165)',
      data: Array(pointsToDisplay).fill(0),
      yAxisID: 'temperature',
      type: 'line',
      borderWidth: 1,
    },
  ],
};
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
      display: true,
      border: {
        dash: [8, 4],
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
      suggestedMax: 100,
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
const liveTemp = computed(() => store.liveData?.LiveTemp ?? 0);
const tempUnits = computed(() => ['ºC', 'F'][store.settings?.TemperatureUnit?.value ?? 0]);
const watts = computed(() => store.liveData?.Watts ?? 0);
const setTemp = computed(() => store.settings?.SetTemperature?.value ?? 0);
const addData = () => {
  data.datasets[0].data.push(liveTemp.value);
  data.datasets[0].data.shift();
  data.datasets[1].data.push(watts.value);
  data.datasets[1].data.shift();
  data.datasets[2].data.push(setTemp.value);
  data.datasets[2].data.shift();
  chart.value.chart.update();
};
setInterval(() => {
  addData();
}, refreshRate);
</script>
<template>
  <div class="chart-holder">
    <div class="temp-display">
      <p class="color-temp">
        Live temp: {{ liveTemp }}{{ tempUnits }}
      </p>
      <p class="color-watts">
        Power: {{ watts }}W
      </p>
      <p class="accent">
        Set temp: {{ setTemp }}{{ tempUnits }}
      </p>
    </div>
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
.temp-display {
  position: absolute;
  top: 15px;
  left: 80px;
  font-size: 1.3rem;
  font-weight: 500;
}
.temp-display p {
  margin-top:-5px;
}
.color-temp {
  color: #f87979;
}
.color-watts {
  color: #00c4ab;
}
</style>
