<?php
//incluir o arquivo que contem a classe Turma()
require_once "../../classes/Aluno.php";

//Obtém o codigo ID enviado pelo método GET
$id = $_GET['id'];

//cria um novo novo objeto turma
$aluno = new Aluno($id);

//chama o métido(função) excluir do obejto turma
$aluno->excluir();

//redireciona o usuario para a lista de turmas
header('Location: alunos-listar.php');

?>