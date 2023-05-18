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
        backgroundColor: '#322c8e',
        borderColor: '#322c8e',
        borderWidth: 4,
        pointBackgroundColor: '#fc370c'
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
          text: "Experimentos realizados por alunos da disciplina de Química III",
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
