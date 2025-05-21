// namespace StrategyPattern
// {

//     public class Program
//     {
//         static void Main(string[] args)
//         {

//             var pix = new Pagamento(new Pix());
//             pix.calcular(195);
//             pix.exibirTotal();
//             var boleto = new Pagamento(new Boleto());
//             boleto.calcular(9878);
//             boleto.exibirTotal();
//             var cartaoCredito = new Pagamento(new CartaoCredito());
//             cartaoCredito.calcular(1250);
//             cartaoCredito.exibirTotal();

//         }

//         public interface IStrategyPagamento
//         {
//             decimal calcular(decimal valor);
//         }

//         public class Pagamento
//         {
//             private IStrategyPagamento _calcularFrete;
//             private decimal valorArmazenado = 0;
//             public Pagamento(IStrategyPagamento TipoPagamento)
//             {
//                 _calcularFrete = TipoPagamento;
//             }

//             public decimal calcular(decimal valor)
//             {
//                 valorArmazenado = _calcularFrete.calcular(valor);
//                 return valorArmazenado;
//             }

//             public void exibirTotal() => Console.WriteLine(valorArmazenado);

//         }

//         public class Pix : IStrategyPagamento
//         {
//             public decimal calcular(decimal valor) => valor;
//         }
//         public class Boleto : IStrategyPagamento
//         {
//             public decimal calcular(decimal valor) => valor + 2;
//         }

//         public class CartaoCredito : IStrategyPagamento
//         {
//             public decimal calcular(decimal valor) => valor + (valor * 5 / 100);
//         }


//     }

// }