<?php
//Incluir o arquivo que contém as definições da classe Turma
require_once "../../classes/Aluno.php";

//cria um novo objeto turma
$aluno = new Aluno();

//define as propriedades descTurma e Ano do objeto Turma
//Com os valores enviados pelo formulário  turmas - inserir.html
$aluno->nome = $_POST['nome'];
$aluno->foto = $_FILES['foto'];
$aluno->email = $_POST['email'];
$aluno->turma_id = $_POST['turma'];

//chama o metodo inserir() do objeto Aluno,
//inserir os dados no banco
$aluno->inserir();




?>
