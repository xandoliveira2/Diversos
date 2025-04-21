using System;
using System.Data;
using System.Windows.Forms;

namespace CalculadoraForms
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
            this.Text = "Calculadora";
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void limpar_Click(object sender, EventArgs e)
        {
            visor.Text = string.Empty;
        }

        private void somar_Click(object sender, EventArgs e)
        {
            visor.Text += " + ";
        }

        private void subtrair_Click(object sender, EventArgs e)
        {
            visor.Text += " - ";
        }

        private void raiz_Click(object sender, EventArgs e)
        {
            visor.Text += "\u221A";
        }

        private void potencia_Click(object sender, EventArgs e)
        {
            visor.Text += " ** ";
        }

        private void divisao_Click(object sender, EventArgs e)
        {
            visor.Text += " / ";
        }

        private void multiplicacao_Click(object sender, EventArgs e)
        {
            visor.Text += " * ";
        }

        private void um_Click(object sender, EventArgs e)
        {
            visor.Text += "1";
        }

        private void dois_Click(object sender, EventArgs e)
        {
            visor.Text += "2";
        }

        private void tres_Click(object sender, EventArgs e)
        {
            visor.Text += "3";
        }

        private void quatro_Click(object sender, EventArgs e)
        {
            visor.Text += "4";
        }

        private void cinco_Click(object sender, EventArgs e)
        {
            visor.Text += "5";
        }

        private void seis_Click(object sender, EventArgs e)
        {
            visor.Text += "6";
        }

        private void sete_Click(object sender, EventArgs e)
        {
            visor.Text += "7";
        }

        private void oito_Click(object sender, EventArgs e)
        {
            visor.Text += "8";
        }

        private void nove_Click(object sender, EventArgs e)
        {
            visor.Text += "9";
        }

        private void zero_Click(object sender, EventArgs e)
        {
            visor.Text += "0";
        }

        private void igual_Click(object sender, EventArgs e)
        {
            try
            {
                string expressao = visor.Text.Replace(" ", "");

                // Passo 1: substituir símbolos por operadores fáceis de detectar
                expressao = expressao.Replace("√", "r");
                expressao = expressao.Replace("**", "^");

                double resultado = ResolverExpressao(expressao);

                visor.Text = resultado.ToString();
            }
            catch
            {
                visor.Text = "Erro";
            }
        }

        private double ResolverExpressao(string expr)
        {
            // Etapa 1: Resolver Raiz (r) e Potência (^)
            expr = ResolverOperacao(expr, "r");
            expr = ResolverOperacao(expr, "^");

            // Etapa 2: Resolver Multiplicação (*) e Divisão (/)
            expr = ResolverOperacao(expr, "*");
            expr = ResolverOperacao(expr, "/");

            // Etapa 3: Resolver Soma (+) e Subtração (-)
            expr = ResolverOperacao(expr, "+");
            expr = ResolverOperacao(expr, "-");

            return double.Parse(expr);
        }

        private string ResolverOperacao(string expr, string operador)
        {
            while (expr.Contains(operador))
            {
                int opIndex = expr.IndexOf(operador);

                // Pega número da direita (ou número dentro da raiz)
                int i = opIndex + 1;
                string numeroDireita = "";
                while (i < expr.Length && (char.IsDigit(expr[i]) || expr[i] == '.'))
                {
                    numeroDireita += expr[i];
                    i++;
                }

                double right = double.Parse(numeroDireita);

                if (operador == "r") // Raiz quadrada
                {
                    double resultado = Math.Sqrt(right);
                    expr = expr.Substring(0, opIndex) + resultado.ToString() + expr.Substring(opIndex + numeroDireita.Length + 1);
                }
                else
                {
                    // Pega número da esquerda
                    int j = opIndex - 1;
                    string numeroEsquerda = "";
                    while (j >= 0 && (char.IsDigit(expr[j]) || expr[j] == '.'))
                    {
                        numeroEsquerda = expr[j] + numeroEsquerda;
                        j--;
                    }

                    double left = double.Parse(numeroEsquerda);
                    double resultado = 0;

                    switch (operador)
                    {
                        case "^": resultado = Math.Pow(left, right); break;
                        case "*": resultado = left * right; break;
                        case "/": resultado = left / right; break;
                        case "+": resultado = left + right; break;
                        case "-": resultado = left - right; break;
                    }

                    expr = expr.Substring(0, j + 1) + resultado.ToString() + expr.Substring(opIndex + numeroDireita.Length + 1);
                }
            }

            return expr;
        }

    }
}
