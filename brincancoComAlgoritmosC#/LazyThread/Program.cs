using System;
using System.Diagnostics.Contracts;
// namespace LazyThreadEx1
// {
//     public class Program
//     {

//         static void Main(string[] args)
//         {
//             Lazy<Relatorio> relatorio = new Lazy<Relatorio>(() => new Relatorio(), LazyThreadSafetyMode.ExecutionAndPublication);
//             relatorio.Value.Exibir();
//         }

//         public class Relatorio
//         {
//             public Relatorio()
//             {
//                 Console.WriteLine("Relatório foi carregado.");
//             }

//             public void Exibir()
//             {
//                 Console.WriteLine("Exibindo relatório...");
//             }
//         }

//     }
// }




namespace LazyThreadEx2
{
    public class Program
    {

        static void Main(string[] args)
        {
            Lazy<UsuarioLogado> user = new Lazy<UsuarioLogado>(() => new UsuarioLogado(), LazyThreadSafetyMode.ExecutionAndPublication);

            // user.Value.ObterNome();
        }


        public class UsuarioLogado
        {
            // private string Nome {
            //     get
            //     { return Nome; }
            //     set
            //     { (string nome) => Nome = nome; } }

            private string Nome = "Nome qualquer";
            public UsuarioLogado()
            {
                Console.WriteLine("Buscando dados do usuário logado...");
            }

            public void ObterNome() => Console.WriteLine(Nome);            


        }


    }
}