<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd"><html xmlns="http://www.w3.org/1999/xhtml">
<head>
  <link href="" id="base"><link rel="stylesheet" type="text/css" href="/css/style.min.css" /><link rel="stylesheet" type="text/css" href="/css/jquery-ui.css" /><link rel="stylesheet" type="text/css" href="/css/ui.jqgrid.css" /><script type="text/javascript" src="/js/jquery.js"></script><script type="text/javascript" src="/js/jquery.json.js"></script><script type="text/javascript" src="/js/grid.locale-pt-br.js"></script><script type="text/javascript" src="/js/jqGrid.js"></script><script type="text/javascript" src="/js/arquivos.js"></script><script type="text/javascript" src="/js/consulta.js"></script>  <title>Portal da Transpar&ecirc;ncia</title>

  <script type="text/javascript">
    $(document).ready(function(){

      $("#cororiginalid").attr('checked',true);

      $("#acessibilidademin").click(function(){
        if($(this).css('margin-left') == '0px'){

          $(this).animate({"margin-left": "-500px"}, 500);
          $("#acessibilidademax").animate({"margin-left": "0px"}, 500);
        }else{

          $(this).animate({"margin-left": "0px"}, 500);
          $("#acessibilidademax").animate({"margin-left": "-500px"}, 500);
        }

      });

      $("#fecharacessibilidade").click(function(){
        $("#acessibilidademin").animate({"margin-left": "0px"}, 500);
        $("#acessibilidademax").animate({"margin-left": "-500px"}, 500);
      });

      $('#fechaacessibilidadex').click(function(){
        $("#acessibilidademin").animate({"margin-left": "0px"}, 500);
        $("#acessibilidademax").animate({"margin-left": "-500px"}, 500);
      });

      $("#irparabusca").click(function(){
        $("#search").focus();
      });

      $("#aumentarfonte").click(function(){
        var fonteatual = $('#main_content').css('font-size').replace('px','');
        var numerico = new Number(fonteatual);
        numerico = parseInt(numerico);

        if(numerico < 17){
          numerico += 1;
          $('#main_content').css('font-size',numerico+'px');
        }



      });

      $("#diminuirfonte").click(function(){
        var fonteatual = $('#main_content').css('font-size').replace('px','');
        var numerico = new Number(fonteatual);
        numerico = parseInt(numerico);

        if(numerico > 7){
          numerico -= 1;
          $('#main_content').css('font-size',numerico+'px');
        }

      });

      $("#fontepadrao").click(function(){
        $('#main_content').css('font-size','11px');
      });

      $("#cororiginalid").click(function(){
        $('#general_content').css('background','none repeat scroll 0 0 #fff');
        $('#buscar h3').css('background-color','#eee');
        $('#navbar ul li a').css('color','#000');
        $('#content').css('background','none repeat scroll 0 0 #ededed');
        $('#consulta_dados fieldset').css('background-color','#fff');
        $('#consulta_dados fieldset').css('color','#333');
        $('table tbody tr td').css('background','none repeat scroll 0 0 #fff');
        $('table tbody tr td').css('color','#000');
        $('table tbody tr th').css('background','none repeat scroll 0 0 #fff');
        $('table tbody tr th').css('color','#000');
        $('.ui-jqgrid-bdiv').css('background-color','#fff');
        $('#breadcrumb').css('color','#333');
        $('#main_content').css('color','#333');
        $('#main_footer').css('background-color','#ededed');
        $('#consulta_dados fieldset legend').css('color','#000');
        $('html').css('background-color','#ededed');
        $('#footer').css('color','#888');
        $('#footer a').css('color','#888');

        $("#acessibilidademin img").attr('src','img/acessibilidade.jpg');
        $("#acessibilidademin").css('color','rgb(16, 78, 139)');

        $("#teclasatalho").css('background-color','#e6efff');
        $("#teclasatalho").css('color','#000');
        $("#letraatalho").css('background-color','#e6efff');
        $("#letraatalho").css('color','#000');

        $("#numero1 div").css('background-color','rgb(230, 239, 255)');
        $("#numero1 div center strong").css('color','#6d6b6b');
        $("#numero1 #irparabusca").css('background-color','#fff');
        $("#numero1 #irparabusca a").css('color','#345076');

        $("#numero2 div").css('background-color','rgb(230, 239, 255)');
        $("#numero2 div center strong").css('color','#6d6b6b');
        $("#numero2 #irparadespesas").css('background-color','#fff');
        $("#numero2 #irparadespesas a").css('color','#345076');

        $("#numero3 div").css('background-color','rgb(230, 239, 255)');
        $("#numero3 div center strong").css('color','#6d6b6b');
        $("#numero3 #irparareceitas").css('background-color','#fff');
        $("#numero3 #irparareceitas a").css('color','#345076');

        $("#numero4 div").css('background-color','rgb(230, 239, 255)');
        $("#numero4 div center strong").css('color','#6d6b6b');
        $("#numero4 #irparadiarias").css('background-color','#fff');
        $("#numero4 #irparadiarias a").css('color','#345076');

        $("#numero5 div").css('background-color','rgb(230, 239, 255)');
        $("#numero5 div center strong").css('color','#6d6b6b');
        $("#numero5 #irparafolhapagamento").css('background-color','#fff');
        $("#numero5 #irparafolhapagamento a").css('color','#345076');

        $("#numero6 div").css('background-color','rgb(230, 239, 255)');
        $("#numero6 div center strong").css('color','#6d6b6b');
        $("#numero6 #irparacontratos").css('background-color','#fff');
        $("#numero6 #irparacontratos a").css('color','#345076');

        $("#numero7 div").css('background-color','rgb(230, 239, 255)');
        $("#numero7 div center strong").css('color','#6d6b6b');
        $("#numero7 #irparalicitacoes").css('background-color','#fff');
        $("#numero7 #irparalicitacoes a").css('color','#345076');

        $("#numero8 div").css('background-color','rgb(230, 239, 255)');
        $("#numero8 div center strong").css('color','#6d6b6b');
        $("#numero8 #cororiginal").css('background-color','#fff');

        $("#numero9 div").css('background-color','rgb(230, 239, 255)');
        $("#numero9 div center strong").css('color','#6d6b6b');
        $("#numero9 #comcontraste").css('background-color','#fff');

      });

      $("#comcontrasteid").click(function(){
        $('#general_content').css('background','none repeat scroll 0 0 #000');
        $('#buscar h3').css('background-color','#000');
        $('#navbar ul li a').css('color','#fff');
        $('#content').css('background','none repeat scroll 0 0 #000');
        $('#consulta_dados fieldset').css('background-color','#000');
        $('#consulta_dados fieldset').css('color','#fff');
        $('table tbody tr td').css('background','none repeat scroll 0 0 #000');
        $('table tbody tr td').css('color','#fff');
        $('table tbody tr th').css('background','none repeat scroll 0 0 #000');
        $('table tbody tr th').css('color','#fff');
        $('.ui-jqgrid-bdiv').css('background-color','#000');
        $('#breadcrumb').css('color','#fff');
        $('#main_content').css('color','#fff');
        $('#main_footer').css('background-color','#000');
        $('#consulta_dados fieldset legend').css('color','#000');
        $('html').css('background-color','#000');
        $('#footer').css('color','#fff');
        $('#footer a').css('color','#fff');
        $("#buscar h3").css('background-color','#000');
        $("#list tbody tr td").css('background-color','#000');
        $("#list tbody tr td").css('color','#fff');
        $("#historico_valores tbody tr td").css('background-color','#000');
        $("#historico_valores tbody tr td").css('color','#fff');
        $(".item-page h4").css('color','#fff');
        $(".item-page p").css('color','#fff');

        $("#acessibilidademin img").attr('src','/img/wheelchair.png');
        $("#acessibilidademin img").css('background-color','#fff');
        $("#acessibilidademin").css('color','#fff');

        $("#teclasatalho").css('background-color','#363636');
        $("#teclasatalho").css('color','#fff');
        $("#letraatalho").css('background-color','#363636');
        $("#letraatalho").css('color','#fff');

        $("#numero1 div").css('background-color','#000');
        $("#numero1 div center strong").css('color','#fff');
        $("#numero1 #irparabusca").css('background-color','#fff');
        $("#numero1 #irparabusca a").css('color','#000');

        $("#numero2 div").css('background-color','#000');
        $("#numero2 div center strong").css('color','#fff');
        $("#numero2 #irparadespesas").css('background-color','#fff');
        $("#numero2 #irparadespesas a").css('color','#000');

        $("#numero3 div").css('background-color','#000');
        $("#numero3 div center strong").css('color','#fff');
        $("#numero3 #irparareceitas").css('background-color','#fff');
        $("#numero3 #irparareceitas a").css('color','#000');

        $("#numero4 div").css('background-color','#000');
        $("#numero4 div center strong").css('color','#fff');
        $("#numero4 #irparadiarias").css('background-color','#fff');
        $("#numero4 #irparadiarias a").css('color','#000');

        $("#numero5 div").css('background-color','#000');
        $("#numero5 div center strong").css('color','#fff');
        $("#numero5 #irparafolhapagamento").css('background-color','#fff');
        $("#numero5 #irparafolhapagamento a").css('color','#000');

        $("#numero6 div").css('background-color','#000');
        $("#numero6 div center strong").css('color','#fff');
        $("#numero6 #irparacontratos").css('background-color','#fff');
        $("#numero6 #irparacontratos a").css('color','#000');

        $("#numero7 div").css('background-color','#000');
        $("#numero7 div center strong").css('color','#fff');
        $("#numero7 #irparalicitacoes").css('background-color','#fff');
        $("#numero7 #irparalicitacoes a").css('color','#000');

        $("#numero8 div").css('background-color','#000');
        $("#numero8 div center strong").css('color','#fff');
        $("#numero8 #cororiginal").css('background-color','#fff');

        $("#numero9 div").css('background-color','#000');
        $("#numero9 div center strong").css('color','#fff');
        $("#numero9 #comcontraste").css('background-color','#fff');
      });

      $(".main").css('float','left');
      $(".main").css('width','100%');
      $("#conteudo").removeAttr('style');

    });
  </script>

  <script src="https://www.google.com/recaptcha/api.js?hl=pt-BR" ></script>
</head>
<body>
<div id="general_content">

  <div id="main_header" class="teste">
    
<div class="to-right">
	<div class="pull-right"><a href="/cms/dashboard" class="label">Área Administrativa</a></div>
</div>
    <a href="/" class="home"><img src="/img/top_header.png" width="100%" height="100%" alt="" /></a>
  </div>

  <div id='acessibilidademin' accesskey='0' href='#'  style="float: left; width: 120px; height: 100px; margin-top: 5px; border-top-right-radius: 20px; border-bottom-right-radius: 20px; cursor: pointer; border: 1px solid rgb(221, 221, 221); color: rgb(16, 78, 139);">
    <img src='img/acessibilidade.jpg' style='margin-left:40px;margin-top:20px;' height="30" width="30">
    <b style="float: left; margin-top: 12px; font-size: 13px; margin-left: 4px;">Acessibilidade</b>
          <b style="float: left; font-size: 11px; margin-top: 5px; margin-left: 33px;">ALT+0</b>
      </div>

  <div id='acessibilidademax' style="padding: 12px;float: left; width: 200px; margin-top: 5px; background-color: rgb(255, 255, 255); border: 1px solid #ddd;margin-left:-500px;position:absolute;">
    <div id='fecharacessibilidade' style='cursor: pointer; float: left; width: 100%;color: #999;height: 30px;'>
      <div id='fechaacessibilidadex' style="cursor: pointer;font-size: 25px; margin-top: 1px; float: left; margin-left: 175px;">
        X
      </div>

    </div>

    <div style="width: 100%; float: left;margin-bottom: 10px;">
      <b style="float: left; font-size: 12px;">
        ACESSIBILIDADE
      </b>
    </div>

    <div style='border-bottom: 1px solid black; float: left; width: 85%;'></div>

    <div style='float: left; width: 90%; margin-top: 10px;'>
      Para navegação via teclado,
    </div>

    <div style='float: left; width: 90%;'>
      utilize a combinação de teclas
    </div>

    <div style='float: left; width: 90%;margin-bottom:5px;'>
      conforme o modelo abaixo:
    </div>

    <div style='float: left; border-radius: 8px; padding: 2px; background-color: #e6efff;'>
      
        <strong>ALT</strong>
      
    </div>

    <div style='float: left; margin-left: 4px; margin-top: 3px; margin-right: 3px;'>
      <strong>+</strong>
    </div>

    <div style='float: left; border-radius: 8px; padding: 2px; background-color: #e6efff;'>
      <strong>[Letra Atalho]</strong>
    </div>

    <div style='float: left; margin-top: 10px;'>
      Atalhos de navegação:
    </div>

    <div id='row' style="float: left; width: 100%; margin-top: 5px;">

      <div id='numero1' style="float: left; width: 100%;margin-bottom: 5px;">
        <div style='float: left; background-color: rgb(230, 239, 255); border-radius: 40px; width: 15px; padding: 4px;'>
          <center>
            <strong style='color:#6d6b6b'> A </strong>
          </center>
        </div>

        <div id='irparabusca' accesskey='a' style='float: left; margin-left: 10px; color: rgb(20, 103, 148); font-size: 11px; margin-top: 1px;'>
          <a href='#' style='text-decoration:none;color:#345076'>
            <small>Ir Para</small>
            <strong>Busca</strong>
          </a>
        </div>
      </div>

      <div id='numero2' style="float: left; width: 100%;margin-bottom: 5px;">
        <div style='float: left; background-color: rgb(230, 239, 255); border-radius: 40px; width: 15px; padding: 4px;'>
          <center>
            <strong style='color:#6d6b6b'> B </strong>
          </center>
        </div>

        <div id="irparadespesas" style='float: left; margin-left: 10px; color: rgb(20, 103, 148); font-size: 11px; margin-top: 1px;'>
          <a href='despesas' accesskey='b' style='text-decoration:none;color:#345076'>
            <small>Ir Para</small>
            <strong>Despesas</strong>
          </a>
        </div>

      </div>

      <div id='numero3' style="float: left; width: 100%;margin-bottom: 5px;">
        <div style='float: left; background-color: rgb(230, 239, 255); border-radius: 40px; width: 15px; padding: 4px;'>
          <center>
            <strong style='color:#6d6b6b'> C </strong>
          </center>
        </div>

        <div id="irparareceitas" style='float: left; margin-left: 10px; color: rgb(20, 103, 148); font-size: 11px; margin-top: 1px;'>
          <a href='receitas' accesskey='c' style='text-decoration:none;color:#345076'>
            <small>Ir Para</small>
            <strong>Receitas</strong>
          </a>
        </div>

      </div>

      <div id='numero4' style="float: left; width: 100%;margin-bottom: 5px;">
        <div style='float: left; background-color: rgb(230, 239, 255); border-radius: 40px; width: 15px; padding: 4px;'>
          <center>
            <strong style='color:#6d6b6b'> G </strong>
          </center>
        </div>

        <div id="irparadiarias" style='float: left; margin-left: 10px; color: rgb(20, 103, 148); font-size: 11px; margin-top: 1px;'>
          <a href='despesas/loadDiarias' accesskey='g' style='text-decoration:none;color:#345076'>
            <small>Ir para</small>
            <strong>Diárias</strong>
          </a>
        </div>

      </div>

      <div id='numero5' style="float: left; width: 100%;margin-bottom: 5px;">
        <div style='float: left; background-color: rgb(230, 239, 255); border-radius: 40px; width: 15px; padding: 4px;'>
          <center>
            <strong style='color:#6d6b6b'> H </strong>
          </center>
        </div>

        <div id="irparafolhapagamento" style='float: left; margin-left: 10px; color: rgb(20, 103, 148); font-size: 11px; margin-top: 1px;'>
          <a href='folha_pagamentos' accesskey='h' style='text-decoration:none;color:#345076'>
            <small>Ir Para</small>
            <strong>Folha de Pagamento</strong>
          </a>
        </div>

      </div>

      <div id='numero6' style="float: left; width: 100%;margin-bottom: 5px;">
        <div style='float: left; background-color: rgb(230, 239, 255); border-radius: 40px; width: 15px; padding: 4px;'>
          <center>
            <strong style='color:#6d6b6b'> I </strong>
          </center>
        </div>

        <div id="irparacontratos" style='float: left; margin-left: 10px; color: rgb(20, 103, 148); font-size: 11px; margin-top: 1px;'>
          <a href='acordos' accesskey='i' style='text-decoration:none;color:#345076'>
            <small>Ir Para</small>
            <strong>Contratos</strong>
          </a>
        </div>

      </div>

      <div id='numero7' style="float: left; width: 100%;margin-bottom: 10px;">
        <div style='float: left; background-color: rgb(230, 239, 255); border-radius: 40px; width: 15px; padding: 4px;'>
          <center>
            <strong style='color:#6d6b6b'> J </strong>
          </center>
        </div>

        <div id="irparalicitacoes" style='float: left; margin-left: 10px; color: rgb(20, 103, 148); font-size: 11px; margin-top: 1px;'>
          <a href='licitacoes' accesskey='j' style='text-decoration:none;color:#345076'>
            <small>Ir Para</small>
            <strong>Licitações</strong>
          </a>
        </div>
      </div>

      <div style="float: left; margin-bottom: 10px;">
        Atalhos para contraste do site:
      </div>

      <div id='numero8' style="float: left; width: 100%; margin-bottom: 7px;">
        <div style='float: left; background-color: rgb(230, 239, 255); border-radius: 40px; width: 15px; padding: 4px;'>
          <center>
            <strong style='color:#6d6b6b'> K </strong>
          </center>
        </div>

        <div id="cororiginal" style='float: left; margin-left: 10px; color: rgb(20, 103, 148); font-size: 11px; margin-top: 1px;'>
          <input id='cororiginalid' type="radio" name="contraste" value="cororiginal" accesskey='K' checked> Cor Original
        </div>
      </div>

      <div id='numero9' style="float: left; width: 100%;margin-bottom: 10px;">
        <div style='float: left; background-color: rgb(230, 239, 255); border-radius: 40px; width: 15px; padding: 4px;'>
          <center>
            <strong style='color:#6d6b6b'> L </strong>
          </center>
        </div>

        <div id="comcontraste" style='float: left; margin-left: 10px; color: rgb(20, 103, 148); font-size: 11px; margin-top: 1px;'>
          <input id='comcontrasteid' type="radio" name="contraste" value="comcontraste" accesskey='l'> Com Contraste
        </div>
      </div>

      <div style='border-bottom: 1px solid black; float: left; width: 85%;margin-bottom: 15px;'></div>

      <div style='float:left;width: 200px;margin-bottom:10px;'>
        Tamanho da fonte:
      </div>

      <div id='aumentarfonte' style='cursor: pointer;float: left; border: 1px solid rgb(0, 0, 0); padding: 5px; width: 75px;margin-right: 10px;'>
        <center>
          <b>A +</b>
        </center>
      </div>

      <div id='diminuirfonte' style='cursor: pointer;float: left; border: 1px solid rgb(0, 0, 0); padding: 5px; width: 75px;'>
        <center>
          <b>A -</b>
        </center>
      </div>

      <div id='fontepadrao' style='cursor: pointer;float: left; border: 1px solid rgb(0, 0, 0); padding: 5px; width: 172px; margin-top: 10px; height: 20px;'>
        <center>
          <div style='width: 30px; float: left; font-size: 15px; margin-left: 57px;'>
            <b>A</b>
          </div>

          <div style="width: 30px; float: left; margin-left: -6px; margin-top: 1px;">
            <img src='img/glyphicons-82-refresh.png'>
          </div>

      </div>


    </div>

  </div>

  <div id="main_content">
    <div id="buscar">
  <h3  style="text-align:right;">
    <form id="procurar" method="get" action="/consultas/pesquisar" style="display:inline-flex;">
            <input value="" id="search" name="parametros" type="text" onkeypress="keypressInBox(event)" placeholder="Buscar" data-url="https://transparencia.saoborja.rs.gov.br/"/>
            <a id="pesquisar" href="#"
         onclick="pesquisar('https://transparencia.saoborja.rs.gov.br/'  , 'search', 'tipobusca'); "  >
        <span>
          <img src="/img/lupa.png" alt="Bot�o de pesquisa">
        </span>
      </a>
    </form>
  </h3>
</div>
	  <h2>Missing Controller</h2>
<p class="error">
	<strong>Error: </strong>
	<em>JsController</em> could not be found.</p>
<p class="error">
	<strong>Error: </strong>
	Create the class <em>JsController</em> below in file: app/controllers/js_controller.php</p>
<pre>
&lt;?php
class JsController extends AppController {

	var $name = 'Js';
}
?&gt;
</pre>
<p class="notice">
	<strong>Notice: </strong>
	If you want to customize this error message, create app/views/errors/missing_controller.ctp</p>	</div>
	<div id="main_footer">
	  <div id="footer">
		   DBSeller Serviços de Informática Ltda. - Porto Alegre - RS | <a  href="http://www.dbseller.com.br">www.dbseller.com.br</a><br>
	  </div>
	</div>

  <div id="ajax-loader" style="display: none">
    <div class="ajax-loader-mask"></div>
    <img src="/img/loader.gif" alt="" />  </div>
</div>

<script type="text/javascript">
  var parentURL = window != window.parent ? true : false;

  if (parentURL == true){

    document.getElementById("main_header").style.display = "none";
    document.getElementById("main_footer").style.display = "none";
    document.getElementById("acessibilidademin").style.display = "none";
    document.getElementById("breadcrumb").style.display = "none";
    document.getElementById("buscar").style.display = "none";
    $('html').css('background-color','#fff');

  }


</script>
</body>
</html>
