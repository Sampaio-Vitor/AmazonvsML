document.addEventListener("DOMContentLoaded", function() {
  var amazonScore = {{ amazon_score }};
  var mercadolivreScore = {{ mercadolivre_score }};

  var amazonChart = new Chart(document.getElementById("amazon-chart"), {
    type: 'doughnut',
    data: {
      labels: ['Amazon Score', 'Remaining'],
      datasets: [{
        data: [amazonScore, 100 - amazonScore],
        backgroundColor: ['#36A2EB', '#E2E2E2'],
      }]
    },
    options: {
      cutoutPercentage: 80,
      plugins: {
        legend: {
          display: false
        }
      },
      tooltips: {
        enabled: false
      }
    }
  });

  var mercadolivreChart = new Chart(document.getElementById("mercadolivre-chart"), {
    type: 'doughnut',
    data: {
      labels: ['Mercado Livre Score', 'Remaining'],
      datasets: [{
        data: [mercadolivreScore, 100 - mercadolivreScore],
        backgroundColor: ['#FFCE56', '#E2E2E2'],
      }]
    },
    options: {
      cutoutPercentage: 80,
      plugins: {
        legend: {
          display: false
        }
      },
      tooltips: {
        enabled: false
      }
    }
  });

  var amazonCenterText = amazonChart.chart.ctx;
  amazonCenterText.font = "20px Arial";
  amazonCenterText.textAlign = 'center';
  amazonCenterText.textBaseline = 'middle';
  amazonCenterText.fillStyle = '#FFFFFF';
  amazonCenterText.fillText(amazonScore, amazonChart.chart.width / 2, amazonChart.chart.height / 2);

  var mercadolivreCenterText = mercadolivreChart.chart.ctx;
  mercadolivreCenterText.font = "20px Arial";
  mercadolivreCenterText.textAlign = 'center';
  mercadolivreCenterText.textBaseline = 'middle';
  mercadolivreCenterText.fillStyle = '#FFFFFF';
  mercadolivreCenterText.fillText(mercadolivreScore, mercadolivreChart.chart.width / 2, mercadolivreChart.chart.height / 2);

  var bestSiteElement = document.getElementById("best-site");
  var bestScoreElement = document.getElementById("best-score");

  if (amazonScore > mercadolivreScore) {
    bestSiteElement.textContent = "Amazon";
    bestScoreElement.textContent = amazonScore;
  } else {
    bestSiteElement.textContent = "Mercado Livre";
    bestScoreElement.textContent = mercadolivreScore;
  }
});
