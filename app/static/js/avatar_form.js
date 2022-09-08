// preload images
    var doctor_m1 = new Image().src = "../static/img/doctor_m1.gif";
    var doctor_f1 = new Image().src = "../static/img/doctor_f1.gif";

    function setImage(imageSelect) {
        imageIndex = imageSelect.options[imageSelect.selectedIndex].value;
        if (document.images)
            document.images[0].src = eval(imageIndex);
    }
