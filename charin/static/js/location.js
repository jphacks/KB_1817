//GPS取得
var num = 0;
var watch_id;

//開いてから位置情報を得るたびにこれが動く

function geolocation() {
    watch_id = navigator.geolocation.watchPosition(locate, function(e) { alert(e.message); }, {"enableHighAccuracy": true, "timeout": 50000, "maximumAge": 100000});
};

function locate(position) {
    var date = new Date(position.timestamp);
    console.log("locate動いた")
    //サーバーと非同期通信データ受け取り
    var xhr_get= new XMLHttpRequest();
    xhr_get.open('GET','/get_users_location',true);
    xhr_get.send(null);

    //データ送る
    var xhr_post = new XMLHttpRequest();
    xhr_post.open('POST','/locate_user',true);
    xhr_post.setRequestHeader('content-type', 'application/x-www-form-urlencoded;charset=UTF-8');
    var latitude = position.coords.latitude;
    var longitude = position.coords.longitude;
    xhr_post.send(`latitude=${position.coords.latitude}&longitude=${position.coords.longitude}&date=${date}`);
}

setInterval(geolocation(), 5000);
