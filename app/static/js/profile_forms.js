function deleteListField (del_btn) {
    console.log(del_btn)
      $(del_btn).closest(".new-input").remove();
    console.log("deleting")
}

function addListField (div_type, div_news, placeholder) {
    $('<div class="new-input">')
        .appendTo(div_news);

    var input = $(div_news).find('div.new-input').last()

    $(div_type)
        .clone().find('input').val('')
        .attr("placeholder", placeholder)
        .end().appendTo(input)
    ;

    $('<img className="img_button" src="../static/img/bin.png" width="20" height="20" onClick="deleteListField(this);"/>\n')
        .insertAfter('div'+div_type+':last');

    $('</div>')
        .appendTo(div_news)
}

function addSpecialism () {
    $('#specialisms').clone().find('input').val('').attr("placeholder", "Add a specialism").end().appendTo('.new_specialisms');
}

function addCertification () {
    $('#certifications').clone().find('input').val('').attr("placeholder", "Add a certification").end().appendTo('.new_certifications');
}

function addTreatment () {
    $('#treatments').clone().find('input').val('').attr("placeholder", "Add a treatment").end().appendTo('.new_treatments');
}

function addInterest () {
    $('#interests').clone().find('input').val('').attr("placeholder", "Add an interest").end().appendTo('.new_interests');
}

function addEducation () {
    $('#education').clone().find('input').val('').attr("placeholder", "Add education").end().appendTo('.new_education');
}
