<?php
//Incluir o arquivo que contém as definições da classe Turma
require_once "../../classes/Turma.php";

//cria um novo objeto turma
$turma = new Turma();

//define as propriedades descTurma e Ano do objeto Turma
//Com os valores enviados pelo formulário  turmas - inserir.html
$turma->descTurma = $_POST['descTurmas'];
$turma->ano = $_POST['ano'];

//chama o metodo inserir() do objeto Turma,
//inserir os dados no banco
$turma->inserir();




?>
