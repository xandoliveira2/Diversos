<?php
// Inclui o arquivo que contém a definição da classe Turma
require_once "../../classes/Disciplina.php"; 

// Obtém o valor do parâmetro "id" passado na URL via método GET
$id = $_GET['id'];

// Cria um novo objeto da classe Turma passando o valor de $id como parâmetro
$disciplina = new Disciplina($id);
?>

<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
    <title>Sistema Acadêmico</title>
</head>
<body>
    <div>
        <div>
            <h1>Sistema Acadêmico</h1>
        </div>
        <div>
            <h3>Disciplinas</h3>
            <form action="disciplinas-editar-gravar.php" method="post" >
                <input type="hidden" name="id" value="<?= $disciplina->id ?>">
                <div>
                    <label for="nomeDisciplina">Disciplina:</label>
                    <input type="text" name="nomeDisciplina" value="<?= $disciplina->nomeDisciplina ?>">
                </div>

                <div>
                    <label for="cargaHoraria">Carga Horária:</label>
                    <input type="text" name="cargaHoraria" value="<?= $disciplina->cargaHoraria ?>">
                </div>
                <div>
                    <input type="submit" value="Gravar">
                </div>

            </form>
        </div>
    </div>
    
</body>
</html>