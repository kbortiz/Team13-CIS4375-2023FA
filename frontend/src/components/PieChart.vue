<!-- eslint-disable prettier/prettier -->
<!-- eslint-disable prettier/prettier -->
<!-- eslint-disable prettier/prettier -->
<!-- eslint-disable prettier/prettier -->
<!-- eslint-disable prettier/prettier -->
<template>
  <div>
    <div class="flex flex-col col-span-2 content-center">
      <table class="min-w-full shadow-md rounded">
        <thead class="bg-gray-50 text-xl">
          <tr>
            <th class="p-4 text-left">Zip Code</th>
            <th class="p-4 text-left">Number of Attendees</th>
          </tr>
        </thead>
        <tbody class="divide-y divide-gray-300">
          <tr v-for="(zip,index) in this.pieChartData.data.labels" :key="index">
            <td class="p-2 text-left">{{zip}}</td>
            <td class="p-2 text-left">
              <span v-for="(dataset, datasetIndex) in this.pieChartData.data.datasets" :key="datasetIndex">{{ dataset.data[index] }}</span>
            </td>
          </tr>        
        </tbody>
      </table>
    </div>
    <!-- canvas element for chart -->
    <label class="font-bold text-4xl text-red-700 tracking-widest text-center mt-10">Attendees by Zipcode</label>
    <canvas id="pie-chart"></canvas>
  </div>
</template>
<script>
import { Chart, registerables } from 'chart.js'

//we have to register the registerables with Chart object
Chart.register(...registerables)

export default {
  name: 'PieChart',
  data() {
    return {
      pieChartData: {
        type: 'pie',
        data: {
          labels: [77449,78806,77067,77840,77650],
          datasets: [
            {
              label: 'Number of attendees',
              data: [2,2,3,4,5],
              backgroundColor: [
                '#f6ad55',
                '#dd6b20',
                '#3b82f6',
                '#ef4444',
                '#10b981'
              ]
            }
          ]
        },
        options: {
          responsive: true,
          plugins: {
            legend: {
              position: 'right'
            }
          }
        }
      }
    }
  },
  mounted() {
    // Mount to canvas with the id "pie-chart"
    const ctx = document.getElementById('pie-chart')
    // Create Chart
    const chart = new Chart(ctx, this.pieChartData)

    // Fetch data from API
    fetch('/events/attendees-by-zipcode')
      .then((response) => response.json())
      .then((data) => {
        // Update chart data
        chart.data.labels = data.map((item) => item.zipCode)
        chart.data.datasets[0].data = data.map((item) => item.count)
        chart.update()

        // Update table data
        this.pieChartData.data.labels = data.map((item) => item.zipCode)
        this.pieChartData.data.datasets[0].data = data.map((item) => item.count)
      })
      .catch((error) => {
        console.log
      })
  }
}
</script>
