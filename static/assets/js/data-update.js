loadingIcon = $('#loading-icon');
let updating = false;

$('#data-update').click(function(){
    dataUpdate();
})

function dataUpdate() {
    if (updating) {
        alert('Mise à jour des données en cours !');
        return
    } else {
        console.log('Lancement de la requête de mise à jour ...');
        $.ajax({
            type: "GET",
            url: "/data-update",
            success: callbackFunc,
        });
        updating = true;
        addAnimation();
    }
}

function addAnimation() {
    loadingIcon.addClass('rotating');
}

function callbackFunc(response) {
    removeAnimation();
    console.log(response);
    updating = false;
    // alert(response + '\nLa page va à présent se recharger ...');
    // document.location.reload();
}

function removeAnimation() {
    loadingIcon.removeClass('rotating');
}