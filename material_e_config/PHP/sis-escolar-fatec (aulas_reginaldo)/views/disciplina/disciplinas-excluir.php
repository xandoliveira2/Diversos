<?php
//incluir o arquivo que contem a classe Turma()
require_once "../../classes/Disciplina.php";

//Obtém o codigo ID enviado pelo método GET
$id = $_GET['id'];

//cria um novo novo objeto turma
$disciplina = new Disciplina($id);

//chama o métido(função) excluir do obejto turma
$disciplina->excluir();

//redireciona o usuario para a lista de turmas
header('Location: disciplinas-listar.php');

?>