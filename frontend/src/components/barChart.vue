<!--Shows chart tag-->
<template>
    <div class="shadow-lg rounded-lg overflow-hidden">
      <canvas class="p-10" ref="attendanceChart"></canvas>
    </div>
  </template>
<script>
import { Chart, registerables } from 'chart.js'
Chart.register(...registerables) //using Chart js

export default {
  props: {
    label: {
      type: Array
    },
    chartData: {
      type: Array
    }
  },
  async mounted() {
    const backgroundColor = this.chartData.map(() => this.getColor())
    const borderColor = backgroundColor.map((e) =>
      e.replace(/[\d\.]+\)$/g, '1)')
    )
    //Hard-coded data for the bar chart in the main page sprint 2. to be changed later
    await new Chart(this.$refs.attendanceChart, {
      type: 'bar',
      data: {
        labels: ["Event A", "Event B", "Event C","Event D", "Event E", "Event F","Event G", "Event H", "Event I","Event J"],//this.label, -->use for sprint 3
        datasets: [
          {
            label: "Number of Attendees in each Events",
            borderWidth: 1,
            backgroundColor: ['rgba(0,0,128,1)'],
            borderColor: ['rgba(0,0,0,1)'],
            data: [10,15,7,9,5,18,23,20,12,6]
          }
        ]
      },
      options: {
        scales: {
          y: {
            ticks: {
              stepSize: 1
            }
          },
          x: {
            gridLines: {
              display: false
            }
          }
        },
        plugins: {
          legend: {
            display: false
          }
        },
        responsive: true,
        maintainAspectRatio: true
      }
    })
  },
  //The 'getColor' method to generate random colors with a set trasparency of 0.2 for a
  methods: {
    getColor() {
      let channel = () => Math.random() * 255
      return `rgba(${channel()}, ${channel()}, ${channel()}, 0.2)`
    }
  }
}
</script>
