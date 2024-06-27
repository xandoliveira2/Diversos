<?php
// Inclui o arquivo que contém a definição da classe Turma
require_once "../../classes/Turma.php"; 

// Obtém o valor do parâmetro "id" passado na URL via método GET
$id = $_GET['id'];

// Cria um novo objeto da classe Turma passando o valor de $id como parâmetro
$turma = new Turma($id);
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
            <h3>Nova Turma</h3>
            <form action="turma-editar-gravar.php" method="post" >
                <input type="hidden" name="id" value="<?= $turma->id ?>">
                <div>
                    <label for="descTurma">Turma:</label>
                    <input type="text" name="descTurma" value="<?= $turma->descTurma ?>">
                </div>

                <div>
                    <label for="ano">Ano:</label>
                    <input type="text" name="ano" value="<?= $turma->ano ?>">
                </div>
                <div>
                    <input type="submit" value="Gravar">
                </div>

            </form>
        </div>
    </div>
    
</body>
</html>