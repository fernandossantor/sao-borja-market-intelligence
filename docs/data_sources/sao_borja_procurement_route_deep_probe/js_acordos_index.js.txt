;(function($) {

  $(function($) {
    var sBaseUrl = $('#base').attr('href');

    $(document).ajaxSend(function() {
      $('#ajax-loader').show()
    })

    $(document).ajaxStop(function() {
      $('#ajax-loader').hide()
    })

    $('#FiltroIndexForm').live('submit', function() {
      var lPass = true;

      // Verifica se os campos obrigatÃ³rios foram preenchidos
      $('select.required').each(function() {

        if (this.value == '') {

          alert("Campo " + $(this).parent().find('label').text() + " Ã© de preenchimento obrigatÃ³rio.");

          lPass = false;
          return false;
        }
      })

      return lPass;
    })

    $('#FiltroInstituicao').live('change', function() {
      var oExercicio = $('#FiltroExercicio');

      $.getJSON( sBaseUrl + '/acordos/buscarExercicios/' + this.value, function(data) {

        if (!Object.keys(data).length) {
          alert('Nenhum exercÃ­cio encontrado para a instituiÃ§Ã£o selecionada.')
          return false
        }

        oExercicio.find('option:not(:first)').remove()
        data = Object.keys(data).reverse();

        $.each(data, function(i, sLabel) {
          oExercicio.append('<option value="' + sLabel + '">' + sLabel + '</option>')
        })
      })
    })

  });
})(jQuery);