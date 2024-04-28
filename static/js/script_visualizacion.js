document.addEventListener('DOMContentLoaded', function () {
  const opciones = [
    'mmorpg',
    'shooter',
    'strategy',
    'moba',
    'racing',
    'sports',
    'social',
    'sandbox',
    'open-world',
    'survival',
    'pvp',
    'pve',
    'pixel',
    'voxel',
    'zombie',
    'turn-based',
    'first-person',
    'third-person',
    'top-down',
    'tank',
    'space',
    'sailing',
    'side-scroller',
    'superhero',
    'permadeath',
    'card',
    'battle-royale',
    'mmo',
    'mmofps',
    'mmotps',
    '3d',
    '2d',
    'anime',
    'fantasy',
    'sci-fi',
    'fighting',
    'action-rpg',
    'action',
    'military',
    'martial-arts',
    'flight',
    'low-spec',
    'tower-defense',
    'horror',
    'mmorts'
  ]

  const url = new URL(window.location.href)

  const params = new URLSearchParams(url.search)

  const genero = params.get('genero')

  const selectElement = document.getElementById('generoJuego')

  function agregarOpciones(opciones, selectElement) {
    opciones.forEach((opcion) => {
      const optionElement = document.createElement('option')

      optionElement.value = opcion
      optionElement.textContent = opcion
      selectElement.appendChild(optionElement)
    })

    const opc = selectElement.options
    for (let i = 0; i < opc.length; i++) {
      if (opc[i].value === genero) {
        opc[i].selected = true
        break
      }
    }
  }

  function actualizarURL() {
    const generoSeleccionado = selectElement.value
    const url = `${window.location.pathname}?genero=${generoSeleccionado}`

    window.location.href = url
  }
  agregarOpciones(opciones, selectElement)

  selectElement.addEventListener('change', actualizarURL)
})
