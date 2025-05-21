// using System;
// using System.Diagnostics.Metrics;
// namespace Singleton
// {
//     public class Program
//     {
//         static void Main(string[] args)
//         {
//             var config1 = ConfiguracaoSistema.Instancia;
//             config1.Ambiente = "Produção";
//             config1.ModoDebug = true;
//             config1.ExibirInformacoes();

//             var config2 = ConfiguracaoSistema.Instancia;
//             config2.Ambiente = "Homologação";
//             config2.ExibirInformacoes(); 
//         }
//     }

//     public class ConfiguracaoSistema
//     {
//         private static ConfiguracaoSistema _instancia;
//         private ConfiguracaoSistema() {}
//         public string Ambiente { get; set;}
//         public bool ModoDebug { get; set; }
//         public static ConfiguracaoSistema Instancia
//         {
//             get
//             {
//                 if (_instancia == null) _instancia =  new ConfiguracaoSistema();
//                 return _instancia;
//             }
//         }
//         public void ExibirInformacoes()
//         {
//             Console.WriteLine("Ambiente: " + Ambiente);
//             Console.WriteLine("Modo Debug: " + ModoDebug);
//         }
//     }
// }