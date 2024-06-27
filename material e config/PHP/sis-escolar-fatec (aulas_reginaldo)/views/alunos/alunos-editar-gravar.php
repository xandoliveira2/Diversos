<?php
// Inclui o arquivo que contém a definição da classe Aluno
require_once "../../classes/Aluno.php";/*******MUNDANÇA DE CAMINHO*****/

// Cria um novo objeto Aluno utilizando o id do objeto como referência
$id = $_POST['id'];
$aluno = new Aluno($id);

// Define as propriedades do objeto Aluno
$aluno->nome = $_POST['txtnome'];
$aluno->turma_id = $_POST['selturma'];
$aluno->email = $_POST['txtemail'];
$aluno->foto = $_FILES['foto'];

// Chama o método atualizar() no objeto Aluno
$aluno->atualizar();

// Redireciona a página para a listagem de alunos
header('Location: alunos-listar.php');
?>