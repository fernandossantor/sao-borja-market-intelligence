

  var oParametros;
  oParametros = $.JSON.decode('{"iIdLink":"1"}');
  ajax1 = false;
  ajax2 = false;

  $(document).ready(
    function(){
      $.ajax({
        type: "POST",
        evalScripts: true,
        url:'/ordem_cronologica/getExercicio/',
        data:{aParametros:$.JSON.encode(oParametros)},
        success: function (data){
          dados =  JSON.parse(data);
          $.each(dados.Exercicio, function (i, item) {
            $('#FiltroAno').append($('<option>', {
              value: item,
              text : item
            }));
          });
          ajax1 = true;
          VerificaAjax();
        },
        error: function(xhr, desc, err){
          console.log('Erro!!!');
        }
      });

      $.ajax({
        type: "POST",
        evalScripts: true,
        url:'/ordem_cronologica/getLista/',
        data:{aParametros:$.JSON.encode(oParametros)},
        success: function (data){
          dados =  JSON.parse(data);
          $.each(dados.ListaCredores, function (i, item) {
            $('#FiltroLista').append($('<option>', {
              value: item.codigo,
              text : item.descricao
            }));
          });

          ajax2 = true;
          VerificaAjax();
        },
        error: function(xhr, desc, err){
          console.log('Erro!!!');
        }
      });

    }
  );

  function ajaxForm(){

    oParametros.iExercicio = $('#FiltroAno').val();
    oParametros.iPago      = $('#FiltroPago').val();
    oParametros.iTipoLista = $('#FiltroLista').val();
    sTitulo                = $('#FiltroLista option:selected').text()

    var oValida = true;

    if($('#periodoInicio').val() != ''){

      if($('#periodoInicio').val() != '') {

        oValida = ComparaData('periodoInicio','periodoFim');
      } else {

        alert('Periodo final não preenchido');
      }
    } else {

      if($('#periodoInicio').val() != '') {

        alert('Periodo inicial não preenchido');
      }
    }

    if(oValida){

      if(ComparaDiaMes($('#periodoInicio').val(),$('#periodoFim').val())){

        oParametros.dtInicio         = oValida.inicio;
        oParametros.dtFim            = oValida.fim;

        $("#resultadotabela").empty();

        if(oParametros.iTipoLista){

          CriaTabela(oParametros, sTitulo);
        } else {
           $.each($('#FiltroLista option'), function (i, item) {

            if($(this).val()){
              sTitulo = $(this).text();
              oParametros.iTipoLista = $(this).val();

              CriaTabela(oParametros, sTitulo);
            }
          });
        }

      } else {

        alert('Periodo Inicial superior ao Periodo Final.')
      }
    }
  }

  function CriaTabela(oParametros, sTitulo){

    if($('#gbox_list_'+oParametros.iTipoLista)){

      $('#gbox_list_'+oParametros.iTipoLista).next('br').remove();
      $('#gbox_list_'+oParametros.iTipoLista).remove();
    }

    $("#resultadotabela").append('<table id="list_'+oParametros.iTipoLista+'" class="list"></table><div id="pager_'+oParametros.iTipoLista+'"></div><br>');


    jQuery(".list").jqGrid({
      url: '/ordem_cronologica/getElementos',
      datatype: "json",
      mtype: "POST",
      postData:{
        aParametros:$.JSON.encode(oParametros)
      },
      colNames:[
        'Código',
        'Nº O.P.',
        'Recebimento',
        'Vencimento',
        'Pagamento',
        'CPF/CNPJ',
        'Credor',
        'Descrição',
        'Número Contrato',
        'Documento Fiscal',
        'Valor',
        'Situação',
        'exercicio',
        'id'
      ],
      colModel:[
        {name:'codigo'          ,index:'codigo'          ,align:'center' ,width:'100px'},
        {name:'operacao'        ,index:'op'              ,align:'center' ,width:'100px'},
        {name:'emissao'         ,index:'emissao'         ,align:'center' ,width:'80px' ,formatter:'date', search:false},
        {name:'vencimento'      ,index:'vencimento'      ,align:'center' ,width:'70px' ,formatter:'date', search:false},
        {name:'pagamento'       ,index:'pagamento'       ,align:'center' ,width:'70px' ,formatter:'date', search:false},
        {name:'cpfcnpj'         ,index:'cpfcnpj'         ,align:'right'  ,width:'120px',formatter:formatarCpfCnpj, search:false},
        {name:'credor'          ,index:'credor'          ,width:'300px'  ,align:'left'},
        {name:'descricao'       ,index:'descricao'       ,width:'300px'  ,align:'right', search:false},
        {name:'nprocesso'       ,index:'nprocesso'       ,width:'100px'  ,align:'right', search:false},
        {name:'ndocumento'      ,index:'ndocumento'      ,width:'100px'  ,align:'center',search:false},
        {name:'valor'           ,index:'valor'           ,width:'80px'   ,align:'right', search:false, formatter:'currency'},
        {name:'situacao'        ,index:'situacao'        ,width:'50px'  ,align:'right', search:false},
        {name:'exercicio'       ,index:'exercicio'       ,hidden:true},
        {name:'id'              ,index:'id'              ,hidden:true},
      ],
      rowNum:      10,
      rowList:     [10,20,30],
      pager:       '#pager_'+oParametros.iTipoLista,
      autowidth:   true,
      shrinkToFit: false,
      sortname:    'vencimento',
      viewrecords: true,
      hiddengrid:  true,
      sortorder:   "asc",
      height:      '240px',

      altRows:     true,
      onCellSelect: function (id) {

        var oDados            = jQuery(this).jqGrid('getRowData',id);
        console.log(oParametros);
        window.open('/despesas/consultas?tipo=empenho&id='+oDados.id+'&ano='+oDados.exercicio,'_blank');
      },

      loadComplete: function (data) {

        if (data.rows) {

          subGridData = data.rows; // save original JSON data
        }
        if(subGridData){

          for (var i = subGridData.length - 1; i >= 0; i--) {

            if(subGridData[i].justificativa){

            } else {

              $('#'+i).children("td.sgcollapsed").unbind().html("").removeClass("ui-sgcollapsed sgcollapsed");
            }
          };
        }
      },
      caption: 'Resultados da Consulta de ' + sTitulo,
      subGrid: true,
      subGridOptions: {
        'expandOnLoad'  : false,
        "plusicon"      : "ui-icon-triangle-1-e",
        "minusicon"     : "ui-icon-triangle-1-s",
        "openicon"      : "ui-icon-arrowreturn-1-e",
        "reloadOnExpand": true,
        "selectOnExpand": true
      },
      subGridRowExpanded: function (grid_id, row_id) {
          var justificativa = ''
        var subgrid_table_id, pager_id;
        subgrid_table_id = grid_id + "_tone";
        pager_id = "pone_" + subgrid_table_id;
        $("#" + grid_id).html("<table id='" + subgrid_table_id + "' class='scroll' style='width:100%'></table><div id='" + pager_id + "' class='scroll'></div>");
        $("#" + subgrid_table_id).jqGrid({
          datatype: 'local',
          data: subGridData[row_id].justificativa,
          colNames: ['Justificativa'],
          colModel: [
            { name: 'justificativa', width:'671px'}
          ],
          height:'auto',
          sortname: 'data',
          viewrecords: true,
          sortorder: "asc"
        });
      }
    });
    jQuery("#list_" + oParametros.iTipoLista).jqGrid('filterToolbar',{stringResult: true,searchOnEnter : false});
  }

  function formatarCpfCnpj(sCellValue, sOptions, oRowObject) {

    var sCpfCnpj = new String(sCellValue);

    var vrc = new String(sCpfCnpj);
        vrc = vrc.replace(".", "");
        vrc = vrc.replace(".", "");
        vrc = vrc.replace("/", "");
        vrc = vrc.replace("-", "");

    var tamString = vrc.length;
    var nCpfCnpj  = new Number(vrc);

    if (!isNaN(nCpfCnpj)) {

      if (tamString == 11 ){

        var vr = new String(sCpfCnpj);
            vr = vr.replace(".", "");
            vr = vr.replace(".", "");
            vr = vr.replace("-", "");

        var iTam = vr.length;

        if (iTam > 3 && iTam < 7)
           sCpfCnpj = vr.substr(0, 3) + '.' +
                      vr.substr(3, iTam);
        if (iTam >= 7 && iTam <10)
           sCpfCnpj = vr.substr(0,3) + '.' +
                      vr.substr(3,3) + '.' +
                      vr.substr(6,iTam-6);
        if (iTam >= 10 && iTam < 12)
           sCpfCnpj = vr.substr(0,3) + '.' +
                      vr.substr(3,3) + '.' +
                      vr.substr(6,3) + '-' +
                      vr.substr(9,iTam-9);

      } else if (tamString > 11){

        var vr = new String(sCpfCnpj);
            vr = vr.replace(".", "");
            vr = vr.replace(".", "");
            vr = vr.replace("/", "");
            vr = vr.replace("-", "");

        var iTam = vr.length;
            sCpfCnpj = vr.substr(0,2) + '.' +
                       vr.substr(2,3) + '.' +
                       vr.substr(5,3) + '/' +
                       vr.substr(8,4)+ '-' +
                       vr.substr(12,iTam-12);

      }
    }

    return sCpfCnpj;
  }

  function imprime(tipo){


    var estilo  = [];
    var tabelas = [];
    // Pega todas as Grids
    $("[id^=list_").each(function (i){

      // Pega o ID da grid Atual
      var value = $(this).attr('id');

      // Filtra apenas a Grid Principal
      // ... o jqGrid cria ids das colunas utilizando o id da grid
      if(value.length == 6){

        // insere configuracoes da respectiva grid
        $.each($('#FiltroLista option'), function (i, item) {

          if($(this).val() == value.substring(5,6)){

            tabelas.push({
              'lista'  : $(this).val(),
              'tipo'   : 'lista',
              'titulo' : $(this).text(),
              'sort'   : $('#'+value).jqGrid('getGridParam','sortname'),
              'filters': $('#'+value).getGridParam("postData").filters,
              'order'  : $('#'+value).jqGrid('getGridParam','sortorder')
            });
          }
        });

        sTemp = $('#FiltroLista option:selected').text();

        sTitulo = 'Resultados para a consulta ';

        if(sTemp == 'Todas'){

          sTitulo += 'de Todas Listas de Credores';
        } else {

          sTitulo += 'da Lista de Credores: ' + sTemp + ' ';
        }

      }
    });

    var url    = '/ordem_cronologica/getRelatorio';
    var dados  = {
      aParametros : $.JSON.encode(oParametros),
      'tipo'      : tipo,
      'consultas' : tabelas,
      'cabecalho' : [
        {
          'tipo'    : 'h2',
          'conteudo': sTitulo
        }
      ],
      'tabelas'   : [
        {
          'titulo':'',
          'colunas' :[
            {
              'titulo' : 'Código',
              'tipo'   : 'centro',
              'size'   : 15
            },
            {
              'titulo' : 'Nº O.P.',
              'tipo'   : 'centro',
              'size'   : 11
            },
            {
              'titulo' : 'Recebimento',
              'tipo'   : 'data',
              'size'   : 19
            },
            {
              'titulo' : 'Vencimento',
              'tipo'   : 'data',
              'size'   : 18
            },
            {
              'titulo' : 'Pagamento',
              'tipo'   : 'data',
              'size'   : 18
            },
            {
              'titulo' : 'CPF/CNPJ',
              'tipo'   : 'cpfcnpj',
              'size'   : 23
            },
            {
              'titulo' : 'Credor',
              'tipo'   : 'esquerda',
              'size'   : 35
            },
            {
              'titulo' : 'Descrição',
              'tipo'   : 'justificado',
              'size'   : 55
            },
            {
              'titulo' : 'Nº Contrato',
              'tipo'   : 'centro',
              'size'   : 18
            },
            {
              'titulo' : 'Doc. Fiscal',
              'tipo'   : 'centro',
              'size'   : 18
            },
            {
              'titulo' : 'Valor',
              'tipo'   : 'moeda',
              'size'   : 20
            },
            {
              'titulo' : 'Situação',
              'tipo'   : 'centro',
              'size'   : 20
            },
            {
              'titulo' : 'id',
              'tipo'   : 'hidden'
            },
            {
              'titulo' : 'exercicio',
              'tipo'   : 'hidden'
            },
            {
              'titulo' : '',
              'tipo'   : 'subtabela',
              'size'   : 270,
              'colunas':[
                {
                  'titulo' : 'Descrição',
                  'tipo'   : 'justificado',
                  'id'     : 'justificativa'
                }
              ]
            }
          ]
        }
      ]
    };
    arquivos(url, dados);
  }

  // Função responsavel pela sincronia das chamadas
  function VerificaAjax(){

    if(ajax1 && ajax2){

      if(typeof oParametros.id_lista !== 'undefined'){

        $('#FiltroAno').val(Number(oParametros.iExercicio));
        $('#FiltroLista').val(Number(oParametros.id_lista));
        ajaxForm();
        var defFilter = '{"groupOp":"AND","rules":[{"field":"'+oParametros.campo+'","op":"gt","data":"'+oParametros.valor+'"}]}'
        $('#list_'+oParametros.id_lista).jqGrid("getGridParam", "postData").filters = defFilter;
      }
    }
  }
