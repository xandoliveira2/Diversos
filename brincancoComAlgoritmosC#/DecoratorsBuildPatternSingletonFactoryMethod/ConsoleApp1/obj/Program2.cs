
// namespace rodar 
// {

//     class Program
//     {
//         static void Main(string[] args)
//         {
//             Func<dynamic, Func<dynamic, bool>> FiltrarStatus = valor1 => valor2 => valor1 == valor2;

            

//             Pessoa[] listaPessoas = [new Pessoa("ful1", 18, "analista"), new Pessoa("ful2",18,"auxiliar"), new Pessoa("ful1",20,"gerente"), new Pessoa("ful3",26,"analista")];
//             var filtroIdade = FiltrarStatus(26);
//             Pessoa[] gerentes = listaPessoas.Where(p => filtroIdade(p.idade)).ToArray();
//             foreach (Pessoa p in gerentes)
//                 Console.WriteLine(p.nome);
            
//         }
//     }
//     public class Pessoa
//     {
//         public string nome { get; set; }
//         public int idade { get; set; }
//         public string cargo { get; set; }
//         public Pessoa(string nome, int idade, string cargo)
//         {
//             this.nome = nome;
//             this.idade = idade;
//             this.cargo = cargo;
//         }
//     }

// }