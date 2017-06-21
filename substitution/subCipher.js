Cipher.toQWERTY = function(text, decode) {
    // ABCDEF to QWERTY map
    var map = {
        a: 'q', b: 'w', c: 'e',
        d: 'r', e: 't', f: 'y',
        g: 'u', h: 'i', i: 'o',
        j: 'p', k: 'a', l: 's',
        m: 'd', n: 'f', o: 'g',
        p: 'h', q: 'j', r: 'k',
        s: 'l', t: 'z', u: 'x',
        v: 'c', w: 'v', x: 'b',
        y: 'n', z: 'm'
    };

    // Flip the map
    if(decode) {
        map = (function() {
            var tmp = {};
            var k;

            // Populate the tmp variable
            for(k in map) {
                if(!map.hasOwnProperty(k)) continue;
                tmp[map[k]] = k;
            }

            return tmp;
        })();
    }

    return text.split('').filter(function(v) {
        // Filter out characters that are not in our list
        return map.hasOwnProperty(v.toLowerCase());
    }).map(function(v) {
        // Replace old character by new one
        // And make it uppercase to make it look fancier
        return map[v.toLowerCase()].toUpperCase();
    }).join('');
};

var text = 'Hello World!';
var encoded = Cipher.toQWERTY(text); // ITSSGVGKSR
var decoded = Cipher.toQWERTY(decoded, true); // HELLOWORLD

function encrypt() {
  var textArray = $('textarea').val().split("");
  $('div#resultContainer').show();
  registerChangeHandlers();
}

function init() {
  $('input#encrypt').click(encrypt);
  $('div#resultContainer').width($('div#input textarea').width());
}

$(document).ready(function() {
  init();
});
