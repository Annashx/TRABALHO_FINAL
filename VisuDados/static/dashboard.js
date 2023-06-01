/* globals Chart:false, feather:false */

(() => {
  'use strict'

  feather.replace({ 'aria-hidden': 'true' })
  console.log(la)
  // Graphs
  const ctx = document.getElementById('myChart')
  // eslint-disable-next-line no-unused-vars
  const myChart = new Chart(ctx, {
    type: 'line',
    data: {
      labels: la,
      datasets: [{
        data: dt,
        lineTension: 0.3,
        backgroundColor: '#4201e4',
        borderColor: '#4203e4',
        borderWidth: 4,
        pointBackgroundColor: '#4201e4'
      }, {
        data: k,
        lineTension: 0.3,
        backgroundColor: '#aa2b14',
        borderColor: '#aa2b14',
        borderWidth: 4,
        pointBackgroundColor: '#aa2b14'
      }]
    },
    options: {
      plugins: {
        legend: {
          display: false,
        },
        tooltip: {
          boxPadding: 3
        },
        title: {
          display: true,
          text: 'Experimentos Química III',
          color: "#000000",
          font: {
            size: 25,
          }
        },
        subtitle: {
          display: true,
          text: "Experimentos realizados por alunos da disciplina de Química III 2023.1",
          color: "#000000",
          font: {
            size: 12,
          },
          padding: {
            bottom: 30
          }

        }
      }
    }
  })
})()
