document.addEventListener("DOMContentLoaded", function() {
    var selectedItem = "{{ selected_item }}";
    var amazonHighestComment = "{{ amazon_highest_score_comment }}";
    var amazonLowestComment = "{{ amazon_lowest_score_comment }}";
    var mercadolivreHighestComment = "{{ mercadolivre_highest_score_comment }}";
    var mercadolivreLowestComment = "{{ mercadolivre_lowest_score_comment }}";
    var amazonScore = {{ amazon_average_score }};
    var mercadolivreScore = {{ mercadolivre_average_score }};
  
    // Atualizar os elementos HTML com os dados recebidos
    document.getElementById("selected-item").textContent = selectedItem;
    document.getElementById("amazon-highest-comment").textContent = amazonHighestComment;
    document.getElementById("amazon-lowest-comment").textContent = amazonLowestComment;
    document.getElementById("mercadolivre-highest-comment").textContent = mercadolivreHighestComment;
    document.getElementById("mercadolivre-lowest-comment").textContent = mercadolivreLowestComment;
  
    // Criar os gráficos de rosca
    var amazonChart = new Chart(document.getElementById("amazon-chart"), {
      type: 'doughnut',
      data: {
        labels: ['Amazon Score', 'Remaining'],
        datasets: [{
          data: [amazonScore, 100 - amazonScore],
          backgroundColor: ['#FFCE56', '#E2E2E2'],
        }]
      },
      options: {
        cutoutPercentage: 80,
        plugins: {
          legend: {
            display: false
          }
        }
      }
    });
  
    var mercadolivreChart = new Chart(document.getElementById("mercadolivre-chart"), {
      type: 'doughnut',
      data: {
        labels: ['Mercado Livre Score', 'Remaining'],
        datasets: [{
          data: [mercadolivreScore, 100 - mercadolivreScore],
          backgroundColor: ['#36A2EB', '#E2E2E2'],
        }]
      },
      options: {
        cutoutPercentage: 80,
        plugins: {
          legend: {
            display: false
          }
        }
      }
    });
  
    // Definir o melhor site e pontuação
    var bestSiteElement = document.getElementById("best-site");
    var bestScoreElement = document.getElementById("best-score");
  
    if (amazonScore > mercadolivreScore) {
      bestSiteElement.textContent = "Amazon";
      bestScoreElement.textContent = amazonScore.toFixed(2);
    } else {
      bestSiteElement.textContent = "Mercado Livre";
      bestScoreElement.textContent = mercadolivreScore.toFixed(2);
    }
  });
  