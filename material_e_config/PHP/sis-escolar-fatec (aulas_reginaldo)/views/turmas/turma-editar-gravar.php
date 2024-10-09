<?php
// Inclui o arquivo que contém a definição da classe Turma
require_once "../../classes/Turma.php";/*******MUNDANÇA DE CAMINHO*****/

// Cria um novo objeto Turma utilizando o id do objeto como referência
$id = $_POST['id'];
$turma = new Turma($id);

// Define as propriedades descTurma e ano do objeto Turma
$turma->descTurma = $_POST['descTurma'];
$turma->ano = $_POST['ano'];

// Chama o método atualizar() no objeto Turma
$turma->atualizar();

// Redireciona a página para a listagem de turmas
header('Location: turmas-listar.php');
?>