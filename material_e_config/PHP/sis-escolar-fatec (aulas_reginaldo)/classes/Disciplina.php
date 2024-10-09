<?php

class Disciplina
{
    public $id;
    public $nomeDisciplina;
    public $cargaHoraria;

    public function __construct($id = false)
    {
        // verifica se a variável $id foi definida
        if ($id) {
            // atribui o valor de $id à propriedade $id do objeto
            $this->id = $id;
            // chama o método carregar() para carregar as informações da turma correspondente ao id
            $this->carregar();
        }
    }

    public function inserir()
    {
        // echo"Turma: ". $this->descTurma ."<br>";
        // echo"Ano: ". $this->ano. "<br>";
        // echo"Turma gravada com sucesso! Mentira!";


        //Define a string SQL de inserção de dados na tabela "tb_turmas"
        $sql = "INSERT INTO tb_disciplinas (nomeDisciplina, cargaHoraria) VALUES (
             '" . $this->nomeDisciplina . "',
             '" . $this->cargaHoraria . "'
             )";

        //cria uma nova conexão PDO com o banco de daddos "sis-escolar"
        include "Conexao.php";

        //executa a string SQL na conexão, enserindo os dados na tabela "tb_turmas"
        $conexao->exec($sql);

        echo "Registro gravado com sucesso";
        //Essa linha retornar para a lista depois de 5 segundos
        header("refresh:3; URL=disciplinas-listar.php");
    }

    public function listar()
    {
        //Cria uma string com o  comando SQL para pegar todos os dados da tabela "tb_turmas"
        $sql = "SELECT * FROM tb_disciplinas ";

        //cria uma nova conexão PDO com o banco de daddos "sis-escolar"
        include "Conexao.php";

        //Executa a string $sql na conexão retornando um objeto com dados
        $resultado = $conexao->query($sql);

        //Extrai todas as linhas de registros do objeto para um array
        $lista = $resultado->fetchAll();

        //Retorna array contendo os dados da consulta ao banco
        return $lista;
    }


    public function excluir()
    {
        //define a string de consulta SQL para deletar um registro
        //da tabela "tb_turmas" com base no seu ID
        $sql = "DELETE FROM tb_disciplinas WHERE id=" . $this->id;
        //echo $sql;
        //die();

        include "Conexao.php";

        $conexao->exec($sql);
    }


    public function carregar()
    {
        // Query SQL para buscar uma turma no banco de dados pelo id
        $sql = "SELECT * FROM tb_disciplinas WHERE id=" . $this->id;
        include "Conexao.php";

        // Execução da query e armazenamento do resultado em uma variável
        $resultado = $conexao->query($sql);
        // Recuperação da primeira linha do resultado como um array associativo
        $linha = $resultado->fetch();

        // Atribuição dos valores dos campos da turma recuperados do banco às propriedades do objeto
        $this->nomeDisciplina = $linha['nomeDisciplina'];
        $this->cargaHoraria = $linha['cargaHoraria'];
    }

    public function atualizar()
    {


        // Query SQL para atualizar uma turma no banco de dados pelo id
        $sql = "UPDATE tb_disciplinas SET 
                    nomeDisciplina = '$this->nomeDisciplina' ,
                    cargaHoraria = '$this->cargaHoraria'
                WHERE id = $this->id ";

        include "Conexao.php";
        $conexao->exec($sql);
    }
}
