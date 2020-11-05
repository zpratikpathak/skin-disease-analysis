var feedback = function(res) {
    
    var urladdress="";
    if (res.success === true) {
        var get_link = res.data.link.replace(/^http:\/\//i, 'https://');
        document.querySelector('.status').classList.add('bg-success');
        urladdress=get_link

        document.querySelector('.status').innerHTML =
            'Image : ' + '<br><input class="image-url" value=\"' + get_link + '\"/>' +'<br>' +'<img class="img" height=200px width=200px alt="Imgur-Upload" src="' + get_link + '"/>';
    }

   
};

new Imgur({
    clientid: '90d02ca0020652b', //You can change this ClientID
    callback: feedback
});