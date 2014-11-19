var marcadores = []; // Array de marcadores
var map = null; // Mapa

/** Marca um ponto no mapa e adiciona ao array. */
function marcar(map, marcador, array){
	array.push(marcador);
	marcador.setMap(map);
}

/** Apaga lista de marcadores. */
function apagar(marcadores){
	for (marcador of marcadores){
		marcador.setMap(null);
	}
	marcadores = [];
}

/** Obtendo pontos do mapa. Após receber os pontos, chama a função plotarPontos */
function getPontos(){
    var requisicao = new XMLHttpRequest(); // Não funciona no IE8 ou mais antigo
    var url = 'json/pontos/';
    var tipo_evento = document.getElementById('id_select_tipo').value;

    url += '?tipo='+tipo_evento
    
    requisicao.open('GET', url, false);
    requisicao.onreadystatechange = function(){
    	plotarPontos(requisicao);
    };
    
    requisicao.send(null);
}

/** Plotando pontos no mapa. */
function plotarPontos(requisicao){
    carregou = requisicao.readyState === 4; // 4 significa que terminou de carregar
    status_ok = requisicao.status === 200;  // 200 significa status OK
    var dados = null;  // Dados da requisição AJAX recebida do servidor
    var pontos = null; // Pontos a serem plotados no mapa
    
    if (carregou && status_ok){
        // Tudo certo. Plotar pontos.
        dados = JSON.parse(requisicao.responseText);
        pontos = dados.eventos;
        
        apagar(marcadores);
        
        for (val of pontos) {
            if (val != null){
                // Marcando ponto
            	var marcador = new google.maps.Marker({
                    position: new google.maps.LatLng(val.lat, val.lng)}); 
                marcar(map, marcador, marcadores);
            }
        }
    } else {
    	// Erro! fazer alguma coisa
        alert("Erro no carregamento da página.");
    }
}

/** Inicialização do mapa. */
function initialize() {
    // inicializando o mapa
    map = new google.maps.Map(document.getElementById('map-canvas'),
                              {
                                  zoom: 15,
                                  center: new google.maps.LatLng(-6.467149,-37.084322),
                                  panControl: false,
                                  zoomControl: false,
                                  scaleControl: true,
                              });
    getPontos();
}

// Listener que inicializa o mapa após o carregamento da página
// para evitar erros.
google.maps.event.addDomListener(window, 'load', initialize);
