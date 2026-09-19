

  $(document).ready(

    function(){

      oParametros = $.JSON.decode('{"dtDataImportacao":"2026-09-19","page":0,"rows":10,"sidx":"descricao","sord":"asc","aHistorico":[],"iNivel":1}');

      jQuery("#list").jqGrid({
        url: '/ordem_cronologica/getInstit',
        datatype: "json",
        mtype: "POST",
        postData:{aParametros:$.JSON.encode(oParametros)},
        colNames:['Instituição','iInstituicao'],
        colModel:[
          {name:'descricao'    ,index:'descricao'   , width:'50', align:'left'},
          {name:'iInstituicao' ,index:'iInstituicao', hidden: true}
        ],
        altRows:   true,
        autowidth: true,
        pager:     '#jqGridPager',
        sortname:  'descricao',
        sortorder: 'desc',
        height:    '150px',
        onCellSelect: function (id) {

          var oDados = jQuery("#list").jqGrid('getRowData',id);
          oParametros.aHistorico.push(oDados)
          oParametros.iInstituicao = id;
          oParametros.iNivel++;

          $.ajax({
            async:true,
            type:'post',
            dataType: 'json',
            data: oParametros,
            beforeSend:function(request) {
              $('#ajax-loader').show();
            },
            complete:  function(request, json) {
              $('#main_content').html(request.responseText);
              $('#ajax-loader').hide();
            },
            url:'/ordem_cronologica/loadLink/1'
          })
        }
      });
    }
  );
