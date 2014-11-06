
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

function create_circle(map){
    new google.maps.Circle({
    	map: map,
    	center: new google.maps.LatLng('-6.4652023', '-37.0942773'),
    	fillColor: 'red',
    	radius: 500,
    	strokeColor:'transparent',
    });
    
    new google.maps.Circle({
        map: map,
        center: new google.maps.LatLng('-6.462477', '-37.1083922'),
        fillColor: 'blue',
        radius: 400,
        strokeColor:'transparent',
    });
    
    new google.maps.Circle({
        map: map,
        center: new google.maps.LatLng(-6.4673078, -37.0851088),
        fillColor: 'green',
        radius: 300,
        strokeColor:'transparent',
    });
    
    new google.maps.Circle({
        map: map,
        center: new google.maps.LatLng(-6.4621788, -37.0943734),
        fillColor: 'yellow',
        radius: 300,
        strokeColor:'transparent',
    });
}

// Inicialização do mapa
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
    
    create_circle(map);
    
}

// Listener que inicializa o mapa após o carregamento da página
// para evitar erros.
google.maps.event.addDomListener(window, 'load', initialize);
