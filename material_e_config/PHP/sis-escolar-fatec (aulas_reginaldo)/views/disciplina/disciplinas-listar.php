<?php
    require "../usuarios/usuario-verifica.php";
    //chama a Classe Turma.php para o baile
    require_once "../../classes/Disciplina.php";

    //Vamos criar mais um objeto Turma
    $disciplina = new Disciplina();

    //chama o método "listar" e armazenar o resultado em uma variavel
    $lista = $disciplina->listar();





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
            <th>Disciplina</th>
            <th>Carga Horaria</th>
            <th>Ações</th>
        </tr>
        <?php foreach($lista as $linha):?>
        <tr>
            <td><?= $linha['id']?></td>
            <td><?= $linha['nomeDisciplina']?></td>
            <td><?= $linha['cargaHoraria']?></td>
            <td>
                <a href="disciplinas-editar.php?id=<?= $linha['id'] ?>">Atualizar</a>
                |
                <a href="disciplinas-excluir.php?id=<?= $linha['id'] ?>">Excluir</a>
            </td>
        </tr>

        <?php endforeach?>
    </table>
    <a href="../../index2.php">VOLTAR</a>


</body>
</html>