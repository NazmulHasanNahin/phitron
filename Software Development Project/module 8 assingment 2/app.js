const searchBtn = document.getElementById('search-btn');
const searchInput = document.getElementById('search-input');
const results = document.getElementById('results');
const selectedPlayers = document.getElementById('selected-players');
const playerModal = document.getElementById('player-modal');
const playerDetails = document.getElementById('player-details');
const closeBtn = document.getElementById('close-btn');
const playerCount = document.getElementById('player-count');

let selectedPlayersList = [];

// Fetch and display 10 players on page load
document.addEventListener('DOMContentLoaded', () => {
  fetch('https://www.thesportsdb.com/api/v1/json/3/searchplayers.php?p=a')
    .then(response => response.json())
    .then(data => {
      if (data.player) {
        displayPlayers(data.player.slice(11, 25));
      }
    });
});

searchBtn.addEventListener('click', () => {
  const query = searchInput.value.trim();
  if (query) {
    fetch(`https://www.thesportsdb.com/api/v1/json/3/searchplayers.php?p=${query}`)
      .then(response => response.json())
      .then(data => {
        if (data.player) {
          displayPlayers(data.player);
        } else {
          results.innerHTML = '<p>No players found</p>';
        }
      });
  }
});

function displayPlayers(players) {
  results.innerHTML = '';
  players.forEach(player => {
    const playerCard = document.createElement('div');
    playerCard.classList.add('card');
    playerCard.innerHTML = `
      <img src="${player.strThumb || 'default-image.jpg'}" alt="${player.strPlayer}">
      <h3>${player.strPlayer}</h3>
      <p>Phone: ${player.strPhone || 'N/A'}</p>
      <p>Email: ${player.strEmail || 'N/A'}</p>
      <p>City: ${player.strCity || 'N/A'}</p>
      <p>Country: ${player.strCountry || 'N/A'}</p>
      <p>Gender: ${player.strGender || 'N/A'}</p>
      <button class="details-btn" data-id="${player.idPlayer}">Details</button>
      <button class="add-btn" data-id="${player.idPlayer}">Add to Group</button>
    `;
    results.appendChild(playerCard);
  });
}

results.addEventListener('click', e => {
  if (e.target.classList.contains('details-btn')) {
    const playerId = e.target.dataset.id;
    fetch(`https://www.thesportsdb.com/api/v1/json/3/lookupplayer.php?id=${playerId}`)
      .then(response => response.json())
      .then(data => {
        displayPlayerDetails(data.players[0]);
      });
  } else if (e.target.classList.contains('add-btn')) {
    const playerId = e.target.dataset.id;
    if (selectedPlayersList.length < 11 && !selectedPlayersList.includes(playerId)) {
      selectedPlayersList.push(playerId);
      fetch(`https://www.thesportsdb.com/api/v1/json/3/lookupplayer.php?id=${playerId}`)
        .then(response => response.json())
        .then(data => {
          addPlayerToGroup(data.players[0]);
          playerCount.textContent = `Added Players: ${selectedPlayersList.length}`;
          if (selectedPlayersList.length === 11) {
            alert('You have added the maximum of 11 players.');
          }
        });
    }
  }
});

function displayPlayerDetails(player) {
  playerDetails.innerHTML = `
    <h2>${player.strPlayer}</h2>
    <p>Team: ${player.strTeam}</p>
    <p>Position: ${player.strPosition}</p>
    <p>Nationality: ${player.strNationality}</p>
    <p>Description: ${player.strDescriptionEN}</p>
    <a href="${player.strYoutube}" target="_blank">Watch Video on YOUTUBE</a>
    <div class="social-links">
      <a href="https://${player.strFacebook}" target="_blank"><i class="fab fa-facebook"></i></a>
      <a href="https://${player.strInstagram}" target="_blank"><i class="fab fa-instagram"></i></a>
      <a href="https://${player.strTwitter}" target="_blank"><i class="fab fa-twitter"></i></a>
    </div>
  `;
  playerModal.style.display = 'block';
}

function addPlayerToGroup(player) {
  const playerCard = document.createElement('div');
  playerCard.classList.add('card');
  playerCard.innerHTML = `
    <img src="${player.strThumb || 'default-image.jpg'}" alt="${player.strPlayer}">
    <h3>${player.strPlayer}</h3>
  `;
  selectedPlayers.appendChild(playerCard);
}

closeBtn.addEventListener('click', () => {
  playerModal.style.display = 'none';
});

window.onclick = function (event) {
  if (event.target == playerModal) {
    playerModal.style.display = 'none';
  }
}
