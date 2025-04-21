using System;
using System.Threading;
namespace Stopwatch
{
    class Program
    {
        // static void Main(string[] args)
        // {
        //     Menu();
        // }

        // static void Menu()
        // {
        //     Console.Clear();
        //     Console.WriteLine("S = Segundo => 10s = 10 segundos");
        //     Console.WriteLine("M = Minuto => 1m = 1 minuto");
        //     Console.WriteLine("0 = Sair");
        //     Console.WriteLine("Quanto tempo deseja contar?");

        //     string data = Console.ReadLine().ToLower();
        //     char type = char.Parse(data.Substring(data.Length - 1,1));
        //     int time  = int.Parse(data.Substring(0,data.Length - 1));
        //     int multiplier = 1;
        //     if(type == 'm') multiplier = 60;
        //     if(time == 0 )System.Environment.Exit(0);
        //     PreStart(time * multiplier); 
        // }

        // static void PreStart(int time)
        // {
        //     Console.Clear();
        //     Console.WriteLine("Ready...");
        //     Thread.Sleep(1000);
        //     Console.WriteLine("Set...");
        //     Thread.Sleep(1000);
        //     Console.WriteLine("Go...");
        //     Thread.Sleep(2500);
        //     Start(time);
            
        // }

        // static void Start(int time)
        // {
        //     int currentTime = 0;
        //     while (currentTime != time)
        //     {
        //         Console.Clear();
        //         currentTime++;
        //         Console.WriteLine(currentTime);
        //         Thread.Sleep(1000);
        //     }
        //     Console.Clear();
        //     Console.WriteLine("Stopwatch finalizado");
        //     Thread.Sleep(2500);
        // }

       static void Main(string[] args)
        {
            if(args.Length >= 2)
            {
                if( int.TryParse(args[0], out int inicio) && int.TryParse(args[1],out int final))
                {
                    Cronometro(inicio,final);
                }
                else Console.WriteLine("Valores de Argumento devem ser passados apenas inteiros / númericos");
            }
            else if(args.Length == 1)
            {
                if(int.TryParse(args[0], out int final))
                {
                    Cronometro(fim : final);
                }
            }
            else
            {
                Console.WriteLine("Digite em qual valor deve se encerrar o cronômetro?");
                if(!int.TryParse(Console.ReadLine(), out int fimInputUsuario))
                { 
                    Console.WriteLine("Valor inválido, impossível converter para inteiro");
                    return;
                }

                Console.WriteLine("Digite em qual valor deve se iniciar o cronômetro? (opcional, aperte Enter para ignorar)");
                var inputComeco = Console.ReadLine();
                try{
                if(string.IsNullOrWhiteSpace(inputComeco) || string.IsNullOrWhiteSpace(inputComeco.Replace("0","")))
                    Cronometro(0,fimInputUsuario);
                else
                    Cronometro(Convert.ToInt32(inputComeco),fimInputUsuario); 
                }
                catch(Exception ex)
                {
                    Console.WriteLine("Formato inválido");
                    return;
                }
            }
        }

        static void Cronometro(int comeco = 1, int fim = 0)
        {
            for(int start = comeco ;start <= fim;start++)
            {
                Console.WriteLine(start);
                Thread.Sleep(1000);
            }
            Console.WriteLine("Fim");
        }

    }
}
