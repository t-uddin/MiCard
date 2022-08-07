function deleteSpecialism () {
    // $(this).parent('div').remove(); x--;
      $(this).closest('#specialisms').remove();
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
    $('#specialisms').clone().find('input').val('').attr("placeholder", "Add education").end().appendTo('.new_education');
}
