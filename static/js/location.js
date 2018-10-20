//GPS取得
var num = 0;
var watch_id;

//開いてから位置情報を得るたびにこれが動く
window.onload = function(){
    watch_id = navigator.geolocation.watchPosition(test2, function(e) { alert(e.message); }, {"enableHighAccuracy": true, "timeout": 50000, "maximumAge": 5000});
}

//画面に表示させてるだけ
function test2(position) {

    var geo_text = "緯度:" + position.coords.latitude + "\n";
    geo_text += "経度:" + position.coords.longitude + "\n";
    geo_text += "高度:" + position.coords.altitude + "\n";
    var date = new Date(position.timestamp);
    geo_text += "取得時刻:" + date + "\n";

    document.getElementById('position_view').innerHTML = geo_text;

}

//サーバーと非同期通信データ受け取り
var xhr= new XMLHttpRequest();
xhr.open("GET","/index.html",true);
xhr.send();

//データ送る
xhr.open('POST', '/index.html',true);
xhr.setRequestHeader('content-type', 'application/x-www-form-urlencoded;charset=UTF-8');
xhr.send( 'latitude=position.coords.latitude&longitude=position.coords.longitude&altitude=position.coords.altitude&date=date' );
