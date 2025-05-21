// using System;
// namespace decorator
// {
//     class Program
//     {
//         static void Main(string[] args)
//         {
//             IRelatorio relatorio = new ComAssinatura(
//                                         new ComBorda(
//                                         new ComData(
//                                             new RelatorioSimples()
//                                         )
//                                     )
//                                 );

//             Console.WriteLine(relatorio.Gerar());
//         }

//         public interface IRelatorio
//         {
//             string Gerar();
//         }

//         public class RelatorioSimples : IRelatorio
//         {
//             public string Gerar() => "Relatório de vendas do mês.";
//         }

//         public class ComBorda : IRelatorio
//         {
//             public IRelatorio _alterar;
//             public ComBorda(IRelatorio relatorioPai)
//             {
//                 _alterar = relatorioPai;
//             }

//             public string Gerar()
//             {
//                 return "***" + _alterar.Gerar() + "***";
//             }
//         }

//         public class ComData : IRelatorio
//         {
//             public IRelatorio _alterar;
//             public ComData(IRelatorio relatorioPai)
//             {
//                 _alterar = relatorioPai;
//             }

//             public string Gerar()
//             {
//                 return "[" + DateTime.Today.ToString("dd/MM/yyyy") + "]" + _alterar.Gerar();
//             }
//         }

//         public class ComAssinatura : IRelatorio
//         {
//             public IRelatorio _alterar;
//             public ComAssinatura(IRelatorio relatorioPai)
//             {
//                 _alterar = relatorioPai;
//             }

//             public string Gerar()
//             {
//                 return _alterar.Gerar() + "\nEmpresa XYZ";
//             } 
//         }
//     }

// }