var marcadores1 = []; // Array de marcadores para a primeira seleção
var marcadores2 = []; // Array de marcadores para a segunda seleção
var map = null;      // Mapa
<<<<<<< HEAD
/** Marca um ponto no mapa e adiciona ao array. */
function marcar(map, marcador, array){
=======

/** Marca um ponto no mapa e adiciona ao array.
 * @param marcador Marcador do tipo google.maps.Marker.
 * @param array Vetor que guarda os pontos.*/
function marcar(marcador, array){
>>>>>>> 375e95362439da7dd3983ab57c2e9529d8783279
	array.push(marcador);
	marcador.setMap(map);
}

/** Apaga lista de marcadores. Seta os mapas dos marcadores como null apagando
 * eles do mapa e atriubui [] ao array.
 * @param array Vetor que guarda os pontos. */
function apagar(array){
	for (marcador of array){
		marcador.setMap(null);
	}
	array = [];
}

<<<<<<< HEAD
/** Obtendo pontos do mapa. Após receber os pontos, chama a função plotarPontos */
function getPontosLeft(){
    var requisicao = new XMLHttpRequest(); // Não funciona no IE8 ou mais antigo
    var url = 'json/pontos/';
    var tipo_evento = document.getElementById('left').value;

    url += '?tipo='+tipo_evento
    
    requisicao.open('GET', url, false);
    requisicao.onreadystatechange = function(){
    	plotarPontos(requisicao,"red",marcadores1);
    };
    
    requisicao.send(null);
}

function getPontosRight(){
=======
/** Obtém pontos do mapa. Após receber os pontos, chama a função plotarPontos. */
function getPontos(){
>>>>>>> 375e95362439da7dd3983ab57c2e9529d8783279
    var requisicao = new XMLHttpRequest(); // Não funciona no IE8 ou mais antigo
    var url = 'json/pontos/';
    var tipo_evento = document.getElementById('right').value;

    url += '?tipo='+tipo_evento
    
    requisicao.open('GET', url, false);
    requisicao.onreadystatechange = function(){
    	plotarPontos(requisicao,"green",marcadores2);
    };
    
    requisicao.send(null);
}

<<<<<<< HEAD
/** Plotando pontos no mapa. */
function plotarPontos(requisicao,cor,marcadores){
=======
/** Plota pontos no mapa.
 * @param requisicao A requisição (XMLHttpRequest) enviada ao servidor. Ela deve
 * conter um vetor chamado 'eventos' que contém propriedades lat e lng em cada 
 * elemento. */
function plotarPontos(requisicao){
>>>>>>> 375e95362439da7dd3983ab57c2e9529d8783279
    carregou = requisicao.readyState === 4; // 4 significa que terminou de carregar
    status_ok = requisicao.status === 200;  // 200 significa status OK
    var dados = null;  // Dados da requisição AJAX recebida do servidor
    var pontos = null; // Pontos a serem plotados no mapa
    
    if (carregou && status_ok){
        // Tudo certo. Plotar pontos.
        dados = JSON.parse(requisicao.responseText);
        pontos = dados.eventos;
        //console.log(color) 
        apagar(marcadores);
        icon = "/static/img/"+ cor + ".png";
        for (val of pontos) {
            if (val != null){
                // Marcando ponto
            	var marcador = new google.maps.Marker({
<<<<<<< HEAD
                    position: new google.maps.LatLng(val.lat, val.lng)
                });
                marcador.setIcon(icon);
                marcar(map, marcador, marcadores);
=======
                    position: new google.maps.LatLng(val.lat, val.lng)}); 
                marcar(marcador, marcadores);
>>>>>>> 375e95362439da7dd3983ab57c2e9529d8783279
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
