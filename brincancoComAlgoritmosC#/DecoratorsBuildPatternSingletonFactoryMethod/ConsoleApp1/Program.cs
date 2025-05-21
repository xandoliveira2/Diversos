using System;
namespace builderRelatorio
{

    public class Program
    {

        static void Main(string[] args)
        {
            var relatorio1 = new RelatorioBuilder()
                .ComTitulo("Relatório de Vendas")
                .ComConteudo("Total vendido: R$15.000")
                .ComRodape("SistemaERP v1.0")
                .Build();

            var relatorio2 = new RelatorioBuilder()
                .ComTitulo("Resumo")
                .ComRodape("Confidencial")
                .Build();

            relatorio1.Exibir();
            relatorio2.Exibir();
        }

        public class Relatorio
        {

            public string titulo = string.Empty;
            public string conteudo = string.Empty;
            public string rodape = string.Empty;

            public string relatorioSimples = string.Empty;
            public void Exibir()
            {
                Console.WriteLine(this.relatorioSimples);
            }

        }

        public class RelatorioBuilder
        {
            private Relatorio _relatorioConstrutor = new Relatorio();

            public Relatorio Build()
            {
                _relatorioConstrutor.relatorioSimples = $"{_relatorioConstrutor.titulo}\n------------------------------------------\n{_relatorioConstrutor.conteudo}\n------------------------------------------\n{_relatorioConstrutor.rodape}";
                return _relatorioConstrutor;
            }



            public RelatorioBuilder ComTitulo(string titulo)
            {
                _relatorioConstrutor.titulo = titulo;
                return this;
            }

            public RelatorioBuilder ComConteudo(string conteudo)
            {
                _relatorioConstrutor.conteudo = conteudo;
                return this;
            }

            public RelatorioBuilder ComRodape(string rodape)
            {
                _relatorioConstrutor.rodape = rodape;
                return this;
            }

        }

    }

}