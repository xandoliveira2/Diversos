<?php
// Inclui o arquivo que contém a definição da classe Turma
require_once "../../classes/Disciplina.php";

// Cria um novo objeto Turma utilizando o id do objeto como referência
$id = $_POST['id'];
$disciplina = new Disciplina($id);

// Define as propriedades descTurma e ano do objeto Turma
$disciplina->nomeDisciplina = $_POST['nomeDisciplina'];
$disciplina->cargaHoraria = $_POST['cargaHoraria'];

// Chama o método atualizar() no objeto Turma
$disciplina->atualizar();

// Redireciona a página para a listagem de turmas
header('Location: disciplinas-listar.php');
?>