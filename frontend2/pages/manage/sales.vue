<template>
    <section class="flex flex-col items-center">
        <div class="w-full max-w-[100vw] md:max-w-[80vw] p-2 bg-blue-500 text-white rounded my-1">a</div>
        <Bar
            id="my-chart-id"
            :options="chartOptions"
            :data="chartData"
            class="max-w-[100vw] md:max-w-[80vw] max-h-[80vh]"
        />
    </section>
  </template>
  
<script setup>
    import { Bar } from 'vue-chartjs'
    import { Chart as ChartJS, Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale } from 'chart.js'
    
    ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale)
    definePageMeta({
        layout: 'manage'
    })
    const chartData = {
        labels: [ '01','02','03','01','02','03','01','02','03','01','02','03','01','02','03','01','02','03','01','02','03','01','02','03','01','02','03','01','02','03', ],
        datasets: [ 
            { 
                label: 'Number Of Sales',
                data: [ 40, 20, 12,40, 20, 12,40, 20, 12,40, 20, 12,40, 20, 12,40, 20, 12,40, 20, 12,40, 20, 12,40, 20, 12,40, 20, 12, ],
                backgroundColor: '#f87979',
                yAxisID: 'y1',
                borderWidth: 1
            },
            { 
                label: 'Number Of Sales',
                data: [ 240, 20, 12,406, 20, 12,430, 20, 12,40, 230, 12,40, 20, 122,40, 20, 12,403, 20, 12,430, 20, 12,40, 20, 12,40, 240, 12, ],
                backgroundColor: '#7c43c7',
                yAxisID: 'y2',
                borderWidth: 1
            } 
        ]
    }
    const  chartOptions = {
        responsive: true,
        legend: {
        position: 'left', // Set the legend position to the left
        },
        scales: {
            y1: {
                type: 'linear',
                display: true,
                position: 'left',
                ticks: {
                beginAtZero: true,
                precision: 0
                },
                grid: {
                display: true
                }
            },
            y2: {
                type: 'linear',
                display: true,
                position: 'right',
                ticks: {
                beginAtZero: true,
                callback: function(value, index, values) {
                    return '$' + value;
                }
                },
                grid: {
                display: false
                }
            }
        },
    }
</script>