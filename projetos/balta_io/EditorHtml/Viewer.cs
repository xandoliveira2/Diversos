using System;
using System.Text.RegularExpressions;

namespace EditorHtml
{
    public class Viewer
    {

        public static void Show(string text)
        {
            Console.Clear();
            Console.BackgroundColor = ConsoleColor.White;
            Console.ForegroundColor = ConsoleColor.Black;
            Console.Clear();
            Console.WriteLine("MODO VISUALIZAÇÃO");
            Console.WriteLine("-----------------");
            Replace(text);
            Console.WriteLine("-----------------");
            Console.WriteLine(text);
            Console.ReadKey();
            Menu.Show();
        }

        public static void Replace(string text)
        {
            var strong = new Regex(@"<\s*strong[^>]*>(.*?)<\s*/\s*strong>");
            // strong.IsMatch
            var words = text.Split(' ');

            for(var  i = 0; i < words.Count(); i++)
            {
                if(strong.IsMatch(words[i]))
                {
                    Console.ForegroundColor = ConsoleColor.Blue;
                    Console.Write(words[i].Substring(
                            words[i].IndexOf('>')+1,
                            (
                                words[i].IndexOf("</") - 
                                words[i].IndexOf('>')
                            )
                        )
                    );
                    Console.WriteLine(" ");
                }
                else
                {
                    Console.ForegroundColor = ConsoleColor.Black;
                    Console.Write(" ");
                }
                Console.Write(words[i]);
            }
        }
    }

}