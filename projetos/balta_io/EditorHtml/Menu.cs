using System;

namespace EditorHtml
{

    public static class Menu
    {
        public static void Show()
        {
            Console.Clear();
            Console.BackgroundColor = ConsoleColor.Blue;
            Console.ForegroundColor = ConsoleColor.Black;
            DrawScreen();
            WriteOptions();
            var option = short.Parse(Console.ReadLine());
            HandleMenuOptions(option);
        }

        public static void DrawScreen()
        {
            Console.Write("+");
            for(int i = 0; i <= 30; i++)
            {
                Console.Write("-");
            }
            Console.WriteLine("+");

            for(int lines = 0; lines<=10; lines++)
            {
                Console.Write("|");
                for(int i = 0; i <= 30; i++)
                {
                    Console.Write(" ");
                }
                Console.WriteLine("|");
            }
            Console.Write("+");
            for(int i = 0; i <= 30; i++)
            {
                Console.Write("-");
            }
            Console.WriteLine("+");
        }
    
        public static void WriteOptions()
        {
            Console.SetCursorPosition(3, 0); // linhas colunas | x y
            Console.WriteLine("Editor HTML");
            Console.SetCursorPosition(3, 2); // linhas colunas | x y
            Console.WriteLine("===========");
            Console.SetCursorPosition(3, 3); // linhas colunas | x y
            Console.WriteLine("Selecione uma opção abaixo");
            Console.SetCursorPosition(3, 5); // linhas colunas | x y
            Console.WriteLine("1 - Novo arquivo");
            Console.SetCursorPosition(3, 6); // linhas colunas | x y
            Console.WriteLine("2 - Abrir arquivo");
            Console.SetCursorPosition(3, 8); // linhas colunas | x y
            Console.WriteLine("0 - Sair");
            Console.SetCursorPosition(3, 9); // linhas colunas | x y
            Console.Write("Opção: ");
            
        }
    
        public static void HandleMenuOptions(short option)
        {
            switch (option)
            {
                case 1: Editor.Show(); break;
                case 2: Console.WriteLine("View"); break;
                case 0: {
                    Console.Clear();
                    Environment.Exit(0);
                    break;
                }
                default: Show(); break;
            }
        }

    }

}