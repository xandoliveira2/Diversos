// using System.Security.Cryptography.X509Certificates;

// namespace Singleton2
// {
//     public class Program
//     {
//         static void Main(string[] args)
//         {
//             var lgs = Logger.Instancia;
//             var tarefas = new List<Thread>();
//             lgs.Log("VARIOS LOG SIMULTANEO 1");
//             for (int i = 1; i <= 5; i++)
//             {
//                 int id = i; // necessário para evitar closure errada
//                 var t = new Thread(() =>
//                 {
//                     lgs.Log($"LOG {id}");
//                 });

//                 tarefas.Add(t);
//                 t.Start();
//             }       
                
//             foreach (var t in tarefas)
//                 t.Join();


//         }
//     }

//     public class Logger
//     {
//         private static Logger _instancia;
//         private static readonly object _lock = new object();


//         public static Logger Instancia
//         {
//             get
//             {
//                 if (_instancia == null)
//                     _instancia = new Logger();
//                 return _instancia;
//             }
//         }
//         private Logger() { }
//         public DateTime Data
//         {
//             get
//             {
//                 return DateTime.Now;
//             }
//         }
//         public async void Log(string mensagem)
//         {
//             lock (_lock)
//             {
//             for(int i = 0; i <= 100; i++)
//                 Console.WriteLine($"[{Data}] {mensagem}|{i}.");
//             }
//         }

//     }
// }