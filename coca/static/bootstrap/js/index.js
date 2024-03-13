removeItem = function (idItem) {
    element = $(`#item-${idItem}`)
   element.remove()
   var number = $('#form_appliances').children().length 
   $('#nombre_appareil').val(number)
    
};
function controleFormulaire(i) {
    // var nomAppareil = $(`#appareil-${i}`).val() === undefined ? $('#empty').val() : $(`#appareil-${i}`).val() ;
    if ($(`#appareil-${i}`).val() === undefined ) {
      var  nomAppareil =  $('#empty').val();
    } else {
        var nomAppareil = $(`#appareil-${i}`).val();
    }
    var quantite = $(`#qte-${i}`).val();
    if (nomAppareil.trim() === "" || quantite.trim() === "") {
        alert("Veuillez remplir tous les champs avant d'ajouter .");
        return false;
    }

    return true;
}



$(document).on('click', '#addBill', function () {
    var number = $('#added_appliances').children().length + 1;
    // var number_a = $('#form_appliances').children().length + 1;
    $('#nombre_appareil').val(number);
    
    let itemAdd = `
            <div class="row" id=item-${number}>
                <h5 class="font-size-14 mb-4"><i class="mdi mdi-arrow-right text-primary me-1"></i> Bill ${number} <button onclick="removeItem(${number})" class="btn p-0 row justify-content-end " type="button" id="close-${number}"> <i class="mdi mdi-close-circle text-danger font-size-18  me-2"></i></button></h5>
                <div class="col-md-6">
                    
                
                    


                </div> <!-- end col -->
                <div class="col-md-12">
                    <div class="mb-3">
                        <label class="form-label" for="formrow-password-input">Quantity</label>
                        <input type="number" name="qte-${number}" class="form-control" id="qte-${number}" placeholder="Enter a quantity">
                    </div>
                </div> <!-- end col -->
            </div> <!-- end row -->

    `

    if (controleFormulaire(number - 1)) {
        end = $('#form_appliances').children();
        $('#added_appliances:last').append(end);
        end.remove;
        $('#form_appliances:last').append(itemAdd)
    }    
    
})  ;  