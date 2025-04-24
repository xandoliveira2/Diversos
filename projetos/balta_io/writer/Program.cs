using System;
using System.IO;
using System.Windows.Forms;
namespace  TextEditor
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
        //     Console.WriteLine("O que você deseja fazer?");
        //     Console.WriteLine("1 - Abrir arquivo");
        //     Console.WriteLine("2 - Criar novo arquivo");
        //     Console.WriteLine("0 - Sair");
        //     short option = short.Parse(Console.ReadLine());
        //     switch(option)
        //     {
        //         case 0 : System.Environment.Exit(0); break;
        //         case 1 : Abrir(); break;
        //         case 2 : Editar(); break;
        //         default: Menu(); break;
        //     }

        // }
        // static void Editar()
        // {
        //     Console.Clear();
        //     Console.WriteLine("Digite seu texto abaixo (ESC para sair)");
        //     Console.WriteLine("----------------------------------------");
        //     string text = "";
        //     do
        //     {
        //         text += Console.ReadLine();
        //         text += Environment.NewLine;
        //     }
        //     while(Console.ReadKey().Key != ConsoleKey.Escape);
        //     Salvar(text);

        // }

        // static void Abrir()
        // {
        //     Console.Clear();
        //     Console.WriteLine("Qual camindo do arquivo?");
        //     string path = Console.ReadLine();
        //     using(var file = new StreamReader(path))
        //     {
        //         string texto = file.ReadToEnd();
        //         Console.WriteLine(texto);
        //     }
        //     Console.WriteLine("");
        //     Console.ReadLine();
        //     Menu();
        // }
        // static void Salvar(string texto)
        // {
        //     Console.Clear();
        //     Console.WriteLine("Qual caminho para salvar o arquivo?");
        //     var path = Console.ReadLine();
        //     using(var arquivo = new StreamWriter(path + "\\escrever.txt"))
        //     {
        //         arquivo.Write(texto);
        //     }
        //     Console.WriteLine($"Arquivo {path} salvo com sucesso");
        //     Console.ReadLine();
        //     Menu();
        // }

        [STAThread] // Muito importante com Forms
        static void Main(string[] args)
        {
            Console.Write("funciona ai bicho namoral");
            Menu();
        }
        static void Menu()
        {
            Console.Clear();
            Console.WriteLine("O que você deseja fazer?");
            Console.WriteLine("1 - Abrir arquivo");
            Console.WriteLine("2 - Criar novo arquivo");
            Console.WriteLine("0 - Sair");
            short option = short.Parse(Console.ReadLine());
            switch(option)
            {
                case 0 : System.Environment.Exit(0); break;
                case 1 : Abrir(); break;
                case 2 : Editar(); break;
                default: Menu(); break;
            }

        }
        static void Editar()
        {
            Console.Clear();
            Console.WriteLine("Digite seu texto abaixo (ESC para sair)");
            Console.WriteLine("----------------------------------------");
            string text = "";
            do
            {
                text += Console.ReadLine();
                text += Environment.NewLine;
            }
            while(Console.ReadKey().Key != ConsoleKey.Escape);
            Salvar(text);

        }

        static void Abrir()
        {
            Console.Clear();
            Console.WriteLine("Qual camindo do arquivo?");
            string path = Console.ReadLine();
            using(var file = new StreamReader(path))
            {
                string texto = file.ReadToEnd();
                Console.WriteLine(texto);
            }
            Console.WriteLine("");
            Console.ReadLine();
            Menu();
        }
        static void Salvar(string texto)
        {
            Console.Clear();
            using(var browser = new FolderBrowserDialog())
            {
                browser.Description = "Selecione uma pasta";
                
                if(browser.ShowDialog() == DialogResult.OK)
                {
                    string caminhoPasta = browser.SelectedPath;
                    Console.WriteLine("Digite nome do arquivo: (não precisa escrever a extensão, por padrão vai ser txt)");
                    var path = Console.ReadLine();
                    using(var arquivo = new StreamWriter(caminhoPasta + path + ".txt"))
                    {
                        arquivo.Write(texto);
                    }
                    Console.WriteLine($"Arquivo {path} salvo com sucesso");
                    Console.ReadLine();
                }
            }
            Menu();
        }



    }
}