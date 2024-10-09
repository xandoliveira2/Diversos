<?php
//Incluir o arquivo que contém as definições da classe Turma
require_once "../../classes/Disciplina.php";

//cria um novo objeto turma
$disciplina = new Disciplina();

//define as propriedades descTurma e Ano do objeto Turma
//Com os valores enviados pelo formulário  turmas - inserir.html
$disciplina->nomeDisciplina = $_POST['nomeDisciplina'];
$disciplina->cargaHoraria = $_POST['cargaHoraria'];

//chama o metodo inserir() do objeto Turma,
//inserir os dados no banco
$disciplina->inserir();




?>
