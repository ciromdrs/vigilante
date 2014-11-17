
// Função de marcação de pontos 
// Possivelmente generalizar para markar N pontos em uma única chamada
function mark(ponto, map){
    if (ponto != null){
        var latitude = ponto.value.split(',')[0];
        var longitude = ponto.value.split(',')[1];
        
        // Marcando ponto
        new google.maps.Marker({
            map:      map,
            position: new google.maps.LatLng(latitude, longitude),
        });
    }
}

/** Obtendo pontos do mapa. Após receber os pontos, chama a função plotarPontos */
function getPontos(map){
	//alert('getPontos');
    var requisicao = new XMLHttpRequest(); // Não funciona no IE8 ou mais antigo
    requisicao.open('GET', 'json/pontos', false);
    requisicao.onreadystatechange = function(){
    	plotarPontos(map, requisicao);
    };
    requisicao.send(null);
}

/** Plotando pontos no mapa. */
function plotarPontos(map, requisicao){
    carregou = requisicao.readyState === 4; // 4 significa que terminou de carregar
    status_ok = requisicao.status === 200;  // 200 significa status OK
    var dados = null;  // Dados da requisição AJAX recebida do servidor
    var pontos = null; // Pontos a serem plotados no mapa
    
    if (carregou && status_ok){
        // Tudo certo. Plotar pontos.
        dados = JSON.parse(requisicao.responseText);
        pontos = dados.eventos;

        for (val of pontos) {
            if (val != null){
                // Marcando ponto
                new google.maps.Marker({
                    map:      map,
                    position: new google.maps.LatLng(val.lat, val.lng),
                });
            };
        }
    } else {
    	// Erro! fazer alguma coisa
        alert("Erro no carregamento da página.");
    }
}

/** Inicialização do mapa. */
function initialize() {
    var mapOptions = {
        zoom: 15,
        center: new google.maps.LatLng(-6.467149,-37.084322),
        panControl: false,
        zoomControl: false,
        scaleControl: true,
    };
    
    // Declarando a variável do mapa
    var map = new google.maps.Map(document.getElementById('map-canvas'),
                                  mapOptions);
    
    // Marcando ponto, caso seja diferente de null
    var ponto = document.getElementById('ponto');
    mark(ponto,map);
    
    getPontos(map);
}

// Listener que inicializa o mapa após o carregamento da página
// para evitar erros.
google.maps.event.addDomListener(window, 'load', initialize);
