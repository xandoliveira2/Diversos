<?php
    //chama a Classe Turma.php para o baile
    require_once "../../classes/Turma.php";

    //Vamos criar mais um objeto Turma
    $turma = new Turma();

    //chama o método "listar" e armazenar o resultado em uma variavel
    $lista = $turma->listar();





?>
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sistema Acadêmico</title>
</head>
<body>
    <h1>Sistema Acadêmico</h1>
    <table border="1">
        <tr>
            <th>Código</th>
            <th>Turma</th>
            <th>Ano</th>
            <th>Ações</th>
        </tr>
        <?php foreach($lista as $linha):?>
        <tr>
            <td><?php echo $linha['id']?></td>
            <td><?php echo $linha['descTurma']?></td>
            <td><?php echo $linha['ano']?></td>
            <td>
                <a href="turmas-editar.php?id=<?= $linha['id'] ?>">Atualizar</a>
                |
                <a href="turmas-excluir.php?id=<?= $linha['id'] ?>">Excluir</a>
            </td>
        </tr>

        <?php endforeach?>
    </table>
    <a href="../../index2.php">VOLTAR</a>


</body>
</html>