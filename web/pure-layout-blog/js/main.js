$(function() {
    var players = loadJsonFromServer('../playerlist.json');
    console.log('s');
    for(var i=0; i<players.length; i++) {
        var platform = players[i]["platform"];
        // if (platform != "douyu") continue;
        var game = players[i]["game"];
        var link = players[i]["link"];
        var player_name = players[i]["playerName"];
        var player_title = players[i]["playerTitle"];
        var player_thumb = players[i]["playerThumb"];

        var $target = $('.' + game)
                        .find('.game-platform.' + platform)
                        .find('ul');

        var $grid = $('<li class="player"><div></div></li>');
        $('<a></a>').attr('href', link)
            .append($('<img class="thumb"/>'))
            .find('img')
            .attr('src', player_thumb)
            .attr('href', link)
            .parent()
            .appendTo($grid.find('div'));
        $('<div></div>').append('<div class="title">'+ player_title +'</div>')
            .append('<div class="playername">'+ player_name +'</div>')
            .appendTo($grid.find('div'));

        $grid.appendTo($target);
    }
});

function loadJsonFromServer(path) {
    htmlobj = $.ajax({
        url: path,
        async: false
    });
    lines = htmlobj.responseText.split('\n');
    for (var i=0; i<lines.length; i++) {
        lines[i] = strToJson(lines[i]);
    }
    return lines.slice(0, -1);
}

function strToJson(str){ 
    return (new Function("return " + str))(); 
}