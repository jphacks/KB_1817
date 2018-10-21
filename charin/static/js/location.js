//GPS取得
var num = 0;
var watch_id;
var near_users;
var now_credit;
//開いてから位置情報を得るたびにこれが動く

function geolocation() {
    watch_id = navigator.geolocation.watchPosition(locate, function(e) { alert(e.message); }, {"enableHighAccuracy": true, "timeout": 5000000, "maximumAge": 100000});
};

function locate(position) {
    var date = new Date(position.timestamp);
    console.log("locate動いた")
    //サーバーと非同期通信データ受け取り
    var xhr_get= new XMLHttpRequest();
    xhr_get.onreadystatechange = function() {
        if (xhr_get.readyState === 4) {
            near_users = xhr_get.response;
            console.log(typeof near_users);
        }
      }
    xhr_get.open('GET','/get_users_location',true);
    xhr_get.responseType = 'json'
    xhr_get.send(null);

    //データ送る
    var xhr_post = new XMLHttpRequest();
    xhr_post.onreadystatechange = function() {
        if (xhr_post.readyState === 4) {
            var credit = parseInt(xhr_post.response);
            now_credit = parseInt(document.getElementsByName("credit")[0].value);
            console.log(credit, now_credit)
            if (now_credit < credit ) {
                alert("あなたに誰かがCharinしました！");
                now_credit = credit;
                document.getElementById("cre").innerHTML=`現在のポイントは　　　${ credit }pt`;

            }
        }
      }
    xhr_post.open('POST','/locate_user',true);
    xhr_post.setRequestHeader('content-type', 'application/x-www-form-urlencoded;charset=UTF-8');
    var latitude = position.coords.latitude;
    var longitude = position.coords.longitude;
    xhr_post.send(`latitude=${position.coords.latitude}&longitude=${position.coords.longitude}&date=${date}`);
}

function give() {
    var xhr_post = new XMLHttpRequest();
    xhr_post.open('POST','/give',true);
    xhr_post.setRequestHeader( 'Content-Type', 'application/json');
    xhr_post.send(JSON.stringify(near_users));
}

var map;
var marker;
function initMap() {
navigator.geolocation.getCurrentPosition(function(position){
  map = new google.maps.Map(document.getElementById('map'), {
  center: {lat: position.coords.latitude, lng: position.coords.longitude},
  zoom: 17
});
  marker = new google.maps.Marker({ // マーカーの追加
  position: {lat: position.coords.latitude, lng: position.coords.longitude}, // マーカーを立てる位置を指定
map: map // マーカーを立てる地図を指定
});
//こっから近くの人のマーカー
for(var i =0; i <near_users["near_users"].length; i++){
    var user_dict = near_users["near_users"][i];
    for ( var key in user_dict){
    marker = new google.maps.Marker({ // マーカーの追加
      position: {lat: user_dict[key][0], lng: user_dict[key][1]}, // マーカーを立てる位置を指定
    map: map // マーカーを立てる地図を指定
    });
}
}
});
}

setInterval(geolocation(), 50000);
